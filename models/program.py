from .task import Task
from tasks.control import SequenceTask

class Program(SequenceTask):
  bearerToken: str
  taskClassMap = dict
  context: dict
  name = ''

  def __init__(self, taskClassMap, **kwargs):
    super().__init__(**kwargs)
    self.context = {}
    self.taskClassMap = taskClassMap
    self.merge_program_file(**kwargs)

  def merge_program_file(self, **kwargs):
    prog = kwargs.get('program')
    if prog:
      self.name = prog.get('name')
      tasks = prog.get('tasks')
      self.loadChildTasks(self, tasks)
    self.childTasks.sort(key=lambda x: x.order)

