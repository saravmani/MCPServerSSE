# Simple HTTP SSE MCP Server

A simple Model Context Protocol (MCP) server that uses HTTP with Server-Sent Events (SSE) for communication. Built with FastAPI and fastapi_mcp.

## Features

- HTTP-based MCP server with SSE support
- Simple tool: `add_numbers` - adds two numbers together
- Web interface for server information
- Health check endpoint

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Server

```bash
python mcp_sse_server.py
```

The server will start on `http://localhost:8000`

## Endpoints

- `/` - Web interface with server information
- `/mcp` - MCP server endpoint for SSE communication
- `/health` - Health check endpoint

## Available Tools

### add_numbers
Adds two numbers together.

**Parameters:**
- `a` (number): First number to add
- `b` (number): Second number to add

**Example:**
```json
{
  "name": "add_numbers",
  "arguments": {
    "a": 5,
    "b": 3
  }
}
```

## Connecting MCP Clients

Configure your MCP client to connect to:
```
http://localhost:8000/mcp
```

The server supports the MCP protocol over HTTP with Server-Sent Events for real-time communication.

## Development

The entire server is contained in a single Python file (`mcp_sse_server.py`) for simplicity.
