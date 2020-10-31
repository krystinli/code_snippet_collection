### Conda_Environment
- [[conda-cheatsheet]](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)

```sh
conda install --channel conda-forge boltons # Install a package (boltons) from a specific channel (conda-forge)
conda remove --name bio-env toolz boltons # Remove one or more packages (toolz, boltons) from a specific environment (bio-env)

conda create --name py35 python=3.5 # Create a new environment named py35, install Python 3.5
conda create --clone py35 --name py35-2 # Make exact copy of an environment

conda list --explicit > bio-env.txt # Save environment to a text file
conda list --revisions # List the history of each change to the current environment
conda install --revision 2 # Restore environment to a previous revision

which -a python # Show the locations of all versions of Python that are currently in the path
```

### Versioning
```sh
# Specifying version numbers:
Fuzzy numpy=1.11 => 1.11.0, 1.11.1, 1.11.2, 1.11.18 etc.
Exact numpy==1.11 => 1.11.0
Greater than or equal to "numpy>=1.11" => 1.11.0 or higher
OR "numpy=1.11.1|1.11.3" => 1.11.1, 1.11.3
AND "numpy>=1.8,<2" => 1.8, 1.9, not 2.0
```

### Kernel
Bug when environment doesn't show up properly in JupyterLab 
```
conda activate myenv
python -m ipykernel install --user --name myenv --display-name "Python (myenv)"
```

