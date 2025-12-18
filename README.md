# AI Generation Service

A modular, Clean Architecture-based Python service built with **FastAPI**. This application provides a unified interface for generating text content using various LLM providers (e.g., OpenAI, Mock) via a flexible provider factory pattern.

## 🚀 Tech Stack

- **Language:** Python 3.13+
- **Framework:** FastAPI
- **Package Manager:** [uv](https://github.com/astral-sh/uv) (Fast Python package installer)
- **Architecture:** Hexagonal / Clean Architecture
- **Testing:** Pytest & HTTPX
- **Linting & Typing:** Ruff & Mypy
- **Hooks:** Pre-commit
- **Containerization:** Docker

## 📂 Project Structure

```text
├── app/
│   ├── domain/           # Core logic, interfaces & schemas (No external deps)
│   ├── application/      # Use cases & service layer
│   ├── infrastructure/   # External implementations (OpenAI, Mock, etc.)
│   ├── presentation/     # API Routers & Endpoints
│   ├── main.py           # App entrypoint & wiring
│   └── dependencies.py   # Dependency injection setup
├── tests/                # Pytest suite
├── pyproject.toml        # Configuration for tools (uv, pytest, ruff, mypy)
├── .pre-commit-config.yaml
├── Dockerfile            # Production Docker image build
└── docker-compose.yml    # Production container orchestration
```

## 🛠️ Setup & Installation

This project uses `uv` for ultra-fast dependency management.

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/andrii-hantkovskyi/llm-service.git
    cd llm-service
    ```

2.  **Install dependencies:**

    ```bash
    uv sync
    ```

3.  **Install pre-commit hooks:**
    This ensures linting and type checking run before every commit.
    ```bash
    uv run pre-commit install
    ```

## 🏃‍♂️ Running the Application

### 1. Local Development (Hot Reloading)

Use this mode for active development. Changes to code will automatically restart the server.

```bash
uv run fastapi dev app/main.py
```

- **Docs:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **API:** [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 2. Docker Production (Stable)

Use this mode to simulate the production environment. It uses a stripped-down, optimized Docker image without dev dependencies or hot reloading.

```bash
docker compose up --build
```

The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## 🧪 Testing

Run the test suite using `pytest`. This includes async tests for the API and unit tests for the factory logic.

```bash
uv run pytest
```

## ✅ Code Quality

We enforce strict typing and linting rules. You can run checks manually without committing:

**Run everything (Lint, Format Check, Mypy):**

```bash
uv run pre-commit run --all-files
```

**Run individual tools:**

```bash
# Type Checking
uv run mypy .

# Linting
uv run ruff check .

# Formatting
uv run ruff format .
```

## 🔌 API Usage Example

**Endpoint:** `POST /generate`

**Request:**

```json
{
  "provider": "mock",
  "prompt": "Write a post about Python 3.13"
}
```

**Response:**

```json
{
  "provider": "mock",
  "content": "Mock response for: Write a post about Python 3.13"
}
```
