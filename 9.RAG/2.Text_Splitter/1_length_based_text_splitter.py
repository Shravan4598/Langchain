from langchain_text_splitters import CharacterTextSplitter

text="""
Space exploration is the physical investigation of outer space by uncrewed robotic space probes and through human spaceflight.
While the observation of objects in space, known as astronomy, predates reliable recorded history, it was the development of large and relatively efficient rockets during the mid-twentieth century that allowed physical space exploration to become a reality. Common rationales for exploring space include advancing scientific research, national prestige, uniting different nations, ensuring the future survival of humanity, and developing military and strategic advantages against other countries.
"""


splitter=CharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=0,
    separator=""
)
result=splitter.split_text(text)

print(result)
