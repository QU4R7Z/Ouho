import os
import subprocess
import platform


def load_file(filename):
    return os.path.join(os.path.dirname(__file__), filename)


def run():
    try:
        system = platform.system()
        print(system)
        l_py_files = []
        for root, dirs, files in os.walk("./"):
            for file in files:
                if file.endswith(".py") and not root.startswith("./venv"):
                    l_py_files.append(os.path.join(root, file))

        print(l_py_files)
        if system == "Windows":
            for i in l_py_files:
                command = f"black {i}"
                subprocess.run(command, shell=True)

        elif system == "Linux":
            print(system)
        elif system == "Darwin":
            print(system)
        else:
            print("OS를 알 수 없음")
    except Exception as e:
        print(e)
