from fastapi import FastAPI, HTTPException
from datetime import date
from pydantic import BaseModel
import pandas as pd
import os

app = FastAPI()

class MaofRequest(BaseModel):
    date_exec: date

@app.get("/maof/")
async def maof(maof_request: MaofRequest):
    try:
        output_csv = "path/to/your/output.csv"  # Placeholder

        return {"message": "CSV generated successfully", "file": output_csv}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
