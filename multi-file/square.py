# square.py

import logging
log = logging.getLogger(__name__)


def square(a):
    result = a*a
    log.debug(f"squaring {a} to get {result}")

