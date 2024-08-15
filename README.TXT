Rental Ski

Realizado por: Pedro Méndez

Descripción

Entre estos está Carlos Araya, que ha decidido abrir un rental de ski en la subida del volcán Villarrica. Para esto, don Carlos desea implementar un sitio web donde sus clientes puedan reservar skis y, tras la devolución del equipo, se puedan anotar observaciones sobre su estado. Este proyecto tiene como objetivo crear una DEMO de la plataforma para convencer a don Carlos de contratar tus servicios como desarrollador(a) de software, utilizando el stack Python/Django y el framework CSS Bootstrap. La meta es desarrollar una aplicación web escalable y robusta con tiempos de implementación eficientes.

Instalación y Configuración

Clonar el Repositorio

git clone <URL del repositorio>
cd <directorio del repositorio>

Instalar Dependencias

pip install -r requirements.txt

Creación de Datos (BD Legacy) "rental_ski.sql"

1. Crear base de datos.
2. Crear tablas.
3. Poblar tablas con datos.

Cargar Base de Datos

python manage.py inspectdb > models.py

Luego, reemplaza este models.py con el de la carpeta en app.

python manage.py migrate

Iniciar el Servidor

python manage.py runserver

Acceder a la Aplicación

Visita http://localhost:8000 en tu navegador.

Puntos a Considerar

- Por defecto, los usuarios creados son clientes y los equipos están disponibles.
- La página inicial requiere iniciar sesión antes de registrar un usuario.
- Al crear un usuario, se debe iniciar sesión automáticamente.
- El código de identificación única de los equipos será el ID por defecto de la tabla.

- El superadmin del sistema (usando Django-Admin) debe ser capaz de agregar nuevos equipos y categorías. Esto se realiza directamente desde las vistas del admin.
- Si se realiza un arriendo, se puede devolver inmediatamente o ir a la vista /mis_arriendos para devolver los equipos.
- Si un operario agrega una observación a un arriendo, el usuario de ese arriendo recibe una penalización. Esto hace que el campo restringido sea verdadero, lo que impide que arrende nada durante un mes o hasta que el administrador quite la restricción.

Usuarios de la Aplicación Ya Instalados en la Base de Datos

- Super usuario: admin | Contraseña: admin
- Usuario cliente: correo@gmail.com | Contraseña: hola1234
- Usuario operario: correo2@gmail.com | Contraseña: hola1234
