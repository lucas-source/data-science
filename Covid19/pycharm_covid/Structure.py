from Constructor import CovidConstructor
from InterfaceCovid import InterfacCv


class CovidStructure(CovidConstructor, InterfacCv):

    def __init__(self) -> None:
        self.consult = None
        super().__init__()

    def to_present(self, num: int = 5) -> None:
        print(self.df.head(num))
        return

    def structure(self) -> None:
        print(f"Lines: {self.df.shape[0]}\n"
              f"Columns: {self.df.shape[1]}\n")
        print("Tipos das variáveis:")
        print(self.df.dtypes)
        return

    def missing_values(self) -> None:
        print((self.df.isnull().sum() / self.df.shape[0]).sort_values(ascending=False))
        return

    def data_analysis(self) -> None:
        print(f"Início: {self.df['date'].min()}\n"
              f"Fim: {self.df['date'].max()}\n")
        return
