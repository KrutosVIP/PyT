import sys
# Based on Prompt Toolkit source code
import functools
from asyncio import get_event_loop
from typing import Any, Callable, List, Optional, Tuple, TypeVar
_T = TypeVar("_T")
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

def _return_none() -> None:
    " Button handler that returns None. "
    get_app().exit()

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

def plmconf(
    title: AnyFormattedText = "",
    text: AnyFormattedText = "",
    text2: Optional[List[AnyFormattedText]] = [""],
    ok_text: str = "Ok",
    cancel_text: str = "Cancel",
    values2: Optional[List[AnyFormattedText]] = [""],
    values: Optional[List[Tuple[_T, AnyFormattedText]]] = None,
    style: Optional[BaseStyle] = None,
) -> Application:
    """
    Display a simple list of element the user can choose multiple values amongst.
    Several elements can be selected at a time using Arrow keys and Enter.
    The focus can be moved between the list and the Ok/Cancel button with tab.
    """
    if values is None:
        values = []

    def ok_handler() -> None:
        get_app().exit(result=[textfield.text, textfield2.text, cb_list.current_values])

    cb_list = CheckboxList(values)

    def accept2(buf: Buffer) -> bool:
        get_app().layout.focus(textfield2)
        return True  # Keep text.

    def accept(buf: Buffer) -> bool:
        get_app().layout.focus(cb_list)
        return True  # Keep text.
    textfield = TextArea(
        multiline=False,
        password=False,
        completer=None,
        validator=None,
        accept_handler=accept2,
    )
    textfield2 = TextArea(
        multiline=False,
        password=False,
        completer=None,
        validator=None,
        accept_handler=accept,
    )
    textfield.text = values2[0]
    textfield2.text = values2[1]
    dialog = Dialog(
        title=title,
        body=HSplit(
            [Label(text=text, dont_extend_height=True), Label(text=text2[0], dont_extend_height=True), textfield, textfield2, Label(text=text2[1], dont_extend_height=True), cb_list],
            padding=1,
        ),
        buttons=[
            Button(text=ok_text, handler=ok_handler),
            Button(text=cancel_text, handler=_return_none),
        ],
        with_background=True,
    )

def pytconf(
    title: AnyFormattedText = "",
    text: AnyFormattedText = "",
    text2: Optional[List[AnyFormattedText]] = [""],
    ok_text: str = "Ok",
    cancel_text: str = "Cancel",
    values2: Optional[List[AnyFormattedText]] = [""],
    values: Optional[List[Tuple[_T, AnyFormattedText]]] = None,
    style: Optional[BaseStyle] = None,
) -> Application:
    """
    Display a simple list of element the user can choose multiple values amongst.
    Several elements can be selected at a time using Arrow keys and Enter.
    The focus can be moved between the list and the Ok/Cancel button with tab.
    """
    if values is None:
        values = []

    def ok_handler() -> None:
        get_app().exit(result=[textfield.text, textfield2.text, cb_list.current_values])

    cb_list = CheckboxList(values)

    def accept2(buf: Buffer) -> bool:
        get_app().layout.focus(textfield2)
        return True  # Keep text.

    def accept(buf: Buffer) -> bool:
        get_app().layout.focus(cb_list)
        return True  # Keep text.
    textfield = TextArea(
        multiline=False,
        password=False,
        completer=None,
        validator=None,
        accept_handler=accept2,
    )
    textfield2 = TextArea(
        multiline=False,
        password=False,
        completer=None,
        validator=None,
        accept_handler=accept,
    )
    textfield.text = values2[0]
    textfield2.text = values2[1]
    dialog = Dialog(
        title=title,
        body=HSplit(
            [Label(text=text, dont_extend_height=True), Label(text=text2[0], dont_extend_height=True), textfield, textfield2, Label(text=text2[1], dont_extend_height=True), cb_list],
            padding=1,
        ),
        buttons=[
            Button(text=ok_text, handler=ok_handler),
            Button(text=cancel_text, handler=_return_none),
        ],
        with_background=True,
    )

    return _create_app(dialog, style)

def plmconf(
    title: AnyFormattedText = "",
    text: AnyFormattedText = "",
    ok_text: str = "Ok",
    cancel_text: str = "Cancel",
    values: Optional[List[Tuple[_T, AnyFormattedText]]] = None,
    values2: Optional[List[Tuple[_T, AnyFormattedText]]] = None,
    style: Optional[BaseStyle] = None,
) -> Application[List[_T]]:
    """
    Display a simple list of element the user can choose multiple values amongst.
    Several elements can be selected at a time using Arrow keys and Enter.
    The focus can be moved between the list and the Ok/Cancel button with tab.
    """
    if values is None:
        values = []

    def ok_handler() -> None:
        get_app().exit(result=[cb_list.current_values, radio_list.current_value])

    cb_list = CheckboxList(values)
    radio_list = RadioList(values2)

    dialog = Dialog(
        title=title,
        body=HSplit(
            [Label(text=text, dont_extend_height=True), cb_list, radio_list],
            padding=1,
        ),
        buttons=[
            Button(text=ok_text, handler=ok_handler),
            Button(text=cancel_text, handler=_return_none),
        ],
        with_background=True,
    )

    return _create_app(dialog, style)


results_array = pytconf(
    title="PyT Configure",
    text="Configure your kernel.",
    ok_text = "Configure", 
    text2 = ["Kernel name and version:", "Kernel Instructions:"],
    values2 = ["PyT-Kernel_21-23_250421_testkeys", "0.0.1-rc7-testing"],
    values=[        ("debug", "Enable Debug"),
        ("custom", "Custom/Modified Kernel"),
        ("dynamic", "Dynamic commands?")
    ]
)#.run()
r_array2 = plmconf(
    title="PLM Configure",
    text="Configure your PLM and graphics type.",
    ok_text = "Configure",
    values = [ ("invisible", "Invisible Password?")],
    values2 = [(0, "No Graphics"), (1, "Normal Mode"), (2, "Easy Mode")]
) #.run()
