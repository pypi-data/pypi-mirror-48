# An Picat Kernel for Jupyter

## Prerequisites
* [Picat](http://www.picat-lang.org)
* [Jupyter Notebook](http://jupyter.readthedocs.org/en/latest/install.html)
* metakernel
* Linux or MacOS


## Instalation via pip
```text
pip install jupyter
pip install metakernel
pip install picat-kernel
```

Add `--user` to install in your private environment.


## Use
```text
jupyter notebook
# In the notebook interface, select Picat from the 'New' menu
```
or
```text
jupyter qtconsole --kernel picat
```
or
```text
jupyter console --kernel picat
```

## Restrictions
* It doesn't work on Windows because restrictions of `pexpect` and `subprocess` libraries
* It isn't possible to have interation using `;` or debugger.



