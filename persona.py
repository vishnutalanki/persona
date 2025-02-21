from pydantic import BaseModel

class Persona(BaseModel):
    name: str 
    ethnicity: str
    location: str
    age: int
    education: str
    university: str
    occupaton: str
    interests: str
    height: str
    weight: str
    location_preferences: str