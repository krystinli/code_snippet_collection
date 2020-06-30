### conda_env
- remove env: `conda env remove --name env_name` 

### kernel
Bug when environment doesn't show up properly in JupyterLab 
```
conda activate myenv
python -m ipykernel install --user --name myenv --display-name "Python (myenv)"
```

