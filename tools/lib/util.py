from os import path
import logging

def config_logger(logfn=''):
    """
    config logger
    """
    s_fmt= '%(asctime)s@%(filename)s:%(lineno)s:%(levelname)s:%(message)s'
    # formatter
    log_fmt = logging.Formatter(s_fmt)
    # root logger
    logger = logging.getLogger()
    # level
    logger.setLevel(logging.DEBUG)
    # handlers
    s_hdr = logging.StreamHandler()
    s_hdr.setFormatter(log_fmt)
    logger.addHandler(s_hdr)
    if logfn:
        f_hdr = logging.FileHandler(logfn, 'w')
        f_hdr.setFormatter(log_fmt)
        logger.addHandler(f_hdr)

def file_main_name(p):
    """"
    Get main name of a path.
    """
    fn = path.split(p)[1]
    name = path.splitext(fn)[0]
    return name
