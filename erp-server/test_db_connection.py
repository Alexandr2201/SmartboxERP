from sqlalchemy import create_engine

def test_connection():
    DATABASE_URI = 'postgresql://postgres:A12345aa@localhost:5432/Smartbox SQL'
    engine = create_engine(DATABASE_URI)

    try:
        connection = engine.connect()
        print("Connection to PostgreSQL DB successful")
        connection.close()
    except Exception as e:
        print(f"The error '{e}' occurred")

test_connection()
