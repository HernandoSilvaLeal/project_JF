import os
import re
from pathlib import Path
import pdfplumber
from collections import Counter
from tqdm import tqdm

BASE = Path("00_docs_base")

SPANISH_STOPWORDS = set([
    "de","la","que","el","en","y","a","los","del","se","las","por","un","para",
    "con","no","una","su","al","lo","como","más","pero","sus","le","ya","o","este",
    "sí","porque","esta","entre","cuando","muy","sin","sobre","también","me","hasta",
])


def tokenize(text: str):
    return re.findall(r"\w+", text.lower(), flags=re.UNICODE)


def extract_text_from_pdf(path: Path) -> str:
    parts = []
    try:
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                t = page.extract_text()
                if t:
                    parts.append(t)
    except Exception:
        return ""
    return "\n".join(parts)


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
    # heuristic: lines that look like headings (short, Title Case, or start with number)
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


def process(folder: Path):
    pdfs = list(folder.glob('*.pdf'))
    md_files = list(folder.glob('*.md'))
    source_name = None
    text = ""

    if pdfs:
        source_name = pdfs[0].name
        text = extract_text_from_pdf(pdfs[0])
    elif md_files:
        source_name = md_files[0].name
        try:
            text = md_files[0].read_text(encoding='utf-8')
        except Exception:
            text = md_files[0].read_text(encoding='latin-1')
    else:
        return False

    if not text.strip():
        return False

    short, long = summarize_long(text, short_sentences=4, long_sentences=16)
    keywords = top_keywords(text, n=18)
    headings = extract_headings_from_text(text)

    lines = []
    lines.append(f"# Resumen enriquecido: {folder.name}\n")
    lines.append(f"**Fuente original:** {source_name}\n")
    rel = os.path.relpath(str(folder), str(Path.cwd()))
    lines.append(f"**Ubicación:** {rel}\n")
    lines.append("## Resumen breve\n")
    lines.append(short + "\n")
    lines.append("## Resumen detallado\n")
    lines.append(long + "\n")
    lines.append("## Conceptos clave (definiciones sugeridas)\n")
    for k in keywords[:8]:
        lines.append(f"- **{k}**: (definir brevemente su significado y rol en el documento)\n")

    if headings:
        lines.append("## Índice sugerido\n")
        for i, h in enumerate(headings, 1):
            lines.append(f"{i}. {h}\n")

    lines.append("## Temas y palabras clave\n")
    lines.append(", ".join(keywords) + "\n")
    lines.append("## Prompts recomendados para IA\n")
    lines.append("- Redacta un resumen ejecutivo de máximo 250 palabras.\n- Extrae 10 preguntas de comprensión con respuestas breves.\n- Genera un índice con 8 secciones y un párrafo explicativo por sección.\n")

    out = folder / 'RESUMEN_NUTRIDO.md'
    out.write_text('\n'.join(lines), encoding='utf-8')
    return True


def main():
    if not BASE.exists():
        print('00_docs_base no encontrado')
        return

    folders = [p for p in BASE.iterdir() if p.is_dir()]
    created = []
    skipped = []
    for f in tqdm(folders, desc='Generando resúmenes enriquecidos'):
        ok = process(f)
        if ok:
            created.append(f.name)
        else:
            skipped.append(f.name)

    print(f"Creados: {len(created)} resúmenes enriquecidos")
    if skipped:
        print(f"Omitidos: {len(skipped)} (sin fuente o sin texto extraíble)")


if __name__ == '__main__':
    main()
