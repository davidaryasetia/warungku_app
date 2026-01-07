from fastapi import FastAPI

app = FastAPI()

def greet():
    return "Test API"