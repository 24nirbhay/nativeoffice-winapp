"""Auto-generated NativeOffice pytest test."""

from pywinauto_recorder.player import *


def test_recorded_actions():
    with UIPath(u"NativeOffice||Window"):
        with UIPath(u"||Group"):
            click(u"||Group->||Group->||Group->||Button")
        click(u"||Group->||Custom->||Pane->||Group->||Group->||Custom#[7,0]")
        click(u"||Custom#[0,0]")
        with UIPath(u"||Group->||Custom->||Pane->||Group->||Group->||Group->||Group->||Group->||Group"):
            click(u"||Custom#[3,0]")
