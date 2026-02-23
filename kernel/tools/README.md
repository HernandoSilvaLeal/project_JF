# ⚙️ SCRIPTS - KERNEL DOCTRINAL RFJ 2026

Herramientas de automatización para validación, generación y análisis de servilletas.

---

## 📋 ÍNDICE DE SCRIPTS

| Script | Estado | Propósito |
|--------|--------|-----------|
| `validate_yaml.py` | ✅ OPERATIVO | Validar estructura y contenido de servilletas |
| `generate_mermaid.py` | 🔄 POR CREAR | Generar diagramas Mermaid desde YAML |
| `export_to_markdown.py` | 🔄 POR CREAR | Convertir YAML a Markdown consumible |
| `generate_pdf.py` | 🔄 POR CREAR | Generar PDFs desde Markdown |
| `check_dependencies.py` | 🔄 POR CREAR | Analizar grafo de dependencias |
| `check_convergencia.py` | 🔄 POR CREAR | Verificar convergencia teológica |
| `analyze_coverage.py` | 🔄 POR CREAR | Analizar cobertura bíblica |
| `batch_validate.py` | 🔄 POR CREAR | Validar múltiples servilletas |

---

## 🛠️ SCRIPTS DETALLADOS

### 1. `validate_yaml.py` ✅

**Propósito:** Validar estructura, trazabilidad y convergencia de servilletas YAML.

**Uso:**
```bash
# Validar una servilleta
python validate_yaml.py ../03_SERVILLETAS/00_KERNEL_PURO/S001_Atributos_Dios.yaml

# Validar con verbose
python validate_yaml.py S001_Atributos_Dios.yaml --verbose

# Validar solo estructura
python validate_yaml.py S001_Atributos_Dios.yaml --skip-bible-api
```

**Validaciones que realiza:**
- ✅ Estructura YAML válida
- ✅ Campos obligatorios presentes
- ✅ Trazabilidad cumple tier (ORO para Kernel)
- ✅ Convergencia coincide con tier
- ✅ Referencias bíblicas válidas
- ✅ Diagrama Mermaid cumple límites (<=9 nodos)
- ✅ No hay dependencias circulares

**Output:**
```
╔════════════════════════════════════════╗
║  VALIDACIÓN S001 - ATRIBUTOS DE DIOS  ║
╠════════════════════════════════════════╣
║  ✅ Estructura YAML válida             ║
║  ✅ Trazabilidad: DIAMANTE (23/20)     ║
║  ✅ Convergencia: 100% (tier válido)   ║
║  ✅ Referencias bíblicas válidas        ║
║  ✅ Diagrama: 7 nodos (límite: 9)      ║
╠════════════════════════════════════════╣
║  RESULTADO: ✅ APROBADA                ║
╚════════════════════════════════════════╝
```

---

### 2. `generate_mermaid.py` 🔄

**Propósito:** Generar diagramas visuales desde YAML.

**Uso planeado:**
```bash
# Generar SVG
python generate_mermaid.py S001 --output svg

# Generar PNG
python generate_mermaid.py S001 --output png --width 1920

# Solo generar código Mermaid
python generate_mermaid.py S001 --output mmd
```

**Output esperado:**
- Archivo `.mmd` en `04_DIAGRAMAS/mermaid/`
- Archivo `.svg` en `04_DIAGRAMAS/svg/`
- Archivo `.png` en `04_DIAGRAMAS/png/`

---

### 3. `export_to_markdown.py` 🔄

**Propósito:** Convertir YAML a Markdown consumible por humanos.

**Uso planeado:**
```bash
# Exportar una servilleta
python export_to_markdown.py S001

# Exportar todas del kernel
python export_to_markdown.py --tier KERNEL_PURO

# Exportar con diagramas embebidos
python export_to_markdown.py S001 --include-diagrams
```

**Output esperado:**
- Archivo `.md` en `05_EXPORTS/markdown/`
- Formato limpio, legible, con anclas bíblicas formateadas
- Enlaces internos a otras servilletas

---

### 4. `generate_pdf.py` 🔄

**Propósito:** Generar PDFs profesionales desde Markdown.

**Uso planeado:**
```bash
# Generar PDF de una servilleta
python generate_pdf.py S001

# Generar con tabla de contenidos
python generate_pdf.py S001 --toc

# Usar template custom
python generate_pdf.py S001 --template custom_template.tex
```

**Requisitos:**
- Pandoc instalado: `https://pandoc.org/installing.html`
- LaTeX instalado (MiKTeX/TeX Live) para mejor calidad

**Output esperado:**
- Archivo `.pdf` en `05_EXPORTS/pdf/`

---

### 5. `check_dependencies.py` 🔄

**Propósito:** Analizar grafo de dependencias entre servilletas.

**Uso planeado:**
```bash
# Ver dependencias de una servilleta
python check_dependencies.py S014

# Generar grafo completo
python check_dependencies.py --all --output graph

# Detectar ciclos
python check_dependencies.py --check-cycles
```

**Output esperado:**
```
S014 - Muerte Sustitutiva
├── DEPENDE DE:
│   ├── S003 - Santidad y Justicia
│   ├── S010 - Culpa Real
│   └── S013 - Vida Perfecta de Cristo
├── REQUERIDA POR:
│   ├── S017 - Sola Gratia
│   └── S018 - Sola Fide
```

---

### 6. `check_convergencia.py` 🔄

**Propósito:** Verificar que convergencia declarada sea real.

**Uso planeado:**
```bash
# Verificar convergencia de una servilleta
python check_convergencia.py S001

# Verificar todas del kernel
python check_convergencia.py --tier KERNEL_PURO

# Generar reporte detallado
python check_convergencia.py S001 --detailed
```

**Validaciones:**
- Consulta fuentes primarias (Westminster, Chafer, etc.)
- Compara con confesiones y credos
- Verifica que % convergencia sea correcto

---

### 7. `analyze_coverage.py` 🔄

**Propósito:** Analizar cobertura bíblica (libros, testamentos, versículos).

**Uso planeado:**
```bash
# Analizar cobertura total
python analyze_coverage.py

# Solo Kernel Puro
python analyze_coverage.py --tier KERNEL_PURO

# Generar visualización
python analyze_coverage.py --output chart
```

**Output esperado:**
```
╔════════════════════════════════════════╗
║  COBERTURA BÍBLICA - KERNEL PURO      ║
╠════════════════════════════════════════╣
║  Antiguo Testamento:                   ║
║    Libros cubiertos:    28/39 (72%)    ║
║    Versículos únicos:   145            ║
║                                        ║
║  Nuevo Testamento:                     ║
║    Libros cubiertos:    27/27 (100%)   ║
║    Versículos únicos:   312            ║
║                                        ║
║  TOTAL:                                ║
║    Libros:              55/66 (83%)    ║
║    Versículos únicos:   457            ║
╚════════════════════════════════════════╝
```

---

### 8. `batch_validate.py` 🔄

**Propósito:** Validar múltiples servilletas de golpe (CI/CD).

**Uso planeado:**
```bash
# Validar todas del kernel
python batch_validate.py --tier KERNEL_PURO

# Validar todas
python batch_validate.py --all

# Generar reporte HTML
python batch_validate.py --all --report html
```

**Output esperado:**
```
Validando 20 servilletas del KERNEL_PURO...

✅ S001 - Atributos de Dios      [PASS]
✅ S002 - Trinidad                [PASS]
❌ S003 - Santidad y Justicia     [FAIL - Trazabilidad insuficiente]
...

RESUMEN:
  Aprobadas:  19/20 (95%)
  Fallidas:    1/20 (5%)

Ver reporte completo: 06_TESTS/results/latest_report.html
```

---

## 🧰 UTILIDADES (utils/)

### `bible_parser.py` 🔄

**Propósito:** Parsear referencias bíblicas y validar formato.

**Funciones planeadas:**
```python
from utils.bible_parser import parse_reference, validate_reference

# Parsear referencia
ref = parse_reference("Juan 3:16")
# Output: {'book': 'Juan', 'chapter': 3, 'verse': 16}

# Validar formato
is_valid = validate_reference("1 Juan 2:1-3")
# Output: True
```

---

### `tier_calculator.py` 🔄

**Propósito:** Calcular tier automáticamente según convergencia.

**Funciones planeadas:**
```python
from utils.tier_calculator import calculate_tier

tier = calculate_tier(convergencia_score=85)
# Output: 'KERNEL'
```

---

### `convergence_scorer.py` 🔄

**Propósito:** Calcular score de convergencia.

**Funciones planeadas:**
```python
from utils.convergence_scorer import score_convergence

tradiciones = [
    {'nombre': 'Reformada', 'afirma': True},
    {'nombre': 'Dispensacional', 'afirma': True},
    {'nombre': 'Luterana', 'afirma': True},
]

score = score_convergence(tradiciones)
# Output: 100 (3/3 = 100%)
```

---

## 📦 INSTALACIÓN

```bash
# Clonar repositorio
cd C:\Users\PC-AORUS\Desktop\RFJ\KERNEL_DOCTRINAL

# Instalar dependencias
pip install -r ../requirements.txt

# Ejecutar tests
pytest 06_TESTS/
```

---

## 🚀 ROADMAP DE SCRIPTS

| Prioridad | Script | ETA | Razón |
|-----------|--------|-----|-------|
| 🔴 ALTA | `generate_mermaid.py` | 23-Feb | Necesario para S002 |
| 🔴 ALTA | `export_to_markdown.py` | 24-Feb | Outputs consumibles |
| 🟠 MEDIA | `batch_validate.py` | 28-Feb | CI/CD |
| 🟠 MEDIA | `check_dependencies.py` | 1-Mar | Grafo del kernel |
| 🟡 BAJA | `generate_pdf.py` | 5-Mar | Nice to have |
| 🟡 BAJA | `check_convergencia.py` | 10-Mar | Auditoría teológica |
| 🟡 BAJA | `analyze_coverage.py` | 10-Mar | Métricas |

---

## 🤝 CONTRIBUIR

Para añadir un script nuevo:

1. Crear archivo en `02_SCRIPTS/`
2. Seguir convenciones:
   - Usar `click` para CLI
   - Usar `rich` para output bonito
   - Documentar con docstrings
   - Añadir tests en `06_TESTS/`
3. Actualizar este README.md
4. Commit: `git commit -m "[SCRIPTS] Añadir nombre_script.py"`

---

**Mantenedor:** Hernando Silva + Cursor AI  
**Última actualización:** 2026-02-22

---

> **"Y Jehová habló a Moisés, diciendo: Mira, yo he llamado por nombre a Bezaleel... y lo he llenado del Espíritu de Dios, en sabiduría y en inteligencia, en ciencia y en todo arte."**  
> — Éxodo 31:1-3
