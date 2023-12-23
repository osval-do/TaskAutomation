
from datetime import datetime
import logging
logger = logging.getLogger('TaskAutomation')

def createLogContent(type, name, content):
  str = "{:%Y-%m-%dT%H:%M:%S} {} {}: {} ".format(datetime.now(), type, name, content)
  return str

def addToLog(type, name, content):
  if type == 'INFO':
    logger.info(createLogContent(type, name, content))
  elif type == 'WARN':
    logger.warning(createLogContent(type, name, content))
  else:
    logger.error(createLogContent(type, name, content))