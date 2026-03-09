from pydantic import BaseModel, Field, EmailStr, field_validator, model_validator

class UserRegister(BaseModel):
    username : str = Field(min_length=5)
    email : EmailStr
    age : int = Field(ge=18)

@field_validator('username')
@classmethod
def username_validator(cls, value):
    if len(value) < 5:
        raise ValueError("Username too short.")
    
    return value

@field_validator('email')
@classmethod
def email_to_lowercase(cls, value: str) -> str:
    return value.lower()

@field_validator('age', mode='after')
@classmethod
def validate_age(cls, value):
    if value < 18:
        raise ValueError("Invalid age provided.")
    
    return value

user_info = {'username' : 'Rinu', 'email' : 'rinugarg', 'age' : 10}

user1 = UserRegister(**user_info)

print(user1)
