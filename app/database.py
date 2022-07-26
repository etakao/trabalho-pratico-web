from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Cria a URL de conexao do banco de dados SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"

# Cria um engine do SQLAlchemy
# O segundo parametro passado eh necessario apenas para SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Cria uma classe de sessao para o banco de dados quando instanciada
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

# Cria uma classe Base para herdar de cada model criado
Base = declarative_base()
