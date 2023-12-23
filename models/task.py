from string import Template
from typing import Iterable
from log import addToLog, logger, createLogContent

class Task:
  name: str
  order = 0
  program: any

  def __init__(self, **kwargs):
    self.name = kwargs.get('name', 'no-name')
    self.order= kwargs.get('order', 0)

  def execute(self, program) -> int:
    self.info('Executed empty task', self.name)

  def info(self, *args: Iterable[str]):
    logger.info(self.__parse_text('INFO', ' '.join(args)))

  def warn(self, *args: Iterable[str]):
    logger.warning(self.__parse_text('WARN', ' '.join(args)))

  def err(self, *args: Iterable[str]):
    logger.error(self.__parse_text('ERROR', ' '.join(args)))

  def __parse_text(self, type, text):
    return createLogContent(type, self.name, text)


  def parseVar(self, text: str) -> str:
    if not text:
      return text
    if not isinstance(text, str):
      return text
    return Template(text).substitute(self.program.context)
