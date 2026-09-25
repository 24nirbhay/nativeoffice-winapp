"""Auto-generated NativeOffice pytest test."""

from pywinauto_recorder.player import *


def test_recorded_actions():
    # encoding: utf-8
    with UIPath(u"NativeOffice||Window"):
        with UIPath(u"||Group"):
            click(u"||Group->||Group->||Group->||Button")
        with UIPath(u"||Group->||Custom->||Pane"):
            click(u"||Group->||Group->||Group->||Group->||Group->||Group->||Group->||Custom#[0,2]")
        with UIPath(u"||Group->||Custom->||Pane->||Window->||Group->||Group->||Group->||Pane->||Group"):
            click(u"＋  New Slide||Button")
            click(u"＋  New Slide||Button")
        with UIPath(u"||Group->||Custom->||Pane->||Window->||Group->||Group"):
            click(u"||Group->||Pane->||Group->||Group->||Group->||Group->||Group#[0,0]")
        with UIPath(u"||Group->||Custom->||Pane->||Window->||Group->||Group->||Pane->||Group->||Group->||Group"):
            click(u"||Button#[0,1]")
