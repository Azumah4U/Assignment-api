from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI(title="Assignment API")

assignments_db = []
current_id = 1

class AssignmentCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    due_date: str
    done: bool = False

class Assignment(AssignmentCreate):
    id: int

@app.get("/assignments", response_model=List[Assignment])
def get_all_assignments():
    return assignments_db

@app.get("/assignments/{assignment_id}", response_model=Assignment)
def get_one_assignment(assignment_id: int):
    for a in assignments_db:
        if a["id"] == assignment_id:
            return a
    raise HTTPException(status_code=404, detail="Assignment not found")

@app.post("/assignments", response_model=Assignment, status_code=201)
def create_assignment(assignment: AssignmentCreate):
    global current_id
    new = {
        "id": current_id,
        "title": assignment.title,
        "due_date": assignment.due_date,
        "done": assignment.done
    }
    assignments_db.append(new)
    current_id += 1
    return new

@app.delete("/assignments/{assignment_id}")
def delete_assignment(assignment_id: int):
    for a in assignments_db:
        if a["id"] == assignment_id:
            assignments_db.remove(a)
            return {"message": "Assignment deleted"}
    raise HTTPException(status_code=404, detail="Assignment not found")

@app.get("/")
def root():
    return {"message": "Assignment API running. Go to /docs"}