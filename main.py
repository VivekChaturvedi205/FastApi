from fastapi import FastAPI
import uvicorn
from typing import Optional
from pydantic import BaseModel

# GET -- GET AN INFORMATION
# POST -- CREATE SOMETHING NEW
# PUT -- UPDATE AN DATA
# DELETE -- DELETE SOMETHING

app=FastAPI()

students={
    1:{
        "name":"vivek",
        "age":205,
        "rollno":"MCA"
    }
}

class Student(BaseModel):
    name:str
    age:int
    rollno:int
    
class UpdateStudent(BaseModel):
    name:Optional[str]=None
    age:Optional[int]=None
    rollno:Optional[int]=None


@app.get("/")
async def index():
    return {"name":"First Data"}

@app.get("/get-students/{student_id}")
async def get_students(student_id:int):
    return students[student_id]
    

@app.get("/get-by-name/")
async def get_by_name(name:Optional[str]=None):
    for student_id in students:
        if students[student_id]['name']==name:
            return students[student_id]
    return {"Data": "Not Found"}


@app.post("/create_student/{student_id}")
async def create_student(student_id:int, student:Student):
    if student_id in students:
        return {"Error": "Student already exists"}
    students[student_id] = student
    return {"Data": "Object created successfully"}


@app.put('/update-student/{student_id}')
async def update_student(student_id:int, student:UpdateStudent):
    if student_id not in students:
        return {'error':"Student does not exist"}
    if student.name != None:
        students[student_id].name = student.name
    if student.age != None:
        students[student_id].age = student.age
    if student.rollno != None:
        student[student_id].rollno = student.rollno
    return {"Data Update": {"Student": student}}
    
@app.delete('/delete_student/{student_id}')
async def delete_student(student_id:int):
    if student_id not in students:
        return {'error':'Student not found'}
    del students[student_id]
    return {'success':"Student deleted successfully"}
    
if __name__ == "__main__":
    uvicorn.run(app)