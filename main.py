import sys, inspect, os, importlib
from models.program import Program, Task
from models.task import addToLog
import tasks.http
import tasks.utils
import tasks.context
import yaml
from log import logger
from logging.handlers import RotatingFileHandler

def get_tasks():
    return {
        'login': tasks.http.Login,
        'http': tasks.http.Http,
        'set_vars': tasks.context.SetContextVar,
        'set_log_level': tasks.utils.SetLogLevel
    }

def main():
    try:
        ymlProg = {}
        if os.path.exists('tareas.yml'):
            with open('tareas.yml', 'r') as ymlFile:
                ymlProg = yaml.safe_load(ymlFile)
        prog = Program(taskClassMap=get_tasks(), **ymlProg)
        for arg in sys.argv:
            if arg == 'main.py': continue
            with open(arg, 'r') as ymlFile:
                ymlProg = yaml.safe_load(ymlFile)
                prog.merge_program_file(**ymlProg)

        return prog.execute(prog)
    except ValueError as ve:
        return str(ve)

if __name__ == "__main__":
    handler = RotatingFileHandler('log.txt', maxBytes=2000, backupCount=1, encoding='utf8')
    logger.addHandler(handler)
    logger.setLevel('INFO')

    addToLog('INFO', 'program', 'Starting execution')

    res = main()

    addToLog('INFO', 'program', 'Finished execution with code '+str(res))
    ok = 0 if res == 1 else -1
    sys.exit(ok)