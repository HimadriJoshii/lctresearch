from sqlalchemy.orm import Mapped,mapped_column
from datetime import datetime,UTC
from sqlalchemy import String,DateTime,Boolean
from database import Base

class Task(Base):
    __tablename__="tasks_task"
    id:Mapped[int]=mapped_column(primary_key=True)
    title:Mapped[str]=mapped_column(String(255))
    completed:Mapped[bool]=mapped_column(Boolean,default=False)
    created_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),default=lambda: datetime.now(UTC))



'''class Task(models.Model):
    title=models.CharField(max_length=255)
    completed=models.BooleanField(default=False)
    creaed_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title'''