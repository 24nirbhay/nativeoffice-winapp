import ctypes
import subprocess
import time
import pytest
from pywinauto import Desktop


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


@pytest.fixture(scope="session", autouse=True)
def nativeoffice():
    # Find NativeOffice in Windows Start Apps
    result = subprocess.run(
        [
            "powershell",
            "-NoProfile",
            "-Command",
            "(Get-StartApps 'NativeOffice' | Select-Object -First 1).AppID"
        ],
        capture_output=True,
        text=True
    )

    app_id = result.stdout.strip()

    if not app_id:
        raise RuntimeError("NativeOffice was not found in Windows Start Apps.")

    # Launch NativeOffice
    subprocess.Popen(
        ["explorer.exe", f"shell:AppsFolder\\{app_id}"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    # Wait for the main window
    app = Desktop(backend="uia").window(title="NativeOffice")
    app.wait("visible", timeout=8)
    maximize_window(app)

    yield app

    # Close NativeOffice after the entire test session
    try:
        app.close()
    except Exception:
        pass
