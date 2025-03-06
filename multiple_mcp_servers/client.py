# Create server parameters for stdio connection
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
import asyncio

from langchain_openai import ChatOpenAI

async def main():
    model = ChatOpenAI(model="gpt-4o")

    async with MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                # Make sure to update to the full absolute path to your math_server.py file
                "args": ["/Users/zzxwill/Programming/go/src/zzxwill/mcp-samples/multiple_mcp_servers/math_server.py"],
                "transport": "stdio",
            },
            "weather": {
                # make sure you start your weather server on port 8000
                "url": "http://localhost:8000/sse",
                "transport": "sse",
            }
        }
    ) as client:
        agent = create_react_agent(model, client.get_tools())
        math_response = await agent.ainvoke({"messages": "what's (3 + 5) x 12?"})
        print("\nMath Query Result:")
        print(math_response)
        
        weather_response = await agent.ainvoke({"messages": "what is the weather in nyc?"})
        print("\nWeather Query Result:")
        print(weather_response)

if __name__ == "__main__":
    asyncio.run(main())