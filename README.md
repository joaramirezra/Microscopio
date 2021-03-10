# Sistema de conteo de minerales para microscopio 

El siguiente repositorio cuenta con la informacion necesaria para ejecutar un sistema de conteo de minerales de manera semi-automatica haciendo uso de un microscopio, para ello es necesario poseer los siguientes componentes :

 - Computador con Linux,Windows o mac (Soporte unicamente para los dos primeros )
 - Carro de conteo automatico de puntos (Opcional ,Mas informacion proximente)
 - Dispositivo de comunicacion entre el carro de conteo y el PC (opcional)

El sistema de funcionamiento cuenta con una interfaz de usuario como se muestra a continuacion 
<p align="center">
 <img src="https://raw.githubusercontent.com/joaramirezra/Microscopio/master/Imagenes/Readme/interfazV1.png" width="400" height="255">
</p>

En ella podemos observar 5 secciones :

 1. Interfaz de conexion con dispositivo fisico
 2. Interfaz para agregar nuevas conbinaciones mineral y conjunto de letras
 3. Interfaz para agregar/borrar minerales al conteo.
 4. Resumen de minerales recientemente agregados
 5. Graficas del total de elementos agregados
 
Esta secciones permiten al usuario interactuar con el dispositivo fisico (si se posee) de tal manera que a medida que se van agregando minerales al conteo, estos de manera automatica se actualizan en la interfaz de usuario a medida que la seccion delgada se mueve de manera automatica 

<p align="center">
<img src="https://raw.githubusercontent.com/joaramirezra/Microscopio/master/Imagenes/Readme/Untitled%20drawing.png" width="400" height="255" >
</p>

## Instalación 

El proceso de instalaccion consiste en la correcta instalacion de las siguientes dependencias 
 - [python 3.6 o superior](https://www.python.org/downloads/)
    - [pyQT5](https://pypi.org/project/PyQt5/)
    - [pySerial](https://pyserial.readthedocs.io/en/latest/pyserial.html#installation)
  
Ademas de la  instalacion de las dependencias se recomienda utilizar un programa para detectar los puertos este puede ser :
- [Arduino](https://www.arduino.cc/en/software)
- [PuTTY](https://www.putty.org/)
- ó cualquiera a elección 

### checkeo requetimientos ( integridad instalacion )

Una vez instaladas las dependencias, entrar al directorio :

```
./pruebas/instalacion/
```

Alli encontrara el scrip llamado `test.py` , al ejecutarse debera obtener una respuesta como la siguiente : 

``` 
Dependencias correctamente instaladas
```

## Puesta en marcha (omitir este paso si no se posee el carro de secciones delgadas)

Para la correcta deteccion del puerto se recomienda seguir con los siguientes paso :
 1. Conexion previa : la conexion se debe realizar como se muestra en el siguiente diagrama
 
 <p align="center">
 <img src="https://raw.githubusercontent.com/joaramirezra/Microscopio/master/Imagenes/Readme/Conexion.png" width="400" height="255">
</p>

 
  alli se debe conectar el dispositivo a una fuente de voltaje de 120 Vac (toma corriente en Colombia), en ese instante debe encender una luz led como se muestra en la siguiente Imagen 
 
 ![imagen1]()

  Una vez conectado la alimentacion del dispositivo, se debe conectar un cable USB entre el computador y el dispositivo, este a su vez encendera una segunda luz en el dispositvo como se muestra en la siguiente imagen:

 ![imagen1]()
 
 2. Deteccion de puerto 
 
 Posterior a la conexion del dispositvo se debe identificar el puerto de conexion para sincronizar el dispositivo con el programa para ello acudimos al programa arduino, (o cualquiera de su preferencia) , alli presionamos
 
``` 
Herramientas/puertos
```
 Debera aparecer el nombre del puerto que se relaciona al dispositvo fisico que conectamos en el paso anterior como se muestra en la siguiente imagen (el nombre del puerto puede variar)
 
 ![imagen1](https://raw.githubusercontent.com/joaramirezra/Microscopio/master/Imagenes/Readme/seleccionar-puerto-arduino-uno.png)
 
  - Nota 1 : En caso de usar linux se recomienda dar permisos de escritura y lectura al puerto mediante el comando `sudo chmod /dev/Nombre_del_puerto` 
  - Nota 2 : En caso de desconectar y reconectar el dispositivo asegurese que el nombre del puerto sea el mismo , en caso contrario se debe dar permisos a este nuevo puerto
  - Nota 3 : En caso de desconectar y reconectar el dispositivo asegurese que el nombre del puerto sea el mismo , en caso contrario actualizar el nombre en la interfaz grafica 
 
 3. Sincronizacion del dispositivo 
 
 Una vez se tiene el identificado el nombre del puerto y el dispositvo este correctamente conectado, se debe introducir el nombre del puerto en la casilla nombre y presionar sincronizar, esto debera 
  
7. Bibliografia 


## Agregar Nuevo combinacion mineral 

Una vez se ha sincronizado el carro con el programa es momento de iniciar a agregar los elementos a la lista de minerales que van a estar disponibles, para ello se se posee la siguientes restricciones

Es Sensible a combinaciones entre mayusculas y minisculas
longitud maxima  3 Letras
No soporta caracteres especiales ni numeros (estos ultimos estan reservados para hacer referencia a los tamaños)




### (Previo) Deteccion de puertos 
  
  

## something else 


# Colaboladores 

- [Johan Ramirez](https://github.com/joaramirezra)
- [Jurgen Krajcy](https://github.com/JurgenHK)
- Thomas Crammer
