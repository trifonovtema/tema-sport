from core.base.base_manager import BaseManager
from core.base.base_repo import BaseRepository
from core.base.base_service import BaseService
from core.base.create_dependencies_factory import create_dependency_factory
from core.models import CourseElement
from core.schemas.course_element import (
    CreateCourseElement,
    UpdateCourseElement,
    ReadCourseElement,
    FilterCourseElement,
)


class CourseElementRepository(
    BaseRepository[
        CourseElement, CreateCourseElement, UpdateCourseElement, FilterCourseElement
    ]
):
    pass


class CourseElementManager(
    BaseManager[CourseElementRepository, ReadCourseElement, FilterCourseElement]
):
    pass


class CourseElementService(
    BaseService[CourseElementManager, ReadCourseElement, FilterCourseElement]
):
    pass


get_course_element_repo, get_course_element_manager, get_course_element_service = (
    create_dependency_factory(
        repo_class=CourseElementRepository,
        manager_class=CourseElementManager,
        service_class=CourseElementService,
        model=CourseElement,
        create_schema=CreateCourseElement,
        update_schema=UpdateCourseElement,
        read_schema=ReadCourseElement,
        filter_schema=FilterCourseElement,
    )
)
