*How to setup project*

- pip install virtualenv
- create new folder for the project
- open folder in terminal or powershell
- python -m venv envName
- envName/Scripts/activate.bat //To activate environment using CMD
- envName/Scripts/Activate.ps1 //To activate environment using Powershel
- deactivate // to deactive virtualenv

- pip freeze > requirements.txt (to create requirement file or list of libraries inside your project)
- pip install -r requirements.txt (to install all libraries for your project)