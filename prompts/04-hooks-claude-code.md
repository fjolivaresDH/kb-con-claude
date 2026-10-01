# Prompt de los hooks · Claude Code

Para que las reglas que más se olvidan las haga cumplir Claude Code: regenerar las vistas, avisar de cambios sin anotar y no editar a mano lo generado.

```
Quiero que las reglas que más se olvidan las haga cumplir Claude Code, no mi memoria.

Crea en _herramientas/ dos scripts en Python:

1. cierre_sesion.py, que se ejecuta al terminar cada respuesta y:
   - regenera las vistas si hay documentos más nuevos que _catalogo.md;
   - avisa si se han tocado documentos después de la última entrada de log.md;
   - busca patrones de contraseñas, claves o tokens en lo recién escrito;
   - avisa si hoy se han tocado documentos y bitacora.md no tiene entrada de hoy.
   Que solo hable cuando haya algo que decir, devolviendo un JSON con "systemMessage".

2. proteger_vistas.py, que DENIEGA editar a mano cualquiera de las vistas generadas
   (_catalogo.md, _pendientes.md, _calendario.md, _cruces.md, _entidades.md) y explica por qué:
   se corrige el documento de origen y se regenera.

Engánchalos en .claude/settings.local.json: el primero en el evento Stop y el segundo en
PreToolUse con matcher "Write|Edit". Deja escrito en las convenciones qué hace cada uno y que
los hooks hacen cumplir las reglas, pero no las sustituyen. Después dime cómo comprobarlo con /hooks.
```
