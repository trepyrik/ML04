from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "vehicle-tracking-system"
    app_env: str = "dev"
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    log_level: str = "INFO"

    postgres_host: str = "localhost"
    postgres_port: int = 5432
    postgres_db: str = "vehicle_tracking"
    postgres_user: str = "vehicle_user"
    postgres_password: str = "vehicle_password"

    redis_host: str = "localhost"
    redis_port: int = 6379

    model_path: str = "models/detectors/best_vehicle_detector.pt"
    model_confidence: float = 0.25
    model_iou: float = 0.45
    model_image_size: int = 640

    tracker_type: str = "stub"
    video_output_dir: str = "data/processed"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+psycopg2://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )

    @property
    def redis_url(self) -> str:
        return f"redis://{self.redis_host}:{self.redis_port}/0"


@lru_cache
def get_settings() -> Settings:
    return Settings()
