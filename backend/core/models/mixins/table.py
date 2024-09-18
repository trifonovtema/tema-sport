from sqlalchemy.orm import declared_attr
from utils.snake_converter import camel_case_to_snake_case


class TableNameMixin:
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{camel_case_to_snake_case(cls.__name__)}s"
