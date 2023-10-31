from pydantic import BaseModel

class Community(BaseModel):
    id:int
    value:str
    department_id:int
