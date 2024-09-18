from typing import Optional

from core.config import settings
from core.models.base import Base
from core.models.user import User
from sqlalchemy.orm import Mapped, mapped_column, relationship


class UserProfile(Base):

    user_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = mapped_column(
        nullable=True
    )

    user: Mapped["User"] = relationship("User", back_populates="user_profiles")
