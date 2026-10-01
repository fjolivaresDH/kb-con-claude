# Prompt inicial · Claude Code

Pégalo en Claude Code, dentro de la carpeta vacía. Antes, sustituye `[ORGANIZACIÓN]` y `[ÁREAS]`. Es el mismo que el de Cowork, pero deja las reglas en un `CLAUDE.md`. Explicación en la [guía de Claude Code](../guia-claude-code.md).

```
Quiero que construyas en esta carpeta una base de conocimiento para [ORGANIZACIÓN].

Para qué la quiero: que hagas de asistente que retiene todo lo que a mí me cuesta recordar o que
tengo desperdigado en correos, carpetas, hojas de cálculo y programas distintos —vencimientos,
accesos, decisiones y por qué se tomaron, contactos, estados de proyectos—. Tú lo guardas en su
sitio y dejas constancia, para que yo pueda preguntártelo después o leerlo directamente.

Usa el formato OKF (Open Knowledge Format de Google Cloud). La especificación es esta,
consúltala antes de empezar:
https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md

Aviso: las siglas "OKF" designan también otras cosas (por ejemplo la Open Knowledge
Foundation). Usa exclusivamente la especificación del enlace anterior.

REGLAS DE FORMATO (aplícalas siempre, también en el futuro):
- Un tema = un archivo .md, con nombre en kebab-case (ejemplo: registro-facturas.md).
- Cada documento de concepto empieza con frontmatter YAML y el campo "type" es OBLIGATORIO.
  "type" es un vocabulario abierto (la spec no registra los valores centralmente), pero que sea
  abierto NO significa libre: dos etiquetas para la misma cosa parten el vocabulario y rompen
  cualquier filtro por tipo. Empezaremos con estos cuatro, en español y en singular:
    Referencia    -> qué es algo y cómo está montado. El caso normal.
    Procedimiento -> pasos para hacer algo.
    Herramienta   -> ficha de una aplicación o servicio.
    Concepto      -> una idea o término, sin instancia concreta detrás.
  Mantén la lista de tipos en uso escrita en el documento de convenciones. Si algún día ninguno
  encaja y hace falta uno nuevo, AÑÁDELO A ESA LISTA en el mismo cambio: si no, nadie sabrá que
  existe y acabará duplicado.
  Incluye también: title, description, tags (lista) y timestamp (fecha AAAA-MM-DD).
- Cada carpeta tiene su propio index.md que lista lo que contiene, PERO los index.md NO llevan
  frontmatter (spec §8). Única excepción: el index.md de la raíz del bundle, que lleva
  únicamente okf_version: "0.2" y nada más.
- Los enlaces entre documentos usan rutas absolutas del bundle: /carpeta/archivo.md
- Hay un log.md en la raíz donde anotas CADA cambio con una línea, agrupando por día bajo una
  cabecera "## AAAA-MM-DD".

CREA ESTA ESTRUCTURA:
1. index.md en la raíz: índice general, con la lista de áreas y cómo está organizado todo
   (su único frontmatter es okf_version: "0.2").
2. log.md en la raíz: diario de cambios (empieza con la línea de la creación inicial).
3. _plantillas/ con index.md y una plantilla vacía por cada tipo, lista para copiar:
   referencia.md, procedimiento.md, herramienta.md y concepto.md. Cada una con su frontmatter de
   ejemplo, y el "type" de cada plantilla debe ser el suyo (la de concepto dice Concepto, no otro).
4. _documentos/ con un README.md que explique que es el "buzón" donde se dejan los PDFs
   pendientes de procesar, y tres subcarpetas: facturas/, contratos/ y otros/ (esta última para
   todo lo que no sea ni factura ni contrato: certificados, ofertas, actas, informes, manuales…).
5. _data/ con index.md, facturas.json y contratos.json (ver el apartado siguiente).
6. Una carpeta por cada una de estas áreas, cada una con su index.md: [ÁREAS]

CAPA DE DATOS EN JSON (_data/):
Además de las tablas en Markdown, quiero los contratos y las facturas en JSON, porque son
registros que se filtran, ordenan y suman. Crea los dos ficheros con el array vacío y un
bloque "_meta" que documente el esquema, usando exactamente estos campos:

facturas.json -> array "facturas", cada elemento con:
  num, contrato_id, fecha, vencimiento, proveedor, proveedor_id, concepto, empresa,
  base, iva, total, moneda, recurrente (true/false), notas

contratos.json -> array "contratos", cada elemento con:
  id, objeto, proveedor, proveedor_id, empresa, fecha, estado, firma_fecha,
  importe, moneda, duracion, vencimiento, preaviso, historico, notas

EL VÍNCULO ENTRE LOS DOS (importante, y es lo que más rendimiento da):
Casi toda factura responde a un contrato, y casi todo contrato acaba en facturas. Guarda ese
vínculo EN UN SOLO SENTIDO, para no mantenerlo dos veces:
- Cada factura lleva "contrato_id" con el id del contrato al que responde, o null si es una
  compra suelta.
- Los contratos NO llevan lista de facturas: se obtiene filtrando por contrato_id.
Con eso se puede preguntar "cuánto llevamos pagado de esta bolsa de horas" o "qué contratos aún
no han generado ninguna factura". Y avísame de las facturas con contrato_id null que deberían
tener uno: significa que se está pagando algo que no está contratado en el registro.

Convenciones de los datos: fechas en formato AAAA-MM-DD; importes numéricos sin separador
de miles; null cuando el dato no consta.

El campo "estado" de los contratos es una LISTA CERRADA declarada en el _meta
(firmado, facturado, sin_firmar, oferta_pendiente, por_confirmar). Usar un valor no declarado
rompe los filtros en silencio: si hace falta uno nuevo, se añade al _meta en el mismo cambio.

Las facturas NO llevan campo "estado": si una factura está pagada, vencida o pendiente es cosa
de la contabilidad, no de la base de conocimiento. Un campo que valiera siempre "registrada" se
leería como estado de pago y estaría mintiendo. No lo añadas.

DECLARA EL ALCANCE DE CADA REGISTRO en su _meta y en la cabecera de su tabla, porque cambia
cómo se usan y no se puede adivinar leyéndolos:
- Contratos = CENSO: aspiran a estar todos. Si falta uno, es un agujero que hay que cerrar. Los
  contratos ya cerrados no se borran: llevan "historico": true y siguen ahí, porque "qué hemos
  contratado alguna vez con X" es una pregunta real.
- Facturas = decide TÚ y escríbelo. Si vas a meterlas todas, es un censo y se pueden sumar. Si
  vas a meter solo algunas para dejar constancia de que ese gasto existe, es una MUESTRA y
  entonces hay que avisar de que NUNCA se suman como gasto total.

En _data/index.md explica para qué sirve la capa de datos, documenta los dos esquemas, deja
ejemplos de consulta y escribe estas dos reglas de mantenimiento:
1. Al añadir o cambiar un contrato o una factura hay que actualizar LAS DOS VISTAS, la tabla
   Markdown (legible, para leer y compartir) y el JSON (estructurado, para consultar).
2. PRIMERO EL JSON Y DESPUÉS LA FILA. Cuando esto se desincroniza, lo que falta casi siempre es
   la fila del Markdown. Y si difieren: el JSON manda en los datos duros (fechas, importes,
   estados) y el Markdown manda en el relato (qué dice el contrato, qué cláusula importa).

Crea también estos dos registros en Markdown, enlazados con sus JSON:
- Un registro de contratos (tabla: contrato, proveedor, objeto, empresa, fecha/estado,
  importe) más una sección "Vencimientos y renovaciones" para poder responder en cualquier
  momento a "qué vence en los próximos 6 meses".
- Un registro de facturas (tabla: nº, fecha, vencimiento, proveedor, concepto, empresa,
  base, IVA, total, notas).

OJO CON "QUÉ VENCE": los contratos con proveedores no son lo único que vence. Los dominios, el
hosting, los certificados y las suscripciones tienen su propio calendario, y suelen vencer antes
y más a menudo. Si llevas esas cosas en otro documento, HAZ QUE LOS DOS SE CITEN MUTUAMENTE, y
para responder "qué vence en los próximos 6 meses" mira siempre los dos. Un calendario que no
sabe que existe el otro da una respuesta incompleta que parece completa.

CÓMO VAMOS A TRABAJAR (esto es lo más importante):
La mayor parte del conocimiento no va a llegarte como documentos en una carpeta, sino que te lo
iré contando: datos sueltos en el chat, correos que pego, capturas de pantalla, decisiones,
aclaraciones y correcciones de cosas que ya me habías guardado. Quiero que eso lo trates como
material de primera y lo archives igual de bien que un PDF. En concreto:
- Cuando te dé un dato o me explique algo, decide TÚ en qué documento del bundle encaja y
  guárdalo ahí, sin preguntarme dónde va. Si no existe el documento adecuado, créalo en el área
  que corresponda y añádelo al index.md de esa carpeta.
- Antes de crear algo nuevo, comprueba si ya existe un documento que cubra ese tema y
  actualízalo en vez de duplicar la información.
- EL BARRIDO: si el dato afecta a varios documentos, propágalo a TODOS los sitios afectados, no
  solo a uno. Este es el paso que convierte una carpeta de archivos en una base de conocimiento,
  y es el que más se olvida. Pregúntate siempre: el index.md de la carpeta (si no, la página nace
  huérfana), el directorio de contactos, los registros y sus JSON, los calendarios de
  vencimientos, los inventarios y los accesos.
- Si lo que te digo contradice algo que ya tienes guardado, AVÍSAME señalando la contradicción
  en vez de sobrescribir sin más. Y si no consta cuál es la buena, DÉJALO ESCRITO en el
  documento, con las dos versiones, la fecha, de dónde sale cada una y qué haría falta para
  cerrarla. Lo peligroso no es la contradicción: es elegir una versión sin dejar rastro, porque
  quien lo lea después verá un dato limpio y no sabrá que hubo dos.
  Ojo: que un dato haya CAMBIADO (un precio que sube, un contacto que se va) no es una
  contradicción, es una actualización: se sustituye y se refecha.
- LO QUE ME RESPONDAS Y VALGA LA PENA, ARCHÍVALO. Buena parte del valor no aparece al guardar un
  documento, sino al preguntar: una comparativa, un cruce entre áreas, un descuadre que sale al
  juntar la información. Eso nace en el chat y muere en el chat si nadie lo escribe. Si una
  respuesta ha costado trabajo y volvería a hacer falta, guárdala como documento en el área que
  toque y añádela a su index.md. Señales de que toca: la pregunta se ha hecho más de una vez, la
  respuesta cruza varios documentos, aparece un dato que no estaba en ninguno, o se toma una
  decisión y conviene saber POR QUÉ dentro de seis meses.
- Si revisamos algo que parecía un problema y decidimos que no lo es, ANÓTALO CON SU FECHA como
  revisado y descartado. Si no, volverá a salir como hallazgo en cada revisión y acabaremos
  ignorando los avisos.
- Cuando te corrija, corrige el documento y no dejes rastros de la versión anterior salvo que
  el histórico tenga valor; en ese caso, márcalo claramente como superado.
- FECHA LA INFORMACIÓN QUE CADUCA. Cuando guardes un dato perecedero —inventarios y recuentos
  (unidades, equipos, licencias), estados ("sin firmar", "pendiente de activar", "en curso"),
  cifras que veas en
  una pantalla o captura, precios y cuotas, contactos— anota entre paréntesis la fecha en que te
  lo doy: por ejemplo "340 unidades contratadas (dato de 2026-03-15)" o "pendiente de activar
  (marzo 2026)". Así sabré si un dato está fresco o caducado. No hace
  falta fechar lo estable (un CIF, una cláusula de un contrato firmado, una definición). Si
  revisamos un dato fechado y sigue vigente, actualiza la fecha.
- Anota cada cambio en log.md, UNA LÍNEA POR CAMBIO, bajo una cabecera "## AAAA-MM-DD" del día.
  Abre una cabecera nueva cada día; no acumules entradas bajo una fecha anterior. El log dice QUÉ
  cambió y CUÁNDO; no es el sitio de los razonamientos ni de los análisis. Si una entrada del log
  te está saliendo de un párrafo, ese párrafo pertenece a un documento.
- Al final de un bloque de trabajo, dime en qué archivos has escrito.

CRITERIOS QUE DEBES RESPETAR SIEMPRE:
- Privacidad: NUNCA guardes contraseñas, claves de API ni datos personales sensibles. Si un
  documento los contiene, extrae solo lo necesario y omite el resto, avisándome de ello.
- Constancia: marca algo como "firmado" o "contratado" SOLO si hay constancia real (documento
  firmado, contrato en vigor o factura). Si es un borrador, una oferta o un gasto autorizado,
  indícalo así; no lo des por firmado.
- Importes: puedes guardarlos en la base de conocimiento, pero no los incluyas en documentos
  destinados a terceros salvo que te lo pida expresamente.
- Ante la duda o si falta un dato, pregúntame o márcalo como "por confirmar". No lo inventes.

Cuando termines:
1. Muéstrame el árbol de carpetas y archivos creados.
2. Crea en la raíz un CLAUDE.md, que es lo que Claude Code lee al abrir cada sesión: un resumen de
   todas las reglas anteriores como instrucciones permanentes (máximo 20 líneas, dirigiéndote a ti
   mismo en segunda persona, sin adornos), y que importe el índice y las convenciones con dos
   líneas "@index.md" y "@CONVENCIONES.md". Pon las reglas de formato completas en CONVENCIONES.md.
3. Dime cómo empezamos a cargar conocimiento.
```
