# Demonstrate how to customize logging output

import logging

# TODO: add another function to log from


# set the output file and debug level, and
# TODO: use a custom formatting specification
logging.basicConfig(filename="output.log",
                    level=logging.DEBUG)

logging.info("This is an info-level log message")
logging.warning("This is a warning-level message")

