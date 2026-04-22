from fastapi import FastAPI
from app.core.config import get_settings
from app.core.logger import setup_logging
from app.api.routes_health import router as health_router
from app.api.routes_tracks import router as tracks_router
from app.api.routes_reports import router as reports_router

settings = get_settings()
setup_logging(settings.log_level)

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="Starter API for vehicle tracking in city environments",
)

app.include_router(health_router)
app.include_router(tracks_router)
app.include_router(reports_router)
