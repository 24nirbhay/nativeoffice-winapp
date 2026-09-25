import ast

from record import convert_to_pytest


def test_convert_to_pytest_normalizes_indentation(tmp_path):
    recorded = tmp_path / "recorded.py"
    recorded.write_text(
        "from pywinauto_recorder.player import *\n\n"
        "with UIPath(u\"NativeOffice||Window\"):\n"
        "\twith UIPath(u\"||Group\"):\n"
        "\t\tclick(u\"||Group\")\n",
        encoding="utf-8",
    )

    output = tmp_path / "generated_test.py"
    convert_to_pytest(recorded, output)

    code = output.read_text(encoding="utf-8")

    assert "\t" not in code
    ast.parse(code)
