from pydantic import BaseModel, Field, EmailStr, ConfigDict
from typing import Optional

class Address(BaseModel):
    house_no : str = Field(max_length=10, description="Provide your building/flat number")
    street: str = Field(max_length=50, description="Provide your street/colony name")
    city: str = Field(min_length=3, description="Provide your city")
    zipcode: str = Field(pattern=r'^\d{6}$', description="Provide your zipcode")

# r'^\d{6}$' => Regex pattern to validate that the zipcode consists of exactly 6 digits.
# - ^ asserts the start of the string
# - \d matches any digit (0-9)
# - {6} specifies that exactly 6 digits should be present
# - $ asserts the end of the string

# For alphanumeric => r'^[a-zA-Z0-9]{6}$' => This regex pattern ensures that the input consists of only letters (both uppercase and lowercase) and digits, with no spaces or special characters.

class User(BaseModel):
    
    model_config = ConfigDict(validate_assignment=True)

# ConfigDict(validate_assignment=True) => This configuration option allows you to enable validation of field values when they are assigned after the model instance has been created. By default, Pydantic only validates field values during model initialization (i.e., when you create an instance of the model). With validate_assignment=True, any time you assign a new value to a field, Pydantic will automatically validate that value against the field's defined constraints and types. If the new value does not meet the validation criteria, Pydantic will raise a ValidationError.

    user_id : int = Field(description="Enter user id")
    name : str = Field(min_length=3, description="Enter your name")
    email: EmailStr = Field(description="Enter a valid email address", examples=['abc@gmail.com'])
    age : int = Field(ge=18, description="Enter your age")
    address : Address
    is_premium : Optional[bool] = False

# Optional[bool] => This indicates that the is_premium field can either be of type bool or it can be None. In other words, the field is not required to have a value, and if it is not provided, it will default to None. However, in this case, since we have set a default value of False, if the field is not provided during model initialization, it will automatically be assigned the value False instead of None.

user = User(
    user_id = 101,
    name = "Rinu",
    email = "rinugarg@gmail.com",
    age = 25,
    address = Address(house_no = "C401", street = "New colony", city = "Gurgaon", zipcode = "122001")
)

print(user)