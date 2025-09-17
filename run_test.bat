cd templates

rmdir /S /Q events_log

powershell -Command "python test_package.py | Tee-Object -FilePath test_log.txt"

python make_dag.py

cd ..