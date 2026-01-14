from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine

class Database_helper:
    def __init__(
        self,
        url:str,
        echo:bool = False,
        pool_size:int = 10,
        max_overflow:int = 10
    ):
        self.engine:AsyncEngine = create_async_engine(
           url=url,
           echo=echo,
           pool_size=pool_size,
           max_overflow=max_overflow    
        )