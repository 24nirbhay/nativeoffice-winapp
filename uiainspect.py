from pywinauto import Desktop

app = Desktop(backend="uia").window(title="NativeOffice")

for control in app.descendants():
    try:
        print(
            f"TYPE={control.element_info.control_type} | "
            f"NAME={control.window_text()} | "
            f"AUTO_ID={control.element_info.automation_id} | "
            f"CLASS={control.element_info.class_name}"
        )
    except Exception:
        pass