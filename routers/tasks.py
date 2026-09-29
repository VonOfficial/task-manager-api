from fastapi import APIRouter, HTTPException

from models.task import Task, TaskOut


router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)


tasks_db = []


@router.get("/", response_model=list[TaskOut])
def get_tasks():
    return tasks_db


@router.post("/", response_model=TaskOut)
def create_task(task: Task):
    new_task = {
        "id": len(tasks_db) + 1,
        **task.model_dump()
    }

    tasks_db.append(new_task)

    return new_task


@router.get("/{task_id}", response_model=TaskOut)
def get_task(task_id: int):
    for task in tasks_db:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail="Задача не найдена"
    )