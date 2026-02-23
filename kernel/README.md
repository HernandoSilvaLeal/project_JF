# 🔥 KERNEL DOCTRINAL RFJ 2026

> **"Los códigos de Dios en módulos atómicos verificables"**

Sistema de gestión de conocimiento teológico con 99 servilletas doctrinales convergentes, trazables y escalables.

---

## 📋 ¿QUÉ ES ESTO?

El **KERNEL_DOCTRINAL** es:

- **99 servilletas** (módulos doctrinales atómicos)
- **Cada una** con tesis, claims, anclas bíblicas, relaciones, diagramas
- **Validadas automáticamente** contra schemas JSON
- **Convergentes teológicamente** entre tradiciones reformadas/dispensacionales sanas
- **Consumibles** por humanos (MD/PDF) y agentes IA (JSON/YAML)

---

## 🚀 INICIO RÁPIDO

### Ver una servilleta

```bash
# Abrir S001 (Atributos de Dios)
cat servilletas/00_kernel/S001_Atributos_Dios.yaml
```

### Validar estructura

```bash
# Instalar dependencias (desde raíz RFJ)
cd ..
pip install -r requirements.txt
cd kernel

# Validar una servilleta
python tools/validate/validate_yaml.py servilletas/00_kernel/S001_Atributos_Dios.yaml

# Validar todas de golpe
python tools/validate/batch_validate.py --tier 00_kernel
```

### Generar exports

```bash
# Generar Markdown consumible
python tools/export/markdown_exporter.py S001

# Generar diagrama SVG
python tools/generate/mermaid_generator.py S001 --output svg

# Generar PDF
python tools/export/pdf_generator.py S001
```

---

## 📂 ESTRUCTURA

```
kernel/
├── config/               # ⚙️ Configuración del sistema
│   └── config.yaml       #   Paths, reglas de validación, exports
├── docs/                 # 📚 Documentación maestra
│   ├── ARQUITECTURA.md   #   Diseño del sistema
│   ├── METODOLOGIA.md    #   Proceso de creación
│   ├── ROADMAP.md        #   Plan S001-S099
│   ├── DECISIONES.md     #   Log de decisiones teológicas
│   └── CHANGELOG.md      #   Historial de cambios
├── schemas/              # 🔧 Validación JSON Schema
│   └── servilleta.schema.json
├── servilletas/          # 🔴 NÚCLEO - Archivos YAML fuente
│   ├── 00_kernel/        #   S001-S020 (Convergencia 80-100%)
│   ├── 01_layer/         #   S021-S070 (Convergencia 50-79%)
│   └── 02_periphery/     #   S071-S099 (Convergencia <50%)
├── tools/                # 🛠️ Scripts organizados por función
│   ├── validate/         #   Validación YAML y constraints
│   ├── generate/         #   Generadores (diagramas, master docs)
│   ├── export/           #   Exportadores (MD, PDF, JSON)
│   ├── analyze/          #   Análisis (estadísticas, coverage)
│   └── utils/            #   Utilidades compartidas
├── outputs/              # 📦 Contenido generado
│   ├── diagrams/         #   Mermaid, SVG, PNG
│   ├── exports/          #   MD, PDF, JSON
│   └── master/           #   Documentos consolidados
├── tests/                # ✅ Suite de pruebas
│   ├── fixtures/         #   Datos de prueba
│   └── results/          #   Resultados de tests
└── workspace/            # 📝 Área temporal
    ├── drafts/           #   Servilletas en construcción
    └── archive/          #   Versiones antiguas
```

---

## 🎯 PROGRESO ACTUAL

```
╔════════════════════════════════════════╗
║  KERNEL DOCTRINAL - ESTADO            ║
╠════════════════════════════════════════╣
║  Completadas:     1/99   (1%)         ║
║  En progreso:     0/99                ║
║  Pendientes:     98/99                ║
╠════════════════════════════════════════╣
║  KERNEL PURO (S001-S020):             ║
║    Completadas:   1/20   (5%)         ║
║    Siguiente:     S002 Trinidad       ║
╠════════════════════════════════════════╣
║  ÚLTIMA ACTUALIZACIÓN: 2026-02-22     ║
╚════════════════════════════════════════╝
```

---

## 📖 DOCUMENTACIÓN

| Documento | Propósito |
|-----------|-----------|
| [METODOLOGIA.md](docs/METODOLOGIA.md) | Método completo para crear servilletas |
| [ARQUITECTURA.md](docs/ARQUITECTURA.md) | Arquitectura del sistema |
| [ROADMAP.md](docs/ROADMAP.md) | Plan S001-S099 |
| [DECISIONES.md](docs/DECISIONES.md) | Log de decisiones teológicas |
| [CHANGELOG.md](docs/CHANGELOG.md) | Historial de cambios |

---

## 🛠️ STACK TECNOLÓGICO

- **Formato:** YAML (servilletas), JSON Schema (validación)
- **Lenguaje:** Python 3.11+
- **Diagramas:** Mermaid
- **Tests:** pytest
- **Exports:** Pandoc (MD → PDF)

---

## 🧪 VALIDACIÓN

Cada servilleta pasa por:

1. ✅ **Validación estructural:** YAML válido, campos obligatorios
2. ✅ **Validación de trazabilidad:** >=ORO para Kernel (>=10 versículos)
3. ✅ **Validación de convergencia:** Tier coincide con score
4. ✅ **Validación de referencias:** Formato bíblico correcto
5. ✅ **Validación de diagrama:** <=9 nodos, <=4 niveles
6. ✅ **Review teológica manual:** Hernando aprueba

---

## 📚 RECURSOS TEOLÓGICOS BASE

**Reformadas:**
- Louis Berkhof - Teología Sistemática
- Herman Bavinck - Reformed Dogmatics
- Westminster (Confesión + Catecismos)

**Dispensacionales:**
- Lewis Sperry Chafer - Systematic Theology
- Charles Ryrie - Basic Theology

**Balanceadas:**
- John MacArthur - Biblical Doctrine
- J.I. Packer - Knowing God

**Credos:**
- Niceno-Constantinopolitano (325/381)
- Calcedonia (451)
- 1689 Bautista de Fe

---

## 🤝 CONTRIBUIR

**Proceso:**

1. Crear servilleta en `workspace/drafts/` usando [template](docs/METODOLOGIA.md#plantilla-yaml)
2. Validar: `python tools/validate/validate_yaml.py workspace/drafts/tu_servilleta.yaml`
3. Review teológica (Hernando)
4. Si aprobada → mover a `servilletas/00_kernel/` (o 01_layer, 02_periphery según tier)
5. Generar exports: `python tools/export/markdown_exporter.py SXXX`
6. Commit a Git

**Requisitos:**
- Convergencia >=80% para Kernel
- Trazabilidad >=ORO (>=10 versículos, >=5 libros)
- Todos los tests en PASS

---

## 📊 MÉTRICAS

**Kernel Puro (S001-S020):**
- Meta: 100% convergencia, DIAMANTE en trazabilidad
- Estado: 1/20 completadas

**Capa (S021-S070):**
- Meta: >=50% convergencia, PLATA en trazabilidad
- Estado: 0/50 completadas

**Periferia (S071-S099):**
- Meta: Divergencias honestas documentadas, BRONCE
- Estado: 0/29 completadas

---

## 🔗 ENLACES

- **Proyecto RFJ:** `C:\Users\PC-AORUS\Desktop\RFJ\`
- **Documento Magno:** `../docs/00_VISION/`
- **Plan 38 días:** `../docs/01_EJECUCION/`
- **README Principal:** `../README.md`

---

## 📧 CONTACTO

**Arquitecto:** Hernando Silva (RFJ)  
**Fecha creación:** 2026-02-22  
**Versión:** 1.0.0

---

> **"Procura con diligencia presentarte a Dios aprobado, como obrero que no tiene de qué avergonzarse, que usa bien la palabra de verdad."**  
> — 2 Timoteo 2:15
