import os
import re

def clean_markdown_final(content):
    """Limpia y formatea todos los archivos MD de forma consistente y segura"""
    
    # 1. Eliminar imágenes en base64
    content = re.sub(r'!\[.*?\]\(data:image/[^)]+\)\n*', '', content)
    
    # 2. Convertir __texto__ a formatos apropiados
    # Si está en su propia línea y parece ser un título con número
    content = re.sub(r'^__(\d+)\.?\s+([^_]+)__\s*$', r'# \1. \2', content, flags=re.MULTILINE)
    # Si está en su propia línea sin número (subtítulos)
    content = re.sub(r'^__([^_\d][^_]+)__\s*$', r'## \1', content, flags=re.MULTILINE)
    
    # 3. Limpiar escapes
    content = content.replace('\\(', '(')
    content = content.replace('\\)', ')')
    content = content.replace('\\-', '-')
    content = content.replace('\\!', '!')
    content = content.replace('\\?', '?')
    content = re.sub(r'(\d+)\\\.',  r'\1.', content)
    
    # 4. Normalizar listas
    content = re.sub(r'^-([^\s-])', r'- \1', content, flags=re.MULTILINE)
    content = re.sub(r'^(\d+)\.([^\s])', r'\1. \2', content, flags=re.MULTILINE)
    
    # 5. Limpiar múltiples líneas vacías
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # 6. Asegurar espaciado alrededor de títulos
    content = re.sub(r'([^\n])\n(#{1,6}\s)', r'\1\n\n\2', content)
    content = re.sub(r'(#{1,6}\s[^\n]+)\n([^#\n])', r'\1\n\n\2', content)
    
    # 7. Limpiar espacios al final de líneas
    content = re.sub(r' +$', '', content, flags=re.MULTILINE)
    
    # 8. Asegurar salto de línea final
    if not content.endswith('\n'):
        content += '\n'
    
    return content

# Archivos Core_* principales
core_files = [
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

print("="*80)
print("LIMPIEZA Y FORMATEO FINAL DE ARCHIVOS MARKDOWN")
print("="*80)

success = 0
for filepath in core_files:
    if os.path.exists(filepath):
        try:
            # Leer archivo
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_size = len(content)
            
            # Limpiar
            cleaned = clean_markdown_final(content)
            
            # Guardar
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(cleaned)
            
            success += 1
            filename = os.path.basename(filepath)
            print(f"✓ {filename[:60]}")
            print(f"  {original_size:,} → {len(cleaned):,} bytes")
            
        except Exception as e:
            print(f"✗ {os.path.basename(filepath)}: {e}")
    else:
        print(f"⚠ No encontrado: {os.path.basename(filepath)}")

print("\n" + "="*80)
print(f"✓ Archivos procesados: {success}/{len(core_files)}")
print("="*80)
