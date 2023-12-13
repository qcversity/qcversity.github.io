Title: Creating Python Virtual Environment with Venv Tool Using Real Project
Date: 2023-12-13 09:00
Category: SoftTools
Tags: python, virtualenv
Status: published
Slug: python-virtual-env-with-venv-flaskproject
Author: Dr Saad Laouadi
Series: Python Development Tools 
Series_index: 3
Summary: This tutorial covers creating, using, and managing Python virtual environments with the `venv` tool. Beginning with the fundamentals of setting up a virtual environment, the article walks you through activating it, using `pip` for package management, and making the most of the `requirements.txt` file. The tutorial is also designed for both Unix-based and Windows systems. 


# Creating Python Virtual Environments using Venv.

This article provides a brief tutorial on creating a virtual environment with the `venv` tool in Python. With the help of the command line interface (CLI), you can create isolated environments for each project, ensuring orderly and organized development workflows.

### Prerequisites

This guide assumes you have a basic understanding of Python and how to navigate the CLI using Terminal (macOS/Linux) or Command Prompt (Windows).

#### Notes
- Most commands work on both Unix-based and Windows systems, but system-specific commands are indicated when necessary.

- The terms "directory" and "folder" are used interchangeably throughout this article.

- Stay tuned for future blog series that will explore CLI usage and command functionalities in more detail.

### Create a Virtual Environment Using `venv`

Before anything else, it's a good idea to consult the help page of the `venv` tool. Use the command line interface to type the next command.

```
python -m venv --help
```

For windows users, the previous command won’t work unless Python is in the system’s ’s search PATH. To check if the `python` command is recognized, type it in the command prompt. If not recognized, a message will indicate so. To add `Python` to the `PATH`, check out this article: [Add Python to the Search Path on Windows](https://qcversity.github.io/2023/add-python-to-search-path-windows.html). In order to follow along this article, you need to take this step. 

#### Create a Virtual Environment

We will guide you through the process of creating a virtual environment for a web development project using the `Flask` framework, a Python library for web development. 

Let's create a folder called "flaskblog" in the `Documents` or (`My Documents` on Windows) directory to hold our project.

The first step is to use the `cd` command to navigate to the `Documents` (My Documents) folder.

```
cd Documents
```

On Windows 

```
cd "My Documents"
```

To create a project folder, use the `mkdir` command followed by the project name, whether on Windows or Unix-based systems.

```
mkdir flaskblog
```

Navigate to this directory by using the `cd` command.

```
cd flaskblog
```


### Creating the Virtual Environment

Creating a virtual environment is simple. Just go to the folder where you want to create it and enter this command:

Time to create a new virtual environment named `flaskvenv` in the `flaskblog` directory.

```
python -m venv flaskvenv
```

The directory name `flaskvenv` will appear on the left side of the command line prompt when we activate the virtual environment.

People conventionally refer to the virtual environment as `venv` or `.venv`, and you can create it in the target project directory like this.

```
python -m venv venv
```

Pay attention, the initial 'venv' creates the virtual environment, and the subsequent 'venv' is the folder name for the new environment's contents. 

Naming your virtual environment `venv` or another name is your choice, but sticking to conventions is beneficial for future use of advanced tools.

To avoid confusion, I'll continue using `flaskvenv` throughout this article instead of `venv`. 

After creating the virtual environment, you can verify the folder's contents using this command on Linux or Mac OS:

```
~/Documents/flaskblog/ tree -L 3
```

To avoid lengthy output, I used the `-L 3` flag to limit the directory content display to three levels. Here's the output from Mac OS System.

```
.
└── flaskvenv
    ├── bin
    │   ├── Activate.ps1
    │   ├── activate
    │   ├── activate.csh
    │   ├── activate.fish
    │   ├── pip
    │   ├── pip3
    │   ├── pip3.10
    │   ├── python -> /usr/local/Caskroom/mambaforge/base/bin/python
    │   ├── python3 -> python
    │   └── python3.10 -> python
    ├── include
    ├── lib
    │   └── python3.10
    └── pyvenv.cfg
```

On Windows, you can use the `dir` command instead: 

```
C:\Users\Public\My Documents\flaskblog> dir flaskvenv 
```

The output will look similar to this (Python 3.12 was used to create the virtual environment on a Windows machine).

```
Include
Lib
pyvenv.cfg
Scripts
```


### Activate the virtual environment:

Once the virtual environment is set up, you must activate it to use it. The activation process varies depending on the system and the shell being used.

##### Linux and Mac OS Users

The `bin` directory contains the activation commands. Use the `tree` command to see what's inside and select the appropriate one for your system or shell. For Zsh or Bash shell users, the activation command is as follows.

```
source bin/activate
```


##### Windows User

The activation commands for Windows users can be found in the `Scripts` directory. If you’re using the command prompt, the activation command is:

```
C:\Users\Public\My Documents\flaskblog> flaksenv\Scripts\activate
```

If you're like me, don't take anything for granted. Check the contents of the `Script` folder using this command:

```
C:\Users\Public\My Documents\flaskblog> dir flaskvenv\Scripts
```

The output will show the available commands, including activating a virtual environment from PowerShell and deactivation. 

For detailed information, refer to the [Python Official Documentation](https://docs.python.org/3/library/venv.html#module-venv). 

#### The `pip` Tool

If you're not familiar with `pip`, it's the tool for managing Python packages in the activated virtual environment, including installation, uninstallation, and listing. For more details, check the [official Pip documentation]


#### Update the `pip` Tool

Using the most current version of a tool is considered best practice in the technical world. Thus, after setting up a new virtual environment, don't forget to upgrade the `pip` package manager with this command:

```
python -m pip install --upgrade pip
```

You can verify the installed `pip` version in the activated virtual environment using the command:

```
pip -V
```

This command will display the `pip` version and indicate the path where the virtual environment is created.


### Install Packages in a Virtual Environment

The next step is to install the Python packages that your project requires. Installing a package is simple - just use the command `python -m pip install` and specify the package name.

To move forward with our project, we have to install the `flask` library in the active virtual environment using either the terminal or command prompt:

```
(flaskvenv) ~/Documents/flaskblog/ python -m pip install flask
```


It's the same procedure Whenever you need to install a new package, please don't forget to activate your environment first. 

If you want to install additional libraries or extensions for your project, such as `Flask-SQLAlchemy`, `Flask-Authorize`, and `flask-login`, ..., which obviously you will need , `pip`  enables you to install them all at once by listing them one after another, separated by a white space like this:

```
python -m pip install -U Flask-SQLAlchemy Flask-Authorize flask-login
```

The `-U` flag ensures to install the latest version of the library. 

### Managing Dependencies in Virtual Environments: The `requirements` File

Maintain a `requirements.txt` file in your project root. This file should list all necessary Python packages and their versions for your project. Use

```
(flaskvenv) ~/Documents/flaskblog/ pip freeze > requirements.txt
```

It is important to update this file regularly after adding new libraries to your virtual environment using the previous command, so that it reflects all project dependencies. 

To view the contents of the `requirements.txt` file, use the `cat` command on Linux-like systems or the `type` command on Windows. Below is a sample preview of our flask project:

```
blinker==1.7.0
click==8.1.7
Flask==3.0.0
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.3
Werkzeug==3.0.1
```

### The Use of `requirements` File

The `requirements.txt` file simplifies of the process of reproduce the project afresh (like on a new machine or in a different environment). So instead of installing each package individually, you can use the command while your virtual environment is activated.

```
python -m pip install -r requirements.txt
```

### Deactivating Virtual Environments

Once you have finished working within the virtual environment, you can simply end the session or deactivate it using the following command:

```
(flaskvenv) ~/Documents/flaskblog/ deactivate
```


### Removing a Virtual environment:

Virtual environment in Python are self-contained, which means all files are stored in the directory where it is created, in our case, the `flaskvenv`. So it is safe to delete that direcotory.

Removing a virtual environment is as simple as deleting that directory. 

##### Delete Virtual Environment for Unix-Based Systems

You can safely delete the `flaskvenv` if you no longer need it like this:


```
(flaskvenv) ~/Documents/flaskblog/ rm -rf flaskvenv
```


##### Delete Virtual Environment for Windows System

You can use the following command on Windows systems to delete the virtual environment:

```
(flaskvenv) C:\Users\Public\My Documents\flaskblog> rm /S flaskvenv
```

As we conclude this exploration of Python virtual environments, it's clear that mastering venv is a crucial step towards professional and organized Python development. By managing project-specific settings and isolating dependencies, you not only prevent conflicts but also gain the freedom to experiment and innovate without limitations. Don't forget, the Python realm is expansive and always evolving, and venv is a valuable tool to navigate it with confidence and creativity. So, apply these skills to your next Python project and seamlessly integrate venv into your development workflow. 

Happy coding!


