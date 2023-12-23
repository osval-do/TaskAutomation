from models.task import Task
# from models.program import Program #Don't add#


class CompositeTask(Task):
  childTasks: list[Task]

  def __init__(self, **kwargs):
    self.childTasks = []

  def loadChildTasks(self, program, taskDir):
    self.program = program
    if taskDir:
        for task in taskDir:
          cs = program.taskClassMap[task.get('class')]
          csInst = cs(**task)
          self.childTasks.append(csInst)
          # print(task.get('class'))

class SequenceTask(CompositeTask):

  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.var_s = kwargs.get('vars')

  def execute(self, program):
    #for name in self.var_s:
    #  program.context[name] = self.parseVar(self.var_s[name])
    last_code = 1
    for task in self.childTasks:
      task.program = self
      last_code = task.execute(self)
      if last_code < 0:
        return last_code
    return last_code