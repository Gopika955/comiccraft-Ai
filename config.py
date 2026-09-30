from functools import lru_cache
from pathlib import Path
from typing import Optional, Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    app_name: str = "ComicCraft"
    debug: bool = True
    host: str = "127.0.0.1"
    port: int = 8000

    gemini_api_key: str = ""
    gemini_flash_model: str = "gemini-2.5-flash"
    gemini_pro_model: str = "gemini-2.5-pro"

    image_backend: Literal["placeholder", "diffusers"] = "placeholder"

    sd_model_id: str = "runwayml/stable-diffusion-v1-5"
    hf_token: str = ""

    comic_panel_count: int = Field(default=5, ge=1, le=10)

    image_width: int = Field(default=512, ge=256, le=1024)
    image_height: int = Field(default=512, ge=256, le=1024)
    image_steps: int = Field(default=25, ge=5, le=100)
    image_guidance_scale: float = Field(default=7.5, ge=1, le=20)

    image_seed: Optional[int] = None

    max_prompt_length: int = Field(
        default=2000,
        ge=100,
        le=10000
    )

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()


STATIC_DIR = BASE_DIR / "static"
PANEL_DIR = STATIC_DIR / "panels"
EXPORT_DIR = STATIC_DIR / "exports"
TEMPLATE_DIR = BASE_DIR / "templates"


STATIC_DIR.mkdir(parents=True, exist_ok=True)
PANEL_DIR.mkdir(parents=True, exist_ok=True)
EXPORT_DIR.mkdir(parents=True, exist_ok=True)
TEMPLATE_DIR.mkdir(parents=True, exist_ok=True)