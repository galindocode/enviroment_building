from pathlib import Path


class Files:
    def __init__(self, path) -> None:
        self.path = path

    def read(self) -> str:
        print(self.path)
        f = open(self.path, 'r')
        data = f.read()
        f.close()
        return data

    def write(self, data) -> None:
        output_file = Path(self.path)
        output_file.parent.mkdir(exist_ok=True, parents=True)
        output_file.write_text(data)

    @staticmethod
    def readFrom(path) -> str:
        f = open(path, 'r')
        return f.read()

    @staticmethod
    def writeFrom(path, data) -> None:
        output_file = Path(path)
        output_file.parent.mkdir(exist_ok=True, parents=True)
        output_file.write_text(data)

    @staticmethod
    def createEnvFiles(data):

        for item in data:
            Files.writeFrom(item["path"], item["data"])
