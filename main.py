from fastapi import FastAPI

from CalculateRequest import CalculateRequest

app = FastAPI()


@app.post("/calculate")
async def calculate(request: CalculateRequest):
    match request.operation:
        case "+":
            return request.a + request.b
        case "-":
            return request.a - request.b
        case "*":
            return request.a * request.b
        case "/":
            return request.a / request.b
        case _:
            return "Invalid operation"
