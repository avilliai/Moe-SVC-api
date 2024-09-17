pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
pip install virtualenv
virtualenv -p python3.9 venv
cd venv/Scripts
call activate.bat
where python
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
pause
cd ../..
venv/Scripts/python.exe -m pip install pip==24.0
pip install -r requirements_win.txt
pause
