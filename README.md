# DNN Alpha - Noticias Financieras Personalizadas para Inversores

Plataforma web responsive (**Mobile-First SPA / PWA**) diseñada para inversores que necesitan informarse sin sobrecarga de información ni contradicciones. El sistema rastrea medios tradicionales y redes sociales, resume las noticias en 2-3 puntos clave sin clickbait, clasifica el impacto estimado en cartera y prioriza el feed mediante un algoritmo de relevancia transparente y continuo.

---

## Características Principales

1. **Feed Personalizado & Motor de Scoring Dinámico**:
   - Ordenamiento por relevancia según los activos en cartera del usuario (no cronológico puro).
   - Scoring ponderado (0-100):
     - **Coincidencia con Cartera (45%)**: Ponderación por tenencia directa de tickers, clases de activo o exposición macro.
     - **Magnitud y Dirección de Impacto (25%)**: Clasificación de impacto (Alto/Medio/Bajo, Positivo/Negativo/Neutral).
     - **Afinidad Histórica (20%)**: Aprendizaje continuo a través de clicks en fuentes, bookmarks y calificaciones.
     - **Frescura Temporal (10%)**: Decaimiento suave de frescura.
   - Indicador transparente *"¿Por qué veo esto?"* que desglosa el cálculo en tiempo real.

2. **Doble Canal de Consumo (Prensa vs Redes)**:
   - Pestaña **Medios de Prensa**: Coberturas de medios tradicionales (Bloomberg, Financial Times, Reuters, WSJ, CNBC, El Cronista, Ámbito).
   - Pestaña **Redes Sociales**: Detección de tendencias y análisis minorista/institucional en X/Twitter, Reddit (r/wallstreetbets, r/investing), YouTube y canales de Telegram.

3. **Card Resumen & Fila de Fuentes Deduplicadas**:
   - Titular objetivo, síntesis ejecutiva y 2-3 bullets accionables.
   - Etiqueta visual de impacto (`▲ Alto Positivo`, `▼ Medio Negativo`) con el activo afectado.
   - Carrusel horizontal con las distintas fuentes que cubrieron el mismo evento.
   - Drawer in-app *"Detalle de Fuente"* para consultar el extracto original o saltar al artículo oficial en nueva pestaña.

4. **Gestión de Portfolio en Vivo & Wizard de Onboarding**:
   - Alta de usuario con selector de experiencia, tolerancia al riesgo y horizonte temporal.
   - Selector rápido y flexible para agregar o quitar tickers (ej: `NVDA`, `BTC`, `AL30`, `SPY`, `BRENT`, `TSLA`, etc.).
   - Switcher de perfiles demo con 1 click:
     - **Inversor Tech & Cripto**: Marcos (`NVDA`, `BTC`, `ETH`, `AAPL`, `SPY`).
     - **Inversor Renta Fija & Valor**: Lucía (`AL30`, `SPY`, `BRENT`, `AAPL`).
     - **Macro Trader**: Javier (`BRENT`, `QQQ`, `BTC`, `AL30`).

5. **Simulador de Pipeline de Ingesta IA**:
   - Herramienta para simular el ingreso de noticias de última hora, procesándolas por el pipeline de deduplicación, síntesis y scoring en tiempo real.

---

## Arquitectura y Stack Tecnológico

- **Frontend**: SPA / PWA responsive con Tailwind CSS, Lucide / Heroicons SVG, tipografía Plus Jakarta Sans y JetBrains Mono, Service Worker para soporte offline e instalación móvil.
- **Backend**: FastAPI (Python 3.14) con OpenAPI / Swagger interactivo en `/docs`.
- **Base de Datos**: SQLite relacional (`financial_news.db`) con esquema normalizado:
  - `users`
  - `portfolio_assets`
  - `sources`
  - `news_stories` (clusters deduplicados)
  - `source_articles` (artículos individuales asociados)
  - `user_interactions` (historial de engagement)

---

## Cómo Ejecutar el Proyecto

### 1. Iniciar Servidor
```bash
python run.py
```

La aplicación estará disponible inmediatamente en:
- **Web App**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **API Swagger**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 2. Ejecutar Pruebas Automatizadas
```bash
python -m pytest tests/ -v
```
