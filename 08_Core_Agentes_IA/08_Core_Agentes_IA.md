# 08_Core_Agentes_IA — “Orquesta de Agentes” (Contrato Base Operativo + Doctrinal + Técnico)

> **Propósito supremo de este Core:**  
> Definir, con rigor de ingeniería y con guardarraíles doctrinales, el **sistema de agentes de IA** que construirá, verificará, versionará, publicará y defenderá el proyecto RFJ 2026 **sin alucinar**, sin diluir el centro, y sin romper la escalabilidad (de 1 a 10.000) ni la fidelidad bíblica.  
>
> Este documento es un **contrato mundial** para:
> - humanos (operador principal / editores / moderadores),
> - y **agentes de ultra inteligencia artificial** (productores, revisores, triage, catalogadores, publicadores, etc.).  
>
> **Principio rector:** *Los agentes no “inventan doctrina”: sirven como obreros que ensamblan, ordenan, conectan y verifican*.

---

## 0) Definiciones Canónicas (glosario operativo)

### 0.1 “Canon” (en RFJ 2026)
- **Canon doctrinal**: núcleo bíblico confesional (Core Doctrinal / Kernel).
- **Canon operativo**: servicios S0..S8 (Core Operativo).
- **Canon misional**: frentes F1..F5 (agrupan los 20 frentes) (Core Misional).
- **Canon producto**: 99 servilletas (Core Producto).
- **Canon alcance**: qué es “centro” vs qué es “periferia” (Core Alcance Doctrinal).
- **Canon canales**: formatos y reglas por plataforma (Core Canales).
- **Canon plataforma**: Casa Madre SaaS (Core Plataforma).
- **Canon contenido**: Catálogo Oficial con `CONTENT_ID` + versión + enlace.

### 0.2 “Agente” (en RFJ 2026)
Un agente es un actor IA con:
- un **rol** (responsabilidad limitada),
- un **contrato de entrada/salida** (I/O schema),
- un **perímetro de permisos** (capabilities),
- y **guardarraíles** (doctrinales, de seguridad, de tono, de alcance).

### 0.3 “Alucinación” (en RFJ 2026)
Cualquier afirmación no sustentada por:
- referencias bíblicas verificables (libro/capítulo/versículo),
- o por los artefactos canónicos del repositorio,
- o por datos explícitos provistos por el usuario / plataforma.

**Regla:** Si no está sustentado, se etiqueta como:
- `NO_CONFIRMADO`,
- `HIPÓTESIS`,
- o `PENDIENTE_VERIFICACIÓN`.

---

## 1) Principios de Diseño: Agentes como “sistema inmunológico” contra el error

### 1.1 Principio de Verificación Bíblica (“Bible-first, Reference-always”)
Todo output doctrinal debe incluir:
- **Textos ancla** (2–6 referencias mínimas),
- **Lógica de conexión** (por qué esos textos sustentan la tesis),
- y un **paso de verificación** (“cómo comprobarlo con tu Biblia”).

> Nota legal/editorial: se privilegia citar **referencias** (libro/capítulo/versículo) sobre pegar largos textos.

### 1.2 Principio de Centro (Core > Periferia)
Los agentes:
- **no** convierten debates periféricos en centro,
- **no** generan “contenido polémico por engagement”,
- **sí** devuelven siempre al centro: carácter de Dios, condición humana, evangelio, vida nueva.

### 1.3 Principio de Escalabilidad (1→n sin colapsar)
Los agentes deben:
- absorber volumen (preguntas, oraciones, comentarios),
- triage + colas + prioridades,
- convertir caos en estructura sin perder humanidad.

### 1.4 Principio Anti-Suplantación (Catálogo Oficial)
Todo contenido público “RFJ” debe poder mapearse a:
- `CONTENT_ID` canónico,
- `SERVILLETA_ID` si aplica,
- `SERVICIO_ID` si aplica,
- enlace al hub de la Casa Madre.

**Si no está catalogado, no es oficial.**

---

## 2) Arquitectura Global del Sistema de Agentes (vista “sistema nervioso”)

### 2.1 Capas (Layered Agent Architecture)
1) **Core Knowledge Layer** (fuentes canónicas)
   - Kernel doctrinal, servilletas, alcance doctrinal, reglas de canales, frentes, servicios, políticas.
2) **Retrieval Layer (RAG)**  
   - búsqueda exacta + semántica (vector) sobre canon interno.
3) **Reasoning/Assembly Layer**
   - agentes que ensamblan: outlines, guiones, respuestas, rutas, empaques.
4) **QA Layer (inmunidad)**
   - agentes que verifican: anclas bíblicas, coherencia, tono, riesgo, alcance.
5) **Publishing Layer**
   - publicadores + catalogadores + versionado.
6) **Feedback/Telemetry Layer**
   - métricas + loops de mejora + backlogs.

### 2.2 Flujo Macro (pipeline)
**IN** (mundo) → **NORMALIZAR** → **ENSAMBLAR** → **VERIFICAR** → **PUBLICAR** → **CATALOGAR** → **APRENDER**
- Entradas: TikTok/IG/YT, sitio web, formularios, comentarios, DMs.
- Salidas: contenido, respuestas, rutas, servilletas nuevas, correcciones.

---

## 3) Inventario de Agentes (Taxonomía de Roles)

> Cada agente es deliberadamente “estrecho” para reducir error.

### 3.1 Agentes de Producción (Productores)
**A1 — Servilleta Builder (S-Builder)**
- Produce: borrador de servilleta (estructura + tesis + textos ancla + diagrama sugerido).
- Input: tema / eje (Dios/Hombre/Evangelio) + alcance permitido.
- Output: `ServilletaDraft`.

**A2 — Script Builder (TT/YT/IG)**
- Produce: guión corto (TikTok) o outline largo (YouTube) basado en una servilleta.
- Output: `ContentDraft`.

**A3 — Course Builder (Academia)**
- Produce: módulos de curso, lecciones, quizzes (opcionales) anclados en servilletas.
- Output: `CourseDraft`.

**A4 — Devocional Builder (Diario)**
- Produce: devocional (audio-texto) con 1–2 referencias y aplicación.
- Output: `DevocionalDraft`.

### 3.2 Agentes de Verificación (QA / “Inmunidad”)
**B1 — Doctrinal Anchor Verifier (DAV)**
- Verifica: que las referencias bíblicas sean coherentes con la tesis.
- Exige: 2–6 anclas.
- Si falla: marca `RECHAZADO_POR_ANCLAS` o `PENDIENTE_VERIFICACIÓN`.

**B2 — Core/Periphery Gatekeeper (CPG)**
- Verifica: no convertir periferia en centro.
- Si el output deriva a polémicas: reencuadra a centro o bloquea.

**B3 — Tone & Audience Adapter (TAA)**
- Verifica: lenguaje apto para no iniciados, sin jerga innecesaria.
- Mantiene: “claridad + gravedad + ternura”.

**B4 — Risk & Safety Triage (RST)**
- Detecta: autolesión, abuso, violencia, crisis clínica.
- Aplica: política de respuesta segura (ver sección 9).

**B5 — Anti-Hallucination Auditor (AHA)**
- Verifica: que cada afirmación doctrinal tenga fuente canónica.
- Prohíbe: “parece que”, “la Biblia dice” sin referencia.

### 3.3 Agentes de Operación (Ops / Moderación / Comunidad)
**C1 — Prayer Triage Agent (PTA)**
- Clasifica oraciones: categoría, urgencia, privacidad.
- Sugerencia: servilleta o servicio recomendado.

**C2 — Questions Triage Agent (QTA)**
- Clasifica preguntas: tema, sensibilidad, nivel, ruta sugerida.
- Reduce caos a backlog.

**C3 — Community Moderator Agent (CMA)**
- Modera: comentarios; detecta toxicidad, discusiones estériles.
- Regla: no “guerra doctrinal” en espacios de inicio.

**C4 — Follow-up Orchestrator (FO)**
- Automatiza: recordatorios, rutas, “siguiente paso” por servicio.
- No invade: respeta privacidad.

### 3.4 Agentes de Publicación y Catálogo (Autenticidad)
**D1 — Content Cataloger (CC)**
- Genera: `CONTENT_ID`, versión, enlaces, UTMs.
- Registra: relación con servilleta y servicio.

**D2 — Publisher (PUB)**
- Publica: (según permisos) o prepara paquete para publicación humana.
- Nunca publica “sin QA” por defecto.

**D3 — Canon Maintainer (CM)**
- Mantiene: consistencia del canon; controla versiones.
- Aprueba: cambios al kernel / alcance / reglas.

---

## 4) Contratos de Entrada/Salida (Schemas)

> Estos schemas son el “lenguaje” entre agentes.  
> Un agente que no cumpla schema, no pasa.

### 4.1 `ServilletaDraft`
- `servilleta_id`: `S001..S099` o `SXXX` (si es borrador)
- `titulo`
- `eje_principal`: `{DIOS, HOMBRE, EVANGELIO}`
- `tesis_central` (1 frase)
- `anclas_biblicas`: lista 2–6 `{libro, cap, vers}`
- `conexion_logica`: bullets (cómo conectan las anclas)
- `diagrama_sugerido`: `{flow, tree, venn, timeline, ladder, map}`
- `riesgos`: `{periferia, ambigüedad, sensibilidad}`
- `cta`: “qué debe hacer el lector”
- `verificacion`: pasos para comprobar con Biblia

### 4.2 `ContentDraft`
- `content_type`: `{TT_SHORT, YT_LONG, IG_REEL, IG_CAROUSEL, PODCAST}`
- `front_id`: `{F1..F5}`
- `servilleta_ref`: `S0xx`
- `hook` (3–7s)
- `body` (guión)
- `cta_to_hub` (URL/slug)
- `anclas_biblicas` (mín 1–3 para short; 2–6 para long)
- `disclaimer` (si aplica)
- `CONTENT_ID` (si ya asignado)

### 4.3 `QAReport`
- `target_id` (servilleta o contenido)
- `status`: `{APPROVED, REVISE, REJECT}`
- `reasons`: lista de hallazgos
- `required_fixes`: acciones claras
- `risk_level`: `{LOW, MED, HIGH}`
- `scope_flags`: `{CORE_OK, PERIPHERY_DRIFT, SENSITIVITY}`

---

## 5) Guardarraíles Doctrinales (Reglas de Oro)

### 5.1 Regla “Ancla o silencio”
- Ninguna afirmación fuerte sin referencia.
- Ningún “Dios me dijo” como soporte.
- Ningún “la Biblia enseña” sin libro/capítulo/versículo.

### 5.2 Regla “Centro constante”
Cada output debe:
- apuntar a Cristo y al evangelio,
- o si es una pieza de Dios/Hombre, preparar el camino hacia evangelio.

### 5.3 Regla “Claridad sobre complejidad”
- Se permite profundidad,
- pero se exige trazabilidad y pedagogía visual.

### 5.4 Regla “No inventar historia, no inventar datos”
- Sin estadísticas no verificadas.
- Sin relatos reales no confirmados.
- Sin atribuciones falsas.

---

## 6) “Ciclo de Vida” de un Artefacto (Servilleta / Contenido / Curso)

### 6.1 Ciclo Servilleta
1) `S-Builder` crea borrador.
2) `DAV` verifica anclas.
3) `CPG` verifica centro vs periferia.
4) `TAA` adapta tono.
5) `CM` aprueba canonicidad.
6) `CC` registra versión y metadata.
7) Se publica en Hub.

### 6.2 Ciclo Contenido (TT/YT/IG)
1) `Script Builder` produce guión desde servilleta.
2) `AHA` revisa alucinaciones.
3) `RST` revisa riesgo.
4) `CC` asigna `CONTENT_ID`.
5) `PUB` prepara publicación.
6) Se publica + se enlaza al Hub.
7) Se mide (telemetría) + se mejora.

---

## 7) Orquestación (cómo “piensan” y “trabajan” los agentes juntos)

### 7.1 Patrón “Fan-out / Fan-in”
- Fan-out: un input genera múltiples borradores (servilleta, short, carrusel, outline).
- Fan-in: todo converge a QA y catálogo antes de publicar.

### 7.2 Patrón “Backlog Vivo”
- Preguntas y oraciones no se “pierden en DMs”.
- Se vuelven:
  - tickets,
  - con prioridad,
  - con ruteo a servicio,
  - con posibles contenidos derivados.

### 7.3 Patrón “One Source of Truth”
- El repositorio + Hub son la verdad oficial.
- Redes son proyección, no repositorio canónico.

---

## 8) Sistema Anti-Alucinación (Diseño Inmunológico)

### 8.1 RAG obligatorio sobre canon interno
Los agentes deben recuperar desde:
- Kernel doctrinal (01),
- Core Operativo (02),
- Core Misional (03),
- Producto 99 (04),
- Alcance doctrinal (05),
- Canales (06),
- Plataforma (07).

### 8.2 “Citas mínimas” por tipo de output
- TikTok short: 1–3 referencias.
- YouTube largo: 2–8 referencias.
- Servilleta: 2–6 (mínimo), ideal 4–8 si el tema es complejo.
- Respuesta consejería: 1–3 + recomendación pastoral prudente.

### 8.3 Señales de alucinación (detector)
- frases “la Biblia dice…” sin referencia
- referencias improbables / inconsistentes
- doctrinas “de moda” sin base
- “citas” textuales largas sin fuente

**Acción:** bloquear → pedir verificación → reescribir.

---

## 9) Política de Riesgo (Crisis, Autolesión, Abuso, etc.)

> Este proyecto entra a la vida real; por tanto, agentes deben obedecer una política de cuidado.

### 9.1 Clasificación de riesgo (RST)
- **LOW**: preguntas doctrinales normales, vida cotidiana.
- **MED**: ansiedad, depresión leve, adicciones en relato no inmediato.
- **HIGH**: suicidio, autolesión, abuso, violencia, riesgo inmediato.

### 9.2 Respuesta por riesgo
- **HIGH**:
  - nunca responder como si fuera terapia suficiente,
  - incluir recomendación urgente de ayuda local,
  - activar ruta de emergencia (según país),
  - limitar automatización,
  - registrar y elevar a humano (si el sistema lo permite).

### 9.3 Guardarraíl: “No suplantar profesionales”
- Acompañamiento espiritual ≠ atención clínica.

---

## 10) Seguridad, Autenticidad y “Prueba de Origen” (anti-clonación)

### 10.1 Catálogo Oficial como “firma pública”
Cada pieza debe poder verificarse:
- `CONTENT_ID`
- fecha
- enlace al Hub
- relación con servilleta

### 10.2 Estrategia anti-suplantación
- Página “Verifica si esto es RFJ”.
- Si un video circula:
  - la audiencia aprende a pedir `CONTENT_ID`.
- Todo contenido oficial referencia el Hub.

### 10.3 Versionado y retractaciones
- Si un contenido tuvo ambigüedad:
  - se corrige y se versiona,
  - se registra “nota editorial”.

---

## 11) Prompts Base (plantillas para agentes)

> Estos no son “promptitos”: son **contratos**.

### 11.1 Plantilla universal de prompt (Agent Contract Prompt)
- **Contexto canónico obligatorio**: (inyección desde repositorio)
- **Rol**: (S-Builder / DAV / etc.)
- **Tarea**: (qué producir)
- **Restricciones**:
  - no inventar
  - anclas mínimas
  - centro doctrinal
  - formato schema
- **Checklist** final

### 11.2 Checklist universal (debe estar en el output de QA)
- ¿Incluye anclas?
- ¿Deriva a periferia?
- ¿Lenguaje para no iniciados?
- ¿CTA al Hub?
- ¿Riesgo?
- ¿Catalogación?

---

## 12) Métricas (telemetría para mejora continua)

### 12.1 Métricas de fidelidad (calidad doctrinal)
- % outputs aprobados por DAV
- # correcciones por alucinación
- # flags por periferia

### 12.2 Métricas de impacto (misión)
- registros al Hub desde cada frente
- completitud de onboarding
- uso de biblioteca 99
- participación en oración/preguntas
- retención semanal/mensual

### 12.3 Métricas de operación
- backlog de preguntas (edad promedio)
- tiempo a primera respuesta
- tasa de escalamiento a humano

---

## 13) Implementación Técnica Recomendada (sin casarse con stack)

### 13.1 Componentes mínimos
- **Agent Orchestrator** (workflow engine): define pipelines.
- **Knowledge Store**:
  - docs canónicos (markdown),
  - índice semántico (vector) + exact match.
- **Queue / Events**:
  - triage async para volumen.
- **Audit Log**:
  - todo cambio queda registrado.

### 13.2 “Permisos por defecto: mínimos”
- Los agentes proponen.
- El sistema publica solo con aprobación (hasta que haya madurez).

---

## 14) Reglas Operativas: “Trabajo agente-céntrico sin caos”

### 14.1 Regla: Todo se convierte en objeto
- Pregunta → `QuestionTicket`
- Oración → `PrayerTicket`
- Comentario → `CommunityEvent`
- Idea → `ContentIdea`
- Borrador → `Draft`

### 14.2 Regla: Ningún humano queda atrapado en DMs
- Todo se canaliza al Hub.
- DMs solo para redirección.

### 14.3 Regla: “Una verdad, muchas formas”
Una servilleta:
- produce 1 short,
- 1 carrusel,
- 1 outline largo,
- 1 devocional,
- 1 FAQ,
- 1 respuesta a objeción,
sin reescribir desde cero.

---

## 15) Interacción con los 99 (cómo los agentes “sirven” al producto)

### 15.1 Servilleta como átomo
Los agentes nunca empiezan “desde el vacío”.
Empiezan desde:
- servilleta existente,
- o borrador de servilleta,
y derivan contenidos.

### 15.2 Servilleta como “unidad de doctrina verificable”
- Cada servilleta es una “pieza estándar” que otros pueden referenciar:
  - “S027” significa lo mismo para todos.

---

## 16) Declaración Final: “Agentes como obreros, no como oráculos”

> Los agentes de IA en RFJ 2026 no son profetas, ni jueces, ni fuentes de revelación.  
> Son **obreros instrumentales** para: ordenar, empaquetar, clarificar, verificar, escalar, y proteger el mensaje.  
>  
> La autoridad final es la Escritura, y el centro es Cristo.  
> El sistema existe para que miles puedan **leer, comprobar, entender y vivir** la verdad — con trazabilidad, con claridad, y con una arquitectura que no se quiebra cuando el mundo la mira.

---

## 17) Entregables (para repositorio)

- `08_Core_Agentes_IA.md` (este documento)
- `/agents/`
  - `roles.md`
  - `schemas.md`
  - `pipelines.md`
  - `qa_checklists.md`
  - `risk_policy.md`
  - `publishing_catalog.md`
  - `prompt_contracts/` (plantillas)

---

## 18) Checklist de Aceptación (Definition of Done)

Este Core se considera listo cuando:
1) Existen roles A/B/C/D definidos con permisos claros.
2) Existen schemas de `ServilletaDraft`, `ContentDraft`, `QAReport`.
3) Existe pipeline “Draft → QA → Catalog → Publish”.
4) Existe política de riesgo (HIGH/MED/LOW).
5) Existe protocolo anti-alucinación (RAG + anclas mínimas).
6) El catálogo oficial opera como firma pública.

---

**FIN — 08_Core_Agentes_IA*