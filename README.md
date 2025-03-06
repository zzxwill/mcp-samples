# mcp-samples

The client will:
1. Connect to the math server via stdio
2. Initialize a session
3. Load MCP tools
4. Create a ReAct agent using GPT-4
5. Process mathematical queries like "what's (3 + 5) x 12?"

## Note
There appears to be a typo in the model name in `client.py`. It should be `"gpt-4"` instead of `"gpt-4o"`.