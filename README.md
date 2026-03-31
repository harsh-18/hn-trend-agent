# Hacker News Tech Trend Intelligence Agent

An AI-powered tech trend analyst built with Google ADK and MCP Toolbox.
Queries live Hacker News data from BigQuery to answer questions about
what the global developer community is discussing right now.

## What It Does
Ask: "What is trending in AI right now?"
Agent calls MCP tool → BigQuery query runs → Gemini formats response
Returns real story titles, scores, URLs and trend analysis

## Architecture
User → ADK Agent (Cloud Run) → MCP Toolbox (Cloud Run) → BigQuery

## Criteria Met
- ADK agent with Gemini 2.5 Flash via Vertex AI
- ONE MCP tool: get_trending_tech_stories
- ONE data source: bigquery-public-data.hacker_news.full
- Retrieved data used directly in final response

## Tech Stack
- Google ADK 1.28.0
- MCP Toolbox for Databases
- BigQuery Public Dataset: hacker_news.full
- Google Cloud Run (2 services)
- Gemini 2.5 Flash via Vertex AI
- Python 3.11

      "parts": [{"text": "What is trending in AI right now?"}]
    }
  }'
