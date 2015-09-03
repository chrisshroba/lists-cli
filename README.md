About
=====
`L` is a command line utility for keeping lists on the command line. It can
be used for Todo lists, idea lists, grocery lists, anything!

Usage:
------
```
L: print usage
L --ls: show all lists
L [list name]: show items from [list name]
L [list name] [item to add]: Add item to list (creates list if it doesn't exist)
```

To use:
-------
```
git clone https://github.com/chrisshroba/lists-cli
cd lists-cli
chmod +x lists.py
ln -s $(pwd)/lists.py /usr/local/bin/L
```

Example:
--------
```
$ L TODO text Alexandra
$ L TODO research how to write C extensions
$ L TODO show off lists-cli
$ L TODO
text Alexandra
research how to write C extensions
show off lists-cli
$ L IDEA add deletion feature to lists-cli
$ L IDEA
add deletion feature to lists-cli
$ L --ls
TODO
IDEA
```
