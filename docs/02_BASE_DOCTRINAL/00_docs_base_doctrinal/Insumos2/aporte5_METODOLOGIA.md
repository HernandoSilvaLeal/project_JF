# METODOLOGÍA - Construcción de Servilletas Doctrinales
## El Código de Dios - RFJ 2026

**Versión:** 1.0.0  
**Fecha:** 2026-02-23  
**Propósito:** Documentar el método exacto para crear las 99 servilletas del kernel doctrinal

---

## 📋 TABLA DE CONTENIDOS

1. [Introducción](#introduccion)
2. [Principios Rectores](#principios-rectores)
3. [Arquitectura de Datos](#arquitectura-de-datos)
4. [Pipeline de Producción](#pipeline-de-produccion)
5. [Criterios de Validación](#criterios-de-validacion)
6. [Roles y Responsabilidades](#roles-y-responsabilidades)
7. [Checklist de Implementación](#checklist-de-implementacion)
8. [FAQ y Troubleshooting](#faq)

---

## 1. INTRODUCCIÓN {#introduccion}

### 1.1 ¿Qué es una "Servilleta"?

Una **servilleta** (napkin) es un módulo doctrinal con las siguientes propiedades:

- **Atómica:** No puede dividirse sin perder significado
- **Verificable:** Cada proposición tiene anclas bíblicas
- **Generativa:** De ella derivan verdades subsecuentes
- **Visual:** Se puede diagramar (máx. 9 nodos)
- **Convergente:** Afirmada por tradiciones sanas (>=80% para kernel)

### 1.2 Objetivo del Sistema

Construir **99 servilletas** que:

1. Representen el "kernel doctrinal" más puro y convergente
2. Sean escalables (de S001 a S099 sin contradicciones)
3. Sean consumibles por humanos Y agentes IA
4. Sirvan como base para todo contenido RFJ

### 1.3 Metáfora Arquitectónica

Piensa en las servilletas como **código fuente de un sistema operativo:**

- **Kernel (S001-S020):** Funciones core que nunca cambian
- **Drivers (S021-S070):** Aplicaciones específicas
- **Plugins (S071-S099):** Extensiones denominacionales

---

## 2. PRINCIPIOS RECTORES {#principios-rectores}

### P1: Sola Scriptura Operativa

- **Toda** proposición DEBE tener >= 2 anclas bíblicas
- Anclas NO son "textos de prueba" sino fundamento integral
- Si no hay versículo claro → NO va al kernel

### P2: Convergencia Sobre Tribalismo

- Kernel = solo lo que tradiciones SANAS afirman (>=80%)
- Debates denominacionales van a PERIFERIA (S071+)
- Objetivo: unidad en lo esencial, libertad en lo secundario

### P3: Granularidad Atómica

- Una proposición = un predicado principal
- Si tiene "y", "porque", "por tanto" → probablemente es compuesta
- Dividir hasta llegar a unidades indivisibles

### P4: Trazabilidad Exhaustiva

- NIVEL BRONCE: >= 2 versículos, >= 1 libro
- NIVEL PLATA: >= 5 versículos, >= 3 libros
- NIVEL ORO: >= 10 versículos, >= 5 libros
- NIVEL DIAMANTE: >= 20 versículos, >= 10 libros (AT + NT)

**Kernel (S001-S020) exige mínimo ORO.**

### P5: Visualización con Límites

- Máximo 9 nodos por diagrama (Ley de Miller 7±2)
- Máximo 4 niveles de profundidad
- Máximo 3 relaciones por nodo
- Si excede → dividir en sub-servilletas

---

## 3. ARQUITECTURA DE DATOS {#arquitectura-de-datos}

### 3.1 Estructura YAML Canónica

Cada servilleta es un archivo `.yaml` con esta estructura:

```yaml
metadata:
  id: S###
  titulo: "..."
  tesis: "..." # 1 línea, máximo 200 caracteres
  tier: KERNEL_PURO | CAPA | PERIFERIA
  convergencia_score: 0-100
  trazabilidad_nivel: BRONCE | PLATA | ORO | DIAMANTE

claims:
  C#_NOMBRE:
    text: "Proposición atómica"
    definicion_tecnica: "..."
    implicaciones: [...]
    anclas_biblicas: [...]
    tradiciones_convergencia: [...]
    tier: KERNEL | CAPA | PERIFERIA
    peso_generativo: 1-10

relaciones:
  - from: C#
    to: C#
    type: FUNDAMENTA | IMPLICA | CONTRASTA | REQUIERE | EJEMPLIFICA | CUMPLE
    explicacion: "..."
    fuerza: 1-10

guardarrailes:
  G#_NOMBRE:
    error: "..."
    refutado_por: [C#, C#]
    textos_clave: [...]
    consecuencias: "..."

tests:
  T#_NOMBRE:
    descripcion: "..."
    criterio: "..."
    status: PASS | FAIL
    detalles: "..."

salidas:
  - id: S###
    titulo: "..."
    dependencia_primaria: C#
    explicacion: "..."

diagrama_mermaid: |
  graph TD
    ...

produccion:
  autor_humano: "..."
  agentes_generadores: [...]
  version: "X.Y.Z"
  estado: DRAFT | REVIEW | APPROVED | PUBLISHED
```

### 3.2 Tipos de Relación (Ontología)

| Tipo | Significado | Ejemplo |
|------|-------------|---------|
| **FUNDAMENTA** | A es base lógica de B | Aseidad → Eternidad |
| **IMPLICA** | A produce necesariamente B | Eternidad → Inmutabilidad |
| **CONTRASTA** | A y B son verdad pero opuestos aparentes | Soberanía ↔ Responsabilidad |
| **REQUIERE** | A necesita B para ser verdadero | Expiación → Santidad de Dios |
| **EJEMPLIFICA** | A es caso específico de B | David → Pecador justificado |
| **CUMPLE** | A cumple profecía/tipo de B | Cristo → Cordero pascual |

### 3.3 Tiers (Niveles de Controversia)

- **KERNEL_PURO:** Convergencia 100%, ninguna tradición sana discrepa
- **KERNEL:** Convergencia >=80%, mayoría afirma
- **CAPA:** Convergencia 50-79%, importante pero divisivo
- **PERIFERIA:** <50%, debates intra-evangélicos

---

## 4. PIPELINE DE PRODUCCIÓN {#pipeline-de-produccion}

### FASE 0: Selección de Tesis

**Objetivo:** Identificar la proposición central que generará la servilleta.

**Método:**

1. **Extrae candidatos** desde teologías sistemáticas:
   - Berkhof (Reformada)
   - Chafer (Dispensacional)
   - Pink, Charnock, Bavinck, MacArthur

2. **Filtra por convergencia:**
   - ¿Cuántas tradiciones afirman?
   - Si <80% → descartar o mover a CAPA/PERIFERIA

3. **Rankea por generatividad:**
   - ¿Cuántas verdades derivan de esta?
   - Ejemplo: "Dios es santo" genera necesidad de expiación, juicio, gracia, etc.

4. **Elige la de máximo score:**
   - Score = (Convergencia × 0.6) + (Generatividad × 0.4)

**Output:** Tesis de 1 línea (máx. 200 caracteres)

---

### FASE 1: Atomización en Claims

**Objetivo:** Dividir la tesis en proposiciones atómicas verificables.

**Método:**

1. **Identifica sub-verdades:**
   - Tesis: "Dios es eterno, auto-existente, inmutable"
   - Claims: C1=Aseidad, C2=Eternidad, C3=Inmutabilidad

2. **Verifica atomicidad:**
   - Test: ¿Puedo negar esta proposición sin negar otra?
   - Si no → aún es compuesta, divide más

3. **Asigna ID único:**
   - Formato: `C#_NOMBRE_DESCRIPTIVO`
   - Ejemplo: `C1_ASEIDAD`, `C2_ETERNIDAD`

**Output:** Lista de 3-7 claims atómicos

---

### FASE 2: Anclaje Bíblico

**Objetivo:** Fundamentar cada claim con versículos verificables.

**Método:**

1. **Busca anclas primarias:**
   - Textos donde la verdad es explícita
   - Ejemplo para "Dios eterno": Salmo 90:2, Apocalipsis 1:8

2. **Busca anclas de contexto:**
   - Textos donde la verdad es implícita pero robusta
   - Ejemplo: 2 Pedro 3:8 (relación divina con tiempo)

3. **Diversifica libros:**
   - Mínimo 3 libros diferentes
   - Ideal: AT + NT, Ley + Profetas + Evangelios + Epístolas

4. **Documenta cada ancla:**
   ```yaml
   - ref: "Libro cap:vers"
     texto: "Cita exacta"
     comentario: "Por qué este texto apoya el claim"
     categoria: "Pentateuco | Históricos | Poesía | Profetas | Evangelios | Hechos | Epístolas | Apocalipsis"
   ```

**Criterio de éxito:**
- Kernel: >= 4 anclas, >= 3 libros
- Nivel ORO o superior

**Output:** Claims con anclas verificables

---

### FASE 3: Mapeo de Relaciones

**Objetivo:** Definir dependencias causales entre claims.

**Método:**

1. **Identifica relaciones lógicas:**
   - ¿C1 fundamenta C2?
   - ¿C2 implica C3?
   - ¿C3 refuerza C1? (bucle de coherencia)

2. **Asigna tipo de relación:**
   - Usa ontología canónica (FUNDAMENTA, IMPLICA, etc.)

3. **Calcula fuerza:**
   - Escala 1-10
   - 10 = necesidad lógica absoluta
   - 1 = relación débil

4. **Documenta:**
   ```yaml
   - from: C1_ASEIDAD
     to: C2_ETERNIDAD
     type: FUNDAMENTA
     explicacion: "Si Dios existe por sí mismo, no puede tener principio"
     fuerza: 10
   ```

**Output:** Grafo de dependencias (dirigido, posiblemente con ciclos)

---

### FASE 4: Construcción de Guardarraíles

**Objetivo:** Identificar herejías/errores que la servilleta refuta.

**Método:**

1. **Identifica errores históricos:**
   - Teísmo abierto, panteísmo, proceso-teología, etc.

2. **Mapea a claims que refutan:**
   - Ejemplo: Teísmo abierto contradice C2 (eternidad) y C3 (inmutabilidad)

3. **Documenta textos clave:**
   - Versículos que directamente niegan el error

4. **Explica consecuencias:**
   - ¿Qué se pierde si se acepta el error?

**Output:** Lista de guardarraíles (herejías invalidadas)

---

### FASE 5: Validación Automática

**Objetivo:** Verificar integridad estructural y teológica.

**Tests obligatorios:**

```yaml
T1_TRAZABILIDAD:
  - Cada claim >= 2 anclas (mínimo absoluto)
  - Kernel >= 4 anclas

T2_CONVERGENCIA:
  - Kernel: score >= 80%
  - Capa: score >= 50%

T3_NO_CONTRADICCION:
  - No hay claims que se nieguen mutuamente
  - Relaciones son coherentes

T4_CREDOS:
  - Compatible con Niceno, Calcedonia, Westminster
  - Ningún conflicto con ortodoxia histórica

T5_GRANULARIDAD:
  - Claims son atómicos (un predicado cada uno)
  - No hay compuestos sin dividir
```

**Output:** Reporte de tests (PASS/FAIL por cada uno)

---

### FASE 6: Visualización (Mermaid)

**Objetivo:** Generar diagrama navegable.

**Método:**

1. **Estructura básica:**
   ```mermaid
   graph TD
     C1[Claim 1] --> C2[Claim 2]
     C2 --> C3[Claim 3]
   ```

2. **Aplica estilos:**
   - Colores por importancia
   - Grosor de flecha por fuerza de relación

3. **Limita complejidad:**
   - Máximo 9 nodos
   - Si excede → diagrama resumen + sub-diagramas

4. **Incluye referencias:**
   - Cada nodo muestra versículo clave

**Output:** Código Mermaid + SVG renderizado

---

### FASE 7: Documentación de Salidas

**Objetivo:** Definir qué servilletas dependen de esta.

**Método:**

1. **Identifica dependencias lógicas:**
   - ¿Qué verdades REQUIEREN esta servilleta?
   - Ejemplo: S002 (Trinidad) requiere S001 (Aseidad)

2. **Documenta:**
   ```yaml
   salidas:
     - id: S002
       titulo: "Trinidad"
       dependencia_primaria: C1_ASEIDAD
       explicacion: "Unidad de esencia trinitaria presupone aseidad"
       textos_puente: ["Juan 5:26", "Juan 17:5"]
   ```

**Output:** Mapa de dependencias para roadmap

---

### FASE 8: Aprobación Final

**Roles requeridos:**

1. **Revisor Teológico Reformado**
   - Valida convergencia con Westminster
   - Verifica anclas bíblicas

2. **Revisor Teológico Dispensacional**
   - Valida hermenéutica literal
   - Verifica compatibilidad AT/NT

3. **Validador Técnico**
   - Ejecuta tests automáticos
   - Verifica integridad YAML

**Criterio de aprobación:**
- 3/3 revisores aprueban
- Todos los tests en PASS
- Cero conflictos con credos

**Output:** Servilleta en estado APPROVED

---

## 5. CRITERIOS DE VALIDACIÓN {#criterios-de-validacion}

### 5.1 Validación Estructural (Automática)

| Test | Descripción | Herramienta |
|------|-------------|-------------|
| **YAML válido** | Parsea sin errores | `pyyaml`, `yamllint` |
| **Campos obligatorios** | Todos presentes | Script custom |
| **IDs únicos** | No hay duplicados | Script custom |
| **Referencias válidas** | Formato "Libro cap:vers" | Regex + Bible API |

### 5.2 Validación Teológica (Manual)

| Criterio | Método | Responsable |
|----------|--------|-------------|
| **Convergencia real** | Consultar fuentes primarias | Revisor Teológico |
| **Anclas correctas** | Verificar contexto | Revisor Teológico |
| **No hay herejía** | Cotejar con credos | Revisor Teológico |
| **Claridad doctrinal** | Lectura crítica | Hernando (final) |

### 5.3 Validación de Diagramas

| Criterio | Límite | Acción si excede |
|----------|--------|------------------|
| **Nodos** | 9 | Dividir en sub-servilletas |
| **Niveles** | 4 | Aplanar jerarquía |
| **Relaciones/nodo** | 3 | Simplificar |

---

## 6. ROLES Y RESPONSABILIDADES {#roles-y-responsabilidades}

### 6.1 Hernando (Orquestador)

**Responsabilidades:**
- Tomar decisiones estratégicas
- Validar aprobación final teológica
- Proveer input doctrinal profundo

**Tareas por servilleta:**
- Aprobar tesis inicial
- Revisar claims y anclas
- Dar luz verde para publicación

### 6.2 Claude (Arquitecto Comandante)

**Responsabilidades:**
- Diseñar arquitectura de datos
- Definir ontología de relaciones
- Resolver conflictos teológicos/técnicos

**Tareas por servilleta:**
- Generar template inicial
- Validar convergencia
- Aprobar estructura YAML

### 6.3 ChatGPT (Director de Operaciones)

**Responsabilidades:**
- Coordinar entre agentes
- Dividir tareas grandes en subtareas
- Tracking de progreso

**Tareas por servilleta:**
- Crear checklist de implementación
- Coordinar con Copilot
- Reportar a Hernando cuando esté lista

### 6.4 Copilot/Sonnet Local (Desarrollador)

**Responsabilidades:**
- Implementar YAML siguiendo template
- Ejecutar scripts de validación
- Generar diagramas Mermaid

**Tareas por servilleta:**
- Crear archivo `.yaml`
- Buscar anclas bíblicas
- Ejecutar tests automáticos
- Commit a Git

---

## 7. CHECKLIST DE IMPLEMENTACIÓN {#checklist-de-implementacion}

### Para cada servilleta nueva:

#### ✅ FASE 0: Preparación

- [ ] Revisar servilletas previas (dependencias)
- [ ] Identificar tesis central
- [ ] Verificar convergencia (>=80% para kernel)

#### ✅ FASE 1: Estructura

- [ ] Crear archivo `S###_Nombre.yaml`
- [ ] Definir metadata (id, titulo, tesis, tier)
- [ ] Atomizar en 3-7 claims

#### ✅ FASE 2: Anclas

- [ ] Buscar >= 4 versículos por claim
- [ ] Diversificar libros (>= 3)
- [ ] Documentar contexto de cada ancla

#### ✅ FASE 3: Relaciones

- [ ] Mapear dependencias entre claims
- [ ] Asignar tipos de relación
- [ ] Calcular fuerza (1-10)

#### ✅ FASE 4: Guardarraíles

- [ ] Identificar >= 2 herejías refutadas
- [ ] Documentar textos clave
- [ ] Explicar consecuencias

#### ✅ FASE 5: Tests

- [ ] Ejecutar `validate_yaml.py`
- [ ] Verificar trazabilidad (ORO mínimo para kernel)
- [ ] Validar convergencia (>=80%)

#### ✅ FASE 6: Diagrama

- [ ] Generar Mermaid
- [ ] Renderizar y verificar (<= 9 nodos)
- [ ] Exportar SVG

#### ✅ FASE 7: Review

- [ ] Enviar a revisor teológico reformado
- [ ] Enviar a revisor teológico dispensacional
- [ ] Incorporar feedback

#### ✅ FASE 8: Aprobación

- [ ] Hernando aprueba
- [ ] Cambiar estado a APPROVED
- [ ] Commit final a Git
- [ ] Actualizar roadmap

---

## 8. FAQ Y TROUBLESHOOTING {#faq}

### Q1: ¿Qué hago si encuentro una verdad divisiva?

**R:** Si convergencia <80% → NO va al kernel.

Opciones:
- Reformular para encontrar punto de acuerdo
- Mover a CAPA (S021-S070) como "énfasis"
- Documentar como PERIFERIA (S071-S099) con disclaimer

### Q2: ¿Qué hago si un claim necesita 20 anclas?

**R:** Probablemente no es atómico.

Acciones:
- Dividir en sub-claims
- O aceptar que es verdad "mega-central" (ej: resurrección de Cristo)

### Q3: ¿Qué hago si dos claims se contradicen?

**R:** Verificar si es contradicción REAL o aparente.

Si real → ERROR GRAVE, revisar teología.
Si aparente → documentar como CONTRASTA (ej: soberanía ↔ responsabilidad)

### Q4: ¿Cómo manejo textos que usan otras traducciones interpretan diferente?

**R:** Usar RVR1960 como base, pero documentar variantes importantes.

Ejemplo:
```yaml
anclas_biblicas:
  - ref: "Juan 1:1"
    texto: "En el principio era el Verbo"
    variantes:
      - version: "NVI"
        texto: "En el principio ya existía el Verbo"
      - nota: "Ambas afirman pre-existencia de Cristo"
```

### Q5: ¿Cuánto tiempo toma hacer una servilleta?

**R:** Depende del tier:

- **Kernel (S001-S020):** 6-10 horas (máximo rigor)
- **Capa (S021-S070):** 3-5 horas
- **Periferia (S071-S099):** 1-3 horas

### Q6: ¿Qué hago si agentes IA "alucinan" teología?

**R:** NUNCA confíes ciegamente en output de IA.

Reglas:
- Toda ancla bíblica DEBE verificarse manualmente
- Claims deben cotejarse con fuentes (Berkhof, Chafer, etc.)
- Guardarraíles requieren aprobación humana

---

## 9. ROADMAP SUGERIDO (S001-S020)

| ID | Título | Dependencias | Prioridad |
|----|--------|--------------|-----------|
| S001 | Atributos Fundamentales de Dios | NINGUNA | 🔴 CRÍTICA |
| S002 | Trinidad | S001 | 🔴 CRÍTICA |
| S003 | Santidad y Justicia | S001 | 🔴 CRÍTICA |
| S004 | Amor y Misericordia | S001 | 🟠 ALTA |
| S005 | Soberanía y Providencia | S001 | 🟠 ALTA |
| S006 | Creación Ex Nihilo | S001, S005 | 🟠 ALTA |
| S007 | Imagen de Dios en el Hombre | S006 | 🟡 MEDIA |
| S008 | Caída y Pecado Original | S007 | 🔴 CRÍTICA |
| S009 | Total Depravación | S008 | 🔴 CRÍTICA |
| S010 | Culpa Real y Muerte Espiritual | S008, S009 | 🔴 CRÍTICA |
| S011 | Promesa de Redención (Protoevangelio) | S010 | 🟠 ALTA |
| S012 | Encarnación de Cristo | S002, S011 | 🔴 CRÍTICA |
| S013 | Vida Perfecta de Cristo | S012 | 🟠 ALTA |
| S014 | Muerte Sustitutiva (Expiación) | S003, S010, S013 | 🔴 CRÍTICA |
| S015 | Resurrección Corporal | S014 | 🔴 CRÍTICA |
| S016 | Ascensión y Señorío | S015 | 🟡 MEDIA |
| S017 | Sola Gratia | S014 | 🔴 CRÍTICA |
| S018 | Sola Fide | S017 | 🔴 CRÍTICA |
| S019 | Regeneración (Nuevo Nacimiento) | S018 | 🔴 CRÍTICA |
| S020 | Justificación vs Santificación | S018, S019 | 🟠 ALTA |

**Orden de construcción:** Secuencial (S001 → S002 → S003...) para respetar dependencias.

---

## 10. REFERENCIAS Y RECURSOS

### 10.1 Teologías Sistemáticas

**Reformadas:**
- Louis Berkhof - *Teología Sistemática*
- Herman Bavinck - *Reformed Dogmatics* (4 vols)
- Wayne Grudem - *Systematic Theology*

**Dispensacionales:**
- Lewis Sperry Chafer - *Systematic Theology* (8 vols)
- Charles Ryrie - *Basic Theology*
- J. Dwight Pentecost - *Things to Come*

**Híbridas/Balanceadas:**
- John MacArthur - *Biblical Doctrine*
- Millard Erickson - *Christian Theology*

### 10.2 Atributos de Dios (Especializado)

- A.W. Pink - *The Attributes of God*
- Stephen Charnock - *The Existence and Attributes of God*
- J.I. Packer - *Knowing God*

### 10.3 Credos y Confesiones

- Credo Niceno-Constantinopolitano (325/381)
- Credo de Calcedonia (451)
- Confesión de Westminster (1646)
- Confesión Bautista de Fe 1689
- 39 Artículos de la Iglesia Anglicana (1563)

### 10.4 Herramientas Técnicas

- **YAML Lint:** https://www.yamllint.com/
- **Mermaid Live:** https://mermaid.live/
- **Bible API:** https://bible-api.com/
- **Python YAML:** `pip install pyyaml`

---

## 11. CONTROL DE VERSIONES

### Versionado Semántico (SemVer)

Formato: `MAJOR.MINOR.PATCH`

- **MAJOR:** Cambio en estructura doctrinal base (rarísimo)
- **MINOR:** Añadir claims, mejorar anclas, nuevas relaciones
- **PATCH:** Correcciones menores, typos, aclaraciones

Ejemplo:
- `1.0.0` - Versión inicial aprobada
- `1.1.0` - Se añadió claim C6 sobre simplicidad divina
- `1.1.1` - Corrección de referencia bíblica en C3

### Changelog

Cada servilleta DEBE documentar cambios:

```yaml
changelog:
  - version: "1.1.0"
    fecha: "2026-03-15"
    cambios:
      - "Añadido C6_SIMPLICIDAD con 5 anclas"
      - "Actualizado diagrama Mermaid"
  - version: "1.0.0"
    fecha: "2026-02-23"
    cambios: "Versión inicial completa"
```

---

## 12. CONCLUSIÓN

Esta metodología NO es "sugerencia". Es **CONTRATO** para mantener:

1. **Convergencia teológica** (verdad robusta)
2. **Escalabilidad técnica** (99 servilletas sin caos)
3. **Verificabilidad** (anti-alucinación de IAs)
4. **Replicabilidad** (cualquiera puede seguir el método)

**Regla de oro:**

> Si no puedes explicar cómo llegaste a una proposición siguiendo este método,  
> esa proposición NO entra al kernel.

---

**FIN DE METODOLOGÍA**

---

**Mantenedores:**
- Hernando Silva (Orquestador)
- Claude Sonnet 4.5 (Arquitecto)
- Comunidad RFJ (Colaboradores futuros)

**Contacto:** [Definir canal oficial]

**Licencia:** [Definir - sugerencia: Creative Commons BY-SA 4.0 para contenido, MIT para código]
