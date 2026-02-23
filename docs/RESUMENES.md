# 📚 Proyecto RFJ 2026 - Sistema de Documentación con Resúmenes IA

## ✅ Completado

### 1. Visor PDF en VS Code
- **Extensión instalada:** PDF Viewer (tomoki1207.pdf v1.2.2)
- **Uso:** Clic derecho en cualquier `.pdf` → "Open With" → "PDF Viewer"

### 2. Resúmenes Markdown generados automáticamente

**Total: 10/18 carpetas con resúmenes completos (55.6%)**

## 📊 Estado detallado por carpeta

### ✅ Carpetas CON resúmenes (10)

| # | Carpeta | Archivos generados |
|---|---------|-------------------|
| 1 | 00 - Teoria Definitiva de Como Crear una Revolucion Ideologica | ✓ RESUMEN_NUTRIDO.md<br>✓ RESUMEN_OCR.md |
| 2 | 01 - Biblia RVR1960 (RVR60) - Referencia | ✓ RESUMEN_NUTRIDO.md<br>✓ RESUMEN_OCR.md |
| 3 | 04 - Credo de Calcedonia | ✓ RESUMEN.md<br>✓ RESUMEN_NUTRIDO.md |
| 4 | 06 - Tesis de Barmen (1934) | ✓ RESUMEN.md<br>✓ RESUMEN_NUTRIDO.md<br>✓ RESUMEN_OCR.md |
| 5 | 07 - Declaración de Chicago sobre la Hermenéutica Bíblica | ✓ RESUMEN.md<br>✓ RESUMEN_NUTRIDO.md |
| 6 | 08 - Juntos por el Evangelio - Afirmaciones y Negaciones | ✓ RESUMEN.md<br>✓ RESUMEN_NUTRIDO.md |
| 7 | 10 - Confesión de Fe Escocesa (1560) | ✓ RESUMEN.md<br>✓ RESUMEN_NUTRIDO.md |
| 8 | 13 - Segunda Confesión Helvética (1566) | ✓ RESUMEN.md<br>✓ RESUMEN_NUTRIDO.md<br>✓ RESUMEN_OCR.md |
| 9 | 14 - Confesión de Fe de Westminster (1646) | ✓ RESUMEN.md<br>✓ RESUMEN_NUTRIDO.md |
| 10 | 15 - Catecismo Mayor de Westminster | ✓ RESUMEN.md<br>✓ RESUMEN_NUTRIDO.md |

### ⚠️ Carpetas PENDIENTES (8) - PDFs corruptos

| # | Carpeta | Estado | Archivo |
|---|---------|--------|---------|
| 1 | 02 - Credo de los Apóstoles | PDF corrupto, MD vacío | RESUMEN_PENDIENTE.md |
| 2 | 03 - Credo Niceno-Constantinopolitano | PDF corrupto, MD vacío | RESUMEN_PENDIENTE.md |
| 3 | 05 - Credo de Atanasio | PDF corrupto, MD vacío | RESUMEN_PENDIENTE.md |
| 4 | 09 - Confesión de Fe RFJ (en construcción) | En construcción | RESUMEN_PENDIENTE.md |
| 5 | 11 - Confesión Belga (1561) | PDF corrupto, MD vacío | RESUMEN_PENDIENTE.md |
| 6 | 12 - Catecismo de Heidelberg (1563) | PDF corrupto, MD vacío | RESUMEN_PENDIENTE.md |
| 7 | 16 - Catecismo Menor de Westminster | PDF procesable pero tesseract faltante | RESUMEN_PENDIENTE.md |
| 8 | 17 - Confesión Bautista de Fe de Londres (1689) | PDF procesable pero tesseract faltante | RESUMEN_PENDIENTE.md |

## 🛠️ Scripts creados

### Ubicación: `scripts/`

1. **extract_and_summarize.py** - Extracción básica de PDFs con texto
2. **generate_enriched_summaries.py** - Resúmenes enriquecidos con IA
3. **ocr_and_generate_summaries.py** - OCR básico con PyMuPDF
4. **ocr_aggressive.py** - OCR agresivo (DPI 300, preprocesamiento)
5. **generate_from_md.py** - Generación desde archivos MD
6. **ocr_pdf2image_final.py** - OCR con pdf2image + Poppler

### Dependencias instaladas

```bash
# Python packages en .venv/
pdfplumber
tqdm
pytesseract
PyMuPDF
Pillow
pdf2image
```

### Herramientas externas

- ✓ Poppler portable descargado en: `tools/poppler/`
- ⚠️ Tesseract-OCR (requiere instalación manual)

## 📋 Cómo completar las 8 carpetas pendientes

### Opción A: Procesamiento manual (recomendado)

1. **Abre cada PDF con el visor de VS Code:**
   - Clic derecho en el PDF → "Open With" → "PDF Viewer"

2. **Copia el texto al archivo `.md` correspondiente:**
   - Ejemplo: copia contenido de `Credo de los Apóstoles.pdf` → `Credo de los Apóstoles.md`

3. **Ejecuta el script de resúmenes:**
   ```powershell
   & 'c:/Users/PC-AORUS/Desktop/RFJ 2026/.venv/Scripts/python.exe' 'c:/Users/PC-AORUS/Desktop/RFJ 2026/scripts/generate_enriched_summaries.py'
   ```

### Opción B: Instalar Tesseract manualmente

1. **Descarga e instala Tesseract OCR:**
   - https://github.com/UB-Mannheim/tesseract/wiki
   - Instala en `C:\Program Files\Tesseract-OCR\`
   - Verifica: `tesseract --version`

2. **Descarga paquete de idioma español:**
   - Incluido en instalador o descarga `spa.traineddata`
   - Copia a `C:\Program Files\Tesseract-OCR\tessdata\`

3. **Ejecuta OCR en carpetas faltantes:**
   ```powershell
   & 'c:/Users/PC-AORUS/Desktop/RFJ 2026/.venv/Scripts/python.exe' 'c:/Users/PC-AORUS/Desktop/RFJ 2026/scripts/ocr_pdf2image_final.py'
   ```

### Opción C: Descargar versiones digitales

Busca versiones en texto/HTML de los documentos:
- Credo de los Apóstoles: Wikipedia, iglesia.net
- Confesión Belga: CPRF, Iglesia Reformada
- Catecismo de Heidelberg: heidelberg-catechism.com

## 📖 Formato de resúmenes generados

Los archivos `RESUMEN_*.md` incluyen:

- **Resumen breve** (4-6 oraciones clave)
- **Resumen detallado** (12-18 oraciones principales)
- **Conceptos clave** (8-12 términos importantes)
- **Índice sugerido** (estructura del documento)
- **Palabras clave** (filtradas por relevancia)
- **Prompts para IAs** (sugerencias de análisis)

## 🔄 Re-ejecutar scripts

Para regenerar todos los resúmenes:

```powershell
# Resúmenes básicos
& '.venv/Scripts/python.exe' 'scripts/extract_and_summarize.py'

# Resúmenes enriquecidos
& '.venv/Scripts/python.exe' 'scripts/generate_enriched_summaries.py'

# OCR (si Tesseract está instalado)
& '.venv/Scripts/python.exe' 'scripts/ocr_pdf2image_final.py'
```

## 📂 Estructura de archivos

```
00_docs_base/
├── __extracted__/           # Textos extraídos en .txt
├── 00 - Teoria.../
│   ├── *.pdf
│   ├── *.md
│   ├── RESUMEN_NUTRIDO.md  ✓
│   └── RESUMEN_OCR.md      ✓
├── 02 - Credo Apóstoles/
│   ├── *.pdf (corrupto)
│   ├── *.md (vacío)
│   └── RESUMEN_PENDIENTE.md
└── ...
```

## ⚙️ Requisitos del sistema

- Python 3.13+ (instalado en `.venv/`)
- VS Code con extensión PDF Viewer
- Windows 10/11
- (Opcional) Tesseract OCR para procesamiento avanzado

## 📝 Notas técnicas

### Problemas encontrados

1. **PDFs corruptos:** 5 documentos tienen errores de sintaxis PDF graves
   - Error: "Couldn't find trailer dictionary"
   - Solución: Usar versiones digitales o reescanear

2. **Tesseract PATH:** La instalación por Chocolatey requiere permisos admin
   - Solución aplicada: Configuración manual en scripts
   - Pendiente: Instalación correcta del binario

3. **Archivos MD vacíos:** Varios `.md` están sin contenido
   - Solución: Copiar manualmente desde PDFs o fuentes digitales

### Métodos probados

✓ pdfplumber (texto nativo)  
✓ PyMuPDF con OCR (fitz)  
✓ pdf2image + Poppler  
⚠️ pytesseract (requiere instalación manual)  

## 🎯 Próximos pasos recomendados

1. [ ] Instalar Tesseract OCR manualmente
2. [ ] Reparar o reemplazar los 5 PDFs corruptos
3. [ ] Completar archivos `.md` vacíos
4. [ ] Re-ejecutar scripts de resumen
5. [ ] Validar calidad de resúmenes generados
6. [ ] Commit final con todos los resúmenes

---

**Fecha de generación:** 13 de febrero de 2026  
**Versión:** 1.0  
**Autor:** Sistema automatizado de documentación RFJ
