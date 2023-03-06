from tkinter import messagebox
from tkinter import filedialog
from tkinter import colorchooser




#messagebox.showwarning('Titulek', 'Sorry Error!')

#odpoved = messagebox.askokcancel('Titulek', 'Otazka..?')
#print(odpoved)

print(colorchooser.askcolor())

odpoved = filedialog.askopenfile()
print(odpoved)