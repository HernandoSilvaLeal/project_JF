import mammoth
import re

# Ruta del archivo .docx
docx_path = r"C:\Users\PC-AORUS\Desktop\RFJ 2026\01_Core_Doctrinal\1. Core Doctrinal - Kernel Biblico (DESACTUALIZADO A 2015).docx"
output_path = r"C:\Users\PC-AORUS\Desktop\RFJ 2026\01_Core_Doctrinal\MARDOWN.md"

# Convertir .docx a Markdown
with open(docx_path, "rb") as docx_file:
    result = mammoth.convert_to_markdown(docx_file)
    markdown_text = result.value
    
    # Limpiar y mejorar el formato
    # Asegurar que los títulos tengan espacio después del #
    markdown_text = re.sub(r'^(#{1,6})([^\s])', r'\1 \2', markdown_text, flags=re.MULTILINE)
    
    # Asegurar líneas en blanco entre secciones
    markdown_text = re.sub(r'\n(#{1,6}\s)', r'\n\n\1', markdown_text)
    
    # Escribir al archivo de salida
    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write(markdown_text)
    
    print(f"✓ Conversión completada exitosamente")
    print(f"✓ Archivo guardado en: {output_path}")
    print(f"\nPrimeras líneas del contenido:")
    print("=" * 60)
    print(markdown_text[:500])
