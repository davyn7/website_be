from sqlmodel import SQLModel, create_engine

# def create_database_connection():
#     engine = None
#     Session = None
#     if not is_github_action:
#         db_url = f"postgresql+psycopg2://{RDS_DB_USER}:{RDS_DB_PASS}@{RDS_ENDPOINT}:{RDS_DB_PORT}/{RDS_DB_NAME}"
#         engine = create_engine(db_url)
#         Session = sessionmaker(bind=engine)
#     return engine, Session

# engine, Session = create_database_connection()

engine = create_engine("sqlite:///database.db")

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)