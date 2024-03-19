from typing import List
from abc import ABC, abstractmethod

class ICommand(ABC):
    @abstractmethod
    def execute(self):
        pass

class MoveCommand(ICommand):
    def execute(self):
        pass

class RotateLeftCommand(ICommand):
    def execute(self):
        pass

class RotateRightCommand(ICommand):
    def execute(self):
        pass

class StringCommandParser:
    BY_EACH_CHARACTER = ""
    START_INDEX = 0

    stringToCommandMap = {
        "L": RotateLeftCommand(),
        "R": RotateRightCommand(),
        "M": MoveCommand()
    }

    def __init__(self, commandString: str):
        self.commandString = commandString

    def toCommands(self) -> List[ICommand]:
        if self.isNullOrEmpty(self.commandString):
            return []
        return self.buildCommandsList(self.commandString)

    def buildCommandsList(self, commandString: str) -> List[ICommand]:
        commands = []
        for commandCharacter in self.commandCharactersFrom(commandString):
            if commandCharacter is None:
                break
            mappedCommand = self.lookupEquivalentCommand(commandCharacter.upper())
            commands.append(mappedCommand)
        return commands

    def isNullOrEmpty(self, commandString: str) -> bool:
        return commandString is None or commandString.strip() == ""

    def commandCharactersFrom(self, commandString: str) -> List[str]:
        return list(commandString)

    def lookupEquivalentCommand(self, commandString: str) -> ICommand:
        return self.stringToCommandMap.get(commandString)

