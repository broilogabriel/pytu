#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

import argparse

import argcomplete


def main(arg):
    print(arg)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("cmd", choices=["start", "stop", "status", "show"])
    argcomplete.autocomplete(parser)
    args = parser.parse_args()
    main(args.cmd)
