# Prompt de crecimiento

**Semanas después**, sobre la base que ya tienes: añade las vistas generadas, las reglas de cruce y las consultas. Funciona en Cowork y en Claude Code. Por qué no se pega el primer día: [guía de Cowork, parte 3](../guia-cowork.md#parte-3--el-prompt-de-crecimiento-cuando-ya-tengas-contenido).

```
La base de conocimiento ya tiene contenido y se me está haciendo grande: para responder una
pregunta tengo que abrir varios archivos. Quiero añadirle las herramientas que lo resuelven.

Antes de escribir nada, LEE lo que ya hay y dime qué encuentras. No inventes reglas genéricas:
quiero que salgan de MIS documentos.

1. VISTAS GENERADAS. Escribe un script en Python, en _herramientas/regenerar.py, que las regenere todas de una vez,
   y créalas:
   - _catalogo.md    -> todos los documentos con su tipo, título y descripción, sacados del
                        frontmatter. Responde "qué documento habla de esto".
   - _pendientes.md  -> cada línea marcada como pendiente o aviso, CON ARCHIVO Y LÍNEA.
                        Se alimenta de los marcadores que yo escriba (⚠️, 🚨, "- [ ]",
                        "pendiente", "por confirmar") y se cierra marcando la línea con ✅
                        o "resuelto". Encabézalo con "lo que tiene fecha", ordenado por
                        proximidad: ahí entra toda fecha futura que aparezca en la línea, y
                        una fecha pasada solo si el texto habla de plazo (antes del, vence,
                        caduca). Ojo: la mayoría de las fechas de la base son sellos de
                        "dato de tal día" y NO son vencimientos; si las cuelas, la vista no
                        sirve.
   - _calendario.md  -> vencimientos y fechas clave ordenados por proximidad.
   - _cruces.md      -> los descuadres. Ver el punto 2.
   - _entidades.md   -> identificadores (correos, CIF, dominios) que aparezcan en 2 o más
                        documentos, con dónde salen.

2. REGLAS DE CRUCE. Este es el punto importante y quiero que lo hagas mirando mis datos:
   revisa la base y proponme reglas de "ausencia esperada" —algo que está en un documento y
   debería estar en otro— basadas en descuadres que veas DE VERDAD. Enséñame la lista con un
   ejemplo real de cada una antes de programarlas, y descartamos las que no valgan.

3. CONSULTAS CON NOMBRE. Un script aparte, en _herramientas/consultar.py, para las preguntas que
   repito, y un _consultas/index.md
   que las liste con su comando. Guarda la RECETA, no la respuesta: una respuesta escrita caduca
   sin avisar y nadie se entera.

4. REVISIÓN DE SALUD. Un revision-salud.md con qué mirar periódicamente: datos fechados de hace
   más de seis meses, pendientes cuya fecha ya pasó, enlaces rotos comprobados abriéndolos,
   descuadres entre cada tabla y su JSON, documentos sin "type" y páginas que no cuelgan de
   ningún index.md.

5. _hallazgos.md: una línea por cada cruce que ya nos haya dado valor, con sus fuentes, para no
   volver a descubrirlo. Arráncalo con los que encuentres ahora.

6. En _data/ (créala si no existe, con su index.md), añade eventos.json (fechas que no son
   vencimientos de contrato: dominios,
   certificados, fines de soporte, recordatorios) y alias.json (nombres distintos para la misma
   cosa, para que el índice de coincidencias no la parta en dos).

REGLAS QUE DEBEN QUEDAR ESCRITAS en el documento de convenciones:
- Las vistas generadas NO se editan a mano, nunca. Se corrige el documento de origen y se
  regenera. Un cambio escrito en la vista se pierde en la siguiente pasada y, mientras dura,
  miente.
- Se regeneran al terminar cada bloque de cambios.
- Un pendiente escrito sin marcador está escondido, no anotado. Y si tiene plazo, la fecha va
  en la misma línea.
- Cuando un descuadre sea una decisión consciente y no un error, se anota el motivo en el
  documento de origen para que deje de saltar.

NO toques el contenido que ya existe salvo para añadir los marcadores que falten, y dime antes
qué vas a cambiar. Al terminar, enséñame el árbol y ejecuta la regeneración una vez para que yo
vea las vistas llenas.
```
