# 07_Core_Plataforma_Web_SaaS — “Casa Madre” (Contrato Base de Plataforma)

> **Propósito supremo de este Core:**  
> Definir, con precisión de ingeniería y reverencia doctrinal, la **plataforma web central (SaaS)** que actuará como **Casa Madre** del proyecto RFJ 2026:  
> el lugar donde **todo lead se captura**, toda interacción se **canaliza**, toda doctrina se **verifica**, todo contenido oficial se **indexa**, y toda escalera de servicios (S0..S8) se vuelve **navegable, accionable y escalable**.  
>  
> Este documento es un **contrato base** para humanos y para **agentes de ultra inteligencia artificial**: aquí se fijan entidades, flujos, módulos, decisiones, guardarraíles, seguridad, y una ruta MVP→V1→V2.

---

## 0) Principio Arquitectónico: “Órbita → Casa Madre → Vida”

### 0.1 La plataforma es el **centro gravitacional**
Las redes sociales son **atracción**. La plataforma es **retención + formación + servicio + trazabilidad**.

- **Atracción (TikTok por frentes F1..F5)** → **Conversión (Registro en Casa Madre)** →  
  **Autoclasificación** → **Ruta sugerida** → **Servicios** → **Progreso** → **Comunidad** → **Perseverancia**

**Regla:** Ningún canal externo debe convertirse en “sistema nervioso”.  
La plataforma es el **sistema nervioso**, y el **catálogo oficial** es su “columna vertebral”.

### 0.2 “No perder leads” es una obligación de diseño
- Captura rápida (cuenta o sesión ligera).
- Onboarding de 2–3 clics.
- Ruta sugerida inmediata.
- Minimizar rebote.
- Registro de intención (por qué vino, qué busca).

### 0.3 “No diluir el evangelio” es una obligación de gobernanza
La plataforma es también:
- **defensa doctrinal**,  
- **claridad confesional**,  
- **control de versiones**,  
- **protección anti-clonación**.

---

## 1) Modelo Mental UI: “Escalera Viva” (Servicios S0..S8)

> Visual principal del Home/Hub: una **escalera/rueda** con 9 nodos:
- **S0**: Oración privada + Administración (operación espiritual + operativa)
- **S1..S8**: Servicios incrementales (núcleo operativo)

### 1.1 Principio clave: escalera **ofrecida**, no impuesta
La plataforma:
- sugiere orden,
- pero permite que el usuario elija “lo que necesita hoy”,
- sin romper guardarraíles (siempre se le devuelve al centro).

### 1.2 Cada nodo (servicio) se despliega en “3 acciones”
Ejemplo de patrón universal (para cada Sx):
- **Acción A:** empezar ahora (paso mínimo)
- **Acción B:** aprender (servilletas/recursos)
- **Acción C:** pedir ayuda (formulario / comunidad)

---

## 2) Taxonomía de Usuarios: de 1 a n sin romperse

### 2.1 Roles (principales)
- **Visitor** (sin cuenta): navegación limitada + CTA registro
- **Member** (usuario registrado): rutas + oraciones + preguntas + biblioteca completa
- **Servant/Helper** (colaborador): responde, modera, acompaña
- **Admin**: gobernanza, publicación, moderación, catálogo oficial
- **Doctrinal Reviewer** (opcional): QA doctrinal (guardarraíl editorial)
- **AI-Agent**: productor asistido con permisos restringidos

### 2.2 Principio “una persona = un ID canónico”
Todo se registra:
- `USER_ID`
- preferencias
- frente de entrada
- intereses y rutas
- histórico de oraciones/preguntas
- progreso por servicios

---

## 3) Módulos Funcionales (Sistema Operativo de la Casa Madre)

> La plataforma se diseña modular: cada módulo es un “lego” que puede crecer.

### 3.1 Módulo A — Identidad / Cuenta / Perfil
**Objetivo:** capturar lead con fricción mínima.
- Login: email mágico / Google / passkey
- Perfil mínimo: nombre (opcional), país, idioma
- Preferencias: frentes (F1..F5), temas, horarios
- Privacidad: controles claros (ver sección 12)

### 3.2 Módulo B — Onboarding “2 clics”
- Pregunta 1: “¿Por qué llegaste hoy?” (dolor / curiosidad / culpa / etc.)
- Pregunta 2: “¿Qué buscas ahora?” (oración / devocional / pregunta / aprender / acompañamiento)
- Resultado: **Ruta sugerida** + botón “Empezar”

### 3.3 Módulo C — Mapa/Tablero de Servicios (S0..S8)
- UI: escalera con nodos
- Estado por nodo: `locked` / `available` / `in_progress` / `completed` (flexible)
- Cada nodo: 3 acciones (ver 1.2)

### 3.4 Módulo D — Biblioteca 99 (Core Producto)
**Objetivo:** entregar el “paquete” global de servilletas como referencia mundial.
- Navegación:
  - por ID: S001..S099
  - por eje: Dios / Hombre / Evangelio (y subejes)
  - por libro bíblico (índice)
  - por temas (glosario)
- Cada servilleta:
  - imagen/diagrama
  - explicación breve
  - textos ancla (2–6)
  - “verificación” (cómo comprobar con Biblia)
  - “siguiente servilleta sugerida”
- Descarga:
  - PDF paquete
  - tarjetas
  - enlaces de share

### 3.5 Módulo E — Catálogo Oficial de Contenidos (Anti-clonación)
**Objetivo:** si no está aquí, no es oficial.
- `CONTENT_ID` global (RFJ-YYYY-...)
- Plataforma(s) publicadas: TikTok / YT / IG / Podcast
- Fecha y versión
- Servilleta asociada (Sxx)
- UTMs
- Hash/huella opcional

### 3.6 Módulo F — Buzón de Oración
**Objetivo:** canalizar oración sin caos, con reverencia y seguimiento.
- Formulario:
  - motivo (selección)
  - detalle (texto)
  - urgencia (1–3)
  - privacidad (público/privado/solo equipo)
- Estados:
  - recibido
  - en oración
  - respondido/testimonio (si aplica)
- Notificaciones:
  - confirmación al usuario
  - opción “quiero que oren conmigo en vivo” (cuando exista)

### 3.7 Módulo G — Buzón de Preguntas (Q&A)
**Objetivo:** convertir la interacción masiva en backlog estructurado.
- Formulario:
  - pregunta
  - contexto
  - tema
  - nivel (nuevo / intermedio)
  - permiso de publicación anónima
- Flujo:
  - triage automático (IA)
  - cola por prioridad
  - respuesta: texto / video / servilleta sugerida / episodio
- Respuesta siempre con:
  - textos ancla
  - vínculo a servilleta
  - advertencias si tema sensible

### 3.8 Módulo H — Devocional (Diario)
**Objetivo:** disciplina sostenible (S3) sin depender de redes.
- “Devocional del día”:
  - audio 2–5 min
  - texto
  - 1–2 versículos
  - 1 aplicación
- Programación:
  - calendario
  - notificación al usuario (email/telegram)
- Archivo histórico (biblioteca devocional)

### 3.9 Módulo I — Academia (S2)
**Objetivo:** rutas autodidactas, curadas.
- Cursos:
  - “Inicio” (evangelio claro)
  - “Doctrina básica”
  - “Cómo leer la Biblia”
  - “Cinco Solas / núcleo”
- Recursos:
  - lecturas
  - videos
  - quizzes ligeros (opcionales)
- Importante: curación de bibliografía (sana doctrina)

### 3.10 Módulo J — Comunidad (S7) / Grupos
**Objetivo:** oración + estudio en equipos, escalable con moderación.
- Fase 1: “comunidad asíncrona” (comentarios / foros moderados)
- Fase 2: grupos (Telegram/Discord/WhatsApp/foro interno)
- Fase 3: células/estudios con calendario (integración Google Meet/Zoom)

### 3.11 Módulo K — Consejería / Discipulado (S5)
**Objetivo:** acompañar sin colapsar, con límites y rutas.
- Entrada: formulario + triage (IA)
- Salida:
  - respuesta pública (anónima) si aplica
  - respuesta privada (si hay capacidad)
  - ruta a congregación local (cuando sea posible)
- Límites:
  - no reemplazar psicología/medicina
  - rutas de emergencia para riesgo (ver sección 13)

### 3.12 Módulo L — Misiones / Predicación / Entrenamiento (S6)
**Objetivo:** formar multiplicadores.
- Ruta: “de alumno → mensajero”
- Paquetes:
  - guiones
  - servilletas para predicar
  - entrenamiento de conversación
  - guía de evangelización contextual

### 3.13 Módulo M — Perseverancia (S8)
**Objetivo:** sostener años, no semanas.
- plan de lectura anual
- recordatorios
- hitos de crecimiento
- testimonios
- “señales de alerta” (abandono, crisis)

---

## 4) Modelo de Datos (Entidades Canónicas)

> Esto es para agentes IA y para diseño DB.

### 4.1 Entidades núcleo
- **User**
  - id, email, profile, preferences, locale
- **Front**
  - id (F1..F5), nombre, descripción, tags
- **Service**
  - id (S0..S8), nombre, propósito, acciones, recursos
- **Servilleta**
  - id (S001..S099), título, ejes, tags, textos_ancla, assets
- **ContentCatalogItem**
  - content_id, platform, url, servilleta_id, created_at, version, utm
- **PrayerRequest**
  - id, user_id, category, text, privacy, status, created_at
- **Question**
  - id, user_id, text, category, sensitivity, status, response_ref
- **Response**
  - id, type (text/video/servilleta/podcast), links, verses, created_at
- **Route**
  - id, name, target (newcomer/...), steps (servilletas/services)
- **Progress**
  - user_id, service_id, status, timestamps, notes

### 4.2 Trazabilidad obligatoria
Toda acción se loguea:
- `event_name`
- `user_id`
- `timestamp`
- `source` (utm)
- `front_id`
- `service_id` (si aplica)
- `servilleta_id` (si aplica)

---

## 5) API & Contrato para Agentes IA (Agent-Centric Architecture)

### 5.1 Principio: agentes trabajan sobre objetos canónicos
Un agente no “inventa contenido”: compone desde:
- servilletas oficiales
- kernel doctrinal
- políticas de alcance
- catálogo oficial

### 5.2 “AI Tooling Layer”
- **Content Generator**: genera borradores (TT script, YT outline, carrusel)
- **Doctrinal QA**: valida anclas, centro, lenguaje, riesgos
- **Triage**: clasifica oraciones/preguntas
- **Repurposer**: convierte una servilleta en 6 formatos
- **Cataloger**: registra CONTENT_ID y publica índices

### 5.3 Permisos (crítico)
- Agente puede: proponer / redactar / clasificar.
- Agente no puede: publicar directo sin aprobación (por defecto).
- Agente no puede: cambiar kernel doctrinal sin “review”.

---

## 6) UX: “Claridad en 7 segundos”

### 6.1 Home del Hub (primer pantallazo)
Debe responder instantáneo:
- ¿Qué es esto?
- ¿Cómo lo uso?
- ¿Dónde empiezo?

Componentes:
1) **Botón**: “Empieza aquí”
2) **Mapa**: escalera S0..S8
3) **Buzones**: Oración / Pregunta
4) **Biblioteca 99**: “Ver paquete”
5) **Credo/Qué creemos**: link visible

### 6.2 Ruta “Start”
La ruta start debe llevar a:
- S1 (evangelio claro)
- S0 (oración privada) — sin moralismo
- y 3 servilletas iniciales (S001..S003)

---

## 7) MVP vs V1 vs V2 (roadmap de plataforma)

### 7.1 MVP (rápido, usable, centraliza)
- Login ligero
- Mapa S0..S8 (UI simple)
- Biblioteca 99 (aunque sea 10 piezas iniciales)
- Buzón Oración + Buzón Preguntas
- Catálogo Oficial (tabla simple)
- Página “Qué creemos”
- UTMs + tracking mínimo

### 7.2 V1 (estructura robusta)
- Rutas sugeridas personalizadas
- Devocional diario (audio + notificación)
- Academia con 2 cursos
- Q&A con triage IA + respuestas indexadas
- Moderación base

### 7.3 V2 (escala y comunidad)
- Comunidades por frente
- Lives integrados (calendar)
- Entrenamiento S6 (misiones)
- Perseverancia S8 con planes + métricas
- Seguridad avanzada anti-clonación

---

## 8) Stack Tecnológico (2026) — orientado a velocidad + trazabilidad

> No se impone stack único; se define un perfil.

### 8.1 Perfil del stack ideal
- Frontend: Next.js / React + Tailwind (rápido, SEO, PWA)
- Backend: Node (NestJS) o Java (Spring) o Python (FastAPI)
- DB: Postgres (canónico) + Redis (caché)
- Search: Meilisearch/Typesense + embeddings (vector DB opcional)
- Storage: S3 compatible
- Auth: NextAuth / Cognito / Auth0 (o custom passkeys)
- Analytics: PostHog / GA4 (con ética)
- Queue: BullMQ / PubSub / SQS
- AI orchestration: workflows + agents (n8n, Temporal, custom)

### 8.2 Vectorización (opcional pero poderosa)
- Indexar:
  - servilletas
  - kernel doctrinal
  - Q&A respondidas
- Permite:
  - búsqueda semántica bíblica (con referencias)
  - recomendación de rutas
  - asistente interno “pregunta y te guía a Sxx + textos”

**Guardarraíl:** el asistente interno nunca reemplaza “verificar con Biblia”.

---

## 9) SEO y Evergreen: “la plataforma respira por búsquedas”

### 9.1 Páginas indexables clave
- /servilletas/S027
- /servicios/S4
- /preguntas/ansiedad-cristiana
- /rutas/inicio
- /que-creemos

### 9.2 Schema + metadatos
- OpenGraph por servilleta
- canonical URLs
- breadcrumbs
- sitemap

---

## 10) Integración con Canales (Core Canales 06)

### 10.1 Link-in-bio temporal
Mientras MVP:
- Linktree: botón #1 Hub
- botones secundarios: YouTube, Podcast, IG

### 10.2 Publicación y Catálogo Oficial
Toda pieza publicada en redes:
- se registra en Catálogo
- obtiene `CONTENT_ID`
- apunta a:
  - servilleta Sxx en Hub
  - servicio Sx si aplica

---

## 11) Política Editorial y QA Doctrinal (dentro del Hub)

### 11.1 Regla editorial de oro
Cada contenido:
- 2–6 textos ancla
- centro en Cristo
- lenguaje para no iniciados
- CTA a ruta/servilleta/servicio
- no periferia como centro

### 11.2 Mecanismo de revisión
- Draft → QA doctrinal → publicación → registro catálogo
- Versionado: v1, v1.1, v2 (si corrige)

---

## 12) Privacidad y Datos Sensibles (oración, crisis, confesiones)

### 12.1 Principios
- Minimización de datos
- Consentimiento explícito
- Control por el usuario
- Seguridad por defecto

### 12.2 Datos delicados
Oraciones/preguntas pueden contener:
- salud mental
- abuso
- autolesión
- violencia

**Regla:** almacenar y mostrar con estricta privacidad; por defecto privado.

---

## 13) Manejo de Riesgo (suicidio, abuso, emergencia)

### 13.1 Detección y rutas
Si texto indica riesgo:
- mostrar mensaje de ayuda inmediata (país)
- recomendar contacto local
- limitar respuestas automatizadas
- marcar como `high_risk`

### 13.2 Política de límites
La plataforma:
- acompaña espiritualmente,
- pero no pretende sustituir emergencias ni psicología clínica.

---

## 14) Seguridad 2026: Anti-clonación y Protección Legal

### 14.1 Canonicidad verificable
- Catálogo oficial público
- IDs canónicos
- timestamps
- rutas oficiales

### 14.2 Defensa contra suplantación
- página “Cómo verificar contenido”
- “Si no está indexado, no es RFJ”
- firma editorial (referencias Sxx + ID)

### 14.3 Registro de disclaimers por contenido
Cada pieza sensible:
- disclaimer automático
- referencias y límites

---

## 15) Diseño para “1 operador” (sostenible) y para “n equipos” (escala)

### 15.1 Panel de administración
- cola de preguntas
- cola de oraciones
- estado de publicaciones
- generador de contenido (IA)
- exportadores (YouTube desc, guiones, etc.)

### 15.2 Automatizaciones mínimas (MVP+)
- clasificación automática de preguntas
- sugerencia de servilleta
- generación de borrador
- creación de `CONTENT_ID`
- registro en catálogo

---

## 16) Declaración Final (la plataforma en una frase)

> **La Casa Madre será el lugar donde una persona —sin ser iniciada— pueda entrar desde su dolor o curiosidad, ser identificada sin fricción, recibir una ruta clara, verificar la verdad con su Biblia, avanzar por la escalera de servicios, y permanecer a largo plazo; mientras cada contenido oficial queda trazado, versionado y protegido, y todo el sistema se vuelve escalable por agentes de inteligencia artificial sin diluir el centro: Cristo, el evangelio y la gloria de Dios.**

---

## 17) Entregables de este Core (para repositorio)

- `07_Core_Plataforma_Web_SaaS.md` (este documento)
- `platform/` (carpeta de specs)
  - `domain_model.md`
  - `events_tracking.md`
  - `roles_permissions.md`
  - `mvp_scope.md`
  - `security_privacy.md`
  - `api_contracts.md`
- `ui/` (wireframes y flujos)
  - `home_hub_flow.md`
  - `service_node_template.md`
  - `servilleta_page_template.md`

---

## 18) Checklist de Aceptación (para agentes IA y humanos)

**Este Core se considera “cumplido” cuando:**
1) Existe un Hub navegable con S0..S8 visibles.
2) Existe registro/login ligero.
3) Existe biblioteca (aunque parcial) de servilletas.
4) Existen buzones (oración/preguntas).
5) Existe catálogo oficial público.
6) Existe “Qué creemos” visible.
7) Cada contenido puede enlazar a Sxx y registrarse con ID.

---

**Fin del contrato base de plataforma.**