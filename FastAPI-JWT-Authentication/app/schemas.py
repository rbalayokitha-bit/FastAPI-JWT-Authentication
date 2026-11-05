from pydantic import BaseModel, EmailStr, Field, ConfigDict


# User Registration
class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=6)


# User Login
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# User Response
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)


# User Update
class UserUpdate(BaseModel):
    username: str = Field(min_length=3, max_length=50)