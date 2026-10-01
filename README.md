# Base de conocimiento con Claude

Cómo montar, en una carpeta de archivos de texto, una **base de conocimiento de trabajo** que Claude ordena, cruza y
mantiene al día: proveedores, contratos, accesos, decisiones, procedimientos y pendientes, cada dato con su fecha y su
origen.

Sale de una base real, usada a diario durante meses. Lo que se publica aquí es **el método**:
las guías, los prompts y lo que aprendimos rompiéndola. El contenido de esa base no está, y no hace falta para montar
la tuya.

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
| [`prompts/04-hooks-claude-code.md`](prompts/04-hooks-claude-code.md) | En Claude Code, para que las reglas se cumplan solas |
| [`prompts/05-bitacora.md`](prompts/05-bitacora.md) | Si trabajas desde más de un equipo |

## La idea en tres principios

1. **Se captura cuando ocurre**: se le cuenta a Claude en el chat, sin formularios.
2. **Cada dato lleva su fecha y su prueba**: si no, no se sabe si está caducado ni se puede comprobar.
3. **Una sola fuente, con dueño**: cada cosa vive en un documento, y los demás la enlazan.

El formato de los documentos sigue el **Open Knowledge Format (OKF) v0.2** de Google Cloud:
<https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md>.

## Autor y licencia

Francisco Javier Rivas Olivares. Publicado bajo [CC BY 4.0](LICENSE): puedes usarlo y adaptarlo citando la autoría.
