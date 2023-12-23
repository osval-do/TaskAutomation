from models.task import Task
from models.program import Program

class SetContextVar(Task):
  var_s: dict

  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.name = 'set_vars'
    self.var_s = kwargs.get('vars')

  def execute(self, program: Program):
    for name in self.var_s:
      program.context[name] = self.parseVar(self.var_s[name])
    return 0