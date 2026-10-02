# Base de conocimiento con Claude

**Español** · [English](README.en.md)

Cómo montar, en una carpeta de archivos de texto, una **base de conocimiento de trabajo** que Claude ordena, cruza y
mantiene al día: proveedores, contratos, accesos, decisiones, procedimientos y pendientes, cada dato con su fecha y su
origen.

Sale de una base real, usada a diario durante meses. Lo que se publica aquí es **el método**:
las guías, los prompts y lo que aprendimos rompiéndola. El contenido de esa base no está, y no hace falta para montar
la tuya.

## Algunos ejemplos de lo que puedes llevar

Proveedores y contactos · contratos y vencimientos · facturas · presupuesto · tickets y gastos · accesos a servicios ·
dominios, certificados y suscripciones · procedimientos · proyectos y decisiones · inventarios · artículos y comunicación.

**Son ejemplos ya trabajados, no un límite: cada uno construye su base con sus propios temas.** Al pegar el prompt
inicial, Claude te los ofrece, te pregunta si alguno es tu caso y qué otros temas quieres llevar, y monta solo eso. Qué monta cada uno y qué preguntas responde: [`casos-de-uso.md`](casos-de-uso.md).

## Por dónde empezar

| Si usas… | Empieza por |
|---|---|
| **Claude Cowork** *(sin instalar nada)* | [`guia-cowork.md`](guia-cowork.md) |
| **Claude Code** *(terminal o pestaña Code de la aplicación de escritorio)* | [`guia-claude-code.md`](guia-claude-code.md) |

Las dos montan la misma estructura sobre la misma carpeta, así que **se pueden usar a la vez**.

**¿En Word?** Las dos guías están para descargar en la [última versión publicada](https://github.com/fjolivaresDH/kb-con-claude/releases/latest).
Se generan solas a partir de estos mismos archivos cada vez que se publica una versión, así que la web y el Word
dicen siempre lo mismo.

## Los prompts, listos para copiar

| Prompt | Cuándo |
|---|---|
| [`prompts/01-inicial-cowork.md`](prompts/01-inicial-cowork.md) | El primer día, en Cowork |
| [`prompts/02-inicial-claude-code.md`](prompts/02-inicial-claude-code.md) | El primer día, en Claude Code |
| [`prompts/03-crecimiento.md`](prompts/03-crecimiento.md) | **Semanas después**: vistas generadas, cruces y consultas |
| [`prompts/04-hooks-claude-code.md`](prompts/04-hooks-claude-code.md) | En Claude Code, después del de crecimiento: para que las reglas se cumplan solas |
| [`prompts/05-bitacora.md`](prompts/05-bitacora.md) | Si trabajas desde más de un equipo |

## La idea en tres principios

1. **Se captura cuando ocurre**: se le cuenta a Claude en el chat, sin formularios.
2. **Cada dato lleva su fecha y su prueba**: si no, no se sabe si está caducado ni se puede comprobar.
3. **Una sola fuente, con dueño**: cada cosa vive en un documento, y los demás la enlazan.

## Por qué este formato

Los documentos siguen el **[Open Knowledge Format (OKF) v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)**,
una especificación abierta de Google Cloud pensada para que el mismo conocimiento lo entiendan igual las personas y los
agentes de IA. Es mínima a propósito: una carpeta de archivos Markdown con una cabecera YAML, sin registro central y sin
ninguna herramienta obligatoria. Eso da a la base cuatro propiedades:

| | Qué significa en la práctica |
|---|---|
| **Se lee sin herramientas** | Son archivos de texto: se abren con cualquier editor, hoy y dentro de diez años. |
| **Un agente la entiende tal cual** | Claude la lee y la escribe directamente, sin adaptadores ni base de datos. |
| **Cada cambio se ve** | Una modificación es una diferencia de texto, en git o en el historial de versiones de tu nube. |
| **Es tuya y se mueve contigo** | No depende de ninguna aplicación: cambias de herramienta o de equipo y te la llevas entera. |

Y es tolerante: lo único obligatorio es que cada documento diga **qué tipo de cosa es**. Todo lo demás es opcional, así
que se puede empezar con poco y ir creciendo.

### Cada dato, con su origen, su fecha y su fiabilidad

La especificación parte de la misma idea que este método. Una base que **mantiene un agente** tiene que poder decir,
además de lo que sabe, de dónde lo sabe y cuánto vale. OKF v0.2 lo resuelve con campos en la cabecera de cada documento;
aquí, con reglas de trabajo que Claude aplica a cada dato:

| La pregunta | En OKF v0.2 | En este método |
|---|---|---|
| **¿De dónde sale?** | `sources`: las fuentes de cada documento | Cada dato lleva su prueba: se enlaza el original (y, si activas el archivo, se guarda en `_documentos/`) |
| **¿Cuánto me fío?** | `verified`: sin verificar, confirmado por un proceso o revisado por una persona | «Firmado» solo con constancia real; lo que falta se marca «por confirmar», nunca se inventa |
| **¿Sigue siendo verdad?** | `stale_after`: una fecha de caducidad por documento | **Cada dato** perecedero lleva la fecha en que se aportó, y la revisión de salud busca los viejos |
| **¿Es lo vigente?** | `status`: borrador, estable u obsoleto | Una sola fuente por tema; lo superado se marca, y `log.md` dice qué cambió y cuándo |
| **¿Lo contradice algo?** | — | Si un dato nuevo choca con uno guardado, se anotan los dos con su origen en vez de elegir en silencio |

## Propón mejoras

Esto sale de una base real y se mejora con lo que aporte cada uno: una regla que sobra, un ejemplo que falta, una
forma más sencilla de explicarlo o una tecnología que ayude. Déjalo en
[las sugerencias del repositorio](https://github.com/fjolivaresDH/kb-con-claude/issues) *(hace falta una cuenta de
GitHub, gratuita)*. Cada versión publicada dice qué ha cambiado.

## Autor y licencia

Francisco Javier Rivas Olivares. Publicado bajo [CC BY 4.0](LICENSE): puedes usarlo y adaptarlo citando la autoría.
