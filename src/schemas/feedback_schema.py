from datetime import datetime

from pydantic import ConfigDict, BaseModel, Field


class CreateUpdateFeedbackSchema(BaseModel):
    text: str = Field(...)
    rate: int = Field(...)
    user_id: str = Field(...)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "text": "Супер уроки!",
                "rate": 5,
                "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            }
        },
    )


class FeedbackSchema(BaseModel):
    id: int = Field(...)
    created_at: datetime = Field(...)
