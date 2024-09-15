from base_api.api.v1.course_elements.dependency import (
    CourseElementService,
    get_course_element_service,
)
from core.base.crud_router_factory import create_crud_router_factory
from core.schemas.course_element import (
    CreateCourseElement,
    UpdateCourseElement,
    FilterCourseElement,
)
from core.config import settings


router = create_crud_router_factory(
    service_class=CourseElementService,
    create_schema=CreateCourseElement,
    update_schema=UpdateCourseElement,
    filter_schema=FilterCourseElement,
    service_dependency=get_course_element_service,
    id_type=settings.db.id_type_class.get_id_type(),
    prefix=settings.api.v1.course_elements,
    tags=["CourseElements"],
)
