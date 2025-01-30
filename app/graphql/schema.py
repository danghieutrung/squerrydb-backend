import strawberry
from typing import List, Optional
from app.graphql.resolvers import get_ratings, search_series
from app.graphql.types import SeriesType

@strawberry.type
class Query:
    get_ratings: Optional[SeriesType] = strawberry.field(resolver=get_ratings)
    search_series: List[SeriesType] = strawberry.field(resolver=search_series)

schema = strawberry.Schema(query=Query)
