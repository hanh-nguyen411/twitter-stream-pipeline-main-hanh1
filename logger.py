import logging
import coloredlogs

coloredlogs.install(level="INFO", fmt="%(asctime)s %(name)s[%(process)d] %(levelname)-8s %(message)s")