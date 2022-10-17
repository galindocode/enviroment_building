from unittest import result


class ProcessData:
    def __init__(self, dict_base) -> None:
        self.dict_base = dict_base
        self.dict_main = dict()

    def __extractVars(self) -> dict:
        variables = self.dict_base["vars"]
        apps = [app for key, app in self.dict_base.items() if key != "vars"]

        self.dict_main = {
            "vars": variables[0],
            "apps": apps
        }

    def __buildVars(self, vars, app):
        data = ''
        app_vars = app["vars"]
        for var in app_vars:
            data += f"{var}={vars[var]}\n"

        return str(data)

    def generateData(self):
        # prepare data
        self.__extractVars()

        # generate data
        data = list()
        apps = self.dict_main["apps"]
        vars = self.dict_main["vars"]
        for app in apps:
            data.append({
                "path": app["path"],
                "data": self.__buildVars(vars, app)
            })

        return data
