# Guía Paso a Paso: Cómo Desplegar tu Proyecto en Vercel (Gratis)

Esta guía te explica cómo dejar la aplicación online en internet con un enlace público (tipo `https://tu-proyecto.vercel.app`) para que tus amigos puedan abrirla, interactuar y probarla desde sus celulares o computadoras sin instalar nada.

---

## Opción Recomendada: Despliegue con GitHub y Vercel (2 minutos)

El proyecto ya está 100% configurado con `vercel.json` y el adaptador serverless `api/index.py`.

### Paso 1: Crear un repositorio en GitHub

   **Método A (Vía web en 30 segundos, sin instalar nada):**
   - Entra a [github.com/new](https://github.com/new) y crea un nuevo repositorio llamado `dnn-financial-news`.
   - En la pantalla que aparece, haz click en el enlace que dice **"uploading an existing file"**.
   - Arrastra todas las carpetas y archivos de este proyecto (`api`, `app`, `static`, `requirements.txt`, `vercel.json`, etc.) a la ventana de GitHub y haz click en **"Commit changes"**.

   **Método B (Si usas Git o GitHub Desktop):**
   - Ejecuta en la terminal:
     ```bash
     git init
     git add .
     git commit -m "Initial commit: DNN Financial News App"
     git branch -M main
     git remote add origin https://github.com/TU_USUARIO/dnn-financial-news.git
     git push -u origin main
     ```

---

### Paso 2: Conectar con Vercel

1. Entra a [vercel.com](https://vercel.com) e inicia sesión con tu cuenta de **GitHub**.
2. En el panel principal (Dashboard), haz click en el botón **"Add New..."** y selecciona **"Project"**.
3. Verás la lista de tus repositorios de GitHub. Busca `dnn-financial-news` y haz click en **"Import"**.
4. En la pantalla de configuración:
   - **Framework Preset**: Puedes dejarlo en *Other* (Vercel detecta automáticamente el archivo `vercel.json`).
   - **Root Directory**: `./` (la raíz del proyecto).
   - **Environment Variables**: No necesitas configurar ninguna variable obligatoria, la base de datos se inicializa y auto-siembra en `/tmp` automáticamente.
5. Haz click en el botón azul **"Deploy"**.

¡Listo! En aproximadamente 1 minuto, Vercel compilará la función de Python y desplegará los archivos estáticos. Te dará una URL pública como:
👉 **`https://dnn-financial-news.vercel.app`**

---

## Opción Alternativa: Despliegue directo desde la terminal con Vercel CLI

Si tienes Node.js / npx instalado y prefieres no pasar por GitHub:

1. En la carpeta del proyecto, ejecuta:
   ```bash
   npx vercel
   ```
2. Te pedirá iniciar sesión o confirmar tu cuenta.
3. Responde a las preguntas de la consola:
   - *Set up and deploy?* -> `y`
   - *Which scope?* -> tu usuario
   - *Link to existing project?* -> `n`
   - *Project name?* -> `dnn-financial-news`
   - *Directory?* -> `./`
4. Al terminar te dará un link de preview. Para el despliegue final a producción ejecuta:
   ```bash
   npx vercel --prod
   ```

---

## ¿Por qué Vercel y cómo funciona tras bambalinas?

- **Python Serverless (`api/index.py`)**: Cada solicitud a `/api/*` y `/docs` es atendida de forma instantánea por una Serverless Function en Python con FastAPI.
- **Archivos Estáticos en CDN Global**: El frontend (`/static/*`) y la página principal (`/`) se distribuyen a través de la red Edge de Vercel a máxima velocidad.
- **Base de Datos SQLite en Memoria/Temporal (`/tmp`)**: En entornos serverless, el directorio de despliegue es de solo lectura. El código detecta automáticamente el entorno de Vercel y aloja la base de datos en `/tmp/financial_news.db`, sembrando los 7 casos reales de noticias y los perfiles de inversor en el primer inicio.

---

## ¿Y qué pasa con Netlify?

Netlify está más orientado a sitios estáticos con Node/Go. Para aplicaciones Python con FastAPI, **Vercel** o **Render** son mucho más naturales y robustos:
- **Vercel**: Es serverless, escala a cero, no cuesta nada y no se "duerme" como los servidores gratuitos tradicionales.
- **Render.com** (Alternativa si prefieres un servidor tradicional continuo):
  1. Conectas el mismo repositorio de GitHub en [render.com](https://render.com).
  2. Creas un **Web Service**.
  3. Build Command: `pip install -r requirements.txt`
  4. Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

---

## Cómo compartirlo con tus amigos

Una vez que tengas la URL de Vercel (ej: `https://dnn-financial-news.vercel.app`):
1. **Pásales el link directamente por WhatsApp o Telegram.**
2. Diles que lo abran desde el navegador de su teléfono (Chrome o Safari).
3. Podrán tocar el botón de su navegador para **"Agregar a pantalla de inicio"** y usarlo a pantalla completa como una aplicación móvil nativa (PWA).
4. Invítalos a cambiar de perfil demo (arriba a la derecha), filtrar por fuentes o simular una noticia con el botón *"Simular Ingesta"*.
