## Backend Application for [SquerryDB](https://squerrydb-frontend-production.up.railway.app/)
Visualizing App for IMDb Series. Data downloaded from [IMDb Non-Commercial Datasets](https://developer.imdb.com/non-commercial-datasets/).
- Database: PostgreSQL
- [GraphQL API](https://squerrydb-backend-production.up.railway.app/graphql): Strawberry
- Backend: FastAPI
![image](https://github.com/user-attachments/assets/97b563f7-2bfd-4cc2-b0f8-822c312d8eb8)




### Running locally
Set the database connection via environment variables:
- `DATABASE_URL` — e.g. `postgresql://user:password@localhost:5432/squerrydb`
- `DATABASE_SSL` — `true` (default) or `false` for a local database without SSL

```
pip install -r requirements.txt
DATABASE_URL=... DATABASE_SSL=false uvicorn main:app --reload
```
