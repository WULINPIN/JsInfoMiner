import os
import sys
import time
import requests
from flask import Flask,send_from_directory
from multiprocess import Process
def print_js_files(folder_path):
    jsfile = []
    for root, dirs, files in os.walk(folder_path):

        # 打印.js文件
        for file in files:
            if file.endswith(".js"):
                file_path = os.path.join(root, file)
                relative_file_path = os.path.relpath(file_path, folder_path).replace('\\', '/')
                jsfile.append(relative_file_path)

    return jsfile

def client_request(path):
    time.sleep(1)
    current_folder = path

    proxy = {"http": "http://127.0.0.1:8080"}
    host = 'http://127.0.0.1:8000'

    jss = print_js_files(current_folder)
    for js in jss:
        url = host + '/' + js
        print(url)
        resp = requests.get(url=url, proxies=proxy)

def start_server(path):
    app = Flask(__name__, root_path=path)
    print("应用的工作目录：", app.root_path)

    @app.route('/<path:subpath>')
    def serve_js(subpath):
        js_directory = os.path.join(app.root_path, os.path.dirname(subpath))
        return send_from_directory(js_directory, os.path.basename(subpath))
    app.run(debug=True, host="127.0.0.1",port=8000,use_reloader=False)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:python JsInfoExtract.py 'js文件根目录'")
        sys.exit()
    path = sys.argv[1]
    client = Process(target=client_request, args=(path,))
    # start_server(path)
    server = Process(target=start_server, args=(path,))
    server.start()
    print("Server start......")
    client.start()


