"""Auto-generated NativeOffice pytest test."""

from pywinauto_recorder.player import *


def test_recorded_actions():
    # encoding: utf-8

    with UIPath(u"NativeOffice||Window"):
        with UIPath(u"||Group"):
            click(u"||Group->||Group->||Group->||Button")
        with UIPath(u"||Group->||Custom->||Pane"):
            click(u"||Group->||Group->||Group->||Group->||Group->||Group->||Group->||Custom#[0,3]")
        with UIPath(u"||Group->||Custom->||Pane->||Window->||Group->||Group->||Group"):
            click(u"Edit||CheckBox")
            click(u"Page||CheckBox")
            click(u"Comment||CheckBox")
            click(u"Tool||CheckBox")
            click(u"Protect||CheckBox")
            click(u"Convert||CheckBox")