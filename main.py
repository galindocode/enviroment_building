import sys
from src.Interpreter import Interpreter


def main():
    command = Interpreter(sys.argv)
    command.run()
    # raw_data = ProcessData(dict_base)
    # data = raw_data.generateData()
    # Files.createEnvFiles(data)


if __name__ == '__main__':
    main()
