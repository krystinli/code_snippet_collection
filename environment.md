### conda_env
- `conda remove -n envname --all` removing env, make sure `conda deactivate` first

### kernel
Bug when environment doesn't show up properly in JupyterLab 
```
conda activate myenv
python -m ipykernel install --user --name myenv --display-name "Python (myenv)"
```

### python_versioning
```
whereis python
>>> /usr/bin/python
```
