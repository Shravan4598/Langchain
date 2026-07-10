from typing import TypedDict

class Person(TypedDict):
    name:str
    age:int

valid_person:Person={"name":"Shravan Kumar Pandey","age":22}
print(valid_person)

invalid_name1:Person={"name":"Pandey Ji","age":"22"}
print(invalid_name1)

invalid_name2:Person={"name":"Pandey Ji","age":"twenty_two"}
print(invalid_name2)
