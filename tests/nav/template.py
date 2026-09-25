"""Auto-generated NativeOffice pytest test."""

from pywinauto_recorder.player import *


def test_recorded_actions():
    with UIPath(u"NativeOffice||Window"):
        with UIPath(u"||Group"):
            click(u"||Group->||Group->||Group->||Button")
        click(u"||Group->||Custom->||Pane->||Group->||Group->||Custom#[5,0]")
        with UIPath(u"Templates||Window->||Group"):
            click(u"||Custom#[1,0]")
            click(u"||Custom#[2,0]")
            click(u"||Custom#[3,0]")
            click(u"||Custom#[4,0]")
            click(u"||Custom#[5,0]")
            click(u"||Custom#[6,0]")
        with UIPath(u"Templates||Window"):
            click(u"||Group->||Custom#[7,0]")
        with UIPath(u"Templates||Window->||TitleBar"):
            click(u"Close||Button")
