from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing import Annotated, Optional

intpk = Annotated[int, mapped_column(primary_key=True)]

class Base(DeclarativeBase):
	pass
	
class StudentModel(Base):
	__tablename__ = "students"
	
	id: Mapped[intpk]
	name: Mapped[str]
	course: Mapped[int]
	av_score: Mapped[float]

