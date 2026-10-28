# Prompt de los hooks · Claude Code

Para que las reglas que más se olvidan las haga cumplir Claude Code: regenerar las vistas, avisar de cambios sin anotar, no editar a mano lo generado y no perder datos al escribir. **Se pega después del prompt de crecimiento (03)**, que es el que crea las vistas.

```
Quiero que las reglas que más se olvidan las haga cumplir Claude Code, no mi memoria.

Crea en _herramientas/ tres scripts en Python para los hooks y una utilidad:

1. cierre_sesion.py, que se ejecuta al terminar cada respuesta y:
   - regenera las vistas si hay documentos más nuevos que _catalogo.md;
   - avisa si se han tocado documentos después de la última entrada de log.md;
   - busca patrones de contraseñas, claves o tokens en lo recién escrito;
   - comprueba que no quede ningún .md vacío;
   - si existe bitacora.md, avisa cuando hoy se han tocado documentos y no tiene entrada de hoy.
   Que solo hable cuando haya algo que decir, devolviendo un JSON con "systemMessage".

2. proteger_vistas.py, que DENIEGA editar a mano cualquiera de las vistas generadas
   (_catalogo.md, _pendientes.md, _calendario.md, _calendario-anual.md, _cruces.md, _entidades.md)
   y explica por qué: se corrige el documento de origen y se regenera.

3. vigilar_tamanos.py, que se ejecuta después de cada acción que escribe y compara el tamaño de
   todos los .md y de los JSON de _data/ con la foto anterior (guárdala en un archivo aparte, dentro
   de la carpeta). Si alguno se ha vaciado, ha encogido a menos de la mitad o ha desaparecido, avisa
   en ese mismo momento, con el nombre del archivo, devolviendo un "systemMessage". Si avisa, hay
   que parar y restaurar antes de seguir.

4. seguro.py, una utilidad que NO es un hook. Ningún script escribe un documento con open(ruta, "w"):
   eso vacía el archivo en el instante de abrirlo, y si después falla la lectura, se queda a cero.
   seguro.py ofrece tres funciones: reemplazar un texto, insertar tras una línea y escribir un archivo
   entero. Las tres LEEN antes, escriben de golpe en un archivo temporal y lo cambian por el
   original, y se NIEGAN a vaciar un archivo o a dejarlo en menos de la mitad. Los cambios en bloque
   se hacen con ella; los sueltos, con la herramienta de edición.

Engancha los tres hooks en .claude/settings.local.json: el primero en el evento Stop, el segundo en
PreToolUse con matcher "Write|Edit" y el tercero en PostToolUse con matcher
"Bash|PowerShell|Write|Edit". Llama a los scripts con "py" y no con "python": en Windows, "python"
puede ser el acceso directo de la Microsoft Store, que no ejecuta nada y falla sin decir nada (en
macOS y Linux, "python3"). Deja escrito en las convenciones qué hace cada uno y que los hooks hacen
cumplir las reglas, pero no las sustituyen. Después, comprueba con /hooks que están dados de alta y
haz una prueba real: con un archivo .md de prueba, vacíalo a propósito y confirma que el aviso
sale; luego bórralo.
```
