from fastapi import FastAPI
from app.shared.dtos.user.create_user_dto import CreateUserDto

from app.usecases.user.create_user import CreateUser

app = FastAPI()

@app.post("/user")
async def root(body: CreateUserDto):
    return CreateUser().handle(body)
