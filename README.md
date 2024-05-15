## Dockerfile

#### Un Dockerfile es un archivo que contiene una serie de instrucciones que se utilizan para construir una imagen de Docker. Docker es una plataforma que permite desarrollar, enviar y ejecutar aplicaciones dentro de contenedores. Un Dockerfile especifica cómo se debe construir una imagen de Docker, incluyendo qué base de imagen usar, cómo instalar dependencias, qué archivos copiar, qué comandos ejecutar y más.

#### A continuación, te explico algunas de las instrucciones comunes que puedes encontrar en un Dockerfile:

	FROM: Define la imagen base desde la que se va a construir la nueva imagen. Por ejemplo, FROM ubuntu:20.04 utiliza Ubuntu versión 20.04 como imagen base.

	RUN: Ejecuta un comando durante el proceso de construcción de la imagen. Por ejemplo, RUN apt-get update && apt-get install -y python3 actualiza los paquetes del sistema e instala Python 3.

	COPY: Copia archivos o directorios desde tu sistema local hacia el sistema de archivos de la imagen de Docker. Por ejemplo, COPY app.py /app/ copia un archivo app.py desde el directorio local actual al directorio /app/ en la imagen.

	ADD: Similar a COPY, pero con capacidades adicionales, como extraer archivos comprimidos durante la copia.

	CMD: Especifica el comando que se ejecutará cuando se inicie un contenedor basado en la imagen. Por ejemplo, CMD ["python3", "/app/app.py"] ejecuta un script de Python.

	EXPOSE: Informa a Docker qué puertos necesita exponer la imagen. Por ejemplo, EXPOSE 8080 indica que la imagen necesita exponer el puerto 8080.

	ENV: Establece variables de entorno dentro de la imagen. Por ejemplo, ENV MY_VAR=my_value establece la variable de entorno MY_VAR con el valor my_value.

	ENTRYPOINT: Similar a CMD, pero se utiliza para definir un comando principal y argumentos que no pueden ser reemplazados por el usuario cuando se inicia el contenedor.

	VOLUME: Define puntos de montaje de volúmenes persistentes dentro de la imagen. Por ejemplo, VOLUME /data define un volumen persistente en el directorio /data.

	USER: Cambia el usuario bajo el cual se ejecutan los comandos y aplicaciones en la imagen. Por ejemplo, USER appuser cambia al usuario appuser.

	WORKDIR: Establece el directorio de trabajo para los comandos ejecutados en las siguientes instrucciones. Por ejemplo, WORKDIR /app cambia el directorio de trabajo a /app.

#### Un Dockerfile te permite definir cómo debe configurarse y ejecutarse tu aplicación dentro de un contenedor Docker de una manera reproducible y portátil. Al construir una imagen a partir de un Dockerfile, obtienes un contenedor que puedes ejecutar en cualquier lugar donde Docker esté disponible.

## Dockerfile del Proyecto
### Parte 1: Entorno de construcción
	FROM node:slim as build: Especifica una imagen base, en este caso, node:slim, que es una versión ligera de la imagen de Node.js. Además, la sección as build nombra esta etapa del Dockerfile como build.

	WORKDIR /app: Establece el directorio de trabajo a /app donde se ejecutarán las siguientes instrucciones.
	
	ENV PATH /app/node_modules/.bin:$PATH: Establece la variable de entorno PATH para incluir el directorio node_modules/.bin, permitiendo ejecutar scripts de Node.js con facilidad.
	
	COPY package.json . y COPY package-lock.json .: Copian los archivos package.json y package-lock.json desde el sistema local al directorio /app en la imagen.

	RUN npm ci --silent: Ejecuta el comando npm ci para instalar las dependencias especificadas en package-lock.json de manera silenciosa (sin mucha salida en la consola).
	
	RUN npm install react-scripts@latest -g --silent: Instala react-scripts globalmente a la última versión de manera silenciosa.

	COPY . .: Copia todos los archivos del directorio actual en el sistema local al directorio de trabajo en la imagen.
	
	RUN npm run build: Ejecuta el script build definido en package.json para compilar la aplicación React.

## Parte 2: Entorno de producción
	
	FROM nginx:stable-alpine: Utiliza una imagen base de Nginx, una variante ligera (alpine) de la versión estable de Nginx.

	COPY --from=build /app/build /usr/share/nginx/html: Copia los archivos compilados de la etapa de construcción (build) desde el directorio /app/build en la imagen de construcción a /usr/share/nginx/html en la imagen de producción.

	COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf: Copia el archivo de configuración personalizado de Nginx desde el sistema local a la ubicación predeterminada de Nginx (/etc/nginx/conf.d/default.conf) dentro de la imagen.

	EXPOSE 3000: Informa a Docker que la aplicación expone el puerto 3000.

	CMD ["nginx", "-g", "daemon off;"]: Especifica que el comando para ejecutar en la imagen es iniciar Nginx en primer plano (daemon off; significa que Nginx se ejecuta en primer plano en lugar de en segundo plano).

## NginX

#### Es un servidor web de alto rendimiento y una solución de servidor de proxy inverso que se utiliza para manejar cargas de trabajo pesadas, balancear la carga, actuar como servidor de caché, y mucho más. Fue desarrollado por Igor Sysoev en 2002 y se ha convertido en uno de los servidores web más populares y ampliamente utilizados en la actualidad.

#### A continuación se describen algunas de las características clave de Nginx:

	Servidor web: Nginx puede servir páginas web estáticas y dinámicas de manera eficiente. Es conocido por su capacidad de manejar grandes cantidades de conexiones simultáneas y ofrecer un rendimiento alto y estable.

	Proxy inverso: Nginx puede actuar como un proxy inverso para aplicaciones web, gestionando solicitudes de clientes y dirigiéndolas a servidores de backend específicos. Esto ayuda a equilibrar la carga entre múltiples servidores de backend, mejorando el rendimiento y la escalabilidad de la aplicación.

	Balanceo de carga: Nginx puede distribuir las solicitudes entrantes entre varios servidores de backend para equilibrar la carga de trabajo y optimizar el rendimiento.

	Caché: Nginx ofrece capacidades de caché para acelerar la entrega de contenido al almacenar versiones en caché de recursos estáticos y dinámicos.

	Servidor de correo: Nginx también se puede utilizar como servidor de correo IMAP/POP3.

	Seguridad: Nginx puede actuar como un firewall de aplicaciones web (WAF), proporcionando protección contra ataques comunes, como ataques de denegación de servicio (DDoS) y otras vulnerabilidades.

	Configurabilidad: La configuración de Nginx es flexible y se basa en un sistema de archivos de texto que permite a los administradores ajustar y personalizar fácilmente el comportamiento del servidor según sus necesidades.

#### Nginx es una opción popular tanto para sitios web grandes como pequeños debido a su eficiencia, flexibilidad y capacidad para manejar cargas de trabajo exigentes. Además, es conocido por su diseño modular, que permite agregar funcionalidades adicionales a través de módulos de terceros o de la propia comunidad de desarrollo.

## Dockerfile Fast-API

    Utiliza python:3.9-slim como la imagen base, que es una versión ligera de Python 3.9.

    Establece el directorio de trabajo en /app.

    Copia los archivos requirements.txt y main.py desde el sistema local al directorio de trabajo en la imagen.

    Instala las dependencias del archivo requirements.txt usando pip.

    Expone el puerto 8000 que la aplicación FastAPI usará para responder a las solicitudes HTTP.
    
    Especifica el comando para iniciar el servidor Uvicorn con tu aplicación FastAPI.

## YAML or YML

	AML (Yet Another Markup Language) y YML (YAML Ain’t Markup Language) son dos acrónimos que se refieren al mismo lenguaje de serialización de datos. YAML es un formato de archivo que se utiliza para almacenar y transmitir datos de manera legible para los humanos.

	YAML se utiliza comúnmente en el diseño de archivos de configuración, ya que es fácil de leer y escribir, y se puede utilizar para serializar datos en un formato de texto plano. Aunque YAML se inspira en lenguajes como XML, no es un lenguaje de marcado en el sentido tradicional, sino que se enfoca en la serialización de datos en lugar de la presentación de documentos.

	En resumen, YAML es un lenguaje de serialización de datos que se utiliza para almacenar y transmitir datos de manera legible y fácil de leer, y se utiliza comúnmente en el diseño de archivos de configuración.
