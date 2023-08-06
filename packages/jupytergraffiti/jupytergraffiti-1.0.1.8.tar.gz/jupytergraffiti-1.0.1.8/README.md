# General instructions for building for pip distribution

After changing `setup.py` or any part of the Graffiti codebase, increase the version number in setup.py appropriately.

Then run the commands shown below to upgrade what's stored in pip

``` shell
python3 setup.py prep_to_build npm_run_build sdist bdist_wheel
```

Uploading to the pypi test servers:

``` shell
python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/* --verbose
```

Installing to a host in the cloud, from the test servers:
``` shell
python3 -m pip install --index-url https://test.pypi.org/simple/ jupytergraffiti
```

Testing new installation on cloud host:

``` shell
jupyter notebook —port=3001 —ip=127.0.0.1 —allow-root
```

Uploading to the pypi production servers:

``` shell
python3 -m twine upload --repository-url https://pypi.org/legacy/ dist/* --verbose
```


# General instructions for building for conda distribution

Coming soon...
