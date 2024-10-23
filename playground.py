from phi.agent import Agent 
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from phi.playground import Playground, serve_playground_app

# Tạo agent
web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=OpenAIChat(
        api_key="your-openai-api-key-here"  # Thêm API key trực tiếp
    ),
    tools=[DuckDuckGo()],
    markdown=True,
)

# Tạo playground app
app = Playground(agents=[web_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)
