`membernator` is a tool that can be used to scan membership cards and establish if
they're valid or not against a CSV database.

# Dependencies

This program is written in Python 3. You will need to install these dependencies
to run `membernator` properly:

* python3
* pygame
* docopt

# Installation

## With setup.py

You can install `membernator` like any other python program with the help of
`setuptools`:

    $ python3 setup.py install

## Manually

Since `membernator` is a single python file, you can call you can it directly:

    $ python3 /path/to/membernator.py

You can also add it to your local path:

    $ sudo cp /path/to/membernator.py /usr/local/bin/membernator
    $ sudo chmod +x /usr/local/bin/membernator

# Usage

    Usage:
        membernator [options] --database FILE
        membernator (-h | --help)
        membernator --version

    Options:
        -h  --help       Shows the help screen
        --version        Outputs version information
        --database FILE  Path to the CSV database
        --id_col ID      "id" column in the CSV database. [default: ID]
        --name_col NAME  "name" column in the CSV database. [default: NAME]
        --time SEC       Delay in secs between scans. [default: 2.5]
        --width WIDTH    Width in pixels. Use 0 for fullscreen. [default: 800]
        --height HEIGHT  Height in pixels. Use 0 for fullscreen. [default: 480]
        --logfile LOG    Path to the logfile
