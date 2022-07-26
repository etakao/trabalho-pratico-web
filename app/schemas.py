from typing import List, Union

from pydantic import BaseModel

# Cria os schemas para definir os atributos usados para se criar e ler dados de uma classe
class StudentBase(BaseModel):
    ra: int
    name: str
    course: str
    subject: str

class StudentCreate(StudentBase):
    pass

# class Config eh criado para dizer ao Pydantic que os dados podem ser lidos mesmo nao sendo como um dicionario
class Student(StudentBase):
    class Config:
      orm_mode = True
