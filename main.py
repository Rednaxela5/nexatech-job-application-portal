# import os
# import sys
# from nexatech_app.__1_apply_home_page import apply_home

# def main():
#     # folder_path = os.path.join(os.path.dirname(__file__), "nexatech-application-form")
#     # script_name = "__1_apply_home_page.py"
#     # script_path = os.path.join(folder_path, script_name)

#     # if os.path.exists(script_path):
#     #     sys.path.append(folder_path)
#     #     script_module = __import__(script_name[:-3])  # Remove the ".py" extension
#     #     if hasattr(script_module, "apply_home") and callable(script_module.apply_home):
#     #         script_module.apply_home()
#     #     else:
#     #         print(f"Function 'apply_home()' not found in '{script_name}'.")
#     # else:
#     #     print(f"Script '{script_name}' not found in the folder.")

#     # main.py

# # Import the function from the specified module
    
#     # Call the apply_home function
#     apply_home()


# if __name__ == "__main__":
#     main()
from pathlib import Path
import sys
import os
import tkinter as tk
from tkinter import ttk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from PIL import Image, ImageTk

# Get the script's directory path
SCRIPT_DIR = Path(sys.argv[0]).resolve().parent

# Set the relative path to the assets directory
ASSETS_PATH = SCRIPT_DIR / "assets" / "apply_frame0"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def apply_home():
    root = tk.Tk()
    root.title("Apply Home")

    # Define image path (using a relative path)
    image_path = "assets/apply_frame0/image_1.png"

    # Load image using PIL
    if os.path.exists(image_path):
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
    else:
        print("Image not found:", image_path)
        root.destroy()
        return

    label = ttk.Label(root, image=photo)
    label.pack()

    root.mainloop()
    

if __name__ == "__main__":
    apply_home()
