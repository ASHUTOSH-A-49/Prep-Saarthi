from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
<<<<<<< HEAD
from app.models.common import PyObjectId

class SRSRecordSchema(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    user_id: str
    reference_id: str = Field(..., description="Can be a Topic Name or a specific Question ID")
    record_type: str = Field(default="topic", description="'topic' or 'question'")
    
    # SM-2 Algorithm Variables
    repetition_count: int = 0
    interval: int = 0  # Interval in days
    ease_factor: float = 2.5  # Standard SM-2 starting ease
    
    last_reviewed_date: Optional[datetime] = None
=======

class SRSRecordSchema(BaseModel):
    user_id: str
    topic: str
    ease_factor: float = 2.5
    interval: int = 0
>>>>>>> 54e60b608fdf90d033ad8adf13a3597d63cc4b10
    next_review_date: datetime = Field(default_factory=datetime.utcnow)
