from models.task import Task
import logging

class Print(Task):


  def execute(self, program):
    return super().execute(program)


class SetLogLevel(Task):
  level: str

  def __init__(self, **kwargs):
    self.level = kwargs.get('level', 'WARN')

  def execute(self, program):
    logger = logging.getLogger('TaskAutomation')
    logger.setLevel(self.level)
    return 0
