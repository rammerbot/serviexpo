##### Español:
### Rammer Portfolio
<div align="center">
<img src="https://github.com/rammerbot/files/blob/main/Captura%20de%20pantalla%202024-05-26%20212126.png?raw=true" align="center" style="width: 100%" />
</div>  
  

### <div align="center">Rammer Portfolio</div>  
  #### Descripcion.
  
> Se trata de un portal personal informativo, con datos sobre proyectos realizados, certificaciones obtenidas, resumen curricular y otras informaciones adicionales. 

#### Características
- Registro de nuevos proyectos.
- Registro de nuevos certificados.
- Detalles de contactos.
- Panel administrativo.
- Cuenta de administrador.

#### Instalación

##### Crear entorno virtual:
```
python -m venv serviexpo
```

##### Entrar en el entorno
```
cd serviexpo
```
##### Activar el entorno dependiendo del sistema operativo
>  windows:
```
cd serviexpo/Script
```
```
activate
```
> en Lunix:
```
source serviexpo/bin/activate
```

##### Clonar el repositorio:

```
git clone https://github.com/rammerbot/serviexpo.git
```

> Navegar al directorio del proyecto:

```
cd serviexpo
```

##### Instalar las dependencias requeridas:

```
pip install -r requirements.txt
```

#### Uso
##### Crear base de dato y configurar la conexion
> luego ejecutar las migraciones
```
python manage.py makemigrations
```
```
python manage.py migrate
```

> Ejecutar la aplicación:

```
python manage.py runserver
```

##### Acceder al sistema a través de la URL proporcionada.

> Crear una cuenta de Administrador

```
python manage.py createsuperuser
```

##### Iniciar sesión con tu cuenta administrativa.
##### Usar la interfaz para cargar, evaluar y generar reportes y balances.

#### Contribuciones
##### Haz un fork del repositorio.

>Crea tu rama de funcionalidad:
  > Copiar código
```
git checkout -b feature/tu-funcionalidad
```
> Realiza tus cambios:

> Copiar código
```
git commit -m 'Agrega alguna funcionalidad'
```

> Sube tus cambios:

> Copiar código
```
git push origin feature/tu-funcionalidad
```
> Abre un pull request.
### Licencia
<p>Este proyecto está licenciado bajo la Licencia MIT. RammerBot</p>


### English:

## Rammer's Portfolio
<div align="center">
<img src="https://github.com/rammerbot/files/blob/main/Captura%20de%20pantalla%202024-05-26%20212126.png?raw=true" align="center" style="width: 100%" />
</div>  
<div align="center">Rammer's portfolio</div>

 ### Description
 
 > It's an informative personal portal with data about completed projects, obtained certifications, a curriculum summary, and other additional information.

#### Features

- Registration of new projects.
- Registration of new certificates.
- Contact details.
- Administrative panel.
- Administrator account.
  
#### Installation
#### Create a virtual environment:

```
python -m venv serviexpo
```

#### Enter the environment
```
cd serviexpo
```
#### Activate the environment depending on the operating system:

> Windows:

```
cd serviexpo/Scripts
```
```
activate
```
> Linux:
```
source serviexpo/bin/activate
```

Clone the repository:
```
git clone https://github.com/rammerbot/serviexpo.git
```

> Navigate to the project directory:

```
cd serviexpo
```

#### Install the required dependencies:
```
pip install -r requirements.txt
```

#### Usage
#### Create a database and configure the connection

> Then run the migrations
```
python manage.py makemigrations
```
```
python manage.py migrate
```

#### Run the application:

```
python manage.py runserver
```

#### Access the system through the provided URL.
 > Create an admin account:

```
python manage.py createsuperuser
```

#### Log in with your administrative account.
#### Use the interface to upload, evaluate, and generate reports and balances.
#### Contributions
> Fork the repository.
> Create your feature branch:

```
git checkout -b feature/your-feature
```

#### Commit your changes:

```
git commit -m 'Add some feature'
```

#### Push to the branch:
```
git push origin feature/your-feature
```

#### Open a pull request.

#### License
<p>This project is licensed under the MIT License. RammerBot</p>
