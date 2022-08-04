import os
import subprocess
import platform


def load_file(filename):
    return os.path.join(os.path.dirname(__file__), filename)


def run():
    try:
        system = platform.system()
        print(system)
        o_py_files = [_ for _ in os.listdir(load_file("../")) if _.endswith("py")]
        utils_py_files = [
            os.path.join("./Utils", _)
            for _ in os.listdir(load_file("../Utils"))
            if _.endswith("py")
        ]
        l_py_files = o_py_files + utils_py_files
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
