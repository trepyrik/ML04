from app.core.config import get_settings
from app.detection.yolo_detector import StubVehicleDetector
from app.tracking.bytetrack_tracker import StubTracker
from app.domain.schemas import FrameInferenceResponse


class InferenceService:
    def __init__(self) -> None:
        settings = get_settings()
        self.detector = StubVehicleDetector(
            model_path=settings.model_path,
            conf=settings.model_confidence,
            iou=settings.model_iou,
            imgsz=settings.model_image_size,
        )
        self.tracker = StubTracker()

    def infer_frame(self, frame, frame_index: int = 0) -> FrameInferenceResponse:
        detections = self.detector.predict(frame)
        tracked = self.tracker.update(detections)
        return FrameInferenceResponse(
            frame_index=frame_index,
            detections=detections,
            tracked_objects=tracked,
        )
