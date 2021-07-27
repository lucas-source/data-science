from abc import ABC, abstractmethod


class InterfaceShape(ABC):

    @abstractmethod
    def data_shape(self) -> None:
        raise Exception("Should impleent comer method")

    def data_header(self) -> None:
        raise Exception("Should impleent comer method")

    def missing_values(self) -> None:
        raise Exception("Should impleent comer method")

    def describe(self) -> None:
        raise Exception("Should impleent comer method")


class InterfacePlot(ABC):

    @abstractmethod
    def graphic_vehicle_theft(self) -> None:
        raise Exception("Should impleent comer method")

    def graphic_general_records(self) -> None:
        raise Exception("Shoul impleent comer method")

    def trend(self) -> None:
        raise Exception("Shoul impleent comer method")
