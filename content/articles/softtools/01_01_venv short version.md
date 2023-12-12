Title: Creating Python Virtual Environment with Venv Tool
Date: 2023-12-12 09:00
Category: SoftTools
Tags: python, virtualenv
Status: draft
Slug: python-virtual-env-with-venv-
Author: Dr Saad Laouadi
Series: Python Development Tools
Series_index: 2
Summary: 

# Creating Python Virtual Environment with Venv 


This is article is the short version of the previously published. This articles contains the steps on how to create a virtual environment using `venv` tool. 

In this article we wiil make use of the command line interface (CLI), **Terminal** app on Unix-Based systems (Mac OS and Linux), and command prompt on windows. 

Some commands work on both systems, while there are few other command that are system specific. We assume that a command works on both systems unless I say so. 

There will be a series of articles on how to use the CLI on both systems. 


This article is the second part in our multi-part series dedicated to Python development tools. Today, we’ll be discussing `venv`, Python’s built-in tool for creating virtual environments. This tool makes it easier to create isolated environments for new projects, a crucial step in modern Python development. In our future articles, we will explore more tools and their unique features to enhance your experience in the Python programming world.


### Create a Virtual Environment Using `venv`

you may want to check the help page of the `venv` tool first. Here is how you can do that from the command line interface:

```
python -m venv --help
```

The previous won't work if Python is not in the system's search PATH on windows. If the command prompt complained about `python` command is not recognized, you may check this article [Add Python to the Search Path on Windows](https://qcversity.github.io/2023/add-python-to-search-path-windows.html) on how resolve the issue

#### Create a Virtual Environment

To create a virtual environment easily, you need to navigate to the folder where you want to create a virtual environment and use the following command: 

Create a new directory (folder) for your project. If you use the command line, you can use the following command to do so, 

Let us create a new folder for our project in the `Documents` folder, (My Documents on Windows) and name it "Test" (give your project an meaningful name).

First we navigate to the `Documents` (My Documents) folder using the `cd` command 

```
cd Documents
```

On Windows 

```
cd "My Documents"
```

Then use the `mkdir` command followed the name of the your project, both for Windows and Unix-Based Systems.

```
mkdir Test
```
	
Let us navigate to this directory using the `cd` command again

```
cd Test
```

The name of this directory will be the name `Test` will be the name of virtual environment. 

The name of the virtual environment will be the name of the current working directory name. 

after you create the virtual environment, you can check what happened using the command:

```
tree
```

or on Windows

```
dir
```

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


Creating and Managing Python Virtual Environments with Venv: A Tutorial

This tutorial, part of our Python Development Tools series, focuses on venv, the built-in tool for creating isolated Python environments. Follow these essential steps to set up, manage, and remove virtual environments effectively:

Creating a Virtual Environment: Use python -m venv /path/to/directory to create a new virtual environment. Choose a directory that will contain the environment, like plenv in your Documents folder.

Activating the Virtual Environment: Activate your virtual environment to use its isolated Python interpreter. On Linux or Mac, use source ~/Documents/plenv/bin/activate. On Windows, use C:\Users\YourUsername\Documents\plenv\bin\activate.bat for Command Prompt or C:\Users\YourUsername\Documents\plenv\bin\activate.ps1 for PowerShell.

Installing Packages with Pip: After activation, use pip install package_name to install necessary packages within your isolated environment. This ensures that your project's dependencies are kept separate from the global Python installation.

Managing Dependencies: Maintain a requirements.txt file in your project root. This file should list all necessary Python packages and their versions for your project. Use pip install -r requirements.txt to install all dependencies at once, ensuring consistency across different setups.

Updating Pip: Regularly update pip within your virtual environment using python -m pip install -U pip to ensure you have the latest features and security fixes.

Deactivating the Virtual Environment: When done, deactivate the virtual environment to return to the system's default Python settings. Simply use the deactivate command in your shell.

Removing a Virtual Environment: To remove a virtual environment, delete its directory. On Linux, use rm -rf ~/Documents/plenv, and on Windows, use rd /S "C:\Users\YourUsername\Documents\plenv".

By following these steps, you can efficiently create, configure, and manage isolated Python environments, enhancing your Python development process.
