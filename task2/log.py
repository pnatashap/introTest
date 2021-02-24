import logging
import logging.config
import os
import sys
from contextlib import contextmanager
from typing import Optional, Tuple, Type, Iterator

default_level = logging.DEBUG
default_formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s')
default_handler = logging.StreamHandler(sys.stderr)
default_handler.setFormatter(default_formatter)
default_handler.setLevel(default_level)
file_handler = logging.FileHandler('scroll_adapter_logs.log')
file_handler.setFormatter(default_formatter)
file_handler.setLevel(default_level)
_logger: logging.Logger = None


def get_logger() -> Optional[logging.Logger]:
    """:returns: Current config :class:`logging.Logger`"""
    return _logger


def setup_logger(name: str, config_path: str = None) -> logging.Logger:
    """
    НGlobal settings :class:`logging.Logger`.

    :param name: Logger name
    :param config_path: Logger config file
    :return: Ready logger :class:`logging.Logger`.
    """
    global _logger
    if _logger is not None and _logger.name != name:
        _logger.disabled = True
    _logger = logging.getLogger(name)
    if config_path and os.path.isfile(config_path):
        _logger.removeHandler(default_handler)
        logging.config.fileConfig(config_path, disable_existing_loggers=True)
    else:
        _logger.addHandler(default_handler)
        _logger.addHandler(file_handler)
        _logger.setLevel(default_level)
    _logger.disabled = False
    return _logger


setup_logger('testing')


class LoggingProxy:

    # pylint: disable=unused-argument
    def __init__(self, **kwargs):
        #: **global** объект :class:`logging.Logger`
        self.logger = get_logger()

    @property
    def name(self) -> str:
        """Class name"""
        return self.__class__.__name__

    def m(self, message: str) -> Tuple[str, str]:
        """
        Add ``[class name]`` into prefix.

        :param message: original message
        :return: logging list Logger'ом.
        """
        return '[%s] ' + message, self.name

    # had to do it explicitly in the sake of statical code analysis
    def debug(self, msg, *args, **kwargs):
        self.logger.debug(*self.m(msg), *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.logger.info(*self.m(msg), *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.logger.warning(*self.m(msg), *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.logger.error(*self.m(msg), *args, **kwargs)

    def exception(self, msg, *args, **kwargs):
        self.logger.exception(*self.m(msg), *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        self.logger.critical(*self.m(msg), *args, **kwargs)

    @contextmanager
    def suppress(self, message: str, *exceptions: Type[Exception]) -> Iterator['LoggingProxy']:
        if not exceptions:
            exceptions = (Exception,)
        try:
            yield self
        except Exception as exc:
            self.exception(message)
            if not isinstance(exc, exceptions):
                raise
