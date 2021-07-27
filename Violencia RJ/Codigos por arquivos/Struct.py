from Constructor import RioDeJaneiro
from Interface import InterfaceShape


class ShapeRio(RioDeJaneiro, InterfaceShape):

    def __init__(self) -> None:
        super().__init__()
        return

    def data_shape(self) -> None:
        """
        -shape
        -columns
        -type variables
        """
        print(f"linhas: {self.df.shape[0]}\n"
              f"colunas: {self.df.shape[1]}")
        print(self.df.columns)
        print(self.df.dtypes)
        return

    def data_header(self, num: int = 5) -> None:
        print(self.df.head(num))
        return

    def missing_values(self) -> None:
        print((self.df.isnull().sum() / self.df.shape[0]).sort_values(ascending=False))

    def describe(self) -> None:
        print(self.df.describe())
