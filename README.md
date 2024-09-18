### Estructura de la aplicación
La aplicación está diseñada utilizando el **Patrón de Arquitectura Hexagonal** o **Arquitectura de Puertos y Adaptadores**. Este enfoque permite aislar la lógica de negocio del sistema de los detalles de implementación externos como bases de datos, servicios externos, o interfaces de usuario. 

### Componentes principales
La aplicación se organiza en varios módulos:

1. **Chat**:
   - Se encuentra bajo el directorio `app/chat`. Aquí se maneja la lógica de negocio relacionada con el sistema de chat. Está dividido en:
     - **Adapters**: Interactúan con el mundo externo.
     - **Application**: Contiene la lógica de aplicación y los casos de uso.
     - **Domain**: Modelos y lógica de negocio pura.
     - **Infrastructure**: Implementaciones técnicas como la persistencia de datos.

2. **Messaging**:
   - Ubicado en `app/messaging`, maneja la mensajería mediante servicios como **RabbitMQ** para enviar y recibir mensajes entre los diferentes componentes.

3. **Multimedia**:
   - Directorio `app/multimedia`, gestiona la subida y el manejo de archivos multimedia en la aplicación.

4. **Users**:
   - `app/users` contiene todo lo relacionado con la gestión de usuarios, incluyendo autenticación, registros y perfiles de usuario.

5. **Pruebas**:
   - `app/tests` incluye pruebas para cada uno de los módulos, asegurando el correcto funcionamiento de los componentes.

### Tecnologías Utilizadas
- **FastAPI**: Framework utilizado para construir la API web.
- **SQLAlchemy**: ORM utilizado para interactuar con bases de datos relacionales como PostgreSQL.
- **MongoDB**: Base de datos NoSQL para almacenar información que no requiere estructuras rígidas.
- **RabbitMQ**: Servicio de mensajería para la comunicación entre los diferentes servicios de la app.
- **Docker**: La app está contenida y orquestada mediante **Docker** y **docker-compose**, lo que facilita la ejecución en múltiples entornos.
  
### Posible contenido para el README en español

---

# Aplicación de Chat con Arquitectura Hexagonal

## Descripción

Esta aplicación implementa un sistema de chat utilizando el **Patrón de Arquitectura Hexagonal**, lo que permite separar la lógica de negocio de los detalles de implementación. Está desarrollada con **FastAPI** y utiliza **SQLAlchemy** para la gestión de bases de datos relacionales como **PostgreSQL**. Además, se integra con **RabbitMQ** para la mensajería entre servicios y **MongoDB** para almacenar datos no relacionales.

## Estructura del Proyecto

El código se organiza en módulos independientes para cada componente de la aplicación:
- **app/chat**: Contiene toda la lógica del sistema de chat.
- **app/messaging**: Maneja el sistema de mensajería y colas de trabajo usando RabbitMQ.
- **app/multimedia**: Gestión de archivos multimedia subidos por los usuarios.
- **app/users**: Administración de usuarios, incluyendo registro, login y autenticación.

Cada módulo sigue una estructura similar:
- **adapters**: Interfaces que conectan con el mundo exterior (API, bases de datos, etc.).
- **application**: Casos de uso que conectan la lógica de negocio con los adaptadores.
- **domain**: Lógica pura de negocio y entidades del sistema.
- **infrastructure**: Implementaciones técnicas como la persistencia de datos y conexiones a servicios externos.

## Tecnologías

- **FastAPI**: Framework web para la creación de APIs rápidas y eficientes.
- **SQLAlchemy**: ORM para la interacción con bases de datos SQL.
- **PostgreSQL**: Base de datos relacional para la persistencia de datos.
- **MongoDB**: Base de datos NoSQL.
- **RabbitMQ**: Sistema de mensajería para la comunicación entre servicios.
- **Docker**: Contenedores para la ejecución de la aplicación en entornos controlados.

## Instalación y Ejecución

1. Clona el repositorio:
   ```bash
   git clone https://github.com/6aligula/App_Chat_Hexagonal_Architecture
   ```

2. Navega al directorio del proyecto:
   ```bash
   cd App_Chat_Hexagonal_Architecture
   ```

3. Levanta los contenedores usando **Docker Compose**:
   ```bash
   docker-compose up --build
   ```

4. La aplicación estará disponible en `http://localhost:8000`.