# Balmes92


## Propósito
Aquí se guardan todos los desarrollos en Odoo12 de Balmes92 y sus clientes.

## Servidores
Balmes tiene hasta el momento 2 servidores que son usados por los desarrolladores. A continuación se detalla.

### Balmes servidor oficial

Este es el servidor oficial de Balmes, por aquí se procesan las solicitudes de los clientes y la empresa hace sus 
operaciones. El acceso es personal de cada usuario.

- URL: https://odoo12.balmes92.com/web
- DB: balmes12_master

### Balmes servidores de pruebas
Cada cliente tiene su propio servidor de pruebas, el cual es un subdominio de `b92d.com`. Los detalles, tales como 
nombre de la DB, credenciales para la autenticación, etc., son dados por el analista.

## Estructura de carpetas usadas en los servidores

Cada servidor montado por Balmes tiene la siguiente estructura de carpetas:
```text
./proyecto_nombre/
├── bin <----- Aquí están varios scripts para automatizar el mantenimiento de Odoo y del servidor
│   
├── filestore <----- Aquí van archivos los estáticos de Odoo.
│
├── local
│       ├── addons <----- Aquí está el código de los módulos desarrollados por Balmes92
│       │
│       └── docs <----- Aquí está la documentación
│
├── logs <----- Aquí están los logs de Odoo, se usan para depurar cualquier problema
├── odoo12.cfg <----- Este es el archivo de configuración de Odoo
├── requirements.txt  <----- Librerias requeridas por los modulos desarrollados por Balmes92
├── src
│       ├── OCA  <----- Aquí se clonan los repositorios de la OCA, para tenerlos en un solo lugar y facilitar su mantenimiento
│       └── odoo <----- Aquí va el código fuente de Odoo Enterprise
└── venv <----- Aquí se pone el entorno virtual de python, lo cual separa las librerías necesarias para Odoo de las del sistema.
```