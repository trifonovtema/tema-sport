from pydantic import BaseModel


class APIResponse(BaseModel):
    trace_id: str
    status: str
    message: str
