import pandas as pd


class CovidConstructor:

    def __init__(self) -> None:
        self.df = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv")
        self.df['date'] = pd.to_datetime(self.df['date'])
        self.gear = {}
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        return
