from abc import ABC, abstractmethod
from typing import List
from app.domain.schemas import Detection, TrackedObject


class BaseTracker(ABC):
    @abstractmethod
    def update(self, detections: List[Detection]) -> List[TrackedObject]:
        raise NotImplementedError
