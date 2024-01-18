from fastapi import FastAPI, Query
from datetime import date
from pydantic import BaseModel
from config import ReportEnum, PopulationEnum
import uvicorn
from reports import dargot, salaries
import pandas as pd
import os

app = FastAPI()

@app.get("/")
async def root(report_type: ReportEnum, population: PopulationEnum, date_exec: date = date.today()):
    if report_type == ReportEnum.dargot:
        df_result = dargot(population,date_exec)
    if report_type == ReportEnum.salaries:
        df_result = salaries(population, date_exec)
    df_result.to_csv("results.csv")
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)