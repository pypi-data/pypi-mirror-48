# gimli
Mines for system information.

## Install gimli
```bash
python3 -m pip install --upgrade gimli
```

## Run it like so
```bash
$ gimli
usage: gimli [-h | cpu_util | cpu_tot | meminfo | memusage | serve [N] | watch]
```

## Or... use the gimli API
```bash
Python 3.7.1 (default, Nov  2 2018, 20:33:06) 
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from gimli import Gimli
>>> g = Gimli()
>>> g.cpu_util()
```
