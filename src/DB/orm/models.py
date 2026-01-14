from sqlalchemy import Table, Column, Integer, String, MetaData, JSON

metadata_obj = MetaData()

        # await conn.execute("""
        # CREATE TABLE IF NOT EXISTS tasks (
        #     id SERIAL PRIMARY KEY,
        #     name VARCHAR(80),
        #     description TEXT,
        #     body TEXT,
        #     answer JSONB
        # );
        # """)
        
tasks_table = Table(
    "tasks",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("description", String),
    Column("body", String),
    Column("answer", JSON)
)
