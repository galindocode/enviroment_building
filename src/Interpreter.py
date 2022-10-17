import json
from .Files import Files
from .ProcessData import ProcessData

commands = {
    '-r': lambda option: Interpreter.generateEnvFiles(option),
    '-h': lambda option: print('Here should be help message :('),
}


class Interpreter:
    def __init__(self, args) -> None:
        self.args = args

    @staticmethod
    def generateEnvFiles(path):
        rawData = Files.readFrom(path)
        dict_base = json.loads(rawData)
        data = ProcessData(dict_base).generateData()
        Files.createEnvFiles(data)

    def run(self):
        try:
            option = ""
            if len(self.args) > 2:
                option = self.args[2]

            commands[self.args[1]](option)
        except KeyError:
            print('invalid command. Use -h for help')
