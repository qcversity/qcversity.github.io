Title: Creating Python Virtual Environment with Venv Tool
Date: 2023-12-11 08:00
Category: SoftTools
Tags: python, virtualenv
Status: published
Slug: python-virtual-env-with-venv
Author: Dr Saad Laouadi
Series: Python Development Tools
Series_index: 2
Summary: A Step by Step on How to Create an isolated virtual environment using VENV tool. This articles shows the essentials steps of creating and managing isolated Python environments using the built-in venv tool in our comprehensive guide. This second part in our Python Development Tools series delves into why virtual environments are vital for dependency management, reproducibility, security, and portability. Learn step-by-step how to create, activate, and use virtual environments across different operating systems. Discover best practices for updating pip, managing packages, and using `requirements.txt` for consistent setups. This article offers valuable insights and practical tips to enhance your Python development experience.

# Creating Python Virtual Environment with Venv 


This article is the second part in our multi-part series dedicated to Python development tools. Today, we’ll be discussing `venv`, Python’s built-in tool for creating virtual environments. This tool makes it easier to create isolated environments for new projects, a crucial step in modern Python development. In our future articles, we will explore more tools and their unique features to enhance your experience in the Python programming world.

## Why Virtual Environment?

In the world of data analysis and programming, setting up a clean and isolated working environment is essential for various reasons:

1. **Dependency Management:** Different projects may require different versions of libraries or Python versions, and conflicts can arise if they share the same environment. Virtual environments allow to manage project-specific dependencies without interfering with each other.

2. **Reproducibility:** Virtual environments make it easy to reproduce the exact environment in which your code was developed. This ensures that your code will work the same way across different machines and at different points in time.

3. **Security:** Isolating your project in a virtual environment can help prevent security vulnerabilities. It limits the access that your code has to system resources.

4. **Portability:** You can easily share virtual environments with others, enabling them to set up and run your code on their own systems without compatibility issues.

### Create a Virtual Environment Using `venv`

When starting with a command-line tool like venv, it's a good idea to first check its help page. This can provide useful information not found elsewhere. Here’s how you can access the help documentation for `venv`:

1. Launch your command-line interface (CLI).

2. Enter the following command:

- **Linux based systems:** 

```
python -m venv --help
```
or 

```
python -v venv -h
```


- **Windows:** I assume Python is installed and added to the search `PATH`. 
 	- You can check if Python is in the search `PATH` by typing `python --version` or just `py --version`.
 	-  if it is not in the system’s search PATH, the command will output an error and you need to add it to the `PATH`. If you need help on how to add Python to the search PATH, you may check this article [Add Python to the Search Path on Windows](https://qcversity.github.io/2023/add-python-to-search-path-windows.html).  

   - If you are all set, then you can check the `help` manual using one of the following commands:

```
python -m venv --help
```

or just
    		 
```
py -v venv -h
```


In the upcoming sections, most commands will function across major platforms unless a command is platform-specific, where I will provide guidance specific to that particular operating system.

**To create a virtual environment in a given directory, you would run the following command:**


```
python -m venv /path/to/directory
```

for example you would like to create a project named `plenv` (this folder will be the name of your environment) in your documents folder, you would run:

##### Linux and Mac OS


```
python -m venv ~/Documents/plenv
```

or you can create a virtual environment in the current working directory like this:

```
python -m venv . 
```
	

The name of the virtual environment will be the name of the current working directory name. 

##### Windows

```
python -m venv C:\Users\YourUsername\Documents\plenv
```

**Note**: Some programmers tend to name the virtual environment `venv`, this can be useful when using other tools, however, I gave a different example to avoid confusion about the `venv` tool and the newly created environment name, you can name whatever you like though. 

If you are curious what happened after executing this command, you can navigate to this directory and display the content of, here is an example from Mac OS:

```
tree -L 2 ~/Documents/plenv

/Users/trainer/Documents/plenv
├── bin
│   ├── Activate.ps1
│   ├── activate
│   ├── activate.csh
│   ├── activate.fish
│   ├── pip
│   ├── pip3
│   ├── pip3.11
│   ├── python -> /usr/local/anaconda3/bin/python
│   ├── python3 -> python
│   └── python3.11 -> python
├── include
│   └── python3.11
├── lib
│   └── python3.11
└── pyvenv.cfg
```

Or you can use the `dir` command on Windows command prompt. 

## What Happens when You Create a Virtual Environment 

When you create a new Python virtual environment using `venv`, it sets up a basic, isolated environment that is separated from the system’s global Python installation. This isolation ensures that any changes you make within the virtual environment do not affect the system-wide Python setup.

Upon creation, the virtual environment only includes the bare minimum to get started: the `pip` and `setuptools` packages:

- **Pip** is a tool used to install Python packages from sources like the Python Package Index (PyPI).

- The `setuptools` is a package that provides tools for packaging Python projects. It allows you to build and distribute Python packages easily, especially those that have dependencies on other packages.

## Activate the virtual environment:

After creating the virtual environment, you need to activate it. This means you'll use the Python interpreter and other tools located within this environment, isolated from your main system.

The activation syntax differs from one platform to another and depends on which shell used by a CLI. Here are a few syntaxes for different platforms and different shells: 

1. **Linux-Based Systems**:
	 - **Bash shell**: `source ~/Documents/plenv/bin/activate`
    - **Csh shell** : `source ~/Documents/plenv/bin/activate.csh`
    - **Fish shell**: `source ~/Documents/plenv/bin/activate.fish`
   
2. **Windows**:
	- **Command Prompt**: `C:\Users\YourUsername\Documents\plenv\bin\activate.bat`
	- **Powershell**: `C:\Users\YourUsername\Documents\plenv\bin\activate.ps1`

## Configure and Use the Virtual Environment

Once you’ve activated the new virtual environment, you can use the `pip` package manager to add and change packages for it. You’ll find `pip` in the Scripts subdirectory of the virtual environment on Windows, and in the bin subdirectory on Unix systems.

### Update `pip`

It is considered best practice in the technical world to use the most up-to-date version of a tool for obvious reasons. Thus, after you have created a new virtual environment, you should upgrade the `pip` package manager using this command

```
python -m pip install -U pip
```

This ensures the upgrade process is run in such a way that Python doesn’t lock crucial files. 


You might be tempted to use the next command to save some typing, however this command may not be able to complete the upgrade properly.

```
pip install -U pip
```


Following the upgrade process, you can verify that the installed `pip` version within the activated virtual environment using the command `pip -V`. This command will display the `pip` version and indicate the path where the virtual environment is created.

### Install Packages in a Virtual Environment

Once you’ve successfully set up and activated your Python virtual environment using `venv` and `updated pip`, the next step is to install the Python packages that your project requires. This process is straightforward, whether you’re familiar with `pip` or not. `Pip` is a package manager for Python, allowing you to install and manage additional libraries and dependencies that are not included in the standard Python library.

To install a package, you simply use the command `pip install` followed by the name of the package. For example, to install the `Flask` web framework, you would type:


```
pip install flask
```

In your terminal or command prompt while your virtual environment is activated. This command will download and install `Flask` specifically in your virtual environment, without impacting any other Python projects or the global Python installation on your computer.


It’s the same procedure for any other package you might need. Whether it’s `Django` for web development, `NumPy` for numerical computations, or `Pandas` for data analysis, the installation process remains consistent: 

```
pip install [package-name]
```
 
If you encounter any confusion or issues while using `pip`, the [official Python documentation](https://pip.pypa.io/en/stable/) provides comprehensive guide to help you navigate through the process.

#### Using the Virtual Environment: Command Line Approach

To effectively use the virtual environment you’ve created for running Python scripts, the process is straightforward when using the command line. First, ensure that your virtual environment is activated – you’ll typically see the name of the environment in your command prompt showing it’s active. 

Once activated, you can run any Python script within this environment simply by invoking Python, followed by the script’s name. For example, if you have a script named `main.py`, you execute it by typing `python main.py` in the command line. 

This approach runs the script using the Python interpreter and the specific package setup of your virtual environment, ensuring consistency and isolation from your global Python installation.

#### Using the Virtual Environment with Integrated Development Environment (IDE) 

Alternatively, if you prefer working with an Integrated Development Environment (IDE) like [PyCharm](https://www.jetbrains.com/pycharm/) or [Visual Studio Code](https://code.visualstudio.com/), using a virtual environment is equally seamless. Most modern IDEs detect virtual environments automatically and allow you to select them as the interpreter for your project. 

After setting up your virtual environment as the project’s interpreter, any script you run from the IDE will use the Python interpreter and packages from the virtual environment. This integrated approach simplifies managing dependencies and interpreter settings, as the IDE handles these aspects for you. 

Running a script is as simple as clicking the run button in the IDE, with the assurance that it is executed within the controlled environment of your virtual setup.

## Managing Packages in Virtual Environments: The `requirements` File

When working on Python projects, especially those with complex dependencies, it is essential to manage your packages effectively within a virtual environment. An excellent practice for achieving this is maintaining a `requirements.txt` file at the root of your project. This file serves as a comprehensive list of all the Python packages your project depends on. Each package, along with its specific version, is listed in `requirements.txt`. This organized approach offers several benefits:

   - **Clarity and Documentation**: The `requirements.txt` file acts as a clear documentation of your project’s dependencies, making it easier for other developers (or even your future self) to understand what packages the project needs.

   - **Ease of Setup:** In scenarios where you or someone else needs to set up the project afresh (like on a new machine or in a different environment), the `requirements.txt` file simplifies the process. Instead of installing each package individually, you can use the command while your virtual environment is activated.

```
pip install -r requirements.txt
```
    

This command instructs `pip` to install automatically all the packages listed in the `requirements.txt`.

   - **Consistency Across Environments:** By using a `requirements.txt` file, you ensure that everyone working on the project is using the same versions of packages, which helps in reducing **"it works on my machine"** problems. This consistency is vital for collaborative projects and for maintaining a stable development environment.

   - **Efficient Virtual Environment Recreation:** If you need to set up your virtual environment again (like if it gets corrupted or you move to a new computer), you can use the requirements.txt file. It lists all your project's dependencies, making it easy to recreate the environment exactly.

### Deactivating Virtual Environments

Once you have finished working within the virtual environment, you deactivate it using one of the following ways:

1. **Ending the Session**: You can terminate the session by closing the terminal or command prompt session in which the virtual environment was activated. This ends the current session, and by extension, deactivates the virtual environment.

2. **Using the deactivate Command:** If you want to continue using the same terminal or command prompt session but return to the default Python interpreter (i.e., exit the virtual environment without closing the session), you you can simply type the command 

```
deactivate
```

This command reverses the changes made to your environment when you activated the virtual environment, returning you to the system’s default Python settings.

### Removing a Virtual environment:

Virtual environments in Python are standalone containers, which means that all the files and configurations specific to a virtual environment are stored in its own directory. This includes the Python interpreter, libraries, and scripts that are installed within the environment. 

Since everything that makes up a virtual environment is confined to its directory, removing a virtual environment is as simple as deleting this directory. This is a straightforward process because there are no system-wide changes or dependencies outside this directory that you need to worry about.

So, if a virtual environment is no longer needed, ensure that you first terminate any active Python instances using the virtual environment to avoid errors, conflicts or crashing running projects that use that virtual environment, then you can safely proceed to delete virtual environment directory. 

#### Delete the Virtual environment on Linux-Based systems:

Assume we have finished working with a virtual environment named `plenv`. We can simply delete it using the next command: 

```
rm -rf ~/Documents/plenv
```

- **Command Details**: I assume familiarity with Unix-based systems commands, however, here is a short description of the previous command:

    - `rm`: The command used for removing files and directories.
        - `-rf`: These options given to the `rm` command.
            - `-r` or ``--recursive` This option tells `rm` to remove directories and their contents recursively. Without this option, `rm` would only delete files and would not be able to delete directories that contain files or other directories.
            - `-f` or `--force`: This option tells `rm` to ignore nonexistent files and arguments and never prompt for confirmation. It ‘forces’ the deletion without asking for confirmation, which can be useful for scripting or when you are certain you want to delete something. However, it can be dangerous because it does not ask for confirmation before deleting.

        - `~/Documents/plenv`: This specifies the target of the `rm` command.

Put together, `rm -rf ~/Documents/plenv` is a command to forcibly and recursively remove the directory named `plenv` located in the Documents directory of the current user’s home folder, along with all of its contents (files and subdirectories).

#### Delete the Virtual environment on Windows system:

If you are using Windows, you can use the next command to delete the no longer need virtual environment:

```bash
rd /S  "C:\Users\YourUsername\Documents\plenv"
```

- The `rd` command is similar to `rm` command that deletes a directory on Windows.
- The `/S` option instructs `rd` to remove all directories and files in the specified directory, in addition to the directory itself.

In conclusion, you now have what it takes to create new virtual environments for your future projects. By following the steps outlined in this guide, you can set up a well-structured and isolated development environment for Python programming. Take advantage of Python virtual environments to begin your next project confidently. 
