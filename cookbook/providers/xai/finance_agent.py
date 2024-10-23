"""Build a Finance Agent using xAI."""

from phi.agent import Agent
from phi.model.xai import xAI
from phi.tools.yfinance import YFinanceTools

agent = Agent(
    model=xAI(id="grok-beta"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    description="You are an investment analyst that researches stocks and helps users make informed decisions.",
    instructions=["Use tables to display data."],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response("Share the TSLA stock price", stream=True)
agent.print_response("Summarize fundamentals for TSLA", stream=True)
