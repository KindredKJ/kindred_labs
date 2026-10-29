# Kindred Labs — Founder, Public Evidence and Press

**Founder:** [Kindred Jermaine Cox (KJ / KindredKJ)](presence/FOUNDER.md)  
**Third-party company directory:** [Kindred on Crunchbase](https://www.crunchbase.com/organization/kindredlabs) (founder-confirmed historical listing; not an independent technical verification)  
**Media kit:** [Kindred Labs press resources](press/MEDIA_KIT.md)  
**Latest founder announcement — October 28, 2026:** [Independently verifiable bounded cross-provider recovery evidence](press/2026-10-28-strata-recovery-evidence.md)  
**Primary technical record:** [Strata Data Port Network PR #40](https://github.com/KindredKJ/strata-data-port-network/pull/40)

Kindred Labs works on agentic AI systems, stateful computation and governed data transport. The latest public research record reports 16/16 independent third-environment checks on **one bounded `HASH_TEXT` signed recovery artifact**. This is not evidence of automatic failover, independently confirmed anonymous endpoint access, abrupt power-loss recovery, physical attestation or production readiness.

This repository also contains a FastAPI/Vercel scaffold. **Do not confuse this scaffold with the separately published Strata recovery service or with a confirmed live Kindred Labs application.** The development notes below are retained for the original project.

---

# FastAPI Starter

Deploy your [FastAPI](https://fastapi.tiangolo.com/) project to Vercel with zero configuration.

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/fastapi&template=fastapi)

_Live Example: https://vercel-plus-fastapi.vercel.app/_

Visit the [FastAPI documentation](https://fastapi.tiangolo.com/) to learn more.

## Project Structure

This example follows the [larger applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/) pattern from the FastAPI docs:

```
app/
├── __init__.py
├── main.py              # FastAPI application entry point
├── templates/
│   └── index.html       # Landing page template
├── api/
│   ├── __init__.py
│   ├── main.py          # API router assembly
│   ├── deps.py          # Shared dependencies
│   └── routes/
│       ├── __init__.py
│       └── items.py     # Item endpoints
└── core/
    ├── __init__.py
    └── config.py        # Application settings
```

## Getting Started

Install the required dependencies using [uv](https://docs.astral.sh/uv/):

```bash
uv sync
```

## Running Locally

```bash
vercel dev
```

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/` | Landing page |
| `GET` | `/api/v1/items/` | List sample items |
| `GET` | `/api/v1/items/{item_id}` | Get item by ID |
| `GET` | `/docs` | Interactive API docs (Swagger UI) |

## Deploying to Vercel

Deploy your project to Vercel with the following command:

```bash
npm install -g vercel
vercel --prod
```

Or `git push` to your repository with our [git integration](https://vercel.com/docs/deployments/git).

To view the source code for this template, [visit the example repository](https://github.com/vercel/vercel/tree/main/examples/fastapi).
