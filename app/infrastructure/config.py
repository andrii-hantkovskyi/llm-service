from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "LLM Client Manager"
    DEBUG: bool = False

    OPENAI_API_KEY: str | None = None
    HUGGINGFACE_API_KEY: str | None = None

    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)


settings = Settings()
