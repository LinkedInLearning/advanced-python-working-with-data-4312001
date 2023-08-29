# demonstrate the logging api in Python
import logging
# TODO: use the built-in logging module


# TODO: Use basicConfig to configure logging
logging.basicConfig(level=logging.DEBUG, filename = "output.log", filemode = "w")
# TODO: Try out each of the log levels
logging.debug("This is a debug level message")
logging.info("This is a info level message")
logging.warning("This is a warniing level message")
logging.error("This is a error level message")
logging.critical("This is a critical level message")
# TODO: Output formatted strings to the log
x = "string"
y = 10

logging.info(f"Here's a {x} variable and and int : {y}")
