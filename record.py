import ctypes
import argparse
import subprocess
import time
from pathlib import Path
from textwrap import dedent, indent

from pywinauto import Desktop
from pywinauto_recorder.recorder import Recorder


def maximize_window(app):
    window = app.wrapper_object()
    user32 = ctypes.windll.user32

    user32.ShowWindow(window.handle, 3)
    deadline = time.monotonic() + 2
    while not user32.IsZoomed(window.handle):
        if time.monotonic() >= deadline:
            raise RuntimeError("NativeOffice window did not maximize.")
        time.sleep(0.05)

    user32.SetForegroundWindow(window.handle)


def launch_nativeoffice():
    result = subprocess.run(
        [
            "powershell",
            "-NoProfile",
            "-Command",
            "(Get-StartApps 'NativeOffice' | "
            "Select-Object -First 1).AppID",
        ],
        capture_output=True,
        text=True,
    )

    app_id = result.stdout.strip()

    if not app_id:
        raise RuntimeError(
            "NativeOffice was not found in Windows Start-menu apps."
        )

    subprocess.Popen(
        [
            "explorer.exe",
            f"shell:AppsFolder\\{app_id}",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    app = Desktop(backend="uia").window(title="NativeOffice")
    app.wait("visible", timeout=8)
    maximize_window(app)


def normalize_recorded_code(source):
    """Convert recorder output into clean, parseable Python."""
    normalized = source.replace("\r\n", "\n").replace("\r", "\n")
    cleaned = []

    for line in normalized.splitlines():
        stripped = line.strip()

        if not stripped:
            cleaned.append("")
            continue

        if stripped.startswith("#") and "coding" in stripped.lower():
            continue

        cleaned.append(line.expandtabs(4).rstrip())

    return dedent("\n".join(cleaned)).strip("\n")


def convert_to_pytest(recorded_file, output_file):
    source = Path(recorded_file).read_text(
        encoding="utf-8-sig"
    )

    lines = normalize_recorded_code(source).splitlines()

    imports = []
    body = []

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("import ") or stripped.startswith("from "):
            imports.append(line)
        else:
            body.append(line)

    with output_file.open(
        "w",
        encoding="utf-8",
        newline="\n",
    ) as f:

        f.write('"""Auto-generated NativeOffice pytest test."""\n\n')

        for line in imports:
            f.write(line.rstrip() + "\n")

        f.write("\n\n")
        f.write("def test_recorded_actions():\n")

        body_text = "\n".join(body).strip()

        if not body_text:
            f.write("    pass\n")
        else:
            body_text = dedent(body_text).strip("\n")
            f.write(indent(body_text, "    "))
            f.write("\n")


def main():
    parser = argparse.ArgumentParser(
        description="NativeOffice GUI recorder for pytest"
    )

    parser.add_argument(
        "-o",
        "--output",
        required=True,
        help="Output pytest file",
    )

    args = parser.parse_args()

    output = Path(args.output).resolve()
    output.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    recorder_dir = (
        Path.home() / "Pywinauto recorder"
    )

    recorder_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    before = {
        p.resolve(): p.stat().st_mtime
        for p in recorder_dir.glob("*.py")
    }

    print("Launching NativeOffice...")
    launch_nativeoffice()

    time.sleep(0.3)

    print("Starting recorder...")

    recorder = Recorder()
    recorder.start_recording()

    print()
    print("Recording: ON")
    print("Use NativeOffice normally.")
    print("Press Ctrl+Alt+R to STOP recording.")
    print()

    try:
        while recorder.mode == "Record":
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\nStopping recorder...")
        recorder.quit()
        return

    time.sleep(1)

    candidates = [
        p
        for p in recorder_dir.glob("*.py")
        if (
            p.resolve() not in before
            or p.stat().st_mtime
            > before.get(p.resolve(), 0)
        )
    ]

    if not candidates:
        recorder.quit()
        raise RuntimeError(
            "No recorded Python script was produced."
        )

    recorded_file = max(
        candidates,
        key=lambda p: p.stat().st_mtime,
    )

    convert_to_pytest(
        recorded_file,
        output,
    )

    recorder.quit()

    print()
    print("Recording saved:")
    print(output)


if __name__ == "__main__":
    main()