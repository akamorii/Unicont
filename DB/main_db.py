import psycopg2
from psycopg2.extras import Json
from dotenv import load_dotenv
from os import getenv

load_dotenv()

conn = psycopg2.connect(
    host=getenv("DB_ADRESS"),
    port=getenv("DB_PORT"),
    user=getenv("DB_USER"),
    password=getenv("DB_PASS"),
    dbname=getenv("DB_NAME")
)

with conn.cursor() as curs:
    curs.execute("""
    CREATE TABLE IF NOT EXISTS tasks ( 
    id SERIAL PRIMARY KEY,
    name VARCHAR(80),
    description TEXT,
    body TEXT,
    answer JSONB
                );
    """)
  
  
def add_task(name: str, description:str, body:str, answer:dict):
    with conn.cursor() as curs:
        curs.execute("""
                     INSERT INTO tasks(name, description, body, answer)
                     VALUES (%s, %s, %s, %s)
                     """,
        (name, description, body, Json(answer))
        )
        conn.commit()

def get_task(task_id):
    with conn.cursor() as curs:
        curs.execute("""
                        SELECT * FROM tasks WHERE id = %s;
                     """,(task_id,))   
        task = curs.fetchone()

        print(f"{task}") 

        
if __name__ == '__main__':
    linear_eq = {
        "name": "linear equation", 
        "description": "easy linear equation", 
        "body": r"\begin{cases}x + y = 10 \\2x - y = 8\end{cases}",
        "answer": {"x": 6, "y":4}
    }
    # add_task(**linear_eq)
    get_task(1)