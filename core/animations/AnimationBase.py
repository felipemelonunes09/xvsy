

from abc import ABCMeta, abstractmethod

class AnimationBase(metaclass=ABCMeta):
    @abstractmethod
    def start(self) -> None:
        pass

    @abstractmethod
    def update(self, dt: float) -> None:
        pass

    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def isFinished(self) -> bool:
        pass

class Animation(AnimationBase):
    def __init__(self):
        super().__init__()
        self.__finished = False
        self.__started = False

    def start(self) -> None:
        self.__started = True
        self.__finished = False
     
    def reset(self) -> None:
        self.__started = False
        self.__finished = False
    
    def isFinished(self) -> bool:
        return self.__finished
    
    def hasStarted(self) -> bool:
        return self.__started
    
