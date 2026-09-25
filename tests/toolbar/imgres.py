"""Auto-generated NativeOffice pytest test."""

from pywinauto_recorder.player import *


def test_recorded_actions():
    with UIPath(u"NativeOffice||Window"):
        with UIPath(u"||Group"):
            click(u"||Group->||Group->||Group->||Button")
            click(u"||Custom->||Pane->||Group->||Group->||Group->||Group->||Group->||Group->||Custom->||Custom#[1,0]")
        with UIPath(u"||Group->||Group->||Group->||Group->||Group->Image Resizer||Tab"):
            click(u"Image Resizer||TabItem")
        with UIPath(u"||Group->||Group->||Group->||Group"):
            click(u"||Group->Image Resizer||Tab->Image Resizer||TabItem")
            click(u"||Button")
