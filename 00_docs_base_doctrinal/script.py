r"""
RFJ - Descarga de documentos base (carpeta por documento + .md vacío + PDF/HTML)

Requisitos:
  pip install requests

Ejecución:
  python script.py

Salida:
  01 - <Titulo>\ <Titulo>.md  (vacío)
                 <Titulo>.pdf (o .html si no es PDF)
"""

from __future__ import annotations

import re
import time
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Tuple

import requests


# -------------------------
# Config
# -------------------------

BASE_DIR = Path(__file__).resolve().parent  # carpeta donde está el script
TIMEOUT = 60
RETRIES = 3
SLEEP_BETWEEN_RETRIES_SEC = 2

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0 Safari/537.36"
    ),
    "Accept": "application/pdf,text/html,application/octet-stream;q=0.9,*/*;q=0.8",
}

INVALID_WIN_CHARS = r'<>:"/\\|?*\x00-\x1F'


def sanitize_name(name: str, max_len: int = 140) -> str:
    """Sanitiza nombres para Windows (carpetas/archivos)."""
    name = re.sub(f"[{INVALID_WIN_CHARS}]", "", name).strip()
    name = re.sub(r"\s+", " ", name).strip()
    name = name.rstrip(". ")
    if len(name) > max_len:
        name = name[:max_len].rstrip(". ")
    return name or "SIN_TITULO"


def is_probably_pdf(first_bytes: bytes, content_type: str) -> bool:
    ct = (content_type or "").lower()
    if "application/pdf" in ct:
        return True
    return first_bytes.startswith(b"%PDF-")


def is_probably_html(first_bytes: bytes, content_type: str) -> bool:
    ct = (content_type or "").lower()
    if "text/html" in ct:
        return True
    sniff = first_bytes.lstrip()[:200].lower()
    return (
        sniff.startswith(b"<!doctype html")
        or sniff.startswith(b"<html")
        or b"<head" in sniff
        or b"<body" in sniff
    )


def ensure_empty_markdown(md_path: Path) -> None:
    if not md_path.exists():
        md_path.write_text("", encoding="utf-8")


@dataclass
class DocSpec:
    title: str
    candidates: List[str]
    prefer_pdf: bool = True


def try_download(url: str) -> Tuple[Optional[bytes], Optional[str], Optional[requests.Response]]:
    """
    Hace GET streaming y devuelve (first_chunk, content_type, response) si abrió OK.
    O (None, None, None) si falla.
    """
    for attempt in range(1, RETRIES + 1):
        try:
            resp = requests.get(
                url,
                headers=HEADERS,
                stream=True,
                timeout=TIMEOUT,
                allow_redirects=True,
            )
            resp.raise_for_status()

            content_type = resp.headers.get("Content-Type", "") or ""
            it = resp.iter_content(chunk_size=64 * 1024)
            first_chunk = next(it, b"")
            return first_chunk, content_type, resp

        except Exception as e:
            print(f"  ! Error ({attempt}/{RETRIES}) {url}: {e}")
            time.sleep(SLEEP_BETWEEN_RETRIES_SEC)

    return None, None, None


def download_best(doc: DocSpec, folder: Path) -> Optional[Path]:
    """
    Intenta candidates en orden.
    Si prefer_pdf=True, evita HTML si hay otra opción.
    Guarda el archivo con el nombre del título y extensión según tipo real.
    Retorna el path guardado o None.
    """
    title = sanitize_name(doc.title)
    tmp_path = folder / f"{title}.download"

    for idx, url in enumerate(doc.candidates):
        print(f"  - Probando fuente {idx+1}/{len(doc.candidates)}: {url}")
        first_chunk, content_type, resp = try_download(url)
        if resp is None or first_chunk is None:
            continue

        # Si se prefiere PDF y esto parece HTML, y aún hay más opciones: saltar
        if doc.prefer_pdf and is_probably_html(first_chunk, content_type) and (idx + 1) < len(doc.candidates):
            try:
                resp.close()
            except Exception:
                pass
            print("    -> Parece HTML; buscando otra fuente (idealmente PDF)...")
            continue

        # Decidir extensión real
        if is_probably_pdf(first_chunk, content_type):
            ext = ".pdf"
        elif is_probably_html(first_chunk, content_type):
            ext = ".html"
        else:
            # fallback por URL
            lower_url = url.lower()
            if lower_url.endswith(".pdf"):
                ext = ".pdf"
            elif lower_url.endswith(".docx"):
                ext = ".docx"
            elif lower_url.endswith(".doc"):
                ext = ".doc"
            else:
                ext = ".bin"

        final_path = folder / f"{title}{ext}"

        # Guardar a disco (stream)
        try:
            with open(tmp_path, "wb") as f:
                if first_chunk:
                    f.write(first_chunk)
                for chunk in resp.iter_content(chunk_size=128 * 1024):
                    if chunk:
                        f.write(chunk)

            try:
                resp.close()
            except Exception:
                pass

            if final_path.exists():
                final_path.unlink()
            tmp_path.rename(final_path)

            print(f"    ✓ Guardado: {final_path.name}")
            return final_path

        except Exception as e:
            print(f"    ! Falló guardado para {url}: {e}")
            try:
                resp.close()
            except Exception:
                pass
            if tmp_path.exists():
                try:
                    tmp_path.unlink()
                except Exception:
                    pass

    return None


def main() -> int:
    docs: List[DocSpec] = [
        DocSpec(
            title="Biblia RVR1960 (RVR60) - Referencia",
            candidates=[
                "https://www.bible.com/es/bible/149/GEN.1.RVR1960",
            ],
            prefer_pdf=False,  # este link típicamente es HTML
        ),
        DocSpec(
            title="Credo de los Apóstoles",
            candidates=[
                "https://network.crcna.org/sites/default/files/EL%20CREDO%20DE%20LOS%20APOSTOLES-SpanishREVISED-CRCNA%20FINAL.pdf",
            ],
        ),
        DocSpec(
            title="Credo Niceno-Constantinopolitano",
            candidates=[
                "https://network.crcna.org/sites/default/files/EL%20CREDO%20NICENO-SpanishREVISED-CRCNA%20FINAL.pdf",
            ],
        ),
        DocSpec(
            title="Credo de Calcedonia",
            candidates=[
                "https://escriturayverdad.cl/wp-content/uploads/Historia/CALCEDONIA.pdf",
            ],
        ),
        DocSpec(
            title="Credo de Atanasio",
            candidates=[
                "https://network.crcna.org/sites/default/files/CredoDeAtanasio-SpanishREVISED-CRCNA%20FINAL.pdf",
            ],
        ),
        DocSpec(
            title="Tesis de Barmen (1934)",
            candidates=[
                "https://www.ev-kirche-mexiko.org/uploads/j0Qo5D2G/DECLARACIN_Barmen.pdf",
            ],
        ),
        DocSpec(
            title="Declaración de Chicago sobre la Hermenéutica Bíblica",
            candidates=[
                "https://archive.etsjets.org/files/documents/Chicago_Statement.pdf",
                "https://etsjets.org/wp-content/uploads/2010/08/files_JETS-PDFs_25_25-4_25-4-pp397-401_JETS.pdf",
            ],
        ),
        DocSpec(
            title="Juntos por el Evangelio - Afirmaciones y Negaciones (2006)",
            candidates=[
                "https://t4g.org/wp-content/uploads/2010/10/Affirmations-Denials-Spanish.pdf",
            ],
        ),
        DocSpec(
            title="Confesión de Fe RFJ (en construcción)",
            candidates=[],
            prefer_pdf=False,
        ),
        DocSpec(
            title="Confesión de Fe Escocesa (1560)",
            candidates=[
                "https://archive.org/download/LaConfesinDeFeEscocesaDe1560/La%20Confesi%C3%B3n%20de%20Fe%20Escocesa%20de%201560.pdf",
            ],
        ),
        DocSpec(
            title="Confesión Belga (1561)",
            candidates=[
                "https://www.crcna.org/sites/default/files/belgic_confession-spanish_from_rca.pdf",
            ],
        ),
        DocSpec(
            title="Catecismo de Heidelberg (1563)",
            candidates=[
                "https://www.crcna.org/sites/default/files/Catecismo%20de%20Heidelberg.pdf",
            ],
        ),
        DocSpec(
            title="Segunda Confesión Helvética (1566) - (Compilación PCUSA en español)",
            candidates=[
                "https://pcusa.org/sites/default/files/confessions-spanish.pdf",
            ],
        ),
        DocSpec(
            title="Confesión de Fe de Westminster (1646)",
            candidates=[
                "https://storage.e.jimdo.com/file/8c9bfe67-d8e6-483d-8ed9-087eda03d6fd/La%20Confesi%C3%B3n%20de%20Fe%20de%20Westminster.pdf",
            ],
        ),
        DocSpec(
            title="Catecismo Mayor de Westminster",
            candidates=[
                "https://storage.e.jimdo.com/file/6d0c5f43-e8f2-4589-9353-50fcbf591572/El%20Catecismo%20Mayor%20de%20Westminster.pdf",
            ],
        ),
        DocSpec(
            title="Catecismo Menor de Westminster",
            candidates=[
                "https://storage.e.jimdo.com/file/b1948498-2bd5-4ee3-b3ae-e3af35e2f552/El%20catecismo%20menor%20de%20Westminster.pdf",
            ],
        ),
        DocSpec(
            title="Confesión Bautista de Fe de Londres (1689)",
            candidates=[
                "https://storage.e.jimdo.com/file/2bbac6d3-07d1-4e04-8601-acde0ca70c0d/La%20Confesi%C3%B3n%20Bautista%20de%20Fe%20de%20Londres%20de%201689.pdf",
            ],
        ),
    ]

    print(f"Base dir: {BASE_DIR}")
    BASE_DIR.mkdir(parents=True, exist_ok=True)

    downloaded = 0
    pending = 0

    for i, doc in enumerate(docs, start=1):
        num = f"{i:02d}"
        title_clean = sanitize_name(doc.title)
        folder = BASE_DIR / f"{num} - {title_clean}"
        folder.mkdir(parents=True, exist_ok=True)

        md_path = folder / f"{title_clean}.md"
        ensure_empty_markdown(md_path)

        print(f"\n[{num}] {doc.title}")
        if not doc.candidates:
            print("  ! Sin URL(s). Carpeta y .md creados; descarga pendiente.")
            pending += 1
            continue

        saved = download_best(doc, folder)
        if saved is None:
            print("  ! No se pudo descargar desde ninguna fuente.")
            pending += 1
        else:
            downloaded += 1

    print("\n==================== RESUMEN ====================")
    print(f"Descargados OK: {downloaded}")
    print(f"Pendientes/Fallidos: {pending}")
    print("================================================\n")

    # salida útil para agentes: 0 = todo OK; 2 = faltó algo
    return 0 if pending == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())

# cd "C:\Users\PC-AORUS\Desktop\RFJ 2026\01_docs_base"
# py -m pip install requests
# py script.py
