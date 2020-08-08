### conda_env
- [[conda-cheatsheet]](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)
- remove env: `conda env remove --name env_name` 
- export env: `conda env export --no-builds | grep -v "prefix" > environment.yml`

### kernel
Bug when environment doesn't show up properly in JupyterLab 
```
conda activate myenv
python -m ipykernel install --user --name myenv --display-name "Python (myenv)"
```

