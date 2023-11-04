from fastapi import APIRouter

from realfans_api.data.database import MyDatabase
from realfans_api.data.models import LeaderboardType

router = APIRouter()


@router.get("/getLeaderBoards")
async def get_leaderboards(leaderboard_type: LeaderboardType):
    ...


@router.get("/getLandingPageStats")
async def get_landingpage_stats():
    ...
