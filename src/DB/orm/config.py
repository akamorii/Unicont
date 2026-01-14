from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_PORT:int
    DB_ADRESS:str    
    DB_USER:str 
    DB_PASS:str
    DB_NAME:str

    @property
    def DATABASE_URL_asyncpg(self):
       return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_ADRESS}:{self.DB_PORT}/{self.DB_NAME}"
    
    
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    
    
settings = Settings()