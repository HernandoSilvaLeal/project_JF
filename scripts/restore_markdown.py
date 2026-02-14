import os
import re

def clean_markdown_safe(content):
    """Limpia y formatea correctamente el contenido Markdown sin romper la codificación"""
    
    # Eliminar tags HTML de ancla
    content = re.sub(r'<a id="[^"]*"></a>\s*', '', content)
    
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
    
    # Normalizar listas con viñetas (asegurar espacio después del guión)
    content = re.sub(r'^-([^\s])', r'- \1', content, flags=re.MULTILINE)
    
    # Normalizar listas numeradas
    content = re.sub(r'^(\d+)\.([^\s])', r'\1. \2', content, flags=re.MULTILINE)
    
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

# Archivos principales del proyecto RFJ  
files_to_fix = [
    r"C:\Users\PC-AORUS\Desktop\RFJ 2026\01_Core_Doctrinal\1. Core Doctrinal - Kernel Biblico (DESACTUALIZADO A 2015).md",
    r"C:\Users\PC-AORUS\Desktop\RFJ 2026\01_Core_Doctrinal\1. Core Doctrinal - Kernel Biblico v1.md",
    r"C:\Users\PC-AORUS\Desktop\RFJ 2026\02_Core_Operativo\2. Core Operativo - Tejido Vivo SINTESIS.md",
    r"C:\Users\PC-AORUS\Desktop\RFJ 2026\02_Core_Operativo\2. Core Operativo - Tejido Vivo y Creciente TABLA COMPLETA.md",
    r"C:\Users\PC-AORUS\Desktop\RFJ 2026\03_Core_Misional\3. Core Misional - Taxonomia de Frentes OS Sintetizada.md",
    r"C:\Users\PC-AORUS\Desktop\RFJ 2026\04_Core_Producto_99_Servilletas\04_Core_Producto_99_Servilletas.md",
    r"C:\Users\PC-AORUS\Desktop\RFJ 2026\05_Core_Alcance_Doctrinal\05_Core_Alcance_Doctrinal.md",
    r"C:\Users\PC-AORUS\Desktop\RFJ 2026\06_Core_Canales\06_Core_Canales.md",
    r"C:\Users\PC-AORUS\Desktop\RFJ 2026\07_Core_Plataforma_Web_SaaS\07_Core_Plataforma_Web_SaaS.md",
    r"C:\Users\PC-AORUS\Desktop\RFJ 2026\08_Core_Agentes_IA\08_Core_Agentes_IA.md",
    r"C:\Users\PC-AORUS\Desktop\RFJ 2026\09_Core_Ingenieria\09_Core_Ingenieria.md",
]

print("Restaurando archivos desde conversión .docx...")
print("="*80)

# Primero, reconvertir el archivo principal desde .docx
import mammoth

docx_path = r"C:\Users\PC-AORUS\Desktop\RFJ 2026\01_Core_Doctrinal\1. Core Doctrinal - Kernel Biblico (DESACTUALIZADO A 2015).docx"
output_md = r"C:\Users\PC-AORUS\Desktop\RFJ 2026\01_Core_Doctrinal\1. Core Doctrinal - Kernel Biblico (DESACTUALIZADO A 2015).md"

print(f"\n1. Reconvirtiendo desde .docx...")
with open(docx_path, "rb") as docx_file:
    result = mammoth.convert_to_markdown(docx_file)
    markdown_text = result.value
    
    # Aplicar limpieza segura
    cleaned = clean_markdown_safe(markdown_text)
    
    with open(output_md, "w", encoding="utf-8") as f:
        f.write(cleaned)
    
    print(f"   ✓ Archivo reconvertido correctamente")
    print(f"   Tamaño: {len(cleaned)} caracteres")

print("\n" + "="*80)
print("✓ Restauración completada")
