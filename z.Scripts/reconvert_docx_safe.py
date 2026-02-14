import mammoth
import re
import os

def format_markdown_safe(content):
    """Formatea Markdown de manera segura sin corromper la codificación"""
    
    # Eliminar tags HTML de ancla
    content = re.sub(r'<a id="[^"]*"></a>\n*', '', content)
    
    # Convertir títulos con formato __texto__ a títulos Markdown
    # Solo si están en su propia línea
    lines = content.split('\n')
    formatted_lines = []
    
    for line in lines:
        # __1\. Título__ -> # 1. Título
        if re.match(r'^__\d+\\?\.\s+[^_]+__\s*$', line):
            line = re.sub(r'^__(\d+)\\?\.', r'# \1.', line)
            line = line.replace('__', '')
        # __Subtítulo__ -> ## Subtítulo (pero no números)
        elif re.match(r'^__[^_\d][^_]+__\s*$', line):
            line = '## ' + line.replace('__', '')
        
        formatted_lines.append(line)
    
    content = '\n'.join(formatted_lines)
    
    # Limpiar escapes innecesarios
    content = content.replace('\\(', '(')
    content = content.replace('\\)', ')')
    content = content.replace('\\-', '-')
    content = content.replace('\\!', '!')
    content = content.replace('\\?', '?')
    content = re.sub(r'(\d+)\\\.',  r'\1.', content)
    
    # Normalizar listas
    content = re.sub(r'^-([^\s-])', r'- \1', content, flags=re.MULTILINE)
    content = re.sub(r'^(\d+)\.([^\s])', r'\1. \2', content, flags=re.MULTILINE)
    
    # Limpiar múltiples líneas vacías
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # Espaciado alrededor de títulos
    content = re.sub(r'([^\n])\n(#{1,6}\s)', r'\1\n\n\2', content)
    content = re.sub(r'(#{1,6}\s[^\n]+)\n([^#\n])', r'\1\n\n\2', content)
    
    # Limpiar espacios al final
    content = re.sub(r' +$', '', content, flags=re.MULTILINE)
    
    # Asegurar salto de línea final
    if not content.endswith('\n'):
        content += '\n'
    
    return content

# Reconvertir el archivo .docx
print("="*80)
print("RECONVIRTIENDO ARCHIVO .DOCX A MARKDOWN")
print("="*80)

docx_path = r"C:\Users\PC-AORUS\Desktop\RFJ 2026\01_Core_Doctrinal\1. Core Doctrinal - Kernel Biblico (DESACTUALIZADO A 2015).docx"
output_path = r"C:\Users\PC-AORUS\Desktop\RFJ 2026\01_Core_Doctrinal\1. Core Doctrinal - Kernel Biblico (DESACTUALIZADO A 2015).md"

try:
    with open(docx_path, "rb") as docx_file:
        result = mammoth.convert_to_markdown(docx_file)
        markdown_content = result.value
    
    print(f"✓ Archivo .docx leído correctamente")
    print(f"  Tamaño: {len(markdown_content)} caracteres")
    
    # Aplicar formateo seguro
    formatted_content = format_markdown_safe(markdown_content)
    
    print(f"✓ Formateo aplicado")
    print(f"  Tamaño final: {len(formatted_content)} caracteres")
    
    # Guardar con UTF-8
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(formatted_content)
    
    print(f"✓ Archivo guardado: {os.path.basename(output_path)}")
    
    # Mostrar primeras líneas para verificar
    print(f"\nPrimeras líneas del contenido:")
    print("-"*80)
    print(formatted_content[:500])
    print("-"*80)
    
except Exception as e:
    print(f"✗ Error: {e}")

print("\n" + "="*80)
print("✓ CONVERSIÓN COMPLETADA")
print("="*80)
