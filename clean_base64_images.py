import re

# Ruta del archivo
file_path = r"C:\Users\PC-AORUS\Desktop\RFJ 2026\01_Core_Doctrinal\MARDOWN.md"

# Leer el archivo
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Eliminar todas las imágenes en base64
# Patrón para detectar imágenes Markdown con data:image en base64
pattern = r'!\[.*?\]\(data:image/[^)]+\)'

# Contar cuántas imágenes se encontraron
matches = re.findall(pattern, content)
print(f"Se encontraron {len(matches)} imágenes en base64")

# Eliminar las imágenes
cleaned_content = re.sub(pattern, '', content)

# Limpiar líneas vacías múltiples dejando solo una
cleaned_content = re.sub(r'\n{3,}', '\n\n', cleaned_content)

# Guardar el archivo limpio
with open(file_path, "w", encoding="utf-8") as f:
    f.write(cleaned_content)

print(f"✓ Archivo limpiado exitosamente")
print(f"✓ Se eliminaron {len(matches)} imágenes en base64")
