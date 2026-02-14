import os
import re
from pathlib import Path
from collections import Counter
from tqdm import tqdm

BASE = Path("00_docs_base")

SPANISH_STOPWORDS = set([
    "de","la","que","el","en","y","a","los","del","se","las","por","un","para",
    "con","no","una","su","al","lo","como","más","pero","sus","le","ya","o","este",
    "sí","porque","esta","entre","cuando","muy","sin","sobre","también","me","hasta",
])

TARGET_FOLDERS = [
    "02 - Credo de los Apóstoles",
    "03 - Credo Niceno-Constantinopolitano",
    "05 - Credo de Atanasio",
    "09 - Confesión de Fe RFJ (en construcción)",
    "11 - Confesión Belga (1561)",
    "12 - Catecismo de Heidelberg (1563)",
    "16 - Catecismo Menor de Westminster",
    "17 - Confesión Bautista de Fe de Londres (1689)",
]

def tokenize(text: str):
    return re.findall(r"\w+", text.lower(), flags=re.UNICODE)

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

def process_from_md(folder: Path):
    """Generate summary from existing MD files."""
    md_files = [f for f in folder.glob('*.md') if not f.name.startswith('RESUMEN')]
    
    if not md_files:
        return False
    
    text = ""
    source_name = md_files[0].name
    
    try:
        text = md_files[0].read_text(encoding='utf-8')
    except Exception:
        try:
            text = md_files[0].read_text(encoding='latin-1')
        except Exception:
            return False
    
    if not text.strip():
        return False

    short, long = summarize_long(text, short_sentences=5, long_sentences=18)
    keywords = top_keywords(text, n=20)
    headings = extract_headings_from_text(text)

    lines = []
    lines.append(f"# Resumen enriquecido: {folder.name}\n")
    lines.append(f"**Fuente original:** {source_name}\n")
    rel = os.path.relpath(str(folder), str(Path.cwd()))
    lines.append(f"**Ubicación:** {rel}\n")
    lines.append("**Tipo:** Documento teológico/confesional\n")
    lines.append("## Resumen ejecutivo\n")
    lines.append(short + "\n")
    lines.append("## Resumen detallado\n")
    lines.append(long + "\n")
    lines.append("## Conceptos clave para profundizar\n")
    for k in keywords[:10]:
        lines.append(f"- **{k}**\n")
    
    if headings:
        lines.append("## Estructura del documento\n")
        for i, h in enumerate(headings, 1):
            lines.append(f"{i}. {h}\n")
    
    lines.append("## Palabras clave y temas\n")
    lines.append(", ".join(keywords) + "\n")
    lines.append("## Prompts sugeridos para análisis con IA\n")
    lines.append("- Resume este credo/confesión en 5 puntos clave.\n")
    lines.append("- Extrae las afirmaciones teológicas principales y sus fundamentos bíblicos.\n")
    lines.append("- Compara este documento con otros credos históricos.\n")
    lines.append("- Genera un glosario de términos teológicos del documento.\n")
    lines.append("- Identifica controversias o herejías que este documento aborda.\n")

    out = folder / 'RESUMEN_FINAL.md'
    out.write_text('\n'.join(lines), encoding='utf-8')
    return True

def main():
    if not BASE.exists():
        print('00_docs_base no encontrado')
        return

    folders = [BASE / name for name in TARGET_FOLDERS]
    created = []
    skipped = []
    
    for f in tqdm(folders, desc='Generando resúmenes desde MD'):
        if f.exists() and f.is_dir():
            ok = process_from_md(f)
            if ok:
                created.append(f.name)
            else:
                skipped.append(f.name)
        else:
            skipped.append(f.name)

    print(f"\n✅ Creados: {len(created)} resúmenes (RESUMEN_FINAL.md)")
    if created:
        for name in created:
            print(f"  ✓ {name}")
    
    if skipped:
        print(f"\n⚠️  Sin generar ({len(skipped)}):")
        for name in skipped:
            print(f"  ✗ {name}")

if __name__ == '__main__':
    main()
