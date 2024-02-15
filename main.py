from fastapi import FastAPI

app = FastAPI()


@app.post("/sumar")
async def root():
    return {"message": "Hello World"}


@app.post("/restar")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
