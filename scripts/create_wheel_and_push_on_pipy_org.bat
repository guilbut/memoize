cd ..
.\python_venv\scripts\pip.exe install wheel
.\python_venv\scripts\pip.exe install twine
.\python_venv\scripts\python.exe setup.py sdist
.\python_venv\scripts\python.exe setup.py bdist_wheel
.\python_venv\scripts\python.exe .\python_venv\Lib\site-packages\twine\__main__.py upload dist/*  
cd scripts