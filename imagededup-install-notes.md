Windows pip install is poorly supported due to dependencies not having the correct binaries for Windows

Default install installs outdated numpy which does not support dependencies. If you don't update numpy, you will experience a runtime error when importing imagededup. If you update numpy to >=1.20, pip will claim an incompatability with imagededup, but this won't cause any problems.

