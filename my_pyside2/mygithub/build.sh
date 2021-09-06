pyinstaller.exe --icon=./logo.ico --onefile --noconsole --add-data './icons/*.svg;./icons' main.py

# pyinstaller.exe -w -F -i=./logo.ico --add-data './icons/*.svg;./icons' --uac-admin main.py # 관리자 권할 실행

# --name 을 추가시 exe파일 아이콘 변경 안됨