from typing import List
from app.domain.schemas import Detection, TrackedObject
from app.tracking.tracker import BaseTracker


class StubTracker(BaseTracker):
    """
    Простая заглушка. Каждой детекции назначает track_id.
    Потом заменишь на ByteTrack / DeepSORT.
    """

    def __init__(self) -> None:
        self._next_id = 1

    def update(self, detections: List[Detection]) -> List[TrackedObject]:
        tracked = []
        for det in detections:
            tracked.append(
                TrackedObject(
                    track_id=self._next_id,
                    x1=det.x1,
                    y1=det.y1,
                    x2=det.x2,
                    y2=det.y2,
                    confidence=det.confidence,
                    class_id=det.class_id,
                    class_name=det.class_name,
                )
            )
            self._next_id += 1
        return tracked
