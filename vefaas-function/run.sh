#!/bin/bash

# Clean up and set PYTHONPATH

# Print environment for debugging
echo "Environment variables:"
env | grep PYTHON

# Check MCP package structure
echo "Checking MCP package structure..."
python3 -c "
import mcp
print('MCP location:', mcp.__file__)
print('\nChecking server module:')
try:
    from mcp.server.fastmcp import FastMCP
    print('✓ Successfully imported FastMCP')
except ImportError as e:
    print('✗ Import failed:', str(e))
    print('\nListing mcp package contents:')
    import pkgutil
    for module in pkgutil.iter_modules(mcp.__path__, mcp.__name__ + '.'):
        print(module.name)
"

# Start the FastAPI server with the same environment
echo "Starting server..."
exec python3 client.py 