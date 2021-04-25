import sys
# Based on Prompt Toolkit source code
from prompt_toolkit.application.current import get_app
from prompt_toolkit import Application
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.formatted_text import AnyFormattedText
from prompt_toolkit.key_binding.bindings.focus import focus_next, focus_previous
from prompt_toolkit.key_binding.defaults import load_key_bindings
from prompt_toolkit.key_binding.key_bindings import KeyBindings, merge_key_bindings
from prompt_toolkit.layout import Layout
from prompt_toolkit.layout.containers import AnyContainer, HSplit
from prompt_toolkit.layout.dimension import Dimension as D
from prompt_toolkit.styles import Style
from prompt_toolkit.widgets import (
    Box,
    Button,
    CheckboxList,
    Dialog,
    Label,
    ProgressBar,
    RadioList,
    TextArea,
    ValidationToolbar,
)

def _return_none() -> None:
    " Button handler that returns None. "
    get_app().exit()

def _create_app(dialog = None, style=None):
    # Key bindings.
    bindings = KeyBindings()
    bindings.add("tab")(focus_next)
    bindings.add("s-tab")(focus_previous)
    
    @bindings.add('c-q')
    def exit(event):
        get_app().exit()

    return Application(
        layout=Layout(dialog),
        key_bindings=merge_key_bindings([load_key_bindings(), bindings]),
        mouse_support=True,
        style=style,
        full_screen=True,
    )

def login_dialog(title, text, ok_text, cancel_text, style):
    def accept(buf: Buffer) -> bool:
        get_app().layout.focus(ok_button)
        return True  # Keep text.

    def ok_handler() -> None:
        get_app().exit(result=[textfield.text, textfield2.text])

    ok_button = Button(text=ok_text, handler=ok_handler)
    cancel_button = Button(text=cancel_text, handler=_return_none)

    textfield = TextArea(
        multiline=False,
        password=False,
        accept_handler=accept,
    )
    textfield2 = TextArea(
        multiline=False,
        password=True,
        accept_handler=accept,
    )

    dialog = Dialog(
        title=title,
        body=HSplit(
            [
                Label(text=text, dont_extend_height=True),
                textfield,
                textfield2,
            ],
            padding=D(preferred=1, max=1),
        ),
        buttons=[ok_button, cancel_button],
        with_background=True,
    )

    return _create_app(dialog, style)
# print(Style.to_dict)
_default_style = Style.from_dict({
        "dialog": "[transparent]",
        "dialog.body": "[transparent]",
        "frame": "[transparent]",
        "frame.border": "[transparent]",
        "frame.label": "[transparent]",
        "button": "[transparent]",
        "button.arrow": "[transparent]",
        "button.text": "[transparent]",
        "label": "[transparent]",
        "text-area": "[transparent]",
        "shadow": "[transparent]",
    })
