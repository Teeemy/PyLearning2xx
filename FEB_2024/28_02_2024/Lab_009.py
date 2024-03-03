from abc import ABC, abstractmethod


# abstraction is used to enforce
class ATB(ABC):
    @abstractmethod
    def perform_task1(self):
        pass

    @abstractmethod
    def perform_task2(self):
        pass


class Amit(ATB):
    def perform_task1(self):
        return "I am a student of ATB "

    def perform_task2(self):
        return "I am performing a task"


amit = Amit()
print(amit.perform_task2())
print(amit.perform_task1())
