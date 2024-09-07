from typing import TypeVar
from pydantic import BaseModel
from core.config import settings
from core.models import Base

# Type variables for the model and repository
ModelType = TypeVar("ModelType", bound=Base)
# Type variables for create and update schemas
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
ReadSchemaType = TypeVar("ReadSchemaType", bound=BaseModel)
FilterSchemaType = TypeVar("FilterSchemaType", bound=BaseModel)
