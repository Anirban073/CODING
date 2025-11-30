# Copilot Instructions for fastapi Codebase

## Big Picture Architecture
- This repo contains multiple FastAPI microservice examples, each in its own numbered folder (e.g., `ch36/`, `ch45/`, `ch79/`, etc.).
- Each chapter folder is a mostly self-contained FastAPI project, often with its own `main.py`, `db.py`, `models.py`, and sometimes `services.py`, `tables.py`, and `alembic/` for migrations.
- The structure is designed for learning and experimentation, not for a single monolithic app.

## Key Patterns & Conventions
- **Routers:** API endpoints are organized using FastAPI routers, typically imported in `main.py` from submodules like `app.user.routers` or `app.product.routers`.
- **Tags:** Use the `tags` parameter in `include_router` for OpenAPI grouping. Route-level `tags` override router-level tags.
- **Database:** Most chapters use SQLite (`sqlite.db`) and SQLAlchemy ORM. Migrations (if present) use Alembic (`alembic/`).
- **Services Layer:** Business logic is often separated into `services.py`.
- **Models:** Pydantic models and SQLAlchemy models are usually defined in `models.py` or `tables.py`.
- **Requirements:** Each chapter has its own `requirements.txt` for dependencies.

## Developer Workflows
- **Run a Chapter:**
  - Navigate to the desired chapter (e.g., `cd ch79`)
  - Install dependencies: `pip install -r requirements.txt`
  - Start server: `uvicorn main:app --reload`
- **Migrations:**
  - If `alembic/` exists, use Alembic commands (e.g., `alembic upgrade head`).
- **Testing:**
  - No global test runner; tests (if any) are chapter-specific.
- **Debugging:**
  - Use FastAPI's built-in `/docs` (Swagger UI) for interactive API exploration.

## Integration Points
- **External Dependencies:**
  - FastAPI, SQLAlchemy, Alembic, Pydantic, Uvicorn.
- **Cross-Component Communication:**
  - Each chapter is isolated; no shared state or inter-chapter communication.

## Examples
- See `ch79/app/main.py` for router inclusion and tag usage.
- See `ch45/models.py` and `ch45/services.py` for model/service separation.
- See `ch46/alembic/` for migration setup.

## Project-Specific Advice
- Always work within the relevant chapter folder.
- Do not assume global configuration or shared dependencies.
- When adding new features, follow the chapter's existing structure and conventions.

---
_If any section is unclear or missing, please provide feedback for improvement._
