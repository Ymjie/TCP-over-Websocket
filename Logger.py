import logging
Log = logging.getLogger('Log')
Log.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s-[%(levelname)s]:%(message)s")
sh = logging.StreamHandler(stream=None)
sh.setLevel(logging.DEBUG)
sh.setFormatter(formatter)
Log.addHandler(sh)