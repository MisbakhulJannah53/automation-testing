# **How to setup and run the automate test**

## **Setup python Environment**

if you haven't intalled python yet. you can install it in your computer first

```
  1. Download python https://www.python.org/ftp/python/3.11.3/python-3.11.3-amd64.exe.
  2. Then install in your local computer.
  3. Open teminal (linux/mac) or powershell (windows).
  4. Run "python --version" to check python installed correctly.
  5. Then run "pip install virtualenv" to build local environment to isolate the project.
```

if you have intalled python. you can setup python project for automate testing

```
  - Create new folder for the project.
  - Open folder in terminal or powershell.
  - Run "python -m venv envName" to create project environment. replce "envName" as needed.
  - Run "envName/Scripts/activate.bat" To activate environment using CMD.
  - Run "envName/Scripts/Activate.ps1" To activate environment using Powershel.
  - Run "deactivate" To disable project environment.
```

if you have setup and activate the environment. you can install the required package.

```
  - Run "pip install selenium" To install selenium. [Read the documentaion](https://selenium-python.readthedocs.io/)
  - Run "pip install git+https://github.com/behave/behaveh". [Read the documentation](https://behave.readthedocs.io/en/latest/install.html/)
  - Download Web Driver if haven't yet. [Chrome webdriver](https://sites.google.com/chromium.org/driver/)
  - Run "pip freeze > requirements.txt" To create requirement file or list of libraries inside your project.
  - Run "install -r requirements.txt" To install all libraries for your project
```

## **Write the code and run the automate test**

if you have install the required packages. you can start to build automation code.

```
  - Create "features" folder in root of you project folder.
  - Then create "steps" folder inside "feature" folder.
  - Inside "features" folder you can add *.feature file to write your gherkin syntax.
  - Inside "steps" folder you can add *.py folder file to write your automation code.
  - Use same filename for *.feature and *.py -> login.feature and login.py.
  - To write gherkin syntax and the code. you can read the [documentation](https://behave.readthedocs.io/en/latest/tutorial.html)
```

#### **The Project tree folder**

```
  automate_tesing
  ├── envName
  ├── feature
  │   ├── steps
  │   │   ├── login.py
  │   ├── login.feature
  ├── Readme.md
  └── requirements.txt
```

## **Link project to github**

add new project to repository

```
  1.  Create you github account. [signup](https://github.com/signup?source=login)
  2.  Create new repository with click "New" button in sidebar.
  3.  Fill the form and click "Create repository" button.
  4.  Open terminal or powershell.
  5.  Open the project folder in terminal.
  6.  Run "git init"
  7.  Run "git branch -M main"
  8.  Run "git remote origin 'remote-link' " replace the remote-link with your remote repository link.
  9.  Run "git add -A"
  10. Run "git commit -m 'init' "
  11. Run "git push -u origin main"
```

add project changes to repository

```
  1.  Run "git add -A"
  2.  Run "git commit -m 'your changes name' "
  3.  Run "git push -u origin main"
```
