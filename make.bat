@echo off
setlocal

REM main function
:main
call :rm_build
call :build_html
goto :eof

REM remove _build directory
:rm_build
if exist _build (
    rmdir /s /q _build
    echo _build directory removed.
) else (
    echo _build directory does not exist.
)
goto :eof

REM generate html documentation
:build_html
sphinx-build -b html . _build
if %errorlevel% neq 0 (
    echo Failed to build HTML documentation. Error code: %errorlevel%
    goto :eof
)
echo HTML documentation built.
goto :eof

REM run main function
call :main
endlocal
