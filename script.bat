REM =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
REM se você está no windows execute este script com o comando: .\script.bat para iniciar a aplicação
REM =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

@echo off
setlocal

set BACKEND_PATH=backend\
set FRONTEND_PATH=frontend\

start cmd /k "cd backend && venv\Scripts\activate.bat && uvicorn main:app --reload"

start cmd /k "cd frontend && npm run dev"

pause
