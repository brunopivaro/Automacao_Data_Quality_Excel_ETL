from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt, validator
from datetime import datetime
from enum import Enum

class CategoriaEnum(str, Enum):
    categoria1 = "categoria1"
    categoria2 = "categoria2"
    categoria3 = "categoria3"


class Vendas(BaseModel):

    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    categoria: CategoriaEnum

    @validator('categoria')
    def categoria_deve_estar_no_enum(cls, error):
        return error