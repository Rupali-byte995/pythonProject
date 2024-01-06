# Python API Automation Framework
Hybrid Custom Framework to test the REST APIs

###Tech Stack
1. Python 3.11
2. Requests -HTTP Requests 
3. Pytest -Testing Framework
4. Reporting - Allure Report,Pytest-HTML
5. Test Data- CSV,Excel,JSON
6. Parallel Execution :x distribute
7. 

How to install packages 
'''pip install requests pytest pytest-html faker allure-pytest jsonschema 
'''
To freeze your package version :
use this 
''pip freeze >requirements.txt
''
How to run test cases parallely
''pip install pytest-xdist
pytest -n auto filename -s -v 
s- print the logs in console
-v verbos logs are added to add moe logs in the console
#To work with the excel file
pip install openpyxl
#To work with json schema u need to install library known as jsonschema 
pip install jsonschema


 ''