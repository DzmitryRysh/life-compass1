from fastapi import FastAPI
from app.api.routes.profile import router as profile_router


def create_app() -> FastAPI:
    app = FastAPI(title="Life Compass", version="0.1.0")

    @app.get("/")
    def root():
        return {"service": "Life Compass", "status": "ok", "docs": "/docs"}

    @app.get("/health")
    def health():
        return {"status": "ok"}

    app.include_router(profile_router)

    return app

app = create_app()