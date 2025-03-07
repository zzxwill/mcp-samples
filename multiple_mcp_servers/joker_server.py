# math_server.py
from mcp.server.fastmcp import FastMCP
import requests
import json

mcp = FastMCP("Joker")

@mcp.tool()
def get_joke() -> str:
        """Get a random joke"""
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        joke = json.loads(response.text)
        return joke

if __name__ == "__main__":
    mcp.run(transport="stdio")

