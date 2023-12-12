## Creating a Virtual Environment with Mamba

Now that you have Mamba installed, you can create virtual environments. The process is similar to using `Conda` but with some improvements in speed and reliability.

1. **Create a new virtual environment:**

    To create a new virtual environment, use the following command:
   
```bash
mamba create -n myenv python=3.9
```

This will create a new environment named `myenv` and install Python 3.9 as the base interpreter.

2. **Activate the environment:**

    To work within your newly created environment, you need to activate it:

```bash
mamba activate myenv
```

3. **Install packages:**

Now, you can use Mamba to install packages within your virtual environment. For example, to install NumPy, you can run:

```bash
mamba install numpy
```

you can install a list of packages in one go like this:

```bash
mamba install numpy pandas scipy
```

Mamba will resolve dependencies and install the package into your environment.

4. **Deactivate the environment:**

 When you're done working in your virtual environment, you can deactivate it:

```bash
conda deactivate
```

This returns you to your base `Conda` environment or system Python environment.


6. **List and Manage Environments:**

You can list your existing environments with:

```bash
mamba env list
```

or 

```bash
mamba info --envs
```

### Deactivate and Remove Environment:

Mamba virtual environments offer a self-contained and isolated space for managing packages and dependencies specific to a particular project or task. This isolation means that the environment encapsulates all the necessary libraries and tools required for that specific project, ensuring that it remains unaffected by changes or conflicts in other environments or the system as a whole.

When you no longer require a virtual environment, it's a best practice to clean up and manage your environments effectively. This can involve several steps:

Deactivation: If the virtual environment is currently active, you should deactivate it. This returns your shell environment to the system's default settings.

Deletion: Once the environment is deactivated, you can safely delete it. Removing a virtual environment frees up disk space and keeps your system organized. You can use the mamba env remove --name myenv (where "myenv" is the name of your environment) command to delete the environment.

To remove an environment:

```bash
conda env remove -n myenv
```
-----------------------------------------------------------------------------------------

### Mamba install software

```bash
# Search for conda packages, will show versions and sources of the package
mamba search edger

# Can specify version to install
mamba install numpy=1.10

# View all packages
mamba list

# Update a package
mamba update pack_name

# Update all packages
mamba update --all

# Remove a package
mamba remove package_name
```
-----------------------------------------------------------------------------------------
## Export and import of conda virtual environment

```bash
#Assume we have an environment called bioapp, we can export it to a yml file
mamba env export --file bioapp.yml --name bioapp

# Then on another computer, we can fully reproduce this environment
# Another advantage of doing this is the software versions are explicitly listed in the yml
# Using conda solving environment will be much faster
mamba env create -f bioapp.yml
```

-----------------------------------------------------------------------------------------

## Use conda-pack to copy directly from the installed location (same operating system)


```bash
#Install conda-pack
mamba install -c conda-forge conda-pack

#Pack the installed environment
conda pack -n my_env_name -o my_env_name.tar.gz

# Copy the packed environment my_env_name.tar.gz to the target machine, and decompress it to any directory, generally recommended under envs directory (anaconda_root/envs). (Note: replace anaconda_root with your own conda install path.)
# Decompress the packed environment
# It will decompress everything to current directory by default, quite spectacular -C must be specified
mkdir -p anaconda_root/envs/my_env
tar -xzf my_env.tar.gz -C anaconda_root/envs/my_env

#Activate environment
mamba activate my_env/bin/activate

#Unpack
conda-unpack

#The environment is now fully copied
mamba deactivate
```
