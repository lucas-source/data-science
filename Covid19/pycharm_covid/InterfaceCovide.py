from abc import ABC, abstractmethod
import inspect


class InterfacCv(ABC):

    @abstractmethod
    def to_present(self) -> None:
        raise Exception(f"must implement the method: {inspect.stack()[0].function}")

    @abstractmethod
    def structure(self) -> None:
        raise Exception(f"must implement the method: {inspect.stack()[0].function}")

    @abstractmethod
    def missing_values(self) -> None:
        raise Exception(f"must implement the method: {inspect.stack()[0].function}")

    @abstractmethod
    def data_analysis(self) -> None:
        raise Exception(f"must implement the method: {inspect.stack()[0].function}")

    def tadoido(self) -> None:
        raise Exception(f"must implement the method: {inspect.stack()[0].function}")


class InterfacPs(ABC):

    @abstractmethod
    def continent_cases(self) -> None:
        raise Exception(f"must implement the method: {inspect.stack()[0].function}")

    @abstractmethod
    def country_cases(self, ax2) -> None:
        raise Exception(f"must implement the method: {inspect.stack()[0].function}")

    @abstractmethod
    def vaccinations_cases(self) -> None:
        raise Exception(f"must implement the method: {inspect.stack()[0].function}")


class InterfaceBr(ABC):

    @abstractmethod
    def structure_br(self) -> None:
        raise Exception(f"must implement the method: {inspect.stack()[0].function}")

    @abstractmethod
    def graphic_br(self) -> None:
        raise Exception(f"must implement the methodo: {inspect.stack()[0].function}")
