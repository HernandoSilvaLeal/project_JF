import os
import re
from pathlib import Path
from collections import Counter
from tqdm import tqdm
import pytesseract
import fitz  # PyMuPDF
from PIL import Image
import io

BASE = Path("00_docs_base")
EXTRACT_DIR = BASE / "__extracted__"
EXTRACT_DIR.mkdir(parents=True, exist_ok=True)

SPANISH_STOPWORDS = set([
    "de","la","que","el","en","y","a","los","del","se","las","por","un","para",
    "con","no","una","su","al","lo","como","más","pero","sus","le","ya","o","este",
    "sí","porque","esta","entre","cuando","muy","sin","sobre","también","me","hasta",
])

def tokenize(text: str):
    return re.findall(r"\w+", text.lower(), flags=re.UNICODE)

def extract_text_via_ocr(pdf_path: Path, timeout_pages=None) -> str:
    """Extract text from PDF using OCR with PyMuPDF + pytesseract."""
    text_parts = []
    try:
        doc = fitz.open(str(pdf_path))
        max_pages = timeout_pages if timeout_pages else len(doc)
        for page_num, page in enumerate(doc[:max_pages]):
            try:
                pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                txt = pytesseract.image_to_string(img, lang='spa')
                if txt.strip():
                    text_parts.append(txt)
            except Exception as e:
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

def process_folder_with_ocr(folder: Path):
    """Process folder with OCR if no text available already."""
    pdfs = list(folder.glob('*.pdf'))
    md_files = list(folder.glob('*.md'))
    text = ""
    source_name = None

    if pdfs:
        source_name = pdfs[0].name
        # Try OCR on PDF
        text = extract_text_via_ocr(pdfs[0], timeout_pages=5)
    
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
    lines.append(f"# Resumen con OCR: {folder.name}\n")
    lines.append(f"**Fuente original:** {source_name}\n")
    rel = os.path.relpath(str(folder), str(Path.cwd()))
    lines.append(f"**Ubicación:** {rel}\n")
    lines.append("**Nota:** Texto extraído mediante OCR (puede contener errores de reconocimiento)\n")
    lines.append("## Resumen breve\n")
    lines.append(short + "\n")
    lines.append("## Resumen detallado\n")
    lines.append(long + "\n")
    lines.append("## Conceptos clave\n")
    for k in keywords[:8]:
        lines.append(f"- **{k}**: (revisar y definir rol en el documento)\n")
    if headings:
        lines.append("## Índice sugerido\n")
        for i, h in enumerate(headings, 1):
            lines.append(f"{i}. {h}\n")
    lines.append("## Temas y palabras clave\n")
    lines.append(", ".join(keywords) + "\n")
    lines.append("## Prompts recomendados para IA\n")
    lines.append("- Revisa y mejora este resumen extraído por OCR.\n- Extrae 10 preguntas clave sobre el documento.\n- Genera un índice estructurado con secciones.\n")

    out = folder / 'RESUMEN_OCR.md'
    out.write_text('\n'.join(lines), encoding='utf-8')
    return True

def main():
    if not BASE.exists():
        print('00_docs_base no encontrado')
        return

    folders = [p for p in BASE.iterdir() if p.is_dir() and not p.name.startswith('__')]
    created = []
    skipped = []
    
    for f in tqdm(folders, desc='OCR y resúmenes'):
        ok = process_folder_with_ocr(f)
        if ok:
            created.append(f.name)
        else:
            skipped.append(f.name)

    print(f"\nCreados: {len(created)} resúmenes con OCR")
    print(f"Carpetas sin resumen OCR: {len(skipped)}")

if __name__ == '__main__':
    main()
