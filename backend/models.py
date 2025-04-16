from pydantic import BaseModel

<<<<<<< HEAD
class Item():
    name: int
=======
class Item(BaseModel):
    name: str
>>>>>>> d78737ca44aebbb43c528f6425ce1b3c85a49559
    description: str

class User(BaseModel):
    username: str
    bio: str
    
    # You can raise your hands and give the answer to the chocolate question