import json
import os


class FileFactory:

    def writeData(self, path, arrData):
        jsonString = json.dumps([item.__dict__ for item in arrData], ensure_ascii=False, indent=4, default=str)
        with open(path, "w", encoding="utf-8") as jsonFile:
            jsonFile.write(jsonString)


    def readData(self, path, ClassName):
        if not os.path.isfile(path):
            return []
        with open(path, "r", encoding="utf-8") as file:
            self.arrData = json.loads(file.read(), object_hook=lambda d: ClassName(**d))
        return self.arrData
