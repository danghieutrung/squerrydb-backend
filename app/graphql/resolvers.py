from app.graphql.types import EpisodeType, SeriesType
from app.models import Episode, Series
from strawberry.types import Info
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional

async def get_ratings(info: Info, tconst: str) -> Optional[SeriesType]:
    session: AsyncSession = info.context["db"]

    result = await session.execute(select(Series).where(Series.tconst == tconst))
    series = result.scalars().first()

    if not series:
        return None

    episodes_result = await session.execute(
        select(Episode).where(Episode.parenttconst == tconst).order_by(Episode.seasonnumber, Episode.episodenumber)
    )

    episodes = [
        EpisodeType(
            tconst=ep.tconst,
            parenttconst=ep.parenttconst,
            seasonnumber=ep.seasonnumber,
            episodenumber=ep.episodenumber,
            titletype=ep.titletype,
            primarytitle=ep.primarytitle,
            originaltitle=ep.originaltitle,
            isadult=ep.isadult,
            startyear=ep.startyear,
            endyear=ep.endyear,
            runtimeminutes=ep.runtimeminutes,
            genres=ep.genres,
            averagerating=ep.averagerating,
            numvotes=ep.numvotes
        )
        for ep in episodes_result.scalars().all()
    ]
    
    return SeriesType(
        tconst=series.tconst,
        titletype=series.titletype,
        primarytitle=series.primarytitle,
        originaltitle=series.originaltitle,
        isadult=series.isadult,
        startyear=series.startyear,
        endyear=series.endyear,
        runtimeminutes=series.runtimeminutes,
        genres=series.genres,
        averagerating=series.averagerating,
        numvotes=series.numvotes,
        episodes=episodes
    )

async def search_series(info: Info, name: str) -> List[SeriesType]:
    session: AsyncSession = info.context["db"]

    result = await session.execute(
        select(Series)
        .where(Series.primarytitle.ilike(f"%{name}%"))
        .order_by(Series.numvotes.desc().nullslast())
        # .limit(20)
    )

    series_list = result.scalars().all()

    return [
        SeriesType(
            tconst=series.tconst,
            primarytitle=series.primarytitle,
            startyear=series.startyear,
            endyear=series.endyear,
            averagerating=series.averagerating,
            numvotes=series.numvotes
        )
        for series in series_list
    ]
