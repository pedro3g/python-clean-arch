from app.shared.dtos.user.create_user_dto import CreateUserDto
from domain.entities.user import User
from domain.mappers.user.create_user_mapper import CreateUserMapper


class CreateUser:
    def __init__(self):
        self.create_user_mapper = CreateUserMapper()

    def handle(self, user: CreateUserDto) -> User:
        user = self.create_user_mapper.mapFrom(user)
        del user.password

        return user
