CLARILAB event filters (for PyQt5)
==================================

Les eventFilters en PyQt5 sont executé a chaque évenement, ou presque.

Cela rend l'utilisation d'un eventFilter codé en python
très très couteux pour l'application.

Ceci est une implémentation C++ permettant un gain de performance considérable.


Compilation
===========
```
qmake
make
make install
python setup.py install
```

Multiarch oneline
```
/usr/lib/x86_64-linux-gnu/qt5/bin/qmake && make clean && make && python setup.py clean && PATH=/usr/lib/x86_64-linux-gnu/qt5/bin:$PATH python setup.py install
```
