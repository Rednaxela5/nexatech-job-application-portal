import tkinter as tk
from tkinter import filedialog
import os

def patchall(entry_names,entries,names,nameentries,fpp,app):

    new_imgnames = [entry.get() for entry in entries]
    new_nameentries = [nameentry.get() for nameentry in nameentries]
    for i, filename in enumerate(os.listdir(app)):
        if filename.endswith('.png'):
            new_name = os.path.join(app, new_imgnames[i] + '.png')  
            os.rename(os.path.join(app, filename), new_name)
    with open(fpp,'r') as f:
        con = f.read()
    for ename,newename in zip(entry_names,new_imgnames):
        if ename in con:
            newename = newename+'.png'
            print(ename,newename)
            con = con.replace(ename,newename)
    for name,newname in zip(names,new_nameentries):
        if name in con:
            if 'self.' in name:
                con = con.replace(name,'self.'+newname)
            else:
                con = con.replace(name,newname)
    with open(fpp,'w') as f1:
        f1.write(con)
def browse_file_path():
    file_path = filedialog.askopenfile(title="Select GUI",filetypes=(("Py Codes","*.py"),))
    if file_path:
        file_path_label.config(text="" + file_path.name)
    return file_path.name

def browse_assets_path():
    assets_path = filedialog.askdirectory()
    if assets_path:
        assets_path_label.config(text="" + assets_path)
    return assets_path
def create_entries(fpp,app):
    input_dir = app
    with open(fpp,'r') as f:
        contents = f.read()
        f.seek(0)
        lines = f.readlines()
    png_files = [filename for filename in os.listdir(input_dir) if filename.endswith(".png")and not filename.startswith("~$")]
    entry_names = []
    for filename in png_files:
        entry_names.append(filename)
    entries = []
    for i in range(len(png_files)):
        if entry_names[i] in contents:
            label = tk.Label(window,width=25, text=f"{entry_names[i]}")
            label.grid(row=i+2, column=0)
            entry = tk.Entry(window, width=20)
            entry.grid(row=i+2, column=1)
            entry.insert(tk.END,entry_names[i].split(".")[0])
            entries.append(entry)
    names = []
    search = ['Entry','Button','Text','Canvas','PhotoImage']
    for line in lines:
        for item in search:
            if item in line.strip() and 'from' not in line and 'import' not in line:
                names.append(line.split("=")[0].strip())
    nameentries = []
    for i in range(len(names)):
        label = tk.Label(window,width=25, text=f"{names[i]}")
        label.grid(row=i+2, column=2)
        entry = tk.Entry(window, width=20)
        entry.grid(row=i+2, column=3)
        entry.insert(tk.END,names[i].replace("self.",""))
        nameentries.append(entry)
    return entry_names,entries,names,nameentries

# Create the main window
window = tk.Tk()
window.title("Name Patcher")

file_path_label = tk.Label(window, text="File Path:")
file_path_label.grid(row=0,column=0,columnspan=3)

assets_path_label = tk.Label(window, text="Assets Path:")
assets_path_label.grid(row=1,column=0,columnspan=3)
fp = browse_file_path()
ap = browse_assets_path()
entry_names,entries,names,nameentries =create_entries(fp,ap)
patch_but = tk.Button(window,text="Patch",command=lambda: patchall(entry_names,entries,names,nameentries,fp,ap))
patch_but.grid(row=0,column=3)

window.mainloop()