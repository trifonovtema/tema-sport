from datetime import datetime, timezone
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import func, TIMESTAMP


class CreatedAtMixin:

    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        default=lambda: datetime.now(timezone.utc),
    )
