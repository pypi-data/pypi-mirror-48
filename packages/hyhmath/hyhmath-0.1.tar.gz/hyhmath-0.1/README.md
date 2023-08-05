
## build
```
python setup.py build
```

## sdist: 打包.tar
```
python setup.py sdist
```

log
```
(py3) ➜  myrm git:(master) ✗  python setup.py sdist
running sdist
running egg_info
writing hyhmath.egg-info/PKG-INFO
writing dependency_links to hyhmath.egg-info/dependency_links.txt
writing top-level names to hyhmath.egg-info/top_level.txt
reading manifest file 'hyhmath.egg-info/SOURCES.txt'
writing manifest file 'hyhmath.egg-info/SOURCES.txt'
warning: sdist: standard file not found: should have one of README, README.rst, README.txt, README.md

running check
creating hyhmath-0.1
creating hyhmath-0.1/hyhmath
creating hyhmath-0.1/hyhmath.egg-info
creating hyhmath-0.1/hyhmath/adv
copying files to hyhmath-0.1...
copying setup.py -> hyhmath-0.1
copying hyhmath/__init__.py -> hyhmath-0.1/hyhmath
copying hyhmath/add.py -> hyhmath-0.1/hyhmath
copying hyhmath.egg-info/PKG-INFO -> hyhmath-0.1/hyhmath.egg-info
copying hyhmath.egg-info/SOURCES.txt -> hyhmath-0.1/hyhmath.egg-info
copying hyhmath.egg-info/dependency_links.txt -> hyhmath-0.1/hyhmath.egg-info
copying hyhmath.egg-info/top_level.txt -> hyhmath-0.1/hyhmath.egg-info
copying hyhmath/adv/__init__.py -> hyhmath-0.1/hyhmath/adv
copying hyhmath/adv/sqrt.py -> hyhmath-0.1/hyhmath/adv
Writing hyhmath-0.1/setup.cfg
creating dist
Creating tar archive
removing 'hyhmath-0.1' (and everything under it)
```


## 发布:egg

```
python setup.py bdist_egg
```
