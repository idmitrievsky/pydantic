from uuid import UUID
from typing import Union
from pydantic import BaseModel


class User(BaseModel):
    id: Union[int, str, UUID]
    name: str


user_01 = User(id=123, name='John Doe')
print(user_01)
#> User id=123 name='John Doe'
print(user_01.id)
#> 123

user_02 = User(id='1234', name='John Doe')
print(user_02)
#> User id=1234 name='John Doe'
print(user_02.id)
#> 1234

user_03_uuid = UUID('cf57432e-809e-4353-adbd-9d5c0d733868')
user_03 = User(id=user_03_uuid, name='John Doe')
print(user_03)
#> User id=275603287559914445491632874575877060712 name='John Doe'
print(user_03.id)
#> 275603287559914445491632874575877060712
print(user_03_uuid.int)
#> 275603287559914445491632874575877060712
