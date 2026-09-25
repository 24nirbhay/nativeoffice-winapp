"""Auto-generated NativeOffice pytest test."""
import pyautogui

from pywinauto_recorder.player import *


def test_recorded_actions():
    # encoding: utf-8

    with UIPath(u"NativeOffice||Window"):
        with UIPath(u"||Group"):
            click(u"||Group->||Group->||Group->||Button")
        with UIPath(u"||Group->||Custom->||Pane"):
            click(u"||Group->||Group->||Group->||Group->||Group->||Group->||Group->||Custom#[0,0]")
            
        pyautogui.click(x=960, y=540)
        pyautogui.write("Typing this out like a real human!")
        
        # Press a specific key
        pyautogui.press("enter")
        pyautogui.write("Here is line two.")

        with UIPath(u"||Group->||Custom->||Pane->||Window->||Group->||Group->||Pane->||Group->||Group->||Group->||Group->||Group->||Group->||Group"):
            click(u"||Button#[0,4]")
            click(u"||CheckBox#[1,2]")
            click(u"||CheckBox#[1,3]")
            click(u"B||CheckBox")
            click(u"I||CheckBox")
            click(u"U||Button")
            click(u"S||CheckBox")
            click(u"x₂||CheckBox")
            click(u"No Spacing||CheckBox")
            click(u"Heading 1||CheckBox")
            click(u"Heading 2||CheckBox")
            click(u"Heading 3||CheckBox")
            click(u"Title||CheckBox")
            click(u"Subtitle||CheckBox")
            click(u"Quote||CheckBox")
            click(u"Strong||CheckBox")
            
        with UIPath(u"||Group->||Custom->||Pane->||Window->||Group->||Group"):
            click(u"||Pane->||Group->||Group->||Group->||Group->||Group->||Group->||Group->Emphasis||CheckBox")
            
        with UIPath(u"||Group->||Custom->||Pane->||Window->||Group->||Group->||Group"):
            click(u"Insert||CheckBox")
            click(u"Page Layout||CheckBox")
            click(u"References||CheckBox")
            click(u"Review||CheckBox")
            click(u"View||CheckBox")
            click(u"Tools||CheckBox")