# math_server.py
from mcp.server.fastmcp import FastMCP

m = FastMCP("Math")

@m.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@m.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

if __name__ == "__main__":
    m.run(transport="stdio")