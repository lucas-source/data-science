import pandas as pd
from InterfaceCovid import InterfacPs, InterfaceBr
from Constructor import CovidConstructor
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


class InfoCoutries(CovidConstructor, InterfacPs):

    sns.set()

    def __init__(self) -> None:
        super().__init__()
        return

    def continent_cases(self) -> None:
        fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))

        check = dict(self.df.groupby(self.df['location'])['total_deaths'].max().sort_values(ascending=False)[1:5])
        new_data = pd.DataFrame(check, index=[0])
        new_data.plot(cmap=plt.get_cmap('cividis'), kind="bar", ax=ax1)
        plt.xticks(rotation=50, ha='right')
        ax1.set_title('$Continents$ $with$ $more$ $cases$')
        ax1.set_xlabel('$places$ $X$')
        ax1.set_ylabel('$quantities$ $Y$')
        plt.tight_layout()
        self.country_cases(ax2)
        return

    def country_cases(self, ax2) -> None:
        country_single = dict(self.df.groupby(self.df['location'])['total_cases'].
                              max().sort_values(ascending=False)[5:6])
        biggest_countries = dict(self.df.groupby(self.df['location'])['total_cases'].
                                 max().sort_values(ascending=False)[7:11])

        self.gear.update(country_single)
        self.gear.update(biggest_countries)
        new_frame = pd.DataFrame(self.gear, index=[0])

        new_frame.plot(cmap=plt.get_cmap('bone'), kind="bar", ax=ax2)
        ax2.set_title('$Countries$ $with$ $more$ $cases$')
        ax2.set_xlabel('$places X$')
        ax2.set_ylabel('$quantities Y$')
        plt.show()
        return

    def vaccinations_cases(self) -> None:
        vaccinations_single = self.df.groupby(self.df['location'])['total_vaccinations'].max().sort_values(
            ascending=False)[2:3]
        vacina_countries = self.df.groupby(self.df['location'])['total_vaccinations'].max().sort_values(
            ascending=False)[6:8]
        self.gear.update(vaccinations_single)
        self.gear.update(vacina_countries)

        peg = []
        for i in self.gear:
            peg.append(i)

        top1 = self.df.loc[self.df.location == peg[0], "total_vaccinations"]
        top2 = self.df.loc[self.df.location == peg[1], "total_vaccinations"]
        top3 = self.df.loc[self.df.location == peg[2], "total_vaccinations"]

        figure, ax = plt.subplots(figsize=(10, 6))

        sns.lineplot(data=self.df, x=self.df.date, y=top1, label=peg[0], color='darkred')
        sns.lineplot(data=self.df, x=self.df.date, y=top2, label=peg[1], color='Gold')
        sns.lineplot(data=self.df, x=self.df.date, y=top3, label=peg[2], color='mediumblue')
        ax.set_title('$top$ $3$ $most$ $vaccinated$ $countries$')
        ax.set_xlabel('$Date X$')
        ax.set_ylabel('$quantities Y$')
        plt.show()
        return


class InfoBrasil(CovidConstructor, InterfaceBr):

    def __init__(self) -> None:
        super().__init__()
        self.br = self.df.loc[self.df.location == "Brazil"].copy()
        return

    def br_head(self) -> None:
        print(self.br.head())

    def structure_br(self) -> None:
        print(f"Início: {self.df['date'].min()}\n"
              f"Fim: {self.df['date'].max()}\n")

        first_case = self.br.loc[self.br['new_cases'] != 0.0].head(1)
        print(f"Primeiro caso de covid no Brasil {first_case.date.loc[13811]}")

        print(f"Até a data desse estudo o Brasil apresenta {self.br['total_cases'].max():,.0f} pessoa infectado covid,"
              f" e um total de {self.br['total_deaths'].max():,.0f} mortes pelo covid!")
        return

    def graphic_br(self) -> None:
        x = np.arange(533)
        y = self.br.total_vaccinations

        fig, ax = plt.subplots(figsize=(10, 4))

        sns.regplot(x, y, color="g", ax=ax, x_bins=70)
        ax.set_title('$vaccinated$ $in$ $Brazil$')
        ax.set_ylabel('$quantities Y$')

        plt.show()
