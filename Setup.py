# Well-Tools


try:
    import sys
    import os

    if sys.platform.startswith("win"):
        print("Installing the python modules required for the Well Tool:")
        os.system("cls")
        os.system("python -m pip install --upgrade pip")
        os.system("python -m pip install -r requirements.txt")
        os.system("python Well.py")

    elif sys.platform.startswith("linux"):
        print("Installing the python modules required for the Well Tool:")
        os.system("clear")
        os.system("python3 -m pip3 install --upgrade pip")
        os.system("python3 -m pip3 install -r requirements.txt")
        os.system("python3 Well.py")
    

except Exception as e:
    input(e)