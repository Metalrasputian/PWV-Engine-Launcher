import webview
import sys
import os

class Api:
    def __init__(self):
        pass

    def init(self):
        response = {
            'message': 'Hello from Python {0}'.format(sys.version)
        }
        return response
    
    def openFileDialog(self):
        file = window.create_file_dialog(webview.OPEN_DIALOG, allow_multiple=False)

        return file[0]

    def getDir(self):
        file = self.openFileDialog()

        path = os.path.dirname(file)

        return path

    def getEngineFiles(self):
        pass

    def getDefaultEngine(self, path):

        main_path = path+"\main.mr"
 
        with open(main_path, "r+") as file:
            text = file.read()
            index = text.index("set_engine") + 10

            engine_name = file[index:-1]

        return engine_name

if __name__ == '__main__':
    api = Api()
    window = webview.create_window('Engine Launcher', "./ui/index.html", js_api=api)
    webview.start(debug=True)