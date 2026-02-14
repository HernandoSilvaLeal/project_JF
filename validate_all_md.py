import os
import re

def validate_and_report_markdown(filepath):
    """Valida y reporta el estado de un archivo Markdown"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Estadísticas
        lines = content.split('\n')
        headers = len(re.findall(r'^#{1,6}\s', content, re.MULTILINE))
        lists = len(re.findall(r'^[\s]*[-*+]\s', content, re.MULTILINE))
        bold_patterns = len(re.findall(r'__[^_]+__', content))
        data_images = len(re.findall(r'data:image', content))
        empty_lines = len([l for l in lines if not l.strip()])
        
        issues = []
        if bold_patterns > 5:
            issues.append(f"⚠ Contiene {bold_patterns} patrones de texto en negrita (__texto__)")
        if data_images > 0:
            issues.append(f"⚠ Contiene {data_images} imágenes en base64")
        if content.count('?') > len(content) * 0.05:
            issues.append(f"⚠ Posible corrupción: muchos caracteres '?'")
        
        return {
            'valid': True,
            'lines': len(lines),
            'headers': headers,
            'lists': lists,
            'empty_lines': empty_lines,
            'size': len(content),
            'issues': issues,
            'has_bold': bold_patterns > 0,
            'has_images': data_images > 0
        }
    except Exception as e:
        return {'valid': False, 'error': str(e)}

# Buscar todos los archivos .md del proyecto RFJ
base_path = r"C:\Users\PC-AORUS\Desktop\RFJ 2026"
md_files = []

for root, dirs, files in os.walk(base_path):
    # Excluir venv
    if '.venv' in root:
        continue
    for file in files:
        if file.endswith('.md'):
            filepath = os.path.join(root, file)
            # Solo si está en una carpeta de Core_*
            if any(x in root for x in ['Core_', '01_', '02_', '03_', '04_', '05_', '06_', '07_', '08_', '09_']):
                md_files.append(filepath)

print("="*100)
print("VALIDACIÓN DE ARCHIVOS MARKDOWN - RFJ 2026")
print("="*100)

for filepath in sorted(md_files):
    relative_path = os.path.relpath(filepath, base_path)
    report = validate_and_report_markdown(filepath)
    
    if report['valid']:
        print(f"\n✓ {relative_path}")
        print(f"   Líneas: {report['lines']} | Títulos: {report['headers']} | Listas: {report['lists']} | Tamaño: {report['size']:,} bytes")
        
        if report['issues']:
            for issue in report['issues']:
                print(f"   {issue}")
        else:
            print(f"   ✓ Sin problemas detectados")
    else:
        print(f"\n✗ {relative_path}")
        print(f"   Error: {report['error']}")

print("\n" + "="*100)
print(f"Total de archivos validados: {len(md_files)}")
print("="*100)
