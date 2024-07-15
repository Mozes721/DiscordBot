from abc import ABC, abstractmethod


class APIMethods(ABC):

    @abstractmethod
    def say_hello(self) -> None:
        pass

    @abstractmethod
    def get_weather(self) -> None:
        pass

    @abstractmethod
    def get_crypto(self) -> None:
        pass

    @abstractmethod
    def get_stock(self) -> None:
        pass


class BotMethods(APIMethods):
    
    @abstractmethod
    def receve_response(self) -> None:
        pass

    @abstractmethod
    def post_hello(self) -> None:
        pass