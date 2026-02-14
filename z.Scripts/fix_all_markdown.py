import os
import re

def clean_markdown(content):
    """Limpia y formatea correctamente el contenido Markdown"""
    
    # Eliminar tags HTML de ancla
    content = re.sub(r'<a id="[^"]*"></a>\n*', '', content)
    
    # Convertir títulos en negrita a títulos Markdown apropiados
    # __1\. Generalidades__ -> # 1. Generalidades
    content = re.sub(r'^__(\d+\\?\.\s+[^_]+)__\s*$', r'# \1', content, flags=re.MULTILINE)
    
    # Convertir subtítulos en negrita a subtítulos Markdown
    # __¿Qué es...?__ -> ## ¿Qué es...?
    content = re.sub(r'^__([^_\d][^_]+)__\s*$', r'## \1', content, flags=re.MULTILINE)
    
    # Limpiar escapes innecesarios en números de secciones
    content = re.sub(r'(\d+)\\\.', r'\1.', content)
    
    # Limpiar escapes innecesarios de paréntesis
    content = re.sub(r'\\\(', '(', content)
    content = re.sub(r'\\\)', ')', content)
    
    # Limpiar escapes de guiones
    content = re.sub(r'\\-', '-', content)
    
    # Limpiar escapes de puntos de exclamación e interrogación
    content = re.sub(r'\\!', '!', content)
    content = re.sub(r'\\?', '?', content)
    
    # Normalizar listas con viñetas
    # Asegurar que las listas tengan espacio después del guión
    content = re.sub(r'^-\s*([^\s])', r'- \1', content, flags=re.MULTILINE)
    
    # Normalizar listas numeradas
    content = re.sub(r'^(\d+)\.\s*([^\s])', r'\1. \2', content, flags=re.MULTILINE)
    
    # Limpiar líneas vacías múltiples (máximo 2 saltos de línea seguidos)
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # Asegurar que los títulos tengan línea en blanco antes (excepto al inicio)
    content = re.sub(r'([^\n])\n(#{1,6}\s)', r'\1\n\n\2', content)
    
    # Asegurar que los títulos tengan línea en blanco después
    content = re.sub(r'(#{1,6}\s[^\n]+)\n([^#\n])', r'\1\n\n\2', content)
    
    # Limpiar espacios al final de las líneas
    content = re.sub(r' +$', '', content, flags=re.MULTILINE)
    
    # Asegurar que el archivo termine con una línea nueva
    if not content.endswith('\n'):
        content += '\n'
    
    return content

def process_markdown_file(filepath):
    """Procesa un archivo Markdown individual"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_length = len(content)
        cleaned_content = clean_markdown(content)
        
        if cleaned_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(cleaned_content)
            return True, f"Corregido ({original_length} → {len(cleaned_content)} chars)"
        else:
            return False, "Sin cambios necesarios"
    except Exception as e:
        return False, f"Error: {e}"

def main():
    base_path = r"C:\Users\PC-AORUS\Desktop\RFJ 2026"
    
    # Buscar todos los archivos .md
    md_files = []
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    
    print(f"Encontrados {len(md_files)} archivos .md\n")
    print("="*80)
    
    modified_count = 0
    for filepath in sorted(md_files):
        relative_path = os.path.relpath(filepath, base_path)
        changed, message = process_markdown_file(filepath)
        
        if changed:
            modified_count += 1
            print(f"✓ {relative_path}")
            print(f"  {message}")
        else:
            print(f"○ {relative_path}")
            print(f"  {message}")
        print()
    
    print("="*80)
    print(f"\n✓ Proceso completado")
    print(f"  Archivos modificados: {modified_count}/{len(md_files)}")
    print(f"  Archivos sin cambios: {len(md_files) - modified_count}/{len(md_files)}")

if __name__ == "__main__":
    main()
