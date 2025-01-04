from langchain_community.agent_toolkits.load_tools import load_tools  # Updated import
from smolagents import Tool, CodeAgent, HfApiModel
import os

# Make sure you have your SERPAPI_API_KEY set
os.environ["SERPAPI_API_KEY"] = "d3ecd29879164e579a1204b1dd7c0083bfb6e8ee1e60ee6b0ce76c2f13ff22d9"  # Replace with your actual key

class SearchTool(Tool):
    name = "search"
    description = "Useful for searching the internet to find information about recent or historical events, facts, and data"
    inputs = {
        "query": {
            "type": "string",
            "description": "The search query to find information"
        }
    }
    output_type = "string"  # Changed from "text" to "string" as it's an authorized type

    def __init__(self):
        super().__init__()
        self.serpapi_tool = load_tools(["serpapi"])[0]
    
    def forward(self, query: str):
        return self.serpapi_tool.run(query)

# Create the model and tools
model = HfApiModel("Qwen/Qwen2.5-Coder-32B-Instruct")
search_tool = SearchTool()

# Create and run the agent
agent = CodeAgent(tools=[search_tool], model=model)

# Run with the query
agent.run(
    "Who have won the latest World Chess Championship in 2024 ?"
)