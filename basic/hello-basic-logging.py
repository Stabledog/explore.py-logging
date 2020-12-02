#!/usr/bin/python3.8

import os
import logging


app_name = os.path.splitext(os.path.basename(__file__))[0]
logfile=f"{os.environ.get('TMPDIR','/tmp')}/{app_name}.log"
logging.basicConfig(filename=logfile,level=logging.DEBUG)


logging.debug("Hello world")

# Don't forget to shutdown to flush the events out
logging.shutdown()

print(f"Log written to {logfile}, contents:")
with open(logfile,'r') as lf:
    print(lf.read())

