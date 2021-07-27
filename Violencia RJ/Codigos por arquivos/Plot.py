from Constructor import RioDeJaneiro
import matplotlib.pyplot as plt
from Interface import InterfacePlot


class PlotRio(RioDeJaneiro, InterfacePlot):

    def __init__(self) -> None:
        super().__init__()
        return

    def graphic_vehicle_theft(self) -> None:
        ax = plt.subplot(131)
        theft = self.df.mean().sort_values(ascending=False)[4:10]
        theft.plot(cmap=plt.get_cmap('Reds'), edgecolor='r', kind="bar", ax=ax)
        plt.xticks(rotation=50,  ha='right')
        ax.set(title="Crimes mais cometidos")
        self.graphic_general_records()
        return

    def graphic_general_records(self) -> None:
        ax = plt.subplot(132)
        theft = self.df.mean().sort_values(ascending=False)[0:4]
        theft.plot(cmap=plt.get_cmap('twilight'), edgecolor='gray', kind="bar", ax=ax)
        plt.xticks(rotation=50, ha='right')
        ax.set(title="Registros")
        self.trend()
        return

    def trend(self) -> None:
        fig, ax = plt.subplots(figsize=(5, 3))
        ax.plot(self.df.sequestro.index, self.df.sequestro, linewidth=1.0,  color='red')
        ax.set(title="Roubo Coletivo")
        plt.show()
        return
