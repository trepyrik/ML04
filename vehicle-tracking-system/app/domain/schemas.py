from pydantic import BaseModel, Field
from typing import List, Optional


class Detection(BaseModel):
    x1: float
    y1: float
    x2: float
    y2: float
    confidence: float = Field(ge=0.0, le=1.0)
    class_id: int = 0
    class_name: str = "vehicle"


class TrackedObject(Detection):
    track_id: int


class FrameInferenceResponse(BaseModel):
    frame_index: int
    detections: List[Detection]
    tracked_objects: List[TrackedObject]


class HealthResponse(BaseModel):
    status: str
    app_name: str
    environment: str


class JobCreateResponse(BaseModel):
    job_id: str
    status: str
    message: str


class CountEvent(BaseModel):
    track_id: int
    frame_index: int
    direction: Optional[str] = None
