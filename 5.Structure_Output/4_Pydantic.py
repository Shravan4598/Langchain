from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name:str="Nitish"
    age:Optional[int]=None
    email:EmailStr
    cgpa:float=Field(
        gt=0,       #greater than 0
        lt=10,      # less than 10
        default=5,  # default value=5.0
        description="A decimal value is representing the cgpa of the  student"
    )


# new_student={"name":"Shravan","email":"abc"} ===> # Error:-value is not a valid email address: An email address must have an @-sign. 
# new_student={"name":"Shravan","email":"abc@gmail.com"} ==> name='Shravan' age=None email='abc@gmail.com' cgpa=5
# new_student={"name":"SKP","age":22,"email":"abc@gmail.com","cgpa":12}
#   Error:- cgpa Input should be less than 10 [type=less_than, input_value=12, input_type=int]


new_student={"name":"Shravan Kumar Pandey","age":22,"email":"shravankumarpandey825412@gmail.com","cgpa":8.4}
student=Student(**new_student)
print(student)
print(dict(student))

student_json=student.model_dump_json()
print(student_json)