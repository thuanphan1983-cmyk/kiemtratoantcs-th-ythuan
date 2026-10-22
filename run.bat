@echo off
chcp 65001 >nul
title HỆ THỐNG KIỂM TRA TOÁN THCS - KẾT NỐI TRI THỨC

echo ======================================================================
echo    KHỞI ĐỘNG HỆ THỐNG KIỂM TRA TOÁN THCS (KẾT NỐI TRI THỨC 6-7-8-9)
echo ======================================================================
echo.

cd /d "%~dp0"

set PY_EXE=python
where python >nul 2>nul
if %errorlevel% neq 0 (
    if exist "%LOCALAPPDATA%\Programs\Python311\tools\python.exe" (
        set PY_EXE="%LOCALAPPDATA%\Programs\Python311\tools\python.exe"
    ) else if exist "C:\Python311\python.exe" (
        set PY_EXE="C:\Python311\python.exe"
    ) else (
        echo Không tìm thấy Python, đang mở trực tiếp file index.html trên trình duyệt...
        start "" "index.html"
        exit /b 0
    )
)

echo [1/2] Đang mở trình duyệt tại: http://localhost:8000
start "" "http://localhost:8000"

echo [2/2] Đang khởi chạy máy chủ web cục bộ...
%PY_EXE% -m http.server 8000

pause
