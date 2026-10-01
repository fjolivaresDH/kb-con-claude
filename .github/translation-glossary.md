# Translation glossary (Spanish → English)

The Spanish files are the **source**. The English files under `en/` are translations and must keep the same
structure: same sections, same tables, same code blocks, in the same order. Use these terms everywhere, so that
the names a user sees in a guide match the ones the prompt creates.

## Files and folders the prompts create

| Spanish | English |
|---|---|
| `_plantillas/` | `_templates/` |
| `_documentos/` (`facturas/`, `contratos/`, `otros/`, `_buzon/`) | `_documents/` (`invoices/`, `contracts/`, `other/`, `_inbox/`) |
| `_data/` | `_data/` |
| `facturas.json` · `contratos.json` | `invoices.json` · `contracts.json` |
| `eventos.json` · `alias.json` | `events.json` · `aliases.json` |
| `_herramientas/` | `_tools/` |
| `_consultas/` | `_queries/` |
| `_catalogo.md` · `_pendientes.md` · `_calendario.md` | `_catalog.md` · `_pending.md` · `_calendar.md` |
| `_cruces.md` · `_entidades.md` · `_hallazgos.md` | `_crosschecks.md` · `_entities.md` · `_findings.md` |
| `revision-salud.md` | `health-check.md` |
| `bitacora.md` | `handoff.md` |
| `CONVENCIONES.md` | `CONVENTIONS.md` |
| `registro-facturas.md` · registro de contratos | `invoice-register.md` · contract register |
| `regenerar.py` · `consultar.py` | `regenerate.py` · `query.py` |
| `cierre_sesion.py` · `proteger_vistas.py` | `session_close.py` · `protect_views.py` |
| `index.md` · `log.md` · `CLAUDE.md` | unchanged |

## Concept types (`type`)

`Referencia` → `Reference` · `Procedimiento` → `Procedure` · `Herramienta` → `Tool` · `Concepto` → `Concept`.
In the English prompt: "in English and in the singular".

## JSON fields

**Invoices:** `num` → `number` · `contrato_id` → `contract_id` · `fecha` → `date` · `vencimiento` → `due_date` ·
`proveedor` → `supplier` · `proveedor_id` → `supplier_id` · `concepto` → `description` · `empresa` → `company` ·
`base` → `net` · `iva` → `tax` · `total` → `total` · `moneda` → `currency` · `recurrente` → `recurring` · `notas` → `notes`.

**Contracts:** `id` → `id` · `objeto` → `subject` · `proveedor` → `supplier` · `proveedor_id` → `supplier_id` ·
`empresa` → `company` · `fecha` → `date` · `estado` → `status` · `firma_fecha` → `signed_date` · `importe` → `amount` ·
`moneda` → `currency` · `duracion` → `duration` · `vencimiento` → `expiry` · `preaviso` → `notice_period` ·
`historico` → `historical` · `notas` → `notes`.

**Contract status values:** `firmado` → `signed` · `facturado` → `invoiced` · `sin_firmar` → `unsigned` ·
`oferta_pendiente` → `pending_offer` · `por_confirmar` → `to_confirm`.

## Markers and recurring words

| Spanish | English |
|---|---|
| «pendiente» · «por confirmar» | "pending" · "to confirm" |
| «resuelto» | "resolved" |
| base de conocimiento | knowledge base |
| vistas generadas | generated views |
| descuadres · cruces | mismatches · cross-checks |
| barrido | sweep |
| bitácora | handoff log (file `handoff.md`) |
| revisión de salud | health check |
| buzón | inbox |
| CIF / identificador fiscal | tax ID |
| IVA | VAT |
| Descargas | Downloads |
| «Instrucciones», «Contexto», «Programado», «Memoria» (Cowork panel) | "Instructions", "Context", "Scheduled", "Memory" |
| tarea programada | scheduled task |
| Lo que aprendimos rompiéndolo | What we learned by breaking it |

## Tone

Plain, direct English, second person ("you"), short sentences. No jargon the Spanish does not use. Keep
the emphasis (**bold**, *italics*) where the Spanish has it. Dates as in the source.
