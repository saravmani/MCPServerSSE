from fastapi import FastAPI
from pydantic import BaseModel
from fastapi_mcp import FastApiMCP
 
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()

@app.get("/Get_Special_Number", operation_id="Get_Special_Number")
async def Get_Special_Number(a: int, b: int):
    """Get_Special_Number"""     
    result = 100+a+b
    return {"sum": result}

mcp = FastApiMCP(
    app,
    name="Addition MCP",
    description="Simple API exposing adding operation",
)

mcp.mount_http()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("some_mcp_tools:app", host="127.0.0.1", port=8000, reload=True, log_level="debug")