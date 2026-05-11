import os
from dataclasses import dataclass


@dataclass
class Config:
    app_name: str
    debug: bool
    db_url: str
    secret_key: str
    allowed_hosts: list[str]
    port: int


def load_config() -> Config:
    return Config(
        app_name=os.getenv("APP_NAME", "frontier-app"),
        debug=os.getenv("DEBUG", "false").lower() == "true",
        db_url=os.getenv("DATABASE_URL", "sqlite:///app.db"),
        secret_key=os.getenv("SECRET_KEY", "change-me-in-production"),
        allowed_hosts=os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1").split(","),
        port=int(os.getenv("PORT", "8080")),
    )


def validate_config(cfg: Config) -> list[str]:
    errors = []
    if cfg.secret_key == "change-me-in-production":
        errors.append("SECRET_KEY must be set in production")
    if cfg.debug and "0.0.0.0" in cfg.allowed_hosts:
        errors.append("DEBUG mode should not allow all hosts")
    if cfg.port < 1 or cfg.port > 65535:
        errors.append(f"PORT {cfg.port} is out of valid range")
    return errors
