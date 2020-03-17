### conda_env
- `conda remove -n envname --all` removing env, make sure `conda deactivate` first

### kernel
```
source activate myenv
python -m ipykernel install --user --name myenv --display-name "Python (myenv)"
```
