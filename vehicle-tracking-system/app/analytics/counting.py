from typing import List
from app.domain.schemas import CountEvent, TrackedObject


def count_line_crossings(tracks: List[TrackedObject], line_y: float, frame_index: int) -> List[CountEvent]:
    events: List[CountEvent] = []
    for track in tracks:
        center_y = (track.y1 + track.y2) / 2.0
        if center_y >= line_y:
            events.append(CountEvent(track_id=track.track_id, frame_index=frame_index, direction="down"))
    return events
