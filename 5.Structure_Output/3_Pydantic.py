from pydantic import BaseModel
from typing import Optional

class student(BaseModel):    
    #name:str
    name:str="ABC"  # By default it has ABC Value

new_student={"name":"Shravan Kumar Pandey"}  # name='Shravan Kumar Pandey'
# new_student={"name":22} ====> Error :- Input should be a valid string
#new_student={}  # name='ABC'
student=student(**new_student)
print(student) # name='Shravan Kumar Pandey'
print(student.name) # Shravan Kumar Pandey
print("===="*10)
# =============================================================================================================

class Student(BaseModel):
    name:str="Nitish"
    # age:Optional[int]=20  # name='Shravan' age=20
    age:Optional[int]=None  # name='Shravan' age=None


# new_student={"name":"Shravan","age":22} #name='Shravan' age=22
# new_student={"name":"Shravan"} # name='Shravan' age=None
new_student={"name":"Shravan","age":"22"} #type casting ==> name='Shravan' age=22
student=Student(**new_student) 
print(student)