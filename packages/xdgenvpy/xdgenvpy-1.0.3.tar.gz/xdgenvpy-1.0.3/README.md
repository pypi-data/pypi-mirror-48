# xdg-env-py

`xdgenvpy` is yet another Python utility for the 
[XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html).

## How to use

### Python

There are three main ways to use xdgenvpy as a Python package,

1. Retrieve XDG environment variables, or the specification defaults.
1. Determine _package_ specific directories based on the XDG spec.
1. Or pedantically create _package_ specific directories before attempting to
    use the directory.

To use xdgenvpy as a simple XDG base directory getter, simply create a new 
`xdgenvpy.XDG` object and use the properties it exposes.

```python
from xdgenvpy import XDG
xdg = XDG()
print(xdg.XDG_DATA_HOME)        # /home/user/.local/share
print(xdg.XDG_CONFIG_HOME)      # /home/user/.config
print(xdg.XDG_CACHE_HOME)       # /home/user/.cache
print(xdg.XDG_RUNTIME_DIR)      # /run/user/1000
print(xdg.XDG_DATA_DIRS)        # /home/user/.local/share:/usr/local/share/:/usr/share/
print(xdg.XDG_CONFIG_DIRS)      # /home/user/.config:/etc/xdg
```

But sometimes you want to use package specific directories derived from the XDG
base directories.  This can be done with the `xdgenvpy.XDGPackage` class.

```python
from xdgenvpy import XDGPackage
xdg = XDGPackage('mypackage') 
print(xdg.XDG_DATA_HOME)        # /home/user/.local/share/mypackage
print(xdg.XDG_CONFIG_HOME)      # /home/user/.config/mypackage
print(xdg.XDG_CACHE_HOME)       # /home/user/.cache/mypackage
print(xdg.XDG_RUNTIME_DIR)      # /run/user/1000/mypackage
print(xdg.XDG_DATA_DIRS)        # /home/user/.local/share/mypackage:/usr/local/share/:/usr/share/
print(xdg.XDG_CONFIG_DIRS)      # /home/user/.config/mypackage:/etc/xdg')
```

Lastly, you could also use `xdgenvpy.XDGPedanticPackage` to ensure each of the 
package specific directories exist before the calling code attempts to use the
directory.  Instances of the `xdgenvpy.XDGPedanticPackage` class will not create
system level directories, only package directories on the DATA, CONFIG, CACHE, 
and RUNTIME variables.

```python
from xdgenvpy import XDGPedanticPackage
xdg = XDGPedanticPackage('mypackage')
print(xdg.XDG_DATA_HOME)        # /home/user/.local/share/mypackage
print(xdg.XDG_CONFIG_HOME)      # /home/user/.config/mypackage
print(xdg.XDG_CACHE_HOME)       # /home/user/.cache/mypackage
print(xdg.XDG_RUNTIME_DIR)      # /run/user/1000/mypackage
print(xdg.XDG_DATA_DIRS)        # /home/user/.local/share/mypackage:/usr/local/share/:/usr/share/
print(xdg.XDG_CONFIG_DIRS)      # /home/user/.config/mypackage:/etc/xdg
```

### CLI

xdgenvpy also includes a runnable module, which is easily accessible via the 
script `xdg-env`.  Pip will normally install scripts under something like:
`~/.local/bin`

The installed `xdg-env` command essentially takes a list of XDG variables, and
an optional package name.  For each XDG variable specified, `xdg-env` will
print its corresponding value based on the specification.  It can optionally
take the name of a package and include that into the variable's values.

But can't we just `echo` the XDG variables like so?

```bash
echo ${XDG_DATA_HOME}
echo ${XDG_CONFIG_HOME}
echo ${XDG_CACHE_HOME}
echo ${XDG_RUNTIME_DIR}
echo ${XDG_DATA_DIRS}
echo ${XDG_CONFIG_DIRS}
```

Well, yes.  But there is a problem when the variables are not defined.  The 
`xdg-env` command will *always* print a value.  If the environment variable does
not exist, then the default value will be returned, as defined by the XDG Base
Directory specification.

Although the Python package supports a _pedantic_ mode, the `xdg-env` command 
will not change the file system.  Even if a package name is supplied and the 
directories do not exist, `xdg-env` will not create any files/directories.

## How to install

Install locally as a normal user:
```bash
pip3 install --user xdgenvpy
```

Or install globally as the all powerful root:
```bash
sudo pip3 install xdgenvpy
```

