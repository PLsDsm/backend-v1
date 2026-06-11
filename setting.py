from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_DATABASE: str

    EMB_API_KEY: str
    
    APP_NAME: str
    
    GROQ_API_KEY: str
    
    GITHUB_REPO: str
    GITHUB_KEY: str
    GITHUB_RAW_URL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()