from fastapi import APIRouter

router = APIRouter(prefix="/reports", tags=["reports"])


@router.get("/summary")
def get_summary():
    return {
        "message": "summary endpoint stub",
        "next_step": "connect PostgreSQL and aggregate events/tracks",
    }
