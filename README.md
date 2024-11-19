# API Sistema De Empleados (JAVA)

API "backend" en python para el proyecto [Sistema de empleados](https://google.com)

## Dependencias
- Flask (3.1.0)
- SQLAlchemy (3.1.1)
- Pymysql (3.1.0)

## Instalacion
1. Crear e iniciar un entorno virtual de python
2. instalar las dependencias

## Iniciar la API
1. Inicia XAMPP
2. Configura una base de datos con el nombre de `SistemaDeEmpleados`
3. Configura `config.py` para que se conecte con la base de datos de XAMPP
4. Inicia la API desde la consola con:

```bash
  python app.py
```
al arrancar saldrá un mensaje tal que así
```bash
  * Serving Flask app 'app'
  * Debug mode: on

  WARNING: This is a development server.
  Do notuse it in a production deployment.
  Use a production WSGI server instead.
  
  * Running on [URL]
  Press CTRL+C to quit
  
  * Restarting with stat
  * Debugger is active!
  * Debugger PIN: [PIN]

```

## Uso de la API

> [!NOTE]  
> Una vez iniciada la API se puede acceder a la info de la base de datos con la siguiente url
> `[URL]/api/users`

### 

> [!IMPORTANT]  
> la API trabaja a base de JsonArray

---

### Metodo GET
Para usar este metodo se usan las siguientes rutas:

#### api/users/
Retorna un JSON con todos los usuarios en la tabla users

#### /api/users/[id]
Recibe un id numerico.
Retorna un JSON con el usuario, en caso contrario retorna JSON con un mensaje de error

#### /api/users/[email]-[password]
Recibe dos string uno para el email y otro para el password.
Retorna un JSON con el usuario, en caso contrario retorna un JSON con un mensaje de error


### Metodo POST
> [!WARNING]  
> Pendiente de implementación, no usar

### Metodo PATCH
> [!WARNING]  
> Pendiente de implementación, no usar

### Metodo DELETE
> [!WARNING]  
> Pendiente de implementación, no usar