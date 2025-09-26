from pydantic import BaseModel, Field, ConfigDict
from fastapi import APIRouter, HTTPException
from database import SessionDep
from models import StudentModel
from sqlalchemy import select
from typing import Optional
class StudentAddSchema(BaseModel):
    # name: Optional[str] = Field(max_length=30)
    # course: Optional[int] = Field(ge=1, le=6)
    # av_score: Optional[float] = Field(ge=2, le=5)
    name: Optional[str] = None
    course: Optional[int] = None
    av_score: Optional[float] = None

    model_config = ConfigDict(extra="forbid")

class StudentSchema(StudentAddSchema):
    id: int

router = APIRouter()# Создаем роутер вместо app

@router.post("/students", tags=["Студенты"], summary="Добавление конкретного студента")
async def add_student(data: StudentAddSchema, session: SessionDep):
    new_student = StudentModel(
        name = data.name,
        course = data.course,
        av_score = data.av_score
    )
    session.add(new_student)
    await session.commit()
    return {"ok": True}

@router.get("/students", tags=["Студенты"], summary="Получение всех студентов")
async def get_students(session: SessionDep):
    query = select(StudentModel)
    res = await session.execute(query)
    return res.scalars().all()

@router.get("/students/{id}", tags=["Студенты"], summary="Получение конкретного студента")
async def get_student(id: int, session: SessionDep):
    student_obj = await session.get(StudentModel, id)
    return student_obj

@router.patch("/students/{id}", tags=["Студенты"], summary="Обновление конкретного студента")
async def update_student(id: int, data: StudentAddSchema, session: SessionDep):
    student_obj = await session.get(StudentModel, id)
    # Более компактно
    if data.name is not None: student_obj.name = data.name
    if data.course is not None: student_obj.course = data.course
    if data.av_score is not None: student_obj.av_score = data.av_score

    await session.commit()

    return {"ok": True}

@router.delete("/students/", tags=["Студенты"], summary="Удаление всех студентов")
async def delete_students(session: SessionDep):
    query = select(StudentModel)
    result = await session.execute(query)
    students = result.scalars().all()

    for student in students:
        await session.delete(student)

    await session.commit()
    return {"ok": True}

@router.delete("/students/{id}", tags=["Студенты"], summary="Удаление конкретного студента")
async def delete_students(id: int, session: SessionDep):
    student = await session.get(StudentModel, id)
    await session.delete(student)
    await session.commit()

    return {"ok": True}
