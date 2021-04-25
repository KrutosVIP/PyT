#Validation Class
import os
from prompt_toolkit import PromptSession, prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import Style as PStyle
from prompt_toolkit import print_formatted_text
from prompt_toolkit.validation import Validator, ValidationError

class InputValidator(Validator):
    def validate(self, document):
        text = document.text
        ok = False
        for cmd in self.cmds:
            if text.startswith(cmd):
               ok = True
        if not ok:
            num = self.session.output.get_size()[1]
            if len(self.text.replace("{cmd}", text.split(" ")[0])) > num:
                text = self.text.replace("{cmd}", text.split(" ")[0])[:num]
            elif len(self.text.replace("{cmd}", text.split(" ")[0])) < num:
                text = self.text.replace("{cmd}", text.split(" ")[0]) + " " *(num-len(self.text.replace("{cmd}", text.split(" ")[0])))
            else:
                text = self.text.replace("{cmd}", text.split(" ")[0])
            raise ValidationError(message=text)

# PTSTD for redirecting inputs/outputs.
class PTSTD:
    def __init__(self):
        self.basesys = sys.stdout
        self.stdout = []

    def flush(self, *args):
        self.basesys.flush()
    
    def write(self, *args):
        self.stdout.append(*args)

def InputMethod(self, root, PStyle, info):
    symbol = "$"
    if root: symbol = "#"
    style = PStyle.from_dict({ '': '#ffffff', 'username': '#42aaff', 'at': '#6a5acd', 'host': '#122faa', 'path': 'underline'})
    message = [ ('class:username', self.info['user']), ('class:at', '@'), ('class:host', info[8]), ('class:space', ' '), ('class:path', self.tempfs), ('class:space2', ' '), ('class:pound', symbol), ("class:space3", " ")]
    temp_cmds = list(info[10]).copy()
    temp_cmds.extend(os.listdir(self.fs[1]))
    self.cmd_completer = WordCompleter(temp_cmds.copy())
    validator = InputValidator()
    validator.cmds = temp_cmds
    validator.text = info[11]['pyt']['invalid_command']
    validator.session = self.session
    del temp_cmds
    return self.session.prompt(message, style=style, completer=self.cmd_completer, validator=validator)
