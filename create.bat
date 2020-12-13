@echo off

set fn=%1
set flag=%2
cd /d %~dp0

If "%1"=="" (
    echo "error"
) else ( 
    if "%2"=="" (
        python "C://Users//HP//MyProjects//Project Creation Automation//main.py" %fn% %flag%
        ) else (
            if "%2"=="l" (
                python "C://Users//HP//MyProjects//Project Creation Automation//local.py" %fn%
            )
        )
    )