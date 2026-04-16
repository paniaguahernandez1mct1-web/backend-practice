from pydantic import BaseModel

class Tarea(BaseModel):
    titulo: str
    completada: bool = False

