# Montar tu base de conocimiento con Claude Code

*Guía práctica, de la carpeta vacía a una base que se mantiene sola.*

> **Para quién es.** Para quien quiera tener su conocimiento de trabajo —proveedores, contratos, accesos,
> decisiones, procedimientos, pendientes— en una carpeta de archivos de texto que **Claude Code** ordena, cruza y
> mantiene al día. No hace falta saber programar: casi todo se hace hablando con Claude. Solo al principio hay que
> instalar un par de cosas.

## Contenido

1. [Qué vas a montar](#1-qué-vas-a-montar)
2. [Antes de empezar](#2-antes-de-empezar)
3. [Instalar Claude Code](#3-instalar-claude-code)
4. [Crear la carpeta y arrancar](#4-crear-la-carpeta-y-arrancar)
5. [El prompt inicial](#5-el-prompt-inicial)
6. [El día a día](#6-el-día-a-día)
7. [Cuando crezca: las vistas y las utilidades](#7-cuando-crezca-las-vistas-y-las-utilidades)
8. [Que las reglas se cumplan solas](#8-que-las-reglas-se-cumplan-solas)
9. [Si trabajas desde más de un equipo](#9-si-trabajas-desde-más-de-un-equipo)
10. [Seguridad y privacidad](#10-seguridad-y-privacidad)
11. [Lo que aprendimos rompiéndolo](#11-lo-que-aprendimos-rompiéndolo)

---

## 1. Qué vas a montar

Una **carpeta de documentos Markdown** —archivos de texto con un poco de formato— organizada por áreas, en la que
Claude Code guarda lo que le cuentas: un dato suelto en el chat, un correo que pegas, una captura, un PDF. Cada cosa
acaba en su sitio, con su fecha y enlazada a lo que tiene que ver.

La diferencia con una carpeta de documentos normal es que **Claude no se limita a guardar**: cuando un dato afecta a
varios documentos los actualiza todos, cuando algo contradice lo que ya había te avisa, y con el tiempo la base
aprende a decirte qué tienes pendiente, qué vence pronto y qué no cuadra entre dos documentos.

### Tres principios

1. **Se captura cuando ocurre.** Lo que no se apunta en el momento se pierde. Por eso se le cuenta a Claude en el
   chat, sin formularios.
2. **Cada dato lleva su fecha y su prueba.** Un dato sin fecha no se sabe si está caducado. Un dato sin origen no se
   puede comprobar.
3. **Una sola fuente, con dueño.** Cada cosa vive en un documento; los demás lo enlazan en lugar de copiarlo.

### Qué no es

- No sustituye a los sistemas de la empresa: la contabilidad sigue en contabilidad y las contraseñas en el gestor de
  contraseñas.
- No es un sitio para datos personales sensibles ni para información que no deba salir de tu equipo: lo que le das a
  Claude se procesa en los servidores de Anthropic.

## 2. Antes de empezar

| Qué necesitas | Para qué |
|---|---|
| **Una cuenta de Claude** con acceso a Claude Code (plan Pro, Max, Team o Enterprise) | Es con lo que trabajas |
| **Windows, macOS o Linux** | Los ejemplos de esta guía son de Windows con PowerShell; en macOS y Linux se usa la terminal |
| **Una carpeta en tu equipo** | Donde vive la base. *Opcional:* dentro de una nube sincronizada (OneDrive, Google Drive, Dropbox…) para tener copia de seguridad e historial de versiones — ver el paso 4 |
| **Python 3** | Solo a partir del paso 7, para las utilidades que regeneran las vistas |

> **No hace falta Git**, ni saber programar. Claude Code escribe él mismo los scripts cuando llega el momento.

> **¿Ya tienes instalada la aplicación de escritorio de Claude?** Entonces **puedes saltarte casi todo el paso 3 y la
> parte de PowerShell del paso 4**: la aplicación trae Claude Code en su pestaña **Code**. Abres la aplicación, vas a
> **Code**, eliges la carpeta de tu base y empiezas a hablarle. **Lo único que sigue haciendo falta es Python**, y no
> hasta el paso 7. Y un detalle: las **tareas programadas** del paso 8 están en la aplicación de escritorio, así que te
> vendrá bien de todos modos.

## 3. Instalar Claude Code

> Si ya tienes la aplicación de escritorio de Claude, **sáltate este paso** salvo el apartado de Python, al final.

Abre **PowerShell con tu usuario**, sin «Ejecutar como administrador». Si lo instalas como administrador, se instala
en el perfil del administrador y tu usuario no lo encuentra.

```powershell
irm https://claude.ai/install.ps1 | iex
```

En macOS o Linux, desde la terminal:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Cierra PowerShell, ábrelo de nuevo y comprueba que responde:

```powershell
claude --version
```

### Si dice que no reconoce «claude»

El instalador lo deja en `%USERPROFILE%\.local\bin`. Si no está en el PATH, añádelo para tu usuario y vuelve a abrir
PowerShell:

```powershell
[Environment]::SetEnvironmentVariable("Path", [Environment]::GetEnvironmentVariable("Path","User") + ";$env:USERPROFILE\.local\bin", "User")
```

Si aún así no lo encuentra, **cierra la sesión de Windows y vuelve a entrar**: el Explorador guarda el PATH antiguo
hasta entonces.

### Python, para más adelante

Descárgalo de **python.org** y, en la primera pantalla del instalador, marca **«Add python.exe to PATH»**. Comprueba
con `python --version`.

## 4. Crear la carpeta y arrancar

1. Crea una **carpeta vacía**, por ejemplo `Conocimiento`.
2. *(Opcional)* Si la pones dentro de una nube sincronizada, márcala para que esté **siempre
   descargada en el equipo**: en el modo «a petición» los archivos son solo marcadores y Claude no
   puede leerlos. En OneDrive, por ejemplo, es clic derecho → «Conservar siempre en este dispositivo».
   Si no usas nube, haz copia de la carpeta de vez en cuando.
3. En PowerShell (o en la terminal), entra en la carpeta y arranca Claude Code:

```powershell
cd "C:\Users\tu.usuario\Documents\Conocimiento"
claude
```

La primera vez te preguntará si confías en la carpeta: di que sí. Ya puedes hablarle.

**Con la aplicación de escritorio**, los pasos 1 y 2 son iguales; en lugar del paso 3, abre la aplicación, ve a la
pestaña **Code** y elige la carpeta.

## 5. El prompt inicial

Es un único mensaje que crea la estructura entera: está en
[`prompts/02-inicial-claude-code.md`](prompts/02-inicial-claude-code.md). Antes de pegarlo, sustituye dos cosas:

- `[ORGANIZACIÓN]` → el nombre de tu empresa, equipo o proyecto.
- `[ÁREAS]` → las áreas que quieras, separadas por comas. Por ejemplo: `proveedores, sistemas, presupuestos, personas`.

Lo primero que hace es **enseñarte la [lista de casos de uso](casos-de-uso.md) y preguntarte cuáles son los tuyos**, y
monta solo esos. Y **adáptalo sin miedo**: si te falta un registro de reuniones o
de incidencias, añádelo. La estructura buena es la que refleja tu día a día.

### Qué crea

| Archivo o carpeta | Qué es |
|---|---|
| `CLAUDE.md` | **Las reglas que Claude lee al abrir cada sesión.** Es lo más importante: lo que no está aquí, se olvida |
| `CONVENCIONES.md` | Las reglas de formato: nombres de archivo, tipos de documento, fechas |
| `index.md` | El mapa de la base, y uno más en cada carpeta |
| `log.md` | Una línea por cambio, agrupadas por día |
| `_plantillas/` | Una plantilla por tipo de documento |
| `_documentos/` | Donde se archivan los originales: facturas, contratos y otros |
| `_data/` | Contratos y facturas también en JSON, para poder filtrarlos y sumarlos |
| Una carpeta por área | Cada una con su `index.md` |

> **Revisa el `CLAUDE.md` que genere.** Debe importar el índice y las convenciones con dos líneas `@index.md` y
> `@CONVENCIONES.md`, para que Claude las tenga siempre delante. Y si algún día le dices «a partir de ahora, haz siempre
> tal cosa», pídele que **lo escriba en el `CLAUDE.md`**: su memoria vive en tu equipo, el archivo viaja con la carpeta.

## 6. El día a día

Se trabaja hablando. Estas son las formas de aportar y de preguntar:

| Quieres… | Cómo |
|---|---|
| Aportar un dato | Cuéntaselo en una frase: «el soporte de X ahora lo lleva Fulano» |
| Aportar un correo o un texto | Pégalo tal cual y di de qué va |
| Aportar un documento | Escribe `@` y la ruta del archivo: `@"C:\Descargas\contrato.pdf"` |
| Aportar una captura | Pégala en el chat |
| Preguntar | «¿Qué vence en los próximos seis meses?», «¿quién lleva X?», «¿qué tengo pendiente de Y?» |
| Guardar una respuesta que te ha costado | «Archívalo» |
| Corregir algo | «Eso no es así: es tal cosa». Lo corrige donde esté |

### Cuatro hábitos que marcan la diferencia

- **Cuéntale lo que no pasa por el chat.** La base solo sabe lo que le llega. Cinco minutos al final de la semana con
  las reuniones y decisiones de pasillo valen más que cualquier otra cosa.
- **Pide que archive las respuestas buenas.** Una comparativa o un cruce que te ha costado una tarde se pierde si se
  queda en el chat.
- **Deja que te lleve la contraria.** Si Claude dice que un dato nuevo contradice uno guardado, no es un fallo: es la
  base funcionando. Decide cuál vale.
- **Mira el log de vez en cuando.** Es la forma rápida de saber qué ha cambiado.

## 7. Cuando crezca: las vistas y las utilidades

**Hazlo semanas después, no el primer día.** Una utilidad que resume algo necesita tener algo que resumir, y las
reglas que detectan descuadres se escriben contra descuadres reales: inventadas, o no avisan nunca o avisan de todo.

### Señales de que ya toca

- Para responder una pregunta fácil hay que abrir tres archivos.
- Repites la misma pregunta por tercera vez.
- Aparece el primer descuadre entre dos documentos.
- Llevas un mes, o 25-30 documentos.

### Qué añade

| Vista | Responde a… |
|---|---|
| `_catalogo.md` | «¿Qué documento habla de esto?» |
| `_pendientes.md` | «¿Qué tengo abierto?», con archivo y línea, y lo que tiene fecha arriba |
| `_calendario.md` | «¿Qué vence pronto?» |
| `_cruces.md` | «¿Qué no cuadra?»: lo que está en un documento y falta en otro |
| `_entidades.md` | «¿Dónde más sale este correo, este CIF o este dominio?» |

Las genera un script de Python que Claude escribe y ejecuta. **Nunca se editan a mano**: se corrige el documento de
origen y se regeneran. El prompt está en [`prompts/03-crecimiento.md`](prompts/03-crecimiento.md).

## 8. Que las reglas se cumplan solas

### Los hooks

Claude Code permite enganchar un script a momentos de la sesión. Con dos basta para que no se olvide lo que siempre se
olvida:

| Cuándo | Qué hace |
|---|---|
| **Al terminar cada respuesta** | Regenera las vistas si hace falta, avisa si hay cambios sin anotar en el log o sin entrada en la bitácora, y busca contraseñas coladas |
| **Antes de escribir un archivo** | Impide editar a mano las vistas generadas |

El prompt para que Claude los monte está en [`prompts/04-hooks-claude-code.md`](prompts/04-hooks-claude-code.md).
Quedan configurados en `.claude\settings.local.json`, dentro de la propia carpeta, con esta forma:

```json
{
  "hooks": {
    "Stop": [
      { "hooks": [ { "type": "command",
                     "command": "cd \"C:/ruta/a/tu/base\" && python _herramientas/cierre_sesion.py",
                     "timeout": 120 } ] }
    ],
    "PreToolUse": [
      { "matcher": "Write|Edit",
        "hooks": [ { "type": "command",
                     "command": "cd \"C:/ruta/a/tu/base\" && python _herramientas/proteger_vistas.py",
                     "timeout": 20 } ] }
    ]
  }
}
```

Se revisan escribiendo `/hooks` en Claude Code.

### Las tareas programadas

En la aplicación de escritorio de Claude se pueden programar tareas. La que más compensa es **regenerar las vistas
cada noche y avisar solo si hay algo nuevo**. Termina siempre la instrucción con «si no hay nada, no hagas nada»: si
no, acaba siendo ruido.

## 9. Si trabajas desde más de un equipo

Si la carpeta está en una nube sincronizada, viaja sola entre equipos, pero **la conversación no**: en el otro equipo no sabrás en qué paso se quedó cada
tema. Tampoco viajan la memoria de Claude ni las tareas programadas.

| No viaja | Qué hacer |
|---|---|
| Las conversaciones | Una **bitácora**: `bitacora.md`, una entrada por sesión con dónde se quedó cada tema |
| Lo que Claude ha aprendido de ti | Pasarlo al `CLAUDE.md`, que sí viaja |
| Las tareas programadas | Tenerlas **en un solo equipo**: si dos regeneran lo mismo, la sincronización crea copias en conflicto |

Y una regla: **nunca dos sesiones abiertas a la vez en dos equipos.** Si los dos escriben el mismo archivo casi a la
vez, el servicio de sincronización guarda uno y crea otro con el nombre del equipo pegado. El prompt de la bitácora está en
[`prompts/05-bitacora.md`](prompts/05-bitacora.md).

## 10. Seguridad y privacidad

- **Contraseñas, claves y tokens: nunca en la base.** Van al gestor de contraseñas. La base puede decir dónde están, no
  cuáles son.
- **Datos personales sensibles: no.** Ni salud, ni documentos de identidad de personas, ni cuentas bancarias, ni
  valoraciones de personas. Datos profesionales de contacto, sí.
- **Lo que pegas en Claude sale de tu equipo.** Si tu empresa tiene una norma de uso de la IA, respétala: hay
  información que no debe pegarse.
- **Lee lo que Claude pide ejecutar antes de aceptarlo.** Claude Code pide permiso para los comandos; no los apruebes a
  ciegas.
- **Si usas una nube con historial de versiones**, lo que se estropea se recupera. Pero por eso mismo, lo que no debe
  quedar en ningún sitio no debe escribirse nunca en la carpeta: aunque lo borres, queda en el historial.

> **Si necesitas guardar algo confidencial**, puedes pedir a Claude una carpeta `_privado/` con archivos cifrados con
> 7-Zip y una ficha visible que solo diga que existen. La contraseña la escribes tú en la terminal: **nunca se la des a
> Claude en el chat**.

## 11. Lo que aprendimos rompiéndolo

Fallos reales de una base como esta. Ninguno dio error: todos aparecieron al ir a mirar.

| Lo que pasó | Cómo se evita |
|---|---|
| Un aviso rojo de «vence en 3 días» era de algo que se renovaba solo, y se dejaron de mirar los avisos | Antes de marcar algo como urgente, comprobar si se renueva solo |
| «¿Qué vence en seis meses?» daba un resultado; había diez más en otro documento que no se citaba | Los documentos que responden a lo mismo se citan entre sí |
| Los originales en la carpeta de Descargas desaparecieron | Lo que importa, se archiva en `_documentos/` |
| Un problema revisado y descartado volvía a salir cada mes | Lo descartado se anota con su fecha |
| Análisis de una tarde que a los tres meses no estaban en ninguna parte | Lo que se responde en el chat y vale, se archiva |
| El resumen del mes salió ordenado por lo documentado, no por lo trabajado | Contarle a Claude lo que no pasa por el chat |
| El antivirus se llevó un CSV archivado | Las tablas se archivan en `.xlsx` o en Markdown |
| La lista de «lo que vence» estaba llena de fechas que no eran plazos | Distinguir la fecha de un dato de la fecha de un plazo |
| Apareció una copia en conflicto del log | Una sola sesión abierta cada vez |
| Las reglas delicadas vivían en la memoria de un solo equipo | Lo que no puede fallar, en el `CLAUDE.md` |
