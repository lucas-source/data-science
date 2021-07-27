import pandas as pd
import matplotlib.pyplot as plt


class RioDeJaneiro:

        def __init__(self) -> None:
            self.data_path = "https://raw.githubusercontent.com/carlosfab/dsnp2/master/datasets/violencia_rio.csv"
            self.df = pd.read_csv(self.data_path)
            self.fig = plt.figure(figsize=(9, 5))
            pd.set_option('display.max_columns', None)
            pd.set_option('display.max_rows', None)
            return
