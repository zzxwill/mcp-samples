# Use Python 3.12 as base image
FROM python:3.12-slim

# Set working directory
WORKDIR /opt/bytefaas

# Install system dependencies and build tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy application files
COPY * ./

# Make run.sh executable
RUN chmod +x run.sh

# Clean install of core dependencies first
RUN pip install --no-cache-dir --no-binary :all: \
    sniffio \
    anyio \
    starlette

# Install remaining dependencies
RUN pip install --no-cache-dir \
    pydantic \
    pydantic-core \
    fastapi \
    uvicorn \
    mcp \
    langchain-core \
    langchain-openai \
    langgraph \
    langchain-mcp-adapters

# Verify installations
RUN python3 -c "import sniffio; import anyio; import fastapi"


# Expose the port the app runs on
EXPOSE 8000


# Command to run the application
CMD ["./run.sh"] 