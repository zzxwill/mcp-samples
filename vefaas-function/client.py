from fastapi import FastAPI
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
import asyncio
import json

app = FastAPI()

async def chat(query: str = "what's (3 + 5) x 12?"):
    model = ChatOpenAI(model="gpt-4o")

    async with MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                # Make sure to update to the full absolute path to your math_server.py file
                "args": ["math_server.py"],
                "transport": "stdio",
            },
            # "weather": {
            #     # make sure you start your weather server on port 8000
            #     "url": "http://localhost:8000/sse",
            #     "transport": "sse",
            # },
            "joker": {
                "command": "python",
                "args": ["joker_server.py"],
                "transport": "stdio",
            }
        }
    ) as client:
        agent = create_react_agent(model, client.get_tools())
        
        response = await agent.ainvoke({"messages": query})
        print("\nQuery Result:")
        print(f"Query: {query}")
        answer = response['messages'][-1].content
        print(f"Answer: {answer}")

        # Create a JSON-serializable version of the response
        serializable_response = {
            "messages": [
                {
                    "role": msg.type,
                    "content": msg.content,
                    "name": msg.name if hasattr(msg, 'name') else None,
                    "function_call": msg.additional_kwargs.get('function_call'),
                    "tool_calls": msg.additional_kwargs.get('tool_calls'),
                    "tool_call_id": msg.additional_kwargs.get('tool_call_id'),
                    "timestamp": msg.additional_kwargs.get('timestamp'),
                    "metadata": msg.additional_kwargs.get('metadata')
                } 
                for msg in response['messages']
            ]
        }

        result = {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'  # Add CORS header if needed
            },
            'body': json.dumps({
                'details': json.dumps(serializable_response),  # Use serializable_response instead of raw response
                'answer': answer
            })
        }
    return result

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/chat")
async def chat_endpoint(question: str = "what's (3 + 5) x 12?"):
    result = await chat(question)
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
