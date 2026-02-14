import os

def fix_corrupted_file(filepath):
    """Repara archivos MD corrompidos con caracteres extraños entre letras"""
    try:
        # Leer con codificación correcta
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # El patrón de corrupción parece ser caracteres '?' entre letras normales
        # Crear nueva versión limpia
        cleaned = ""
        skip_next = False
        
        for i, char in enumerate(content):
            # Si es un '?' que no es realmente un signo de interrogación válido
            if char == '?' and i > 0 and i < len(content) - 1:
                # Verificar si está entre caracteres normales (patrón de corrupción)
                prev_char = content[i-1]
                next_char = content[i+1] if i+1 < len(content) else ''
                
                # Si el '?' está rodeado de letras/números, probablemente es corrupción
                if (prev_char.isalnum() or prev_char.isspace()) and next_char not in ('\n', '\r', ''):
                    continue  # Saltar este '?'
            
            cleaned += char
        
        # Guardar archivo corregido
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(cleaned)
        
        return True, len(content), len(cleaned)
    
    except Exception as e:
        return False, 0, 0, str(e)

# Archivos a reparar
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

print("Reparando archivos MD corrompidos...")
print("="*80)

fixed_count = 0
for filepath in files_to_fix:
    if os.path.exists(filepath):
        filename = os.path.basename(filepath)
        result = fix_corrupted_file(filepath)
        
        if result[0]:
            fixed_count += 1
            print(f"✓ {filename}")
            print(f"  {result[1]} → {result[2]} caracteres")
        else:
            print(f"✗ {filename}: {result[3] if len(result) > 3 else 'Error'}")
    else:
        print(f"⚠ Archivo no encontrado: {os.path.basename(filepath)}")

print("\n" + "="*80)
print(f"✓ Archivos reparados: {fixed_count}/{len(files_to_fix)}")
