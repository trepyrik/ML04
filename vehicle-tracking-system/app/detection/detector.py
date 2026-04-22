from abc import ABC, abstractmethod
from typing import List
import numpy as np
from app.domain.schemas import Detection


class BaseDetector(ABC):
    @abstractmethod
    def predict(self, frame: np.ndarray) -> List[Detection]:
        raise NotImplementedError
