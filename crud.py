from pydantic import BaseModel, Field, ConfigDict
from fastapi import APIRouter, HTTPException
from database import SessionDep
from models import StudentModel
from sqlalchemy import select, update, delete
from typing import Optional

class StudentAddSchema(BaseModel):
    name: Optional[str] = Field(default=None, max_length=30)
    course: Optional[int] = Field(default=None, ge=1, le=6)
    av_score: Optional[float] = Field(default=None, ge=2, le=5)

    model_config = ConfigDict(extra="forbid")

class StudentSchema(StudentAddSchema):
    id: int

router = APIRouter()# Создаем роутер вместо app

@router.post("/students", tags=["Студенты🧑‍🎓"], summary="Добавление конкретного студента")
async def add_student(data: StudentAddSchema, session: SessionDep):
    new_student = StudentModel(
        name = data.name,
        course = data.course,
        av_score = data.av_score
    )
    session.add(new_student)
    await session.commit()
    return {"ok": True, "message": f"Student {data.name} is appended"}

@router.get("/students", tags=["Студенты🧑‍🎓"], summary="Получение всех студентов")
async def get_students(session: SessionDep):
    query = select(StudentModel)
    res = await session.execute(query)
    return res.scalars().all()

@router.get("/students/{id}", tags=["Студенты🧑‍🎓"], summary="Получение конкретного студента")
async def get_student(id: int, session: SessionDep):
    student_obj = await session.get(StudentModel, id)
    #query = select(StudentModel).where(StudentModel.id == id)
    #res = await session.execute(query)
    #return res.scalars().first()
    return student_obj

@router.patch("/students/{id}", tags={"Студенты🧑‍🎓"}, summary="Обновление конкретного студента")
async def update_student(student_id: int, data: StudentAddSchema, session: SessionDep):

    data_dict = data.model_dump(exclude_unset=True, exclude_none=True)
    print("Type of data_dict = ", type(data_dict))
    await session.execute(
        update(StudentModel)
        .where(StudentModel.id == student_id)
        .values(**data_dict)
    )

    await session.commit()

    return {"ok": True, "message": f"The student with id {student_id} is successfully updated"}

@router.delete("/students/", tags=["Студенты🧑‍🎓"], summary="Удаление всех студентов")
async def delete_students(session: SessionDep):

    await session.execute(delete(StudentModel))

    await session.commit()
    return {"ok": True, "message": "All students are deleted"}

@router.delete("/students/{id}", tags=["Студенты🧑‍🎓"], summary="Удаление конкретного студента")
async def delete_students(student_id: int, session: SessionDep):

    await session.execute(
        delete(StudentModel)
        .where(StudentModel.id == student_id)
    )

    await session.commit()

    return {"ok": True, "message": f"The student with id {student_id} is deleted"}
