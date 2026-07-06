# African Startup Tracker

African Startup Tracker is a simple full-stack project for tracking startup funding across African markets. It includes:

- Spring Boot backend API with JPA data access
- In-memory H2 database for local development (PostgreSQL supported)
- Responsive frontend dashboard with chart visualizations
- Python ingestion script for importing startup deals

## What it does

- Displays startup names, country, sector, and funding amounts
- Renders investment distribution by country and sector
- Seeds sample startup data automatically on startup
- Supports developer-friendly local setup with H2 and optional PostgreSQL

## Backend setup

1. Open a terminal and navigate to `backend`
2. Run the application:
   - Windows: `./mvnw.cmd spring-boot:run`
   - macOS/Linux: `./mvnw spring-boot:run`
3. The API will be available at `http://localhost:8080/startups`

### Optional PostgreSQL profile

To run against PostgreSQL, create a database named `startup_db` and set the correct credentials in `backend/src/main/resources/application-postgres.properties`.

Start with the profile:

```bash
./mvnw.cmd spring-boot:run -Dspring-boot.run.profiles=postgres
```

## Frontend setup

1. Open `frontend/index.html` in your browser, or serve the folder with a static file server.
2. The dashboard fetches data from the backend and displays:
   - startup table
   - funding by country chart
   - funding by sector chart
   - summary metrics and filter controls

## Ingestion script

The ingestion workflow lives in `ingestion/scraper.py`. Install its dependencies with:

```bash
python -m pip install -r ingestion/requirements.txt
```

Run the script with:

```bash
python ingestion/scraper.py --url https://example.com
```

## Notes

- By default, the backend uses an in-memory H2 database so the project works without additional setup.
- Sample startup data is inserted at startup when the database is empty.
- If you want to use PostgreSQL, enable the `postgres` Spring profile.
