import os
import re
from pathlib import Path
from collections import Counter
from tqdm import tqdm
import pytesseract
from pdf2image import convert_from_path
from PIL import Image, ImageEnhance

# Configure tesseract path
TESSERACT_PATHS = [
    r"C:\Program Files\Tesseract-OCR\tesseract.exe",
    r"C:\ProgramData\chocolatey\lib\tesseract\tools\tesseract.exe",
    r"C:\tools\tesseract\tesseract.exe",
]
for tpath in TESSERACT_PATHS:
    if Path(tpath).exists():
        pytesseract.pytesseract.tesseract_cmd = tpath
        break

BASE = Path("00_docs_base")
POPPLER_PATH = Path("tools/poppler/poppler-24.08.0/Library/bin")

TARGET_FOLDERS = [
    "02 - Credo de los Apóstoles",
    "03 - Credo Niceno-Constantinopolitano",
    "05 - Credo de Atanasio",
    "11 - Confesión Belga (1561)",
    "12 - Catecismo de Heidelberg (1563)",
    "16 - Catecismo Menor de Westminster",
    "17 - Confesión Bautista de Fe de Londres (1689)",
]

SPANISH_STOPWORDS = set([
    "de","la","que","el","en","y","a","los","del","se","las","por","un","para",
    "con","no","una","su","al","lo","como","más","pero","sus","le","ya","o","este",
    "sí","porque","esta","entre","cuando","muy","sin","sobre","también","me","hasta",
])

def tokenize(text: str):
    return re.findall(r"\w+", text.lower(), flags=re.UNICODE)

def preprocess_image(img):
    """Enhance image for better OCR."""
    img = img.convert("L")
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2.5)
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(1.2)
    enhancer = ImageEnhance.Sharpness(img)
    img = enhancer.enhance(2.0)
    return img

def extract_with_pdf2image(pdf_path: Path) -> str:
    """Extract text using pdf2image + tesseract."""
    text_parts = []
    try:
        pages = convert_from_path(
            str(pdf_path),
            dpi=300,
            poppler_path=str(POPPLER_PATH.absolute()),
            fmt='png'
        )
        
        for i, page_img in enumerate(pages[:15]):  # Max 15 pages
            try:
                # Preprocess
                img = preprocess_image(page_img)
                
                # OCR with Spanish
                custom_config = r'--oem 3 --psm 6'
                text = pytesseract.image_to_string(img, lang='spa', config=custom_config)
                
                if text.strip():
                    text_parts.append(f"--- Página {i+1} ---\n{text}")
            except Exception as e:
                print(f"  Error en página {i+1}: {str(e)[:50]}")
                
    except Exception as e:
        print(f"  Error procesando PDF: {str(e)[:100]}")
        return ""
    
    return "\n\n".join(text_parts)

def split_sentences(text: str):
    s = re.split(r'(?<=[\.!?])\s+', text)
    return [x.strip() for x in s if x.strip()]

def summarize_long(text: str, short_sentences=5, long_sentences=15):
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

def top_keywords(text: str, n=20):
    words = [w for w in tokenize(text) if w not in SPANISH_STOPWORDS and len(w) > 3]
    c = Counter(words)
    return [w for w, _ in c.most_common(n)]

def process_folder(folder: Path):
    """Process folder with pdf2image OCR."""
    pdfs = list(folder.glob('*.pdf'))
    
    if not pdfs:
        return False
    
    pdf = pdfs[0]
    print(f"\nProcesando: {pdf.name}")
    
    text = extract_with_pdf2image(pdf)
    
    if not text.strip():
        print(f"  ✗ No se pudo extraer texto")
        return False

    # Save extracted text
    extract_dir = BASE / "__extracted__"
    extract_dir.mkdir(exist_ok=True)
    extract_txt = extract_dir / f"{folder.name}_pdf2image.txt"
    extract_txt.write_text(text, encoding='utf-8')
    
    short, long = summarize_long(text, short_sentences=6, long_sentences=18)
    keywords = top_keywords(text, n=20)

    lines = []
    lines.append(f"# Resumen profesional: {folder.name}\n")
    lines.append(f"**Fuente:** {pdf.name}\n")
    lines.append(f"**Ubicación:** {os.path.relpath(str(folder), str(Path.cwd()))}\n")
    lines.append("**Método:** OCR con pdf2image + Tesseract (DPI 300)\n")
    lines.append("---\n")
    lines.append("## Resumen ejecutivo\n")
    lines.append(short + "\n")
    lines.append("## Resumen detallado\n")
    lines.append(long + "\n")
    lines.append("## Conceptos y términos clave\n")
    for i, k in enumerate(keywords[:12], 1):
        lines.append(f"{i}. **{k}**\n")
    lines.append("\n## Palabras clave completas\n")
    lines.append(", ".join(keywords) + "\n")
    lines.append("## Uso con IAs\n")
    lines.append("**Prompts sugeridos:**\n")
    lines.append("- Resume este documento teológico en 8 puntos principales.\n")
    lines.append("- Extrae las afirmaciones doctrinales centrales.\n")
    lines.append("- Genera un índice temático del documento.\n")
    lines.append("- Identifica controversias históricas que aborda.\n")
    lines.append("- Compara con otros credos/confesiones contemporáneos.\n")

    out = folder / 'RESUMEN_COMPLETO.md'
    out.write_text('\n'.join(lines), encoding='utf-8')
    print(f"  ✓ Creado: RESUMEN_COMPLETO.md")
    return True

def main():
    if not BASE.exists():
        print('❌ 00_docs_base no encontrado')
        return
    
    if not POPPLER_PATH.exists():
        print(f'❌ Poppler no encontrado en: {POPPLER_PATH}')
        return

    print(f"✓ Usando Poppler desde: {POPPLER_PATH.absolute()}\n")
    
    folders = [BASE / name for name in TARGET_FOLDERS]
    created = []
    failed = []
    
    for f in folders:
        if f.exists() and f.is_dir():
            ok = process_folder(f)
            if ok:
                created.append(f.name)
            else:
                failed.append(f.name)
    
    print(f"\n{'='*60}")
    print(f"✅ Resúmenes creados: {len(created)}")
    for name in created:
        print(f"  ✓ {name}")
    
    if failed:
        print(f"\n❌ No procesados: {len(failed)}")
        for name in failed:
            print(f"  ✗ {name}")

if __name__ == '__main__':
    main()
