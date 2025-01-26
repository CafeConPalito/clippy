# CLIPPY

## Descripción

Este proyecto tiene como objetivo crear una interfaz gráfica con el icónico Clippy de Windows, pero con conexión a Azure Open AI o OpenAI API. La aplicación también es compatible con Linux y macOS.

## Características

- Interfaz gráfica con Clippy
- Conexión a Azure Open AI o OpenAI API
- Compatibilidad con Linux y macOS

## Requisitos

- Cuenta de Azure Open AI o OpenAI API

## Requisitos funcionales del proyecto

### Obligatorio:

- [ ] Hacer una ventana transparente
- [ ] Permitir que se interactúe con lo que haya por detrás
- [ ] Poner un avatar estático (clippy del Windows viejo)
- [ ] Poner burbujas de out/in para tener una conversación con él
- [ ] Mostrar dos mensajes a la vez, pregunta del usuario, respuesta del bot
- [x] Conectar el bot con Azure AI y solo hacer prompt engineering
- [x] Guardar credenciales en el vault de windows

### Opcional:

- [ ] Animar el avatar
- [ ] Poner más de dos burbujas
- [ ] Hacer una ventana de configuración de variables de entorno
- [x] Hacer un conector universal para diferentes AI 
- [ ] Implementar técnicas avanzadas de AI(rag)

## Para colaborar en el proyecto

1. Clona el repositorio:
    ```bash
    git clone https://github.com/CafeConPalito/clippy
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd clippy
    ```
3. Crea un entorno virtual de Python:
    ```bash
    python -m venv env
    ```

4. Activa el entorno virtual:

    - En Windows:
        ```bash
        .\env\Scripts\activate
        ```
    - En macOS y Linux:
        ```bash
        source env/bin/activate
        ```

5. Instala las dependencias necesarias:
    ```bash
    pip install -r requirements.txt
    ```

### Crear una rama y hacer un merge request

1. Crea una nueva rama con el siguiente patrón `develop-username-feature`:
    ```bash
    git checkout -b develop-username-feature
    ```

2. Realiza los cambios necesarios y haz commit (Asegúrate de seguir las convenciones de commit convencionales (Conventional Commits) al realizar tus commits)(Más información sobre Conventional Commits: https://www.conventionalcommits.org/):
    ```bash
    git add .
    git commit -m "feat: Descripción de los cambios realizados"
    ```

3. Sube la rama al repositorio remoto:
    ```bash
    git push origin develop-username-feature
    ```

4. Abre un pull request desde `develop-username-feature` hacia `main` en Github

## Si solo quieres usar la app

1. Descarga el ejecutable para tu sistema operativo desde la sección de [Releases](https://github.com/CafeConPalito/clippy/releases) en GitHub.
2. Ejecuta el archivo descargado y sigue las instrucciones en pantalla.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio.

## Licencia

Este proyecto está bajo la Licencia GNU/v3.