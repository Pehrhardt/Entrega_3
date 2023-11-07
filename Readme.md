La página posee 5 secciones: Buscador, Clientes, Fondos de inversion, Bonos y Acciones
1. En primer lugar se deben agregar Clientes en el formulario dentro de la página /Clientes
2. En segundo lugar se deben agregar Fondos de inversión en el formulario dentro de la página /Fondos_inversion
3. En tercer lugar se deben agregar bonos dentro de la página /bonos
4. En cuarto lugar se deben agregar acciones dentro de la página /acciones
5. En último lugar en la página principal (buscador) podemos buscar si se encuentra un fondo disponible dentro de la página

Las funcionalidades se encuentran en:

app1/urls.py nos redirecciona a las distintas páginas html de la carpeta templates/app1 que son las vistas

app1/models.py aqui crearemos las clases que utilizaremos para luego crear nuestra base de datos y crear funciones de .views a partir de ellas con sus distintos atributos, por ejemplo Clientes con nombre, apellido y email que luego serán llamadas a los archivos admin.py y views.py

app1/views.py en este lugar encontraremos las funciones que devolverán las vistas de las páginas al servidor como también el ingreso a través de inputs a la BD
de los distintos modelos creados previamente. dentro de estos se encuentran los clientes, fondos de inversion, bonos y acciones. Por último se encuentra la función
que realiza la busqueda dentro de la base de datos para devolver el resultado que se encuentra en la base de datos y sus caracteristicas (el nombre del fondo y la cantidad de activos del mismo.

app1/admin.py en esta sección le ingresamos las clases a la consola de administración para que pueda modificar datos dentro de la BD.

Por último se toma el index.html donde se encuentra el bloque raiz de la página y luego se crean herencia para las otras 4 creando bloques por cada sección y agregando los distintos formularios para las distintas clases que luego serán almacenadas en la base de datos.


