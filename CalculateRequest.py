from pydantic import BaseModel


class CalculateRequest(BaseModel):
    a: int
    b: int
    operation: str
