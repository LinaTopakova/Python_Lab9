from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "FastAPI Lab"
    environment: str = "development"
    database_url: str = "sqlite:///./app.db"  
    secret_key: str

    model_config = SettingsConfigDict(env_file=".env")