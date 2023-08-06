#!/usr/bin/env python3
""" Script for checking fits and editing fit params

    Usage:
        edit <peaklist> <data> [options]

    Arguments:
        <peaklist>  peaklist output from read_peaklist.py (csv, tab or pkl)
        <data>      NMRPipe data

    Options:
        --dims=<id,f1,f2>  order of dimensions [default: 0,1,2]

"""
import sys
import os
from pathlib import Path
from shutil import which

import nmrglue as ng
from docopt import docopt
from schema import Schema, And, SchemaError

from peakipy.core import run_log

# import subprocess
def main(argv):
    args = docopt(__doc__, argv=argv)

    schema = Schema(
        {
            "<peaklist>": And(
                os.path.exists,
                open,
                error=f"{args['<peaklist>']} should exist and be readable",
            ),
            "<data>": And(
                os.path.exists,
                ng.pipe.read,
                error=f"{args['<data>']} either does not exist or is not an NMRPipe format 2D or 3D",
            ),
            "--dims": And(
                lambda n: [int(i) for i in eval(n)],
                error="--dims should be list of integers e.g. --dims=0,1,2",
            ),
        }
    )

    try:
        args = schema.validate(args)
    except SchemaError as e:
        exit(e)


    peaklist = Path(args.get("<peaklist>"))
    data = args.get("<data>")
    dims = args.get("--dims")

    script = which("edit_fits_script.py")

    # p = subprocess.Popen(['bokeh','serve', '--show', script, '--args', peaklist, data, f'--dims={dims}' ])
    run_log()
    os.system(f"bokeh serve --show {script} --args {peaklist} {data} --dims={dims}")

if __name__ == "__main__":
    argv = sys.argv[1:]
    main(argv)
