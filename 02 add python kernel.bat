@echo off
call venv\Scripts\activate
pip install ipykernel
python -m ipykernel install --name=venv