import os
import re
from pathlib import Path
from collections import Counter
from tqdm import tqdm
import pytesseract
import fitz  # PyMuPDF
from PIL import Image, ImageEnhance, ImageFilter
import io

BASE = Path("00_docs_base")
EXTRACT_DIR = BASE / "__extracted__"
EXTRACT_DIR.mkdir(parents=True, exist_ok=True)

SPANISH_STOPWORDS = set([
    "de","la","que","el","en","y","a","los","del","se","las","por","un","para",
    "con","no","una","su","al","lo","como","más","pero","sus","le","ya","o","este",
    "sí","porque","esta","entre","cuando","muy","sin","sobre","también","me","hasta",
])

# Target folders without summaries
TARGET_FOLDERS = {
    "02 - Credo de los Apóstoles",
    "03 - Credo Niceno-Constantinopolitano",
    "05 - Credo de Atanasio",
    "09 - Confesión de Fe RFJ (en construcción)",
    "11 - Confesión Belga (1561)",
    "12 - Catecismo de Heidelberg (1563)",
    "16 - Catecismo Menor de Westminster",
    "17 - Confesión Bautista de Fe de Londres (1689)",
}

def tokenize(text: str):
    return re.findall(r"\w+", text.lower(), flags=re.UNICODE)

def preprocess_image(img):
    """Enhance image for better OCR."""
    img = img.convert("L")  # Grayscale
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2)  # Increase contrast
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(1.1)
    return img

def extract_text_via_ocr_aggressive(pdf_path: Path, max_pages=10) -> str:
    """Extract text from PDF using aggressive OCR settings."""
    text_parts = []
    try:
        doc = fitz.open(str(pdf_path))
        for page_num, page in enumerate(doc[:max_pages]):
            try:
                # Higher DPI for better recognition
                pix = page.get_pixmap(matrix=fitz.Matrix(3, 3), alpha=False)
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                
                # Preprocess
                img = preprocess_image(img)
                
                # Aggressive OCR config
                config = "--psm 6 --oem 1"  # Full page of text, legacy OCR
                txt = pytesseract.image_to_string(img, lang='spa', config=config)
                
                if txt.strip():
                    text_parts.append(txt)
            except Exception as e:
                try:
                    # Fallback: try with different PSM
                    pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), alpha=False)
                    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                    config = "--psm 1"  # Auto page segmentation
                    txt = pytesseract.image_to_string(img, lang='spa', config=config)
                    if txt.strip():
                        text_parts.append(txt)
                except Exception:
                    pass
        doc.close()
    except Exception as e:
        return ""
    return "\n\n".join(text_parts)

def split_sentences(text: str):
    s = re.split(r'(?<=[\.!?])\s+', text)
    return [x.strip() for x in s if x.strip()]

def summarize_long(text: str, short_sentences=4, long_sentences=12):
    sentences = split_sentences(text)
    if not sentences:
        return "", ""
    words = [w for w in tokenize(text) if w not in SPANISH_STOPWORDS]
    freq = Counter(words)
    def score(sent):
        toks = tokenize(sent)
        if not toks:
            return 0
        return sum(freq.get(t, 0) for t in toks) / (len(toks) + 0.1)
    scored = [(i, score(s), s) for i, s in enumerate(sentences)]
    top_long = sorted(scored, key=lambda x: x[1], reverse=True)[:long_sentences]
    top_short = sorted(scored, key=lambda x: x[1], reverse=True)[:short_sentences]
    short_sorted = [s for (_, _, s) in sorted(top_short, key=lambda x: x[0])]
    long_sorted = [s for (_, _, s) in sorted(top_long, key=lambda x: x[0])]
    return "\n\n".join(short_sorted), "\n\n".join(long_sorted)

def top_keywords(text: str, n=15):
    words = [w for w in tokenize(text) if w not in SPANISH_STOPWORDS]
    c = Counter(words)
    return [w for w, _ in c.most_common(n)]

def extract_headings_from_text(text: str):
    headings = []
    for line in text.splitlines():
        line = line.strip()
        if not line or len(line) > 120:
            continue
        if re.match(r'^[0-9]+[\.).]', line) or (line.istitle() and 3 < len(line.split()) < 10):
            headings.append(line)
        elif 0 < len(line.split()) <= 6 and line.upper() == line:
            headings.append(line)
    return headings[:12]

def process_folder_aggressive_ocr(folder: Path):
    """Process folder with aggressive OCR."""
    pdfs = list(folder.glob('*.pdf'))
    md_files = list(folder.glob('*.md'))
    
    # Only process target folders without resumen
    if folder.name not in TARGET_FOLDERS:
        return False
    
    text = ""
    source_name = None

    if pdfs:
        source_name = pdfs[0].name
        text = extract_text_via_ocr_aggressive(pdfs[0], max_pages=15)
    
    if not text.strip() and md_files:
        source_name = md_files[0].name
        try:
            text = md_files[0].read_text(encoding='utf-8')
        except Exception:
            try:
                text = md_files[0].read_text(encoding='latin-1')
            except Exception:
                text = ""

    if not text.strip():
        return False

    short, long = summarize_long(text, short_sentences=4, long_sentences=16)
    keywords = top_keywords(text, n=18)
    headings = extract_headings_from_text(text)

    lines = []
    lines.append(f"# Resumen OCR (Agresivo): {folder.name}\n")
    lines.append(f"**Fuente original:** {source_name}\n")
    rel = os.path.relpath(str(folder), str(Path.cwd()))
    lines.append(f"**Ubicación:** {rel}\n")
    lines.append("**Nota:** Texto extraído mediante OCR agresivo (DPI 300, config PSM optimizada). Revisar para corregir errores de OCR\n")
    lines.append("## Resumen breve\n")
    lines.append(short + "\n")
    lines.append("## Resumen detallado\n")
    lines.append(long + "\n")
    lines.append("## Conceptos clave\n")
    for k in keywords[:8]:
        lines.append(f"- **{k}**: (revisar)\n")
    if headings:
        lines.append("## Índice sugerido\n")
        for i, h in enumerate(headings, 1):
            lines.append(f"{i}. {h}\n")
    lines.append("## Temas y palabras clave\n")
    lines.append(", ".join(keywords) + "\n")
    lines.append("## Prompts para mejorar con IA\n")
    lines.append("- Corrige errores OCR en este resumen.\n- Resume el documento en párrafos claros.\n- Extrae los 10 conceptos más importantes.\n")

    out = folder / 'RESUMEN_OCR_AGRESIVO.md'
    out.write_text('\n'.join(lines), encoding='utf-8')
    return True

def main():
    if not BASE.exists():
        print('00_docs_base no encontrado')
        return

    folders = [p for p in BASE.iterdir() if p.is_dir() and p.name in TARGET_FOLDERS]
    created = []
    skipped = []
    
    for f in tqdm(folders, desc='OCR Agresivo'):
        ok = process_folder_aggressive_ocr(f)
        if ok:
            created.append(f.name)
        else:
            skipped.append(f.name)

    print(f"\nCreados: {len(created)} resúmenes OCR agresivo")
    if created:
        print("Creados en:")
        for name in created:
            print(f"  - {name}")
    if skipped:
        print(f"\nNo se pudo OCR ({len(skipped)}):")
        for name in skipped:
            print(f"  - {name}")

if __name__ == '__main__':
    main()
