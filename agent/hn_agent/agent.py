import os
from google.adk.agents import Agent
from toolbox_core import ToolboxSyncClient

# Uses local toolbox when testing, Cloud Run URL in production
MCP_URL = os.environ.get("MCP_SERVER_URL", "http://127.0.0.1:5000")

toolbox = ToolboxSyncClient(MCP_URL)
tools = toolbox.load_toolset("hn_toolset")

root_agent = Agent(
    name="hn_trend_agent",
    model="gemini-2.5-flash",
    description=(
        "A tech trend intelligence agent that tells you what the "
        "global developer community is talking about right now, "
        "using live Hacker News data from BigQuery."
    ),
    instruction=(
        "You are a tech trend analyst. When a user asks about "
        "what is trending, popular, or being discussed in tech, "
        "always use the get_trending_tech_stories tool first to "
        "fetch live data from BigQuery before answering. "
        "Present results clearly: story title, score, date, and URL. "
        "After the list, write 2-3 sentences explaining what these "
        "results reveal about the current trend. "
        "Never answer from memory — always fetch data first."
    ),
    tools=tools,
)
