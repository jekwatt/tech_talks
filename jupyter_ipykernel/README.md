# jupyter ipykernel

Install jupyter and the ipykernel in your environment

```bash
# ipykernel installs all dependencies needed to use jupyter
conda env create -f jupyter_ipykernel/environment.yaml
conda activate jupyter_a
```

Looking around

```bash
conda env list
conda info --envs

conda list -n jupyter_a
conda env export --from-history
```

Installs the kernel for this environment

```bash
python -m ipykernel install --user --name=jupyter_a
```

Manage jupyter ipykernel

```bash
jupyter kernelspec list
jupyter kernelspec remove <my-env>
```
