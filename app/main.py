from typing import List, Union

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

#Cria as tabelas no banco de dados
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Cria a dependencia para uso de db
def get_db():
    db = SessionLocal()
    try:
      yield db
    finally:
      db.close()

# Define a rota padrão com retorno de uma string
@app.get("/")
def default_route():
    return "Acesse /docs para interagir com as funções da API"

# Define a rota de pesquisa de um estudante por RA
@app.get("/student/{student_ra}", response_model=schemas.Student)
def read_student(student_ra: int, db: Session = Depends(get_db)):
    db_student = crud.get_student_by_ra(db, student_ra=student_ra)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

# Define a rota de listagem dos estudantes, tendo a possibilidade de filtrar por curso e por materia
@app.get("/students/", response_model=List[schemas.Student])
# def read_students(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
def read_students(db: Session = Depends(get_db), course: Union[str, None] = None, subject: Union[str, None] = None):
    # students = crud.get_students(db, skip=skip)
    students = crud.get_students(db=db)
    if course:
        students = crud.get_students_by_course(db=db, student_course=course)
    if subject:
        students = crud.get_students_by_subject(db=db, student_subject=subject)
    return students

# Define a rota de criacao de um estudante
@app.post("/student/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    response = crud.create_student(db=db, student=student)
    return response

# Define a rota de exclusao de um estudante baseado em seu RA
@app.delete("/student/{student_ra}/", response_model=schemas.Student)
def delete_student(student_ra: int, db: Session = Depends(get_db)):
    db_student = crud.delete_student(db=db, student_ra=student_ra)
    return db_student
