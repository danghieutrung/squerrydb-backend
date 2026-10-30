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
- `DATABASE_ECHO` — `true` to log every SQL statement (default `false`)

```
pip install -r requirements.txt
DATABASE_URL=... DATABASE_SSL=false uvicorn main:app --reload
```

### Deploying on Railway
1. Create a project with a PostgreSQL service, then load the data from a local dump:
   ```
   pg_dump "$LOCAL_DATABASE_URL" --no-owner --no-acl -f squerrydb.sql
   psql "$RAILWAY_DATABASE_PUBLIC_URL" -f squerrydb.sql
   ```
2. Add this repo as a service and set `DATABASE_URL=${{Postgres.DATABASE_URL}}`. Railway starts it with the `Procfile`.
3. Generate a domain under Settings → Networking; the API is served at `/graphql`.
