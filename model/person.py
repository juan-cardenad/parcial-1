from pydantic import BaseModel
from model.location import Location
from model.typedoc import Typedoc

class Person(BaseModel):
    id: str
    name: str
    lastname: str
    age: int
    typedoc: Typedoc
    gender: str
    location: Location
