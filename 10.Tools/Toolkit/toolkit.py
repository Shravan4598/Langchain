from langchain_community.tools import tool

@tool
def multiply(a:int,b:int)->int:
    """Multiply two number"""
    return a*b

@tool
def add(a:int,b:int)->int:
    """Add two number"""
    return a+b

class MathToolKit:
    def get_tools(self):
        return [add,multiply]
    
toolkit=MathToolKit()
tools=toolkit.get_tools()

for tool in tools:
    print(tool.name,"=>",tool.description)


"""
add => Add two number
multiply => Multiply two number
"""
result=tools[0].invoke({"a":3,"b":5}) #addition
print(result) #8

result=tools[1].invoke({"a":3,"b":5}) #multiplication
print(result) #15
