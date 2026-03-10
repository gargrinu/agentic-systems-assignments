from pydantic import BaseModel, Field, EmailStr, ConfigDict

class Address(BaseModel):
    house_no : str = Field(max_length=10, description="Provide your building/flat number")
    street: str = Field(max_length=50, description="Provide your street/colony name")
    city: str = Field(min_length=3, description="Provide your city")
    zipcode: str = Field(min_length=6, max_length=6, description="Provide your zipcode")

class User(BaseModel):
    
    model_config = ConfigDict(validate_assignment=True)


    user_id : int = Field(description="Enter user id")
    name : str = Field(min_length=3, description="Enter your name")
    email: EmailStr = Field(description="Enter a valid email address", examples=['abc@gmail.com'])
    age : int = Field(ge=18, description="Enter your age")
    address : Address
    is_premium : bool = Field(default=False)

user = User(
    user_id = 101,
    name = "Rinu",
    email = "rinugarg@gmail.com",
    age = 25,
    address = Address(house_no = "C401", street = "New colony", city = "Gurgaon", zipcode = "122001"),
    is_premium = True
)

print(user)