from fastapi import FastAPI
from app.api.routes.profile import router as profile_router
from fastapi import Request
import time
from app.logger import logger




def create_app() -> FastAPI:
    app = FastAPI(title="Life Compass", version="0.1.0")
    logger.info(" Life Compass API is starting")

    @app.middleware("http")
    async def log_requests(request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        duration = time.time() - start_time

        logger.info(
            f"{request.method} {request.url.path} "
            f"→ {response.status_code} ({duration:.3f}s)"
        )
        return response


    @app.get("/")
    def root():
        return {"service": "Life Compass", "status": "ok", "docs": "/docs"}

    @app.get("/health")
    def health():
        logger.info("Health check requested")
        return {"status": "ok"}

    app.include_router(profile_router)

    return app

app = create_app()

