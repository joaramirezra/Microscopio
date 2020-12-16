# Sistema de conteo de minerales para microscopio 

El siguiente repositorio cuenta con la informacion necesaria para ejecutar un sistema de conteo de minerales de manera semi-automatica haciendo uso de un microscopio, para ello es necesario poseer los siguientes componentes :

 - Computador con Linux,Windows o mac (Soporte unicamente para los dos primeros )
 - Carro de conteo automatico de puntos (Opcional ,Mas informacion proximente)
 - Dispositivo de comunicacion entre el carro de conteo y el PC (opcional)

El sistema de funcionamiento cuenta con una interfaz de usuario como se muestra a continuacion 

<center><img src="https://raw.githubusercontent.com/joaramirezra/Microscopio/master/Imagenes/Readme/interfazV1.png" width="400" height="255">
</center>

En ella podemos observar 5 secciones :

 1. Interfaz de conexion con dispositivo fisico
 2. Interfaz para agregar nuevas conbinaciones mineral y conjunto de letras
 3. Interfaz para agregar/borrar minerales al conteo.
 4. Resumen de minerales recientemente agregados
 5. Graficas del total de elementos agregados
 
Esta secciones permiten al usuario interactuar con el dispositivo fisico (si se posee) de tal manera que a medida que se van agregando minerales al conteo, estos de manera automatica se actualizan en la interfaz de usuario

<center><img src="https://raw.githubusercontent.com/joaramirezra/Microscopio/master/Imagenes/Readme/Untitled%20drawing.png" width="400" height="255">



## Instalación 

El proceso de instalaccion consiste en la correcta instalacion de las siguientes dependencias 
 - [python 3.6 o superior](https://www.python.org/downloads/)
    - [pyQT5](https://pypi.org/project/PyQt5/)
    - [pySerial](https://pyserial.readthedocs.io/en/latest/pyserial.html#installation)
  
Ademas de la correcta instalacion de las dependencias se recomienda utilizar un programa para detectar los puertos este puede ser 
- [Arduino](https://www.arduino.cc/en/software)
- [PuTTY](https://www.putty.org/)
- ó cualquiera a elección 

## Chequeo de la integridad de la instalacion 

### (Previo) Deteccion de puertos 
  
  
# Colaboladores 

- [Johan Ramirez](https://github.com/joaramirezra)
- [Jurgen Krajcy](https://github.com/JurgenHK)
- Thomas Crammer
