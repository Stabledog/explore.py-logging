#!/usr/bin/python3.8

# Python logging with multiple files + loggers: each one gets named for its __name__

import os
import logging

def main_logging_init():
    # Set up logfile in tmp based on main module filename:
    app_name = os.path.splitext(os.path.basename(__file__))[0]
    logfile=f"{os.environ.get('TMPDIR','/tmp')}/{app_name}.log"

    # Add basic config:
    fmt="%(asctime)s %(levelname)s %(name)s %(message)s"
    datefmt="%Y-%m-%dT%H:%M:%S%z"
    logging.basicConfig(filename=logfile,level=logging.DEBUG,format=fmt,datefmt=datefmt)

    return logfile

# IMPORTANT: call main_logging_init() before any of our other modules
# are imported!
logfile = main_logging_init()
log = logging.getLogger(__name__)  # Use this line in every module during import

from square import square

if __name__=="__main__":
    log.debug(f"Hello world: {square(3)}")

    # Don't forget to shutdown to flush the events out
    logging.shutdown()

    print(f"Log written to {logfile}, contents:")
    with open(logfile,'r') as lf:
        print(lf.read())
