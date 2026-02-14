import os
import re

def fix_corrupted_md_file(filepath):
    """
    Repara archivos MD que tienen '?' entre cada carácter.
    Patrón: ?#? ?1?.? ?G?e?n?e?r?a?l? -> # 1. General
    """
    try:
        with open(filepath, 'rb') as f:
            raw_bytes = f.read()
        
        # Intentar decodificar correctamente
        # La corrupción parece venir de leer UTF-8 como si fuera otro encoding
        try:
            # Primero intentar UTF-16
            content = raw_bytes.decode('utf-16-le', errors='ignore')
            # Limpiar caracteres NUL
            content = content.replace('\x00', '')
        except:
            # Si falla, intentar UTF-8
            content = raw_bytes.decode('utf-8', errors='ignore')
        
        # Si aún está corrompido, eliminar los '?' espurios
        if content.count('?') > len(content) * 0.3:  # Si más del 30% son '?'
            # Eliminar el patrón ?X? donde X es cualquier carácter
            lines = []
            for line in content.split('\n'):
                cleaned_line = ''
                i = 0
                while i < len(line):
                    if line[i] == '?':
                        # Saltar el '?'
                        i += 1
                    else:
                        cleaned_line += line[i]
                        i += 1
                lines.append(cleaned_line)
            content = '\n'.join(lines)
        
        # Guardar archivo corregido
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True, len(content)
    
    except Exception as e:
        return False, str(e)

# Lista de archivos RFJ
files_to_fix = [
    r"C:\Users\PC-AORUS\Desktop\RFJ 2026\01_Core_Doctrinal\1. Core Doctrinal - Kernel Biblico (DESACTUALIZADO A 2015).md",
    r"C:\Users\PC-AORUS\Desktop\RFJ 2026\01_Core_Doctrinal\1. Core Doctrinal -  Kernel Biblico v1.md",
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

print("=" * 80)
print("REPARANDO ARCHIVOS MD CORROMPIDOS")
print("=" * 80)

success_count = 0
for filepath in files_to_fix:
    if os.path.exists(filepath):
        filename = os.path.basename(filepath)
        result = fix_corrupted_md_file(filepath)
        
        if result[0]:
            success_count += 1
            print(f"✓ {filename[:60]}")
            print(f"  Tamaño final: {result[1]} caracteres\n")
        else:
            print(f"✗ {filename}: {result[1]}\n")
    else:
        print(f"⚠ No encontrado: {os.path.basename(filepath)}\n")

print("=" * 80)
print(f"✓ Reparados: {success_count}/{len(files_to_fix)} archivos")
print("=" * 80)
