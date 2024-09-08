from typing import TypeVar
from pydantic import BaseModel
from core.models import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
ReadSchemaType = TypeVar("ReadSchemaType", bound=BaseModel)
FilterSchemaType = TypeVar("FilterSchemaType", bound=BaseModel)
