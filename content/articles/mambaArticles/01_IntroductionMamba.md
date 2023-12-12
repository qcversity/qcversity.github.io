Title: Introduction to Mamba distribution
Date: 2023-12-12 09:00
Category: SoftTools
Tags: python, virtualenv
Status: draft
Slug:mamba-distribution
Author: Dr Saad Laouadi
Series: Python Development Tools
Series_index: 2
Summary: 

# Creating Virtual Environments with Mamba: A Short User Guide

Virtual environments are a fundamental tool for isolating and managing dependencies in your Python projects. While Python's built-in `venv` and `pip` can serve this purpose, there are other package managers that offer enhanced capabilities. One such package manager is **Mamba**. In this guide, we'll explore how to create virtual environments using Mamba.

## What is Mamba?

**Mamba** is an open-source package manager designed as an alternative to **conda**, built specifically for data science and scientific computing. It is known for its speed, which makes it an attractive option for managing Python environments and packages. It can create and manage isolated environments, and it works seamlessly with the **Conda** ecosystem.

**Mamba** is a much faster alternative to conda, and environment creation and updating benefits from the use of a much faster (C++ backend) dependency solver. Mamba is a fast, drop-in replacement for the Conda package manager. It provides faster package management operations compared to Conda.

## The Advantages of `Mamba` Over `Conda`

`Mamba` package manager is a powerful tool that offers several advantages over traditional package managers like Conda:

1. **Speed**: Mamba is known for its incredible speed, making package installations a breeze. It implements highly efficient algorithms for dependency resolution and package installation, drastically reducing the time required to fetch and configure dependencies. What might have taken minutes to hours with Conda can now be accomplished in a matter of minutes or even seconds using Mamba¹.

2. **Performance**: Mamba utilizes `C++` code for critical operations, taking advantage of the low-level performance optimizations inherent in the language¹. This allows it to handle computations and data processing with remarkable speed¹.

3. **Parallel Computing**: Mamba utilizes the power of parallel computing, distributing tasks across multiple CPU cores and significantly accelerating the installation process, especially for complex dependency graphs and large environments.

4. **Reliability**: `Mamba` offers more reliable environment solutions compared to `Conda`. It helps you create and manage virtual environments, allowing you to maintain separate configurations for different projects without conflicts.

5. **Drop-in Replacement for Conda**: `Mamba` provides a drop-in replacement for `Conda`, meaning it can be used in place of `Conda` without any major changes to your existing setup.

6. **Exclusive Features**: `Mamba` has added exclusive features such as `mamba repoquery`, which are not available in `Conda`.

These advantages make `Mamba` an excellent choice for Python package management, particularly when dealing with large environments or complex dependency graphs.


## Installation

Before we can start using `Mamba`, we need to install it first. For a fresh installation, as mentioned in the official documentation, it is recommended to start with the **Miniforge distribution**. Miniforge comes with minimal installer for **conda**  with the popular **conda-forge** channel preconfigured, but the configuration can be modified later to use any preferred channel. 


**Installing Miniforge:** To install Miniforge you can download the Miniforge distribution for your platfrom from [here](https://github.com/conda-forge/miniforge). After the downlaod is complete, follow the installation instructions for your platform.


Before you can start using `Mamba`, you need to install it. You can do this with `pip`, but it's recommended to install it using `conda`. If you don't have `conda` installed, you can use Miniconda, a minimal installer for Conda, to get started.

1. **Install Miniconda:** You can download Miniconda from [here](https://docs.conda.io/en/latest/miniconda.html). Follow the installation instructions for your platform.

2. **Checking Mamba Installation**: After installing `mamba` you may want to check it is correctly installed:
    - **Unix-based systems**:
        - You can check that `mamba` is installed using this command `which mamba`. If you ran `mamba init` you will get a function instead of the path where the executable file of the command. [Check this section for more options how to check about `mamba` command]()
        - Or you can check the version if `mamba` if correctly installed using `mamba --version` command. 
      
    - **Windows:**
        - To check  `mamba` path, from **miniforge prompt** you can type the command `where mamba`, or from the command prompt if `mamba` was added to the search path
        - To check for version, type `mamba --version`
     
## Getting Familiar with `Mamba`

`Mamba` is a command line tool that provides a lot of capabilities to manage conda's environments. If you ever used `conda`, then can you can swich to `mamba` easily as almost all conda commands are available through `mamba`. If you are new to this world, this artilce aims to provide you with the necessary commands that you need to start with:



1. **Accessing Help**

with any newly installed command-line tool like `Mamba` or any other software, you may not be immediately familiar with its capabilities and how to use it effectively. This is the reason why you should always consider checking the tool's help page as the first step, because it provides valuable information about the tool's usage, options, and functionality. 

So, familiarize yourself with `Mamba` by checking its help page by running this command:

```bash
mamba --help
```

2. **Update Mamba**

It is recommended to use the lastest version of `Mamba` package manager. It's also considered good practice to regularly update this package manager to access new features, prevent problems like bugs and conflicts, and maintain system stability.

The `Mamba`s typically located in the base environment, and to update it to the most recent version, you can execute the following command:

```bash
mamba update --name base mamba
```

If you are new to using the command line tool or new to `mamba` and have no experience with `conda`, this command might look cryptic, however, the command `mamba update --name base mamba` all it does is to update the `Mamb`a package manager itself in the base environment. Here we will breakdown this command :
    - `mamba`: The name of the command-line executable which invokes the `Mamba` package manager.
    - `update:` A subcommand that instructs `Mamba` to update packages or package managers.
    - `--name base`: This specifies the name of the environment in which the update should be performed. In this case, it is the base environment.  The "base" environment is typically the default environment created when you install Mamba
    - `mamba`: This is the package you want to update within the "base" environment. You are essentially updating the `Mamba` package manager itself.


2. **Getting Information**

```bash
mamba info
```

## Configure `Mamba` 

### Adding Channels

```bash
conda config --add channels r
conda config --add channels bioconda
conda config --add channels conda-forge
```

### Configure the Virtual Environment Directory

```bash
mamba config --append envs_dirs 
```
