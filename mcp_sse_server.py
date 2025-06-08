
import asyncio
from typing import Any, List
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi_mcp import FastApiMCP
import uvicorn


# Create FastAPI app
app = FastAPI(title="Simple MCP SSE Server", version="1.0.0")




 


@app.get("/", response_class=HTMLResponse)
async def root():
    """
    Root endpoint with basic information about the server.
    """
    return "working"

@app.get("/users/{user_id}", operation_id="get_user_info")
async def read_user(user_id: int):
    return {"user_id": "my name is saravana manikandan"}

@app.get("/health")
async def health_check():
    """
    Health check endpoint.
    """
    return {"status": "healthy", "server": "Simple MCP SSE Server"}

# Create MCP server instance
mcp_server = FastApiMCP(app)
mcp_server.mount()

if __name__ == "__main__":
    print("Starting Simple MCP SSE Server...")
    print("Server will be available at: http://localhost:8000")
    print("MCP endpoint will be available at: http://localhost:8000/mcp")
    print("Press Ctrl+C to stop the server")
    
    # Run the server
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info"
    )
