"""Пример запуска инференса на видео. Пока это каркас."""

import cv2
from app.services.inference_service import InferenceService


def main(video_path: str) -> None:
    cap = cv2.VideoCapture(video_path)
    service = InferenceService()
    frame_index = 0

    while True:
        ok, frame = cap.read()
        if not ok:
            break

        result = service.infer_frame(frame, frame_index)
        print(result.model_dump())
        frame_index += 1

    cap.release()


if __name__ == "__main__":
    main("data/samples/demo.mp4")
