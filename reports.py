from datetime import date
import pandas as pd
from config import PopulationEnum

def dargot(population: PopulationEnum, date_exec: date):
    df_dargot = pd.read_csv("dargot.csv")
    if population != PopulationEnum.all:
        df_dargot = df_dargot[df_dargot["population"]==population]
    df_result = df_dargot[(date_exec >= df_dargot["start"]) & (date_exec < df_dargot["end"])]
    return df_result

def salaries(population: PopulationEnum, date_exec: date):
    df_salaries = pd.read_csv("salaries.csv")
    if population != PopulationEnum.all:
        df_salaries = df_salaries[df_salaries["population"] == population]
    df_result = df_salaries[(date_exec >= df_salaries["start"]) & (date_exec < df_salaries["end"])]
    return df_result

def dargot_salaries(date_exec: date):
    return 0