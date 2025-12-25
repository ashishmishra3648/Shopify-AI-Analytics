# Shopify AI Analytics App - Implementation Plan

## Objective
Build a mini AI-powered analytics application that connects to a Shopify store, reads data, and answers natural language questions using a Rails API and a Python AI service.

## Architecture
The system consists of two main components:
1.  **Rails API (Backend Gateway)**: Handles client requests, authentication, and routing to the AI service.
2.  **Python AI Service**: specific service for NLP processing, converting questions to ShopifyQL, and executing queries.

## Tech Stack
-   **Backend**: Ruby on Rails (API mode)
-   **AI Service**: Python (FastAPI + LangChain/LlamaIndex)
-   **Database**: SQLite/PostgreSQL (default Rails)
-   **Shopify Integration**: `shopify_api` gem (Ruby) or REST/GraphQL in Python?
    -   Requirement says: "Python AI Service... queries Shopify". So Python will handle the actual data fetching for analytics. Rails handles Auth?
    -   Requirements: "Connect to a Shopify Store... Authenticate with Shopify using OAuth" -> This is usually done in Rails.
    -   "Rails API... Forward requests to a Python AI service... Accepts: user questions, store context".
    -   "Python AI Service... queries Shopify".
    -   *Decision*: Rails handles the OAuth flow to get the Access Token. Rails passes the Question + Access Token to Python. Python uses the token to query Shopify.

## Step-by-Step Plan

### Phase 1: Setup & Scaffolding
- [ ] Create project directory `shopify-ai-analytics`.
- [ ] Initialize Python service directory `python_service`.
- [ ] Initialize Rails app directory `rails_app`. (Note: User environment lacks Ruby, files will be created manually).

### Phase 2: Python AI Service (FastAPI)
- [ ] Create `requirements.txt` (FastAPI, uvicorn, langchain, shopify-python-api?).
- [ ] Create `main.py` entry point.
- [ ] Implement `ShopifyQLGenerator` class.
- [ ] Implement `QueryExecutor` class.
- [ ] Create endpoint `/analyze` that accepts `{ question, shop_url, access_token }`.

### Phase 3: Rails API Gateway
- [ ] Create `Gemfile` (rails, shopify_app, httparty/faraday).
- [ ] Create `config/routes.rb`.
- [ ] Create `QueriesController`.
- [ ] Implement `POST /api/v1/queries` endpoint.
- [ ] Mock/Implement Shopify OAuth flow (Skeleton code since we can't run it).

### Phase 4: Integration
- [ ] Ensure Rails can talk to Python service (HTTP request).
- [ ] Define JSON contract between Rails and Python.

### Phase 5: Documentation
- [ ] Create `README.md` with setup instructions and architecture diagram description.
