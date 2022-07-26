from sqlalchemy.orm import Session
from fastapi import HTTPException

from . import models, schemas

# Recebe db e o RA do estudante a ser procurado
def get_student_by_ra(db: Session, student_ra: int):
    return db.query(models.Student).filter(models.Student.ra == student_ra).first()

# Recebe db e o curso e retorna os estudantes com aquele curso
# def get_students_by_course(db: Session, student_course: str, skip: int = 0, limit: int = 50):
def get_students_by_course(db: Session, student_course: str):
    return db.query(models.Student).filter(models.Student.course == student_course).all()

# Recebe db e a materia e retorna os estudantes com aquela materia
# def get_students_by_subject(db: Session, student_subject: str, skip: int = 0, limit: int = 50):
def get_students_by_subject(db: Session, student_subject: str):
    return db.query(models.Student).filter(models.Student.subject == student_subject).all()

# Recebe apenas db e retorna todos os estudantes, podendo ser aplicado um limitante da quantidade de estudantes retornados
# def get_students(db: Session, skip: int = 0, limit: int = 50):
def get_students(db: Session):
    return db.query(models.Student).all()

# Recebe db e os dados necessarios para criar o estudante
def create_student(db: Session, student: schemas.StudentCreate):
    check_student = get_student_by_ra(db, student_ra=student.ra)
    if check_student:
      raise HTTPException(status_code=400, detail="RA already registered")
    else:
        db_student = models.Student(**student.dict())
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return db_student

# Recebe db e o RA do estudante a ser deletado
def delete_student(db: Session, student_ra: int):
    db_student = db.query(models.Student).filter(models.Student.ra == student_ra).delete(synchronize_session='fetch')
    if db_student:
        db.commit()
    else: 
        raise HTTPException(status_code=404, detail="Student not found")
    return
