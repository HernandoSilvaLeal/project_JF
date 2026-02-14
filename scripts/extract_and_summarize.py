import os
import re
import math
from pathlib import Path
import pdfplumber
from collections import Counter
from tqdm import tqdm


BASE = Path("00_docs_base")
EXTRACT_DIR = BASE / "__extracted__"
EXTRACT_DIR.mkdir(parents=True, exist_ok=True)


SPANISH_STOPWORDS = set([
    # short list of common spanish stopwords to improve scoring
    "de","la","que","el","en","y","a","los","del","se","las","por","un","para",
    "con","no","una","su","al","lo","como","más","pero","sus","le","ya","o","este",
    "sí","porque","esta","entre","cuando","muy","sin","sobre","también","me","hasta",
])


def split_sentences(text: str):
    # naive sentence splitter that keeps punctuation
    sentences = re.split(r'(?<=[\.!?])\s+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    return sentences


def tokenize(text: str):
    # lowercase, keep letters and numbers, split
    words = re.findall(r"\w+", text.lower(), flags=re.UNICODE)
    return words


def summarize(text: str, max_sentences: int = 8):
    sentences = split_sentences(text)
    if not sentences:
        return ""

    words = tokenize(text)
    words = [w for w in words if w not in SPANISH_STOPWORDS]
    if not words:
        # fallback: return first sentences
        return "\n\n".join(sentences[:max_sentences])

    freq = Counter(words)
    # score sentences
    sent_scores = []
    for i, s in enumerate(sentences):
        toks = tokenize(s)
        if not toks:
            score = 0
        else:
            score = sum(freq.get(t, 0) for t in toks) / (len(toks) + 0.1)
        sent_scores.append((i, score, s))

    # pick top sentences by score
    top = sorted(sent_scores, key=lambda x: x[1], reverse=True)[: max_sentences]
    top_sorted_by_pos = sorted(top, key=lambda x: x[0])
    summary = "\n\n".join(s for (_, __, s) in top_sorted_by_pos)
    return summary


def extract_text_from_pdf(pdf_path: Path) -> str:
    text_parts = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                t = page.extract_text()
                if t:
                    text_parts.append(t)
    except Exception:
        return ""
    return "\n".join(text_parts)


def top_keywords(text: str, n=12):
    words = [w for w in tokenize(text) if w not in SPANISH_STOPWORDS]
    c = Counter(words)
    return [w for w, _ in c.most_common(n)]


def process_folder(folder: Path):
    # find pdf files
    pdfs = list(folder.glob("*.pdf"))
    if not pdfs:
        return False
    pdf = pdfs[0]
    text = extract_text_from_pdf(pdf)
    if not text.strip():
        return False

    # save extracted text
    out_txt = EXTRACT_DIR / (folder.name + ".txt")
    out_txt.write_text(text, encoding="utf-8")

    # build summary
    summary = summarize(text, max_sentences=10)
    keywords = top_keywords(text, n=12)

    md_lines = []
    md_lines.append(f"# Resumen: {folder.name}\n")
    md_lines.append(f"**Archivo original:** {pdf.name}\n")
    try:
        rel = os.path.relpath(str(folder), str(Path.cwd()))
    except Exception:
        rel = str(folder)
    md_lines.append("**Ubicación:** " + rel + "\n")
    md_lines.append("**Resumen profesional (breve):**\n")
    md_lines.append(summary + "\n")
    md_lines.append("**Temas clave:**\n")
    md_lines.append(", ".join(keywords) + "\n")
    md_lines.append("**Sugerencia de prompts para IA:**\n")
    md_lines.append(
        "- Resume este documento en 6-8 viñetas claras y numeradas.\n- Extrae 5 conceptos clave con definiciones breves.\n- Genera un índice de contenido con 6-8 entradas.\n"
    )

    md = "\n".join(md_lines)
    resumen_path = folder / "RESUMEN.md"
    resumen_path.write_text(md, encoding="utf-8")
    return True


def main():
    base = BASE
    if not base.exists():
        print("00_docs_base no existe en el cwd. Ejecuta desde la raíz del repo.")
        return

    folders = [p for p in base.iterdir() if p.is_dir() and not p.name.startswith("__")]
    processed = 0
    for folder in tqdm(folders, desc="Procesando carpetas"):
        ok = process_folder(folder)
        if ok:
            processed += 1

    print(f"Procesados: {processed} carpetas. Archivos RESUMEN.md creados donde aplicable.")


if __name__ == "__main__":
    main()
