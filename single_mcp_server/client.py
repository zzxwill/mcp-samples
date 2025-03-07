# Create server parameters for stdio connection
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import asyncio

from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent

from langchain_openai import ChatOpenAI

async def main():
    model = ChatOpenAI(model="gpt-4o")

    server_params = StdioServerParameters(
        command="python",
        # Make sure to update to the full absolute path to your math_server.py file
        args=["/Users/bytedance/Programming/golang/src/zzxwill/mcp-samples/single_mcp_server/math_server.py"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # Get tools
            tools = await load_mcp_tools(session)

            # Create and run the agent
            agent = create_react_agent(model, tools)
            agent_response = await agent.ainvoke({"messages": "what's (3 + 5) x 12?"})

            # Get the final AI message content
            final_response = agent_response['messages'][-1].content

            result = f"--- Agent response: {agent_response}\n--- Answer: {final_response}"

            print(result)

if __name__ == "__main__":
    asyncio.run(main())
