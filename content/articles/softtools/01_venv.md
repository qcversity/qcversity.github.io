Title: Creating Python Virtual Environment with `venv`
Date: 2023-12-11 08:00
Category: SoftTools
Tags: python, virtualenv
Status: draft
Slug: python-virtual-env-tools
Author: Dr Saad Laouadi
Series: Python Development Tools
Series_index: 2
Summary: A list of tools for creating Python virtual environment. 

# Creating Python Virtual Environment with `venv`


This article is the second part in our multi-part series dedicated to Python development tools. Today, we'll be discussing `venv`, Python's built-in tool for creating virtual environments. This tool makes it easier to create isolated environments for new projects, a crucial step in modern Python development. In our future articles, we will explore more tools and their unique features to enhance your Python programming.



## Why Virtual Environment

In the world of data analysis and programming, setting up a clean and isolated working environment is essential for various reasons:

1. **Dependency Management:** Different projects may require different versions of libraries or Python versions, and conflicts can arise if they share the same environment. Virtual environments allow to manage project-specific dependencies without interfering with each other.

2. **Reproducibility:** Virtual environments make it easy to reproduce the exact environment in which your code was developed. This ensures that your code will work the same way across different machines and at different points in time.

3. **Security:** Isolating your project in a virtual environment can help prevent security vulnerabilities. It limits the access that your code has to system resources.

4. **Portability:** Virtual environments can be easily shared with others, allowing them to set up and run your code on their own systems without compatibility issues.


### Create Virtual Environment Using `venv`


It is considered best practice that, when dealing with a command-line tool or utility, the firt step should be to consult its native help documentation. Because the information exists in that page may not be available elsewhere. Here's how you can access the help documentation for venv:

1. Launch your command-line interface (CLI).
2. Enter the following command:
    - **Linux based systems:** `python -m venv --help` or `python -v venv -h`
    - **Windows:** I assume that Python is installed and added to the search `PATH`. You can check if Python is in the search `PATH` by typing `python --version` or just `py --version`, if it is not in the path, the command will output an error and you need to add it to the `PATH`. If you need help on how to add Python to the search path check this [Add Python to the Search Path on Windows](#add-python-to-the-search-path-on-windows). Now you can check the help using this command
        - `python -m venv --help` or just
        - `py -v venv -h`

In the upcoming sections, most commands will function across major platforms unless a command is platform-specific, where I will provide guidance specific to that particular operating system.

1. To create a virtual environment in a given directory, you would run the following command:

```bash
python -m venv /path/to/directory
```
for example you would like to create a project named `plenv` (this folder will be the name of your environment) in your documents folder, you would run:

1. **Linux and Mac OS:**

```
python -m venv ~/Documents/plenv
```

or you can create a virtual environment in the current working directory like this:

```
python -m venv . 
```

The name of the virtual environment will be the name of current working directory name. 


2. **Windows:**


```
python -m venv C:\Users\YourUsername\Documents\plenv
```

If you are curious what happened after executing this command, you can navigate to this directory and display the content of, here is an example from Mac OS:

```bash
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

