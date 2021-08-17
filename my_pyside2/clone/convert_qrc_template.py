import os

# Conver qrc resource file to python resource file
os.system("pyrcc5 python_app.qrc -o python_app_rc.py")
# pyrcc5 -o resources.py resources.qrc
import python_app_rc
