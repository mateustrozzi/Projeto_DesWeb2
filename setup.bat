:: setup.bat

python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
cd %USERPROFILE%\Downloads\backend\
code .
