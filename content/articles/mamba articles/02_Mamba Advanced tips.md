## `Mamba` Command Under Investigation


While installing `mambaforge` or `miniforge` via a command-line tool like **Terminal** on Unix-based systems such as Linux and Mac OS (at the time of writing this article, I installed `mambaforge` on Mac OS, my primary system, and on `Fedora`, my secondary system), you will be prompted to run `mamba init`. You have the option to proceed by typing 'yes' to accept the initialization, or you can choose not to initialize it at that moment, deferring the process for later by typing 'no'.

Assuming you opt for initialization, executing `mamba init` will create a shell function `mamba` and append it into the runtime configuration file of your system's default shell. In the case of Fedora, where the default shell is **Bash**, the `mamba init` will add the following script to the `.bashrc` file:

```bash
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/trainer/mambaforge/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/trainer/mambaforge/etc/profile.d/conda.sh" ]; then
        . "/home/trainer/mambaforge/etc/profile.d/conda.sh"
    else
        export PATH="/home/trainer/mambaforge/bin:$PATH"
    fi
fi
unset __conda_setup

if [ -f "/home/trainer/mambaforge/etc/profile.d/mamba.sh" ]; then
    . "/home/trainer/mambaforge/etc/profile.d/mamba.sh"
fi
# <<< conda initialize <<<
```

When using Mac OS, where **Zsh** is the default shell, and the previous command will append the script shown bellow to the `.zshrc` file. Note that I installed **mambaforge** using the **Homebrew** utility, which installs software and places it in a specific location on Mac OS machines.

The installation command used was `brew install --cask mambaforge`. Here's a snippet of the code that was added to the `.zshrc` file:

```bash
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/usr/local/Caskroom/mambaforge/base/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/usr/local/Caskroom/mambaforge/base/etc/profile.d/conda.sh" ]; then
        . "/usr/local/Caskroom/mambaforge/base/etc/profile.d/conda.sh"
    else
        export PATH="/usr/local/Caskroom/mambaforge/base/bin:$PATH"
    fi
fi
unset __conda_setup

if [ -f "/usr/local/Caskroom/mambaforge/base/etc/profile.d/mamba.sh" ]; then
    . "/usr/local/Caskroom/mambaforge/base/etc/profile.d/mamba.sh"
fi
# <<< conda initialize <<<
```

If you use a different shell as your main shell and wish to initialize `mamba`, the `mamba init` command accetps different types of shells, including 'bash,' 'fish,' and 'zsh.' For instance, if you intend to initialize mamba for **Zsh**, you would use the following command: 
```bash
mamba init zsh
```

For more detailed information and options related to initializing mamba with different shells, you can access the help documentation by typing `mamba init --help` in your command-line interface. 

-----------------------------------------------------------------------------------------

## The `Mamba` Executable File

Now it is the time to discuss where to find the executable file of `mamba` command. After installing a software that works on a command line tool on the system, you might have the habit of checking the location of the executable file by running `which` command. Reading messages and the prompts while installing a new software is useful and gives a broader overview of what happened and may save you a good amount of time reading the documentation. While installing `Mamba` I did just that, and I essentially understood that the `.zshrc` on Mac OS and `.bashrc` or/and `.bash_profile` on Fedora were changed; however, I did not check those files to investigate the change. Instead, after the installation has finished I ran `which mamba`, and here is the output from Fedora:

```bash
mamba ()
{ 
    \local cmd="${1-__missing__}";
    case "$cmd" in 
        activate | deactivate)
            __conda_activate "$@"
        ;;
        install | update | upgrade | remove | uninstall)
            __mamba_exe "$@" || \return;
            __conda_reactivate
        ;;
        *)
            __mamba_exe "$@"
        ;;
    esac
}
```

And the output from Mac OS:

```bash
mamba () {
	\local cmd="${1-__missing__}"
	case "$cmd" in
		(activate | deactivate) __conda_activate "$@" ;;
		(install | update | upgrade | remove | uninstall) __mamba_exe "$@" || \return
			__conda_reactivate ;;
		(*) __mamba_exe "$@" ;;
	esac
}
```

At this time, I had to check the changes that happened to `rc` files to have more understanding of the situation. The changes I started the previous section with. Although the function script gives us much information, I prefer to see just the executable path of the specific command. After checking the manual page of `which` and `type` commands, I narrowed down few commands that would display the `mamba` executable path. These commands are tested on Mac OS and Fedora systems and on two shells **Bash and Zsh** 

- The **Bash** Shell:
  1. **Fedora**
      1. `which mamba` or `type mamba`: This shows the `mamba` function script
      2. `which -a mamba` or `type -a mamba`: This shows the functions script as well as the executable paths of `mamba`
      3. `which -a --skip-functions mamba`: If you want to skip the function script you can add the `--skip-function` flag. 
    
  2. **Mac OS**:
      1. `which mamba`: It shows the executable path.
      2. `which -a mamba`: It shows all paths where `mamba` exists
      3. `type mamba`: This also outputs the executable path prededed with `mamba is` text.
      4. `type -p mamba`: Using the `-p` flag will give the absolute path.



- The **Zsh** Shell On Mac OS:
  1. `which mamba`: It displays the function script
  2. `which -a mamba`: The function script along the `mamba` paths 
  3. `which -p mamba`: It displays only the `mamba` path.
  4. `whence -p mamba`: Just like `which -p mamba` 
  5. `type mamba`: It shows the shell function path.
  6. `type -p mamba`: It shows the executable path of `mamba` path. -p flag is used, `type' either returns the name of the disk
    file that would be executed
  7. `type -a mamba`: It displays all paths for executable `mamba` files as well the function.  (The `-a` flag is used to display everything including aliases, functions and all of the places that contain an executable named `file'). 
    
-----------------------------------------------------------------------------------------
## Conda Environment Variables 

You check the environment variable using the command `mamba info -s`

1. CONDA_DEFAULT_ENV: The "base" conda default environment 
2. CONDA_EXE: 
3. CONDA_PREFIX
4. CONDA_PYTHON_EXE
5. CONDA_PROMPT_MODIFIER
7. CONDA_SHLVL

## Conclusion

Creating and managing virtual environments is essential for organizing and isolating Python projects. Mamba, with its improved speed and compatibility with the Conda ecosystem, is a powerful package manager for this purpose. By following the steps outlined in this guide, you can efficiently create and manage virtual environments for your Python projects using Mamba.
