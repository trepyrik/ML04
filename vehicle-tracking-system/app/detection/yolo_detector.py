from typing import List
import numpy as np
from app.detection.detector import BaseDetector
from app.domain.schemas import Detection


class StubVehicleDetector(BaseDetector):
    """
    Заглушка. Здесь потом можно подключить Ultralytics YOLO.
    """

    def __init__(self, model_path: str, conf: float = 0.25, iou: float = 0.45, imgsz: int = 640):
        self.model_path = model_path
        self.conf = conf
        self.iou = iou
        self.imgsz = imgsz

    def predict(self, frame: np.ndarray) -> List[Detection]:
        if frame is None or frame.size == 0:
            return []

        height, width = frame.shape[:2]
        # Демонстрационная фиктивная детекция по центру кадра.
        return [
            Detection(
                x1=width * 0.35,
                y1=height * 0.35,
                x2=width * 0.65,
                y2=height * 0.75,
                confidence=0.90,
                class_id=0,
                class_name="vehicle",
            )
        ]
