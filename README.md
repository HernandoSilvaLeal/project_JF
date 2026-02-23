# 🔥 RFJ 2026 - Revolution For Jesus

> **"Evangelio con verdad, arquitectura y escala"**

Sistema integral de producción de contenido evangélico: desde teología reformada hasta distribución multicanal con IA.

---

## 📋 ¿QUÉ ES RFJ?

**Revolution For Jesus 2026** es un proyecto de evangelización que:

- **Define doctrina sólida** en 99 módulos teológicos verificables (Kernel Doctrinal)
- **Estructura operaciones** en 9 servicios escalables (S0-S8)
- **Mapea necesidades** en 5 frentes y 20 dolores específicos (Taxonomía Misional)
- **Produce contenido** en múltiples formatos y canales (99 Servilletas)
- **Automatiza con IA** para alcance masivo sin comprometer verdad bíblica

---

## 🏗️ ARQUITECTURA DEL PROYECTO

### Estructura de Carpetas (9 Raíces)

```
RFJ/
├── 📂 docs/                    # Documentación estratégica y visión
│   ├── 00_VISION/              # Documento Magno RFJ 2026
│   ├── 01_EJECUCION/           # Plan de 38 días con sprints
│   ├── 02_BASE_DOCTRINAL/      # Credos, confesiones, teologías base
│   └── RESUMENES.md            # Resúmenes de documentos clave
│
├── 📂 cores/                   # 9 Cores Arquitectónicos del Sistema
│   ├── 01_doctrinal/           # Core 1: Kernel Bíblico
│   ├── 02_operativo/           # Core 2: S0-S8 Escalera de Servicios
│   ├── 03_misional/            # Core 3: F1-F5 Frentes + A1-A20 Dolores
│   ├── 04_producto/            # Core 4: 99 Servilletas como Producto
│   ├── 05_alcance/             # Core 5: C0-C3 Círculos Doctrinales
│   ├── 06_canales/             # Core 6: TikTok, YouTube, IG, Podcast
│   ├── 07_plataforma/          # Core 7: SaaS Web Platform
│   ├── 08_agentes_ia/          # Core 8: Orquestación de IA
│   └── 09_ingenieria/          # Core 9: CI/CD, DevOps, Testing
│
├── 📂 kernel/                  # Sistema de Conocimiento Teológico
│   ├── config/                 # Configuración del sistema
│   ├── docs/                   # Arquitectura, Metodología, Roadmap
│   ├── schemas/                # Validación JSON Schema
│   ├── servilletas/            # 99 módulos YAML (00_kernel, 01_layer, 02_periphery)
│   ├── tools/                  # Scripts (validate, generate, export, analyze)
│   ├── outputs/                # Diagramas, PDFs, JSONs generados
│   ├── tests/                  # Suite de pruebas
│   └── workspace/              # Drafts y archivo temporal
│
├── 📂 scripts/                 # Scripts operacionales globales
│   ├── convert_*.py            # Conversión de formatos (docx, excel, etc.)
│   ├── extract_*.py            # Extracción de contenido
│   └── ocr_*.py                # Procesamiento OCR
│
├── 📂 tools/                   # Utilidades globales reutilizables
│   └── poppler/                # Dependencias externas
│
├── 📂 outputs/                 # Contenido generado para producción
│   ├── content/                # Videos, posts, artículos
│   ├── reports/                # Reportes analíticos
│   └── exports/                # Exportaciones masivas
│
├── 📂 .workspace/              # Archivos temporales (no commitear)
│   ├── tracked_files.txt
│   └── ignored_now.txt
│
├── 📂 .vscode/                 # Configuración IDE
└── 📂 .venv/                   # Entorno virtual Python

```

---

## 🎯 NÚCLEOS DEL SISTEMA

### 1. **KERNEL DOCTRINAL** (`kernel/`)
Sistema de 99 servilletas teológicas con:
- ✅ Trazabilidad bíblica total (>=20 versículos/claim)
- ✅ Convergencia entre tradiciones sanas (80-100% para S001-S020)
- ✅ Validación automática con JSON Schema
- ✅ Exports: PDF, Markdown, JSON, Diagramas SVG

**Ver:** [kernel/README.md](kernel/README.md) | [kernel/docs/ARQUITECTURA.md](kernel/docs/ARQUITECTURA.md)

### 2. **CORES ARQUITECTÓNICOS** (`cores/`)
9 subsistemas que estructuran toda la operación:

| Core | Propósito | Estado |
|------|-----------|--------|
| `01_doctrinal/` | Fundamento teológico convergente | ✅ Kernel en construcción |
| `02_operativo/` | S0-S8: Escalera de servicios (Evangelio → Plantación) | 📋 Documentado |
| `03_misional/` | F1-F5 frentes (Individuo, Familia, Comunidad, etc.) | 📋 Taxonomía completa |
| `04_producto/` | 99 Servilletas como producto MVP | 🚧 En diseño |
| `05_alcance/` | C0-C3: Círculos concéntricos de doctrina | 📋 Definido |
| `06_canales/` | Distribución multicanal (TikTok, YouTube, IG) | 🚧 En análisis |
| `07_plataforma/` | SaaS para gestión de contenido | 🔜 Planificado |
| `08_agentes_ia/` | Orquestación de agentes IA | 🔜 Planificado |
| `09_ingenieria/` | Pipeline CI/CD, testing, infraestructura | 🔜 Planificado |

### 3. **DOCUMENTACIÓN** (`docs/`)
Estrategia y fundamentos:
- `00_VISION/`: Análisis crítico completo del proyecto (Documento Magno)
- `01_EJECUCION/`: Plan de 38 días con sprints detallados
- `02_BASE_DOCTRINAL/`: Credos históricos, confesiones reformadas, recursos teológicos

---

## 🚀 INICIO RÁPIDO

### Prerrequisitos
```powershell
# Python 3.11+
python --version

# Activar entorno virtual
.\.venv\Scripts\Activate.ps1

# Instalar dependencias
pip install -r requirements.txt
```

### Validar Servilleta
```powershell
# Validar S001 (Atributos de Dios)
cd kernel
python tools/validate/validate_yaml.py servilletas/00_kernel/S001_Atributos_Dios.yaml
```

### Generar Exports
```powershell
# Generar diagrama Mermaid
python tools/generate/mermaid_generator.py S001 --output svg

# Exportar a Markdown
python tools/export/markdown_exporter.py S001

# Generar PDF
python tools/export/pdf_generator.py S001
```

---

## 📊 PROGRESO GLOBAL

```
╔══════════════════════════════════════════════════════╗
║  RFJ 2026 - ESTADO GENERAL                          ║
╠══════════════════════════════════════════════════════╣
║  📅 FASE ACTUAL:        Sprint 1 - Kernel Doctrinal ║
║  📆 FECHA:              22 Feb 2026                  ║
║  ⏱️  TIEMPO RESTANTE:   38 días                      ║
╠══════════════════════════════════════════════════════╣
║  KERNEL DOCTRINAL:                                   ║
║    ✅ Completadas:      1/99   (1%)                  ║
║    🚧 En progreso:      S002 Trinidad                ║
║    📋 Pendientes:       98/99                        ║
╠══════════════════════════════════════════════════════╣
║  CORES:                                              ║
║    ✅ Completados:      0/9                          ║
║    📋 Documentados:     4/9 (Doctrinal, Operativo,  ║
║                              Misional, Alcance)      ║
║    🚧 En diseño:        2/9 (Producto, Canales)     ║
║    🔜 Planificados:     3/9 (Plataforma, IA, Ing.)  ║
╠══════════════════════════════════════════════════════╣
║  🎯 PRÓXIMO HITO:       S020 completado (Kernel)    ║
║  📍 OBJETIVO 38 DÍAS:   Kernel + MVP Servilletas    ║
╚══════════════════════════════════════════════════════╝
```

---

## 📖 DOCUMENTOS CLAVE

| Documento | Ubicación | Propósito |
|-----------|-----------|-----------|
| **Arquitectura Kernel** | [kernel/docs/ARQUITECTURA.md](kernel/docs/ARQUITECTURA.md) | Sistema de servilletas doctrinales |
| **Metodología** | [kernel/docs/METODOLOGIA.md](kernel/docs/METODOLOGIA.md) | Proceso de creación de servilletas |
| **Roadmap** | [kernel/docs/ROADMAP.md](kernel/docs/ROADMAP.md) | Plan de desarrollo 99 servilletas |
| **Documento Magno** | [docs/00_VISION/](docs/00_VISION/) | Visión completa RFJ 2026 |
| **Plan 38 Días** | [docs/01_EJECUCION/](docs/01_EJECUCION/) | Sprints y entregas |
| **Core Operativo** | [cores/02_operativo/](cores/02_operativo/) | S0-S8 Escalera de servicios |
| **Taxonomía Misional** | [cores/03_misional/](cores/03_misional/) | F1-F5 Frentes + A1-A20 Dolores |

---

## 🛠️ STACK TECNOLÓGICO

```
📊 Datos:              YAML (source), JSON Schema (validación)
🐍 Backend:            Python 3.11+ (pyyaml, jsonschema, pytest)
📈 Visualización:      Mermaid.js (diagramas), SVG/PNG exports
📄 Documentación:      Markdown, Pandoc (MD → PDF)
🤖 IA:                 Claude/GPT-4 (asistencia), Agentes autónomos (futuro)
🌐 Plataforma:         SaaS web (futuro), API REST (futuro)
📦 Distribución:       TikTok, YouTube, Instagram, Podcast, Web
```

---

## 🔐 PRINCIPIOS RECTORES

1. **Sola Scriptura:** Toda doctrina anclada en >=2 versículos bíblicos
2. **Convergencia Teológica:** Priorizar acuerdos entre tradiciones sanas
3. **Atomicidad:** Una servilleta = una verdad indivisible
4. **Verificabilidad:** Validación automática con schemas JSON
5. **Escalabilidad:** Arquitectura soporta crecimiento sin refactoring
6. **Reproducibilidad:** Todo proceso automatizado y documentado
7. **Integridad:** Git como fuente de verdad, tests automáticos

---

## 🤝 CONTRIBUCIÓN

Este es un proyecto en desarrollo activo. Para contribuir:

1. **Crear servilletas:** Seguir [kernel/docs/METODOLOGIA.md](kernel/docs/METODOLOGIA.md)
2. **Validar cambios:** Ejecutar `pytest tests/` antes de commit
3. **Documentar decisiones:** Agregar a [kernel/docs/DECISIONES.md](kernel/docs/DECISIONES.md)
4. **Reportar issues:** Usar sistema de tracking interno

---

## 📝 LICENCIA

**Copyright © 2026 Revolution For Jesus (RFJ)**  
Contenido doctrinal: Uso libre para fines evangelísticos (Creative Commons BY-SA 4.0)  
Código fuente: MIT License

---

## 📞 CONTACTO

**Proyecto:** RFJ 2026 - Revolution For Jesus  
**Visión:** Evangelio con verdad, arquitectura y escala  
**Inicio:** Febrero 2026  
**Versión:** 1.0.0-alpha

---

> *"Toda la Escritura es inspirada por Dios y útil para enseñar, para reprender, para corregir, para instruir en justicia, a fin de que el hombre de Dios sea perfecto, equipado para toda buena obra."* — 2 Timoteo 3:16-17 (RVR60)
