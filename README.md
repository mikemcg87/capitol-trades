# Capitol Trades

A document intelligence platform for tracking congressional stock trading disclosures. Built with Python, FastAPI, and Docling.

## Overview

Capitol Trades automatically ingests, parses, and tracks stock trades made by members of Congress using public disclosure documents. The platform is designed to be extensible for other document intelligence use cases.

## Features

- **Automated Ingestion**: Scrapes Senate and House financial disclosure sites
- **Document Processing**: Uses Docling to extract structured data from PDFs
- **Historical Data**: Backfill capability for high-profile politicians
- **REST API**: Query trades by politician, ticker, date, or amount
- **Real-time Alerts**: Webhook notifications for new trades

## Tech Stack

- **Backend**: Python 3.11+, FastAPI, Pydantic v2
- **Document Processing**: Docling
- **Database**: PostgreSQL with SQLAlchemy
- **Queue**: Redis + Celery
- **Web Scraping**: Bright Data API
- **Frontend**: React (coming soon)

## Project Structure

```
capitol-trades/
├── backend/           # Python backend
│   ├── app/
│   │   ├── api/       # FastAPI routes
│   │   ├── core/      # Config, database, deps
│   │   ├── models/    # SQLAlchemy models
│   │   ├── services/  # Business logic
│   │   └── workers/   # Celery tasks
│   ├── tests/
│   └── alembic/       # Database migrations
├── frontend/          # React frontend (TBD)
├── docs/              # Documentation
├── scripts/           # Utility scripts
└── data/              # Local data storage
    ├── raw/           # Raw documents
    └── processed/     # Processed data
```

## Getting Started

(Coming soon)

## Roadmap

### Phase 1: MVP
- [ ] Senate disclosure ingestion
- [ ] Docling integration for PDF parsing
- [ ] Basic data model (politicians, transactions, assets)
- [ ] REST API endpoints
- [ ] Simple web interface

### Phase 2: Enhancement
- [ ] House disclosure support
- [ ] Historical data backfill
- [ ] Alert system
- [ ] Enhanced filtering and search

### Phase 3: Platform
- [ ] Abstract document processing framework
- [ ] Add SEC Form 4 support
- [ ] Multi-source correlation
- [ ] Advanced analytics

## License

MIT

## Contributing

This is a portfolio project, but feedback and suggestions are welcome!
