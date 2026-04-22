from fastapi import APIRouter
import numpy as np
from app.services.inference_service import InferenceService

router = APIRouter(prefix="/tracks", tags=["tracks"])
service = InferenceService()


@router.get("/demo-frame")
def demo_frame_inference():
    frame = np.zeros((720, 1280, 3), dtype=np.uint8)
    return service.infer_frame(frame=frame, frame_index=0)
