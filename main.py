from src.Files import Files
from src.ProcessData import ProcessData

dict_base = {
    "vars": [
        {
            "var1": "value1",
            "var2": "value2"
        }
    ],
    "app_1": {
        "name": "app_1",
        "path": "./test/app_1",
        "vars": [
            "var1", "var2"
        ]
    }
}


def main():
    raw_data = ProcessData(dict_base)
    data = raw_data.generateData()
    Files.createEnvFiles(data)


if __name__ == '__main__':
    main()
