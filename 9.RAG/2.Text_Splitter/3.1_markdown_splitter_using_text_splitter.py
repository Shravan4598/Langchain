from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

text = """
# Project Name: Smart Student Tracker

A simple Python-based project to manage and track student data, including their grades, age, and academic status.


## Features

- Add new students with relevant info
- View student details
- Check if a student is passing
- Easily extendable class-based design


## 🛠 Tech Stack

- Python 3.10+
- No external dependencies


## Getting Started

1. Clone the repo  
   ```bash
   git clone https://github.com/your-username/student-tracker.git

"""

splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=300,
    chunk_overlap=0
)

result=splitter.split_text(text)
print(result)
print("==="*25)
for i in range(3):
    print(result[i])
    print("==="*25)


#output
"""
['# Project Name: Smart Student Tracker\n\nA simple Python-based project to manage and track student data, including their grades, age, and academic status.', '## Features\n\n- Add new students with relevant info\n- View student details\n- Check if a student is passing\n- Easily extendable class-based design\n\n\n## 🛠 Tech Stack\n\n- Python 3.10+\n- No external dependencies', '## Getting Started\n\n1. Clone the repo  \n   ```bash\n   git clone https://github.com/your-username/student-tracker.git']
===========================================================================
# Project Name: Smart Student Tracker

A simple Python-based project to manage and track student data, including their grades, age, and academic status.
===========================================================================
## Features

- Add new students with relevant info
- View student details
- Check if a student is passing
- Easily extendable class-based design


## 🛠 Tech Stack

- Python 3.10+
- No external dependencies
===========================================================================
## Getting Started

1. Clone the repo  
   ```bash
   git clone https://github.com/your-username/student-tracker.git
===========================================================================
"""