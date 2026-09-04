# lemma-lookup

**Live demo:** https://<your-username>.github.io/lemma-lookup/

Minimal German lemma lookup application using React, Django, and spaCy.

## MVP Build Checklist

Build the project in the following order. Each step should leave the project in a runnable/testable state before moving on.

### 1. Python project configuration

* [x] `pyproject.toml`

  * Define Python project metadata.
  * Define backend dependencies.
  * Include Django and spaCy.
  * Establish the Python version requirement.

### 2. Django project

* [x] `backend/manage.py`

  * Django command-line entry point.

* [x] `backend/config/settings.py`

  * Django configuration.
  * Installed apps.
  * Middleware.
  * CORS configuration.
  * Allowed hosts.
  * Environment-specific settings.

* [x] `backend/config/urls.py`

  * Root URL routing.
  * Connect the lookup application.

* [x] `backend/config/asgi.py`

  * ASGI entry point for asynchronous-compatible deployment.

* [x] `backend/config/wsgi.py`

  * WSGI entry point for production deployment.

### 3. Lookup Django application

* [x] `backend/lookup/apps.py`

  * Register the lookup Django application.

* [x] `backend/lookup/services.py`

  * Core NLP logic.
  * Load the German spaCy model.
  * Process a supplied word.
  * Extract lemma, word class, and morphology.
  * Return structured Python data.

* [x] `backend/lookup/views.py`

  * HTTP/API layer.
  * Validate the request.
  * Apply input limits/rate limiting.
  * Call the lookup service.
  * Return JSON.

* [x] `backend/lookup/urls.py`

  * Define API endpoints.
  * `/api/lookup/`
  * `/api/health/`

* [x] `backend/lookup/tests.py`

  * Test lookup behavior.
  * Test API responses.
  * Test invalid input.
  * Test health endpoint.

### 4. Verify the backend

* [x] Run Django locally.
* [x] Test `/api/health/`.
* [x] Test `/api/lookup/?word=gingen`.
* [x] Confirm the response contains structured JSON.
* [x] Confirm spaCy returns the expected lemma and morphology.

### 5. React + TypeScript frontend

* [x] `frontend/package.json`

  * Define frontend dependencies and scripts.

* [x] `frontend/tsconfig.json`

  * Configure the TypeScript compiler.
  * Define TypeScript compiler options.
  * Enable strict type checking.
  * Configure React JSX support.
  * Define the frontend source directory.  

* [x] `frontend/vite.config.ts`

  * Configure Vite.

* [x] `frontend/index.html`

  * HTML entry point for the React application.

* [ ] `frontend/src/main.tsx`

  * Bootstrap the React application.

* [ ] `frontend/src/types.ts`

  * Define TypeScript types for Django API responses.

* [ ] `frontend/src/api.ts`

  * Handle requests to the Django API.
  * Convert API responses into typed data.

* [ ] `frontend/src/App.tsx`

  * Main dictionary UI.
  * Word input.
  * Lookup button.
  * Last lookup.
  * Lemma information.
  * Word class.
  * Morphology.
  * Error/loading states.

* [ ] `frontend/src/style.css`

  * Minimal responsive styling.
  * Input/button styling.
  * Dictionary entry layout.
  * Information boxes.

### 6. Connect frontend and backend

* [ ] Configure the frontend API URL.
* [ ] Configure Django CORS.
* [ ] Perform a lookup from React.
* [ ] Render the returned JSON as dictionary information.
* [ ] Handle loading and API errors.

### 7. Documentation

* [ ] `docs/conf.py`

  * Configure Sphinx.
  * Configure the Furo theme.

* [ ] `docs/index.rst`

  * Documentation entry point.

* [ ] `docs/architecture.rst`

  * Describe the frontend → API → spaCy architecture.

* [ ] `docs/api.rst`

  * Document API endpoints and JSON responses.

* [ ] `docs/development.rst`

  * Explain local development and testing.

* [ ] Build the Sphinx documentation successfully.

### 8. Docker / Hugging Face deployment

* [ ] `Dockerfile`

  * Build the Django backend image.
  * Install Python dependencies.
  * Install the German spaCy model.
  * Run the production server.
  * Expose the required port.

* [ ] Run the Docker image locally.

* [ ] Verify the API from inside the container.

* [ ] Deploy the backend to Hugging Face.

### 9. GitHub Actions

* [ ] `.github/workflows/test.yml`

  * Install dependencies.
  * Run Django tests.
  * Build the frontend.
  * Build the documentation.

* [ ] `.github/workflows/deploy-pages.yml`

  * Build the React/Vite frontend.
  * Deploy `dist/` to GitHub Pages.

### 10. Final MVP verification

* [ ] Open the GitHub Pages frontend.
* [ ] Enter a German word.
* [ ] Send the lookup request.
* [ ] Confirm Django receives it.
* [ ] Confirm spaCy processes it.
* [ ] Confirm JSON is returned.
* [ ] Confirm React renders the result.
* [ ] Test invalid/empty input.
* [ ] Test a few inflected German forms.
* [ ] Confirm the production deployment works end-to-end.

---

## Architecture

```text
React + TypeScript + Vite
            │
            │ HTTPS / JSON
            ▼
      Django REST API
            │
            ▼
          spaCy
            │
            ▼
    Structured JSON response
            │
            ▼
       React UI
```

The frontend is a static application deployed to GitHub Pages. The Django API runs separately in a Docker container on Hugging Face.

## API

### Lookup

```text
GET /api/lookup/?word=gingen
```

Example response:

```json
{
  "word": "gingen",
  "lemma": "gehen",
  "pos": "VERB",
  "morphology": {
    "tense": "past",
    "person": "3",
    "number": "plural"
  }
}
```

### Health

```text
GET /api/health/
```

Example response:

```json
{
  "status": "ok",
  "spacy": true,
  "model": "de_core_news_sm"
}
```

## Development

Backend:

```bash
cd backend
python manage.py runserver
```

Frontend:

```bash
cd frontend
npm install
npm run dev
```

Documentation:

```bash
sphinx-build -b html docs docs/_build/html
```

## Deployment

* Frontend → GitHub Pages
* Backend → Hugging Face Space
* CI/CD → GitHub Actions
* Backend container → Docker

## License

See `LICENSE`.

