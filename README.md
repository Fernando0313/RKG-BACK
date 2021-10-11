# PROYECTO BACKEND RKG  ![logo-nuevo](https://user-images.githubusercontent.com/74431425/136596976-bf36329d-7766-4c2c-a150-7379fbe18bfc.png)
## E-commerce de mascotas - Tienda de mascotas y apartado de adopciones
AUTORES 💻 :

>  _Kevin More_ 😎

>  _Renzo Estrada_ 😎
 
>  _Guillermo Mujica_ 😎
- hola

### Idea del proyecto 😼:
La idea principal es tener un ecommerce enfocado a las
mascotas, respecto a las ideas secundarias estarían enfocadas a un apartado de adopciones y donaciones a centro de rescate de mascotas

#### Soluciones:
> Agilizar el proceso de compras
> Difundir la concientización de adopción de animales
> Incentivar a las personas a apoyar en los refugios de animales

#### Tecnologías:
>Base de datos: postgres
>
>Frameworks : Django
>
>Editor de código: VisualCode
>
>Lector de base de datos : DataGrip
>
>Repositorio : GitHub
>
>Tester: Postman
>
>Diagramador del MER: MySQL WorkBench
>
>Canal de comunicación: Discord, Whatsapp, llamadas telefónicas
>
# Instrucciones

1. Para navegar en el proyecto descargarte el repositorio mediante el siguiente comando:

```
git clone https://github.com/kevinmore26/RKG-BACK
```

2. Una vez que haya descargado, ahora, tendrás que ingresar a la carpeta `RKG-BACK\` y  entrar a la rama `main` (estará por defecto)

3. Instalamos los requirements.txt para el correcto funcionamiento
```
pip install -r requirements.txt
```

4. Procede con el siguiente comando para crear las migraciones
```
python manage.py gestion --name <nombre_tabla>
```

>  No es necesario entrar a una carpeta para encontrar el manage.py ya que se encuentra afuera para una mejor organización por tema de tener varias apps (facturacion,gestion...)

5. Creamos una DATABASE con el siguiente nombre: `django_rkg_revenge\`

6. Seguido del siguiente comando para ejecutar las migraciones
```
python manage.py migrate gestion
```
7.Ejecutamos el servidor 
```
python manage.py runserver
```


