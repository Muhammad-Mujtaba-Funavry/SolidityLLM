from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from typing import Optional
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(title="Solidity Contract Generator API")

# Get cloud server URL from environment variable
CLOUD_SERVER_URL = os.getenv("CLOUD_SERVER_URL")
if not CLOUD_SERVER_URL:
    raise ValueError("CLOUD_SERVER_URL environment variable is not set")

class PromptRequest(BaseModel):
    prompt: str
    max_tokens: Optional[int] = 1000
    temperature: Optional[float] = 0.7

class PromptResponse(BaseModel):
    generated_contract: str
    status: str

@app.post("/generate-contract", response_model=PromptResponse)
async def generate_contract(request: PromptRequest):
    try:
        # Prepare the request payload
        payload = {
            "prompt": request.prompt,
            "max_tokens": request.max_tokens,
            "temperature": request.temperature
        }

        # Send request to cloud server
        response = requests.post(
            CLOUD_SERVER_URL,
            json=payload,
            timeout=30  # 30 seconds timeout
        )
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Parse the response
        result = response.json()
        
        return PromptResponse(
            generated_contract=result.get("generated_contract", ""),
            status="success"
        )
        
    except requests.exceptions.RequestException as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error communicating with cloud server: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
