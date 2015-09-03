#!/usr/bin/env python
import sys
from textwrap import dedent
import os

cmd = sys.argv[0]
LIST_DIR = os.path.expanduser("~/.lists")
EXTENSION = ".txt"
if not os.path.isdir(LIST_DIR):
    os.mkdir(LIST_DIR)

def print_usage():
    print dedent("""
    Usage:
    {cmd}: print usage
    {cmd} -ls: show all lists
    {cmd} [list name]: show items from [list name]
    {cmd} [list name] [item to add]: Add item to list
    """).strip().format(cmd="l")

def print_lists():
    files = get_lists()
    with_lengths = [(open(file).read().count("\n"), file[:-len(EXTENSION)]) for file in files]
    for length, name in with_lengths:
        print "[{length:<3}] {name}".format(length=length, name=name)

def print_list(name):
    try:
        print open(name+EXTENSION).read()
    except:
        sys.stderr.write("No list with name \"{}\" found.".format(name))
def add_to_list(name, item):
    with open(name+EXTENSION, 'a') as file:
        file.write(item)
        file.write("\n")

def get_lists():
    return os.listdir(LIST_DIR)


args = sys.argv

if len(args) == 1:
    print_usage()
elif args[1] == "-ls":
    print_lists()
elif len(args) == 2:
    print_list(args[1])
else:
    add_to_list(args[1], " ".join(args[2:]))
