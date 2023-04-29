
![Logo](https://raw.githubusercontent.com/PabloSki19/bloc-notas/main/assets/logo-bloc-de-notas.png)


# Bloc de notas

Es una aplicación que sirve para ver y editar archivos de texto de la extensión txt.

## Screenshots

![Ventana principal](https://raw.githubusercontent.com/PabloSki19/bloc-notas/main/assets/ventana-principal.png)

![Color de fondo y color de texto](https://github.com/PabloSki19/bloc-notas/blob/main/assets/ventana-color.png)

![Buscar / Reemplazar](https://raw.githubusercontent.com/PabloSki19/bloc-notas/main/assets/ventana-buscar.png)


## Características

- Buscar y reemplazar palabras
- Cortar, copiar, pegar y eliminar texto
- Deshacer acciones hasta la primera acción y rehacer hasta la última
- Cambiar tipo, tamaño, estilo y color de la fuente
- Cambiar el color de fondo del texto
- Menú contextual para el botón derecho del mouse


## Instalación

IMPORTANTE: Tener instalado Python en su equipo (se recomenda la versión 3.11.2 en Windows) para su correcta ejecución.

Hacer clic en el botón fork del repositorio con su cuenta de GitHub o descargarlo directamente de allí.


## Ejecución

Para ejecutarlo, usar el siguente comando en una terminal:

```bash
  python main.py
```

IMPORTANTE: Para una correcta ejecución, el archivo main.py tiene que estar en una misma carpeta con las carpetas data y icons.


## Preguntas frecuentes

#### ¿Cómo se cambia el tamaño, tipo y estilo de fuente?

Si se modifica el tamaño, tipo y estilo de la fuente, cambiará la apariencia de todo el texto del archivo, no solo de una parte.
1. Abrir el Bloc de notas.
2. Ir a la barra de herramientas.
3. Seleccione un tipo de fuente, un estilo de fuente y un tamaño; y se cambiará automáticamente.

#### ¿Cómo se cambia el color de fondo o el color de texto?

Para cambiar el color de fondo:
1. Abrir el Bloc de notas.
2. Haga clic en el menú Ver y, luego, en Color de fondo; o en el icono de la barra de herramientas correspondiente,
3. Seleccione un color, y después haga clic en Aceptar.

Para cambiar el color de texto:
1. Abrir el Bloc de notas.
2. Ir a la barra de herramientas, en el icono correspondiente.
3. Seleccione un color, y después haga clic en Aceptar.

#### ¿Cómo se corta, copia, pega o elimina texto?

1. Abrir el Bloc de notas.
2. Realice una de las acciones siguientes:

• Para mover texto de un lugar a otro, selecciónelo, pulse o haga clic en el menú Editar y después pulse o haga clic en Cortar.

• Para tener el mismo texto en dos lugares diferentes, selecciónelo, pulse o haga clic en el menú Editar y después pulse o haga clic en Copiar.

• Para pegar texto que ha cortado o copiado, pulse o haga clic en el lugar del archivo donde desee pegar el texto, pulse o haga clic en el menú Editar y después pulse o haga clic en Pegar.

• Para eliminar texto, selecciónelo, pulse o haga clic en el menú Editar y después pulse o haga clic en Eliminar. 

• Para deshacer la última acción, pulse o haga clic en el menú Editar y después pulse o haga clic en Deshacer.

• Para rehacer la acción, pulse o haga clic en el menú Editar y después pulse o haga clic en Rehacer.

También, se pueden realizar las acciones mencionadas anteriormente con los iconos de la barra de herramientas, según correspondan.

#### ¿Cómo se buscan y reemplazan caracteres o palabras específicos?

Para buscar palabras o caracteres específicos:
1. Abrir el Bloc de notas.
2. Haga clic en el menú Editar y, luego, en Buscar / Reemplazar; o en el icono de la barra de herramientas correspondiente.
3. En el cuadro Buscar, escriba los caracteres o las palabras que desee buscar.
4. Haga clic en Buscar.

Para reemplazar palabras o caracteres específicos:
1. Abrir el Bloc de notas.
2. Haga clic en el menú Editar y, luego, en Buscar / Reemplazar; o en el icono de la barra de herramientas correspondiente.
3. En el cuadro Buscar, escriba los caracteres o las palabras que desee buscar.
4. En el cuadro Reemplazar, escriba el texto de reemplazo.
5. Haga clic en Buscar y, a continuación, en Reemplazar.

#### ¿Se va a grabar las modificaciones de la fuente y/o color en mi archivo .txt?

No, cualquier modificación de la fuente (tipo, estilo o tamaño) o del color (de fondo o del texto) es sólo de muestra y va a ser mientras que corra el programa, no se va a grabar en el archivo txt.


## Bugs conocidos

1. Los usuarios de MacOS no pueden dar con el botón derecho del mouse en el texto para que aparezca el menú contextual. La solución es modificar Button-3 por Button-2 en la línea 536 de main.py para que quede de la siguiente manera:

```bash
  root.bind("<Button-2>", hacer_contextual_texto)
```

2. Cualquier modificación de la fuente (tipo, estilo o tamaño) o del color (de fondo o del texto) es sólo de muestra y va a ser mientras que corra el programa, no se va a grabar en el archivo txt. No se va a poder encontrar una solución.


## Autor

- Pablo Aguilar (GitHub: [@PabloSki19](https://github.com/PabloSki19))


## Un especial agradecimiento al:

 - [Equipo de CódigoFacilito](https://codigofacilito.com/)


## Feedback

Si tiene algún feedback, comuníquese al siguiente correo electrónico: pabloaguiarri19@gmail.com


## Soporte

Para soporte, el correo electrónico es: pabloaguiarri19@gmail.com.

