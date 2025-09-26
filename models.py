from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
	pass
	
class StudentModel(Base):
	__tablename__ = "students"
	
	id: Mapped[int] = mapped_column(primary_key=True)
	name: Mapped[str]
	course: Mapped[int]
	av_score: Mapped[float]

