import sys
# Based on Prompt Toolkit source code
import functools
from asyncio import get_event_loop
from typing import Any, Callable, List, Optional, Tuple, TypeVar

from prompt_toolkit.styles import Style
from prompt_toolkit.application import Application
from prompt_toolkit.application.current import get_app
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.completion import Completer
from prompt_toolkit.eventloop import run_in_executor_with_context
from prompt_toolkit.filters import FilterOrBool
from prompt_toolkit.formatted_text import AnyFormattedText
from prompt_toolkit.key_binding.bindings.focus import focus_next, focus_previous
from prompt_toolkit.key_binding.defaults import load_key_bindings
from prompt_toolkit.key_binding.key_bindings import KeyBindings, merge_key_bindings
from prompt_toolkit.layout import Layout
from prompt_toolkit.layout.containers import AnyContainer, HSplit
from prompt_toolkit.layout.dimension import Dimension as D
from prompt_toolkit.styles import BaseStyle
from prompt_toolkit.validation import Validator
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
_T = TypeVar("_T")

def _return_none() -> None:
    " Button handler that returns None. "
    get_app().exit()

class Exit:
    pass

def _return_exit() -> None:
    " Button handler that returns None. "
    get_app().exit(Exit)


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
def input_dialog(
    title: AnyFormattedText = "",
    text: AnyFormattedText = "",
    ok_text: str = "OK",
    cancel_text: str = "Cancel",
    completer: Optional[Completer] = None,
    validator: Optional[Validator] = None,
    password: FilterOrBool = False,
    style: Optional[BaseStyle] = None,
) -> Application[str]:
    """
    Display a text input box.
    Return the given text, or None when cancelled.
    """

    def accept(buf: Buffer) -> bool:
        get_app().layout.focus(ok_button)
        return True  # Keep text.

    def ok_handler() -> None:
        get_app().exit(result=textfield.text)

    ok_button = Button(text=ok_text, handler=ok_handler)
    cancel_button = Button(text=cancel_text, handler=_return_exit)

    textfield = TextArea(
        multiline=False,
        password=password,
        completer=completer,
        validator=validator,
        accept_handler=accept,
    )

    
    dialog = Dialog(
        title=title,
        body=HSplit(
            [
                Label(text=text, dont_extend_height=True),
                textfield,
                ValidationToolbar(),
            ],
            padding=D(preferred=1, max=1),
        ),
        buttons=[ok_button, cancel_button],
        with_background=True,
    )

    return _create_app(dialog, style)


def input_dialog_inv(
    title: AnyFormattedText = "",
    text: AnyFormattedText = "",
    ok_text: str = "OK",
    cancel_text: str = "Cancel",
    completer: Optional[Completer] = None,
    validator: Optional[Validator] = None,
    password: FilterOrBool = False,
    style: Optional[BaseStyle] = None,
) -> Application[str]:
    """
    Display a text input box.
    Return the given text, or None when cancelled.
    """

    def accept(buf: Buffer) -> bool:
        get_app().layout.focus(ok_button)
        return True  # Keep text.

    def ok_handler() -> None:
        get_app().exit(result=textfield.text)

    ok_button = Button(text=ok_text, handler=ok_handler)
    cancel_button = Button(text=cancel_text, handler=_return_exit)

    textfield = TextArea(
        multiline=False,
        password=password,
        completer=completer,
        validator=validator,
        accept_handler=accept,
    )

    textfield.control.input_processors[1].processor.char = ""
    
    dialog = Dialog(
        title=title,
        body=HSplit(
            [
                Label(text=text, dont_extend_height=True),
                textfield,
                ValidationToolbar(),
            ],
            padding=D(preferred=1, max=1),
        ),
        buttons=[ok_button, cancel_button],
        with_background=True,
    )

    return _create_app(dialog, style)


def create_dialog(title, text, text2, text3, ok_text, cancel_text, root, style = None):
    def accept(buf: Buffer) -> bool:
        get_app().layout.focus(textfield2)
        return True  # Keep text.
    def accept2(buf: Buffer) -> bool:
        get_app().layout.focus(ok_button)
        return True  # Keep text.
    def accept3(buf: Buffer) -> bool:
        get_app().layout.focus(textfield)
        return True  # Keep text.

    def ok_handler() -> None:
        get_app().exit(result=[cb_list.current_values, textfield3.text, [textfield.text, textfield2.text]])

    def _pwsd_none() -> None:
        if textfield.text == "null":
            get_app().exit(result=[cb_list.current_values, textfield3.text, [None, None]])
        else:
            _return_none()
    
    ok_button = Button(text=ok_text, handler=ok_handler)
    cancel_button = Button(text=cancel_text, handler=_pwsd_none)
    cb_list = CheckboxList([("root", root)])
    textfield = TextArea(
        multiline=False,
        password=False,
        accept_handler=accept,
    )
    textfield2 = TextArea(
        multiline=False,
        password=True,
        accept_handler=accept2,
    )

    textfield3 = TextArea(
        multiline=False,
        password=False,
        accept_handler=accept3,
    )
    
    textfield.control.input_processors[1].processor.char = "*"
    textfield2.control.input_processors[1].processor.char = "*"

    dialog = Dialog(
        title=title,
        body=HSplit(
            [
                Label(text=text2, dont_extend_height=True),
                textfield3,
                Label(text=text3, dont_extend_height=True),
                cb_list,
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

def passwd_dialog(title, text, ok_text, pswd_none, cancel_text, style = None):
    def accept(buf: Buffer) -> bool:
        get_app().layout.focus(textfield2)
        return True  # Keep text.
    def accept2(buf: Buffer) -> bool:
        get_app().layout.focus(ok_button)
        return True  # Keep text.

    def ok_handler() -> None:
        get_app().exit(result=[textfield.text, textfield2.text])

    def pwsd_none() -> None:
        get_app().exit(result=[None, None])   
    
    ok_button = Button(text=ok_text, handler=ok_handler)
    pswdn_button = Button(text=pswd_none, handler=pwsd_none)
    cancel_button = Button(text=cancel_text, handler=_return_none)

    textfield = TextArea(
        multiline=False,
        password=True,
        accept_handler=accept,
    )
    textfield2 = TextArea(
        multiline=False,
        password=True,
        accept_handler=accept2,
    )
    textfield.control.input_processors[1].processor.char = "*"
    textfield2.control.input_processors[1].processor.char = "*"

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
        buttons=[ok_button, pswdn_button, cancel_button],
        with_background=True,
    )
    return _create_app(dialog, style)

