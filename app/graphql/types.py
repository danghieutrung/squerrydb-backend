import strawberry
from typing import Optional, List
from app.models import Series, Episode

@strawberry.type
class SeriesType:
    tconst: str
    titletype: Optional[str] = None
    primarytitle: Optional[str] = None
    originaltitle: Optional[str] = None
    isadult: Optional[bool] = None
    startyear: Optional[int] = None
    endyear: Optional[int] = None
    runtimeminutes: Optional[int] = None
    genres: Optional[str] = None
    averagerating: float
    numvotes: int
    episodes: Optional[List["EpisodeType"]] = None

@strawberry.type
class EpisodeType:
    tconst: str
    parenttconst: str
    seasonnumber: int
    episodenumber: int
    titletype: Optional[str] = None
    primarytitle: Optional[str] = None
    originaltitle: Optional[str] = None
    isadult: Optional[bool] = None
    startyear: Optional[int] = None
    endyear: Optional[int] = None
    runtimeminutes: Optional[int] = None
    genres: Optional[str] = None
    averagerating: float
    numvotes: int