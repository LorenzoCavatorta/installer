#from prompt import Prompt
from fakeprompt import FakePrompt

def before_all(context):
    #context.prompt = Prompt()
    context.prompt = FakePrompt()
