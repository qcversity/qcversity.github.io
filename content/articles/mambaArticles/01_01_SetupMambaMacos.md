Title: Mamba Installation on Mac OS Machines
Date: 2023-12-12 09:00
Category: SoftTools
Tags: python, virtualenv
Status: draft
Slug:install-mamba-macos
Author: Dr Saad Laouadi
Series: Data Science Development Tools: Mamba Distribution
Series_index: 2
Summary: Installing a software can be sometimes daunting and time consuming especially for people with less technical background. This article walks you step-by-by how to install mamba on Mac Os machines. 



Step 1: Install Homebrew

If you don't have Homebrew installed on your system, you can install it by running the following command in the Terminal:


```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Follow the instructions provided during the installation process.

Step 2: Update Homebrew

Make sure Homebrew is up-to-date by running:

```
brew update
```

Step 3: Install Mamba
Now, you can use Homebrew to install Mamba:


```
brew install mamba
```

Step 4: Verify Installation
Check if Mamba is installed successfully by running:


```
mamba --version
```

You should see the version number of Mamba, indicating that the installation was successful.

Step 5: Create and Manage Environments
You can now use Mamba to create and manage Python environments. For example, to create a new environment named "myenv" with Python 3.8:

```
mamba create -n myenv python=3.8
```

Activate the environment:

```
conda activate myenv
```

Step 6: Install Packages
Use Mamba to install packages in the activated environment. For example, to install NumPy:

```
mamba install numpy
```

Step 7: Deactivate Environment
When you're done working in the environment, deactivate it:

```
conda deactivate
```

Step 8: Remove Mamba (Optional)
If you ever want to uninstall Mamba, you can do so with Homebrew:

```
brew uninstall mamba
```

Additional Notes:
Remember to activate your conda environment before using Mamba.
If you encounter any issues, check the Mamba documentation for troubleshooting.
Keep your packages and environments organized for better management.








## Installation

Before we can start using `Mamba`, we need to install it first. For a fresh installation, as mentioned in the official documentation, it is recommended to start with the **Miniforge distribution**. Miniforge comes with minimal installer for **conda**  with the popular **conda-forge** channel preconfigured, but the configuration can be modified later to use any preferred channels. 


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

If you are new to using the command line tool or new to `mamba` and have no experience with `conda`, this command might look cryptic, however, the command `mamba update --name base mamba` all it does is to update the `Mamba`a package manager itself in the base environment. Here we will breakdown this command :
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
