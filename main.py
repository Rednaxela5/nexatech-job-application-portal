import os
import sys

def main():
    folder_path = os.path.join(os.path.dirname(__file__), "nexatech-application-form")
    script_name = "__1_apply_home_page.py"
    script_path = os.path.join(folder_path, script_name)

    if os.path.exists(script_path):
        sys.path.append(folder_path)
        script_module = __import__(script_name[:-3])  # Remove the ".py" extension
        if hasattr(script_module, "apply_home") and callable(script_module.apply_home):
            script_module.apply_home()
        else:
            print(f"Function 'apply_home()' not found in '{script_name}'.")
    else:
        print(f"Script '{script_name}' not found in the folder.")

if __name__ == "__main__":
    main()
