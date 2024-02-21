@echo off
set "venv=venv"
echo criando o ambiente virtual...
python -m venv %venv%

if exist "requirements.txt" goto EXISTREQUIREMENTS

if not exist "requirements.txt" goto NOTEXISTREQUIREMENTS

:EXISTREQUIREMENTS
echo ativando o venv e instalando o requirements.txt
call venv\Scripts\activate
pip install -r requirements.txt
goto CONTINUE1

:NOTEXISTREQUIREMENTS
echo nao encontrei o requirements.txt
goto CONTINUE1

:CONTINUE1

if exist ".gitignore" goto EXISTGITIGNORE

if not exist ".gitignore" goto NOTEXISTGITIGNORE

:EXISTGITIGNORE
echo Adicionando a pasta %venv%\ ao .gitignore
echo %venv%/*>> .gitignore
goto CLOSE

:NOTEXISTGITIGNORE
echo Criando .gitignore e adicionando a pasta %venv%\
echo %venv%/*> .gitignore
goto CLOSE

:CLOSE
pause