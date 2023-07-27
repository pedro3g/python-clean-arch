from app.shared.dtos.user.create_user_dto import CreateUserDto
from domain.entities.user import User


class CreateUserMapper:
    def mapFrom(self, user: CreateUserDto) -> User:
        return User(None, user.name, user.email, user.password)

    def mapTo(self, user: User) -> CreateUserDto:
        return CreateUserDto(user.name, user.email, user.password)
