import tkinter as tk
from tkinter import font
import tkinter.ttk as ttk
import os,time,sys
import pickle

def resource_path(relative_path):
	base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
	return os.path.join(base_path, relative_path)
app_icon = resource_path("calc1.ico")
# backspace_key_icon = resource_path("backspace_key_stroke.png")

class DefaultValues(object):
	display_bg_color = "#3b3b3b"
	display_fg_color = "#a8a8a8"
	digits_bg_color = "#e0e0e0"
	digits_fg_color = "#000000"
	digits_bg_active_color = "#AEAEAE"
	math_operators_bg_color = "#f3933d"
	math_operators_fg_color = "#FFFFFF"
	math_operators_bg_active_color = "#CC7B33"
	extra_funcs_bg_color = "#bebebe"
	extra_funcs_fg_color = "#000000"
	extra_funcs_bg_active_color = "#787878"
	mainwindow_alpha = 0.95
	subwindows_alpha = 0.95

class AboutWindow(object):
	def __init__(self, master, windowtitle, alpha):
		self.master = master
		self.windowtitle = windowtitle
		self.alpha = alpha

		self.about_window = tk.Toplevel(self.master)
		self.config_gui()
		self.create_widgets()
		self.about_window.mainloop()

	def config_gui(self):
		self.about_window_bg_color = "#3b3b3b"
		self.label_text_color = "#FFFFFF"

		self.bold = font.Font(family='Segoe UI', size=10, weight="bold")
		self.normal = font.Font(family='Segoe UI Semilight', size=10, weight="normal")

		self.about_window.title(self.windowtitle)
		self.about_window.attributes('-alpha', self.alpha)
		self.about_window.iconbitmap(app_icon)
		self.about_window.configure(bd=5, bg=self.about_window_bg_color)
		self.about_window.geometry("360x60")

	def create_widgets(self):
		self.spiderman_label = tk.Label(self.about_window, text="Created by your friendly neighborhood SpiderMan.", font=self.bold, bg=self.about_window_bg_color, fg=self.label_text_color, anchor=tk.W)
		self.spiderman_label.grid(row=0, column=0, sticky=tk.NSEW)
		self.copyright_label = tk.Label(self.about_window, text="©Marvel Stud.", font=self.bold, bg=self.about_window_bg_color, fg=self.label_text_color, anchor=tk.W)
		self.copyright_label.grid(row=1, column=0, sticky=tk.NSEW)

class ShortcutsWindow(object):
	def __init__(self,  master, windowtitle, alpha):
		self.master = master
		self.windowtitle = windowtitle
		self.alpha = alpha

		self.shortcuts_window = tk.Toplevel(self.master)
		self.config_gui()
		self.create_widgets()
		self.shortcuts_window.mainloop()

	def config_gui(self):
		self.shortcuts_window_bg_color = "#3b3b3b"
		self.label_text_color = "#FFFFFF"

		self.bold_column_header = font.Font(family='Segoe UI', size=10, weight="bold")
		self.normal_column_entry = font.Font(family='Segoe UI Semilight', size=10, weight="normal")

		self.shortcuts_window.title(self.windowtitle)
		self.shortcuts_window.attributes('-alpha', self.alpha)
		self.shortcuts_window.iconbitmap(app_icon)
		self.shortcuts_window.configure(bd=5, bg=self.shortcuts_window_bg_color)

	def create_widgets(self):
		self.key_combination_header_label = tk.Label(self.shortcuts_window, text="Key combination", font=self.bold_column_header, bg=self.shortcuts_window_bg_color, fg=self.label_text_color, relief=tk.SOLID, bd=1, padx=3, pady=3 )
		self.key_combination_header_label.grid(row=0, column=0, sticky=tk.NSEW)

		self.function_header_label = tk.Label(self.shortcuts_window, text="Binding function", font=self.bold_column_header, bg=self.shortcuts_window_bg_color, fg=self.label_text_color, relief=tk.SOLID, bd=1, padx=3, pady=3 )
		self.function_header_label.grid(row=0, column=1, sticky=tk.NSEW)

		self.shortcut1_key_label = tk.Label(self.shortcuts_window, text="<Alt>", font=self.normal_column_entry, bg=self.shortcuts_window_bg_color, fg=self.label_text_color, relief=tk.SOLID, bd=1, padx=3, pady=3 )
		self.shortcut1_key_label.grid(row=1, column=0, sticky=tk.NSEW)
		self.shortcut1_function_label = tk.Label(self.shortcuts_window, text="Show menubar", font=self.normal_column_entry, bg=self.shortcuts_window_bg_color, fg=self.label_text_color, relief=tk.SOLID, bd=1, padx=3, pady=3 )
		self.shortcut1_function_label.grid(row=1, column=1, sticky=tk.NSEW)

		self.shortcut2_key_label = tk.Label(self.shortcuts_window, text="<Ctrl+Alt>", font=self.normal_column_entry, bg=self.shortcuts_window_bg_color, fg=self.label_text_color, relief=tk.SOLID, bd=1, padx=3, pady=3 )
		self.shortcut2_key_label.grid(row=2, column=0, sticky=tk.NSEW)
		self.shortcut2_function_label = tk.Label(self.shortcuts_window, text="Hide menubar", font=self.normal_column_entry, bg=self.shortcuts_window_bg_color, fg=self.label_text_color, relief=tk.SOLID, bd=1, padx=3, pady=3 )
		self.shortcut2_function_label.grid(row=2, column=1, sticky=tk.NSEW)

class PreferenceWindow(object):
	try:
		loaddata = pickle.load(open("preferences.p", "rb"))
		# print("loaded data:")
		# print(loaddata)

		display_bg_color = loaddata[0]
		display_fg_color = loaddata[1]
		digits_bg_color = loaddata[2]
		digits_fg_color = loaddata[3]
		digits_bg_active_color = loaddata[4]
		math_operators_bg_color = loaddata[5]
		math_operators_fg_color = loaddata[6]
		math_operators_bg_active_color = loaddata[7]
		extra_funcs_bg_color = loaddata[8]
		extra_funcs_fg_color = loaddata[9]
		extra_funcs_bg_active_color = loaddata[10]
		mainwindow_alpha = loaddata[11]
		subwindows_alpha = loaddata[12]
	except FileNotFoundError:
		display_bg_color ="#3b3b3b"
		display_fg_color ="#a8a8a8"
		digits_bg_color ="#e0e0e0"
		digits_fg_color = "#000000"
		digits_bg_active_color ="#AEAEAE"
		math_operators_bg_color ="#f3933d"
		math_operators_fg_color ="#FFFFFF"
		math_operators_bg_active_color ="#CC7B33"
		extra_funcs_bg_color ="#bebebe"
		extra_funcs_fg_color ="#000000"
		extra_funcs_bg_active_color = "#787878"
		mainwindow_alpha = 0.95
		subwindows_alpha = 0.95

	def __init__(self, master, windowtitle, alpha):
		self.master = master
		self.windowtitle = windowtitle
		self.alpha = alpha

		self.pref_window = tk.Toplevel(self.master)
		self.config_gui()
		self.create_widgets()
		self.pref_window.mainloop()

	def save_and_close(self):
		# print("Dick")
		PreferenceWindow.display_bg_color = self.display_box_bg_color_entry.get()
		PreferenceWindow.display_fg_color = self.display_box_fg_color_entry.get()
		PreferenceWindow.digits_bg_color = self.digits_bg_color_entry.get()
		PreferenceWindow.digits_fg_color = self.digits_fg_color_entry.get()
		PreferenceWindow.digits_bg_active_color = self.digits_bg_active_color_entry.get()
		PreferenceWindow.math_operators_bg_color = self.math_operators_bg_color_entry.get()
		PreferenceWindow.math_operators_fg_color = self.math_operators_fg_color_entry.get()
		PreferenceWindow.math_operators_bg_active_color = self.math_operators_bg_active_color_entry.get()
		PreferenceWindow.extra_funcs_bg_color = self.extra_funcs_bg_color_entry.get()
		PreferenceWindow.extra_funcs_fg_color = self.extra_funcs_fg_color_entry.get()
		PreferenceWindow.extra_funcs_bg_active_color = self.extra_funcs_bg_active_color_entry.get()
		PreferenceWindow.mainwindow_alpha = self.mainwindow_alpha_entry.get()
		PreferenceWindow.subwindows_alpha = self.subwindow_alpha_entry.get()

		savedata = (PreferenceWindow.display_bg_color,
			PreferenceWindow.display_fg_color,
			PreferenceWindow.digits_bg_color,
			PreferenceWindow.digits_fg_color,
			PreferenceWindow.digits_bg_active_color,
			PreferenceWindow.math_operators_bg_color,
			PreferenceWindow.math_operators_fg_color,
			PreferenceWindow.math_operators_bg_active_color,
			PreferenceWindow.extra_funcs_bg_color,
			PreferenceWindow.extra_funcs_fg_color,
			PreferenceWindow.extra_funcs_bg_active_color,
			PreferenceWindow.mainwindow_alpha,
			PreferenceWindow.subwindows_alpha)

		pickle.dump(savedata, open("preferences.p", "wb"))
		self.pref_window.destroy()


	def config_gui(self):
		self.pref_window_bg_color = "#3b3b3b"
		self.label_text_color = "#FFFFFF"

		self.pref_window.title(self.windowtitle)
		self.pref_window.attributes('-alpha', self.alpha)
		self.pref_window.iconbitmap(app_icon)
		self.pref_window.configure(bd=5, bg=self.pref_window_bg_color)

	def create_widgets(self):
		self.heading_label = tk.Label(self.pref_window, bg=self.pref_window_bg_color, fg=self.label_text_color, text="Change setting as required. Changes will take place after restarting the Calculator")
		self.heading_label.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW)

		## DISPLAY BOX SETTINGS
		self.display_box_bg_color_label = tk.Label(self.pref_window, bg=self.pref_window_bg_color, fg=self.label_text_color, text="Display Box BG Color : ", anchor=tk.W)
		self.display_box_bg_color_label.grid(row=1, column=0, sticky=tk.NSEW)
		self.display_box_fg_color_label = tk.Label(self.pref_window, bg=self.pref_window_bg_color, fg=self.label_text_color, text="Display Box FG Color : ", anchor=tk.W)
		self.display_box_fg_color_label.grid(row=2, column=0, sticky=tk.NSEW)

		self.display_box_bg_color_entry = tk.Entry(self.pref_window, bg=self.pref_window_bg_color, fg=self.label_text_color,)
		self.display_box_bg_color_entry.grid(row=1, column=1, sticky=tk.NSEW)
		self.display_box_fg_color_entry = tk.Entry(self.pref_window, bg=self.pref_window_bg_color, fg=self.label_text_color,)
		self.display_box_fg_color_entry.grid(row=2, column=1, sticky=tk.NSEW)

		self.display_box_bg_color_entry.insert(tk.END, PreferenceWindow.display_bg_color)
		self.display_box_fg_color_entry.insert(tk.END, PreferenceWindow.display_fg_color)

		## DIGIT BUTTONS SETTINGS
		self.digits_bg_color_label = tk.Label(self.pref_window, bg=self.pref_window_bg_color, fg=self.label_text_color, text="Digits (0-9.) BG Color : ", anchor=tk.W)
		self.digits_bg_color_label.grid(row=3, column=0, sticky=tk.NSEW)
		self.digits_fg_color_label = tk.Label(self.pref_window, bg=self.pref_window_bg_color, fg=self.label_text_color, text="Digits (0-9.) FG Color : ", anchor=tk.W)
		self.digits_fg_color_label.grid(row=4, column=0, sticky=tk.NSEW)
		self.digits_bg_active_color_label = tk.Label(self.pref_window, bg=self.pref_window_bg_color, fg=self.label_text_color, text="Digits (0-9.) Pressed BG Color : ", anchor=tk.W)
		self.digits_bg_active_color_label.grid(row=5, column=0, sticky=tk.NSEW)

		self.digits_bg_color_entry = tk.Entry(self.pref_window, bg=self.pref_window_bg_color, fg=self.label_text_color,)
		self.digits_bg_color_entry.grid(row=3, column=1, sticky=tk.NSEW)
		self.digits_fg_color_entry = tk.Entry(self.pref_window, bg=self.pref_window_bg_color, fg=self.label_text_color,)
		self.digits_fg_color_entry.grid(row=4, column=1, sticky=tk.NSEW)
		self.digits_bg_active_color_entry = tk.Entry(self.pref_window, bg=self.pref_window_bg_color, fg=self.label_text_color,)
		self.digits_bg_active_color_entry.grid(row=5, column=1, sticky=tk.NSEW)

		self.digits_bg_color_entry.insert(tk.END, PreferenceWindow.digits_bg_color)
		self.digits_fg_color_entry.insert(tk.END, PreferenceWindow.digits_fg_color)
		self.digits_bg_active_color_entry.insert(tk.END, PreferenceWindow.digits_bg_active_color)

		## MATH OPERATOR BUTTONS SETTINGS
		self.math_operators_bg_color_label = tk.Label(self.pref_window, bg=self.pref_window_bg_color, fg=self.label_text_color, text="Operators (+×-÷) BG Color : ", anchor=tk.W)
		self.math_operators_bg_color_label.grid(row=6, column=0, sticky=tk.NSEW)
		self.math_operators_fg_color_label = tk.Label(self.pref_window, bg=self.pref_window_bg_color, fg=self.label_text_color, text="Operators (+×-÷) FG Color : ", anchor=tk.W)
		self.math_operators_fg_color_label.grid(row=7, column=0, sticky=tk.NSEW)
		self.math_operators_bg_active_color_label = tk.Label(self.pref_window, bg=self.pref_window_bg_color, fg=self.label_text_color, text="Operators (+×-÷) Pressed BG Color : ", anchor=tk.W)
		self.math_operators_bg_active_color_label.grid(row=8, column=0, sticky=tk.NSEW)

		self.math_operators_bg_color_entry = tk.Entry(self.pref_window, bg=self.pref_window_bg_color, fg=self.label_text_color,)
		self.math_operators_bg_color_entry.grid(row=6, column=1, sticky=tk.NSEW)
		self.math_operators_fg_color_entry = tk.Entry(self.pref_window, bg=self.pref_window_bg_color, fg=self.label_text_color,)
		self.math_operators_fg_color_entry.grid(row=7, column=1, sticky=tk.NSEW)
		self.math_operators_bg_active_color_entry = tk.Entry(self.pref_window, bg=self.pref_window_bg_color, fg=self.label_text_color,)
		self.math_operators_bg_active_color_entry.grid(row=8, column=1, sticky=tk.NSEW)

		self.math_operators_bg_color_entry.insert(tk.END, PreferenceWindow.math_operators_bg_color)
		self.math_operators_fg_color_entry.insert(tk.END, PreferenceWindow.math_operators_fg_color)
		self.math_operators_bg_active_color_entry.insert(tk.END, PreferenceWindow.math_operators_bg_active_color)

		## EXTRA FUNCTIONS BUTTONS SETTINGS
		self.extra_funcs_bg_color_label = tk.Label(self.pref_window, bg=self.pref_window_bg_color, fg=self.label_text_color, text="Extra functions BG Color : ", anchor=tk.W)
		self.extra_funcs_bg_color_label.grid(row=9, column=0, sticky=tk.NSEW)
		self.extra_funcs_fg_color_label = tk.Label(self.pref_window, bg=self.pref_window_bg_color, fg=self.label_text_color, text="Extra functions FG Color : ", anchor=tk.W)
		self.extra_funcs_fg_color_label.grid(row=10, column=0, sticky=tk.NSEW)
		self.extra_funcs_bg_active_color_label = tk.Label(self.pref_window, bg=self.pref_window_bg_color, fg=self.label_text_color, text="Extra functions Pressed BG Color : ", anchor=tk.W)
		self.extra_funcs_bg_active_color_label.grid(row=11, column=0, sticky=tk.NSEW)

		self.extra_funcs_bg_color_entry = tk.Entry(self.pref_window, bg=self.pref_window_bg_color, fg=self.label_text_color,)
		self.extra_funcs_bg_color_entry.grid(row=9, column=1, sticky=tk.NSEW)
		self.extra_funcs_fg_color_entry = tk.Entry(self.pref_window, bg=self.pref_window_bg_color, fg=self.label_text_color,)
		self.extra_funcs_fg_color_entry.grid(row=10, column=1, sticky=tk.NSEW)
		self.extra_funcs_bg_active_color_entry = tk.Entry(self.pref_window, bg=self.pref_window_bg_color, fg=self.label_text_color,)
		self.extra_funcs_bg_active_color_entry.grid(row=11, column=1, sticky=tk.NSEW)

		self.extra_funcs_bg_color_entry.insert(tk.END, PreferenceWindow.extra_funcs_bg_color)
		self.extra_funcs_fg_color_entry.insert(tk.END, PreferenceWindow.extra_funcs_fg_color)
		self.extra_funcs_bg_active_color_entry.insert(tk.END, PreferenceWindow.extra_funcs_bg_active_color)

		## TRANSPARENCY SETTINGS
		self.mainwindow_alpha_label = tk.Label(self.pref_window, bg=self.pref_window_bg_color, fg=self.label_text_color, text="Calculator transprency : ", anchor=tk.W)
		self.mainwindow_alpha_label.grid(row=12, column=0, sticky=tk.NSEW)
		self.subwindow_alpha_label = tk.Label(self.pref_window, bg=self.pref_window_bg_color, fg=self.label_text_color, text="Subwindow transprency : ", anchor=tk.W)
		self.subwindow_alpha_label.grid(row=13, column=0, sticky=tk.NSEW)

		self.mainwindow_alpha_entry = tk.Entry(self.pref_window, bg=self.pref_window_bg_color, fg=self.label_text_color,)
		self.mainwindow_alpha_entry.grid(row=12, column=1, sticky=tk.NSEW)
		self.subwindow_alpha_entry = tk.Entry(self.pref_window, bg=self.pref_window_bg_color, fg=self.label_text_color,)
		self.subwindow_alpha_entry.grid(row=13, column=1, sticky=tk.NSEW)

		self.mainwindow_alpha_entry.insert(tk.END, PreferenceWindow.mainwindow_alpha)
		self.subwindow_alpha_entry.insert(tk.END, PreferenceWindow.subwindows_alpha)

		## SAVE AND CLOSE BUTTON
		self.save_and_close_button = tk.Button(self.pref_window, text="Save & Close", command=self.save_and_close, bg=self.pref_window_bg_color, fg=self.label_text_color,)
		self.save_and_close_button.grid(row=14, column=1, sticky=tk.E)

class MainApplication(object):

	def __init__(self, *args, **kwargs):
		self.master = tk.Tk()
		self.operator = ""
		self.text_input = tk.StringVar()
		self.config_gui()
		self.create_widgets()
		self.button_list = (self.clear_button, self.backspace, self.square_button, self.divide_button, self.open_bracket, self.seven_button, self.eight_button, self.nine_button, self.prod_button, self.close_bracket, self.four_button, self.five_button, self.six_button, self.minus_button, self.raised_to, self.one_button, self.two_button, self.three_button, self.plus_button, self.reciprocal, self.zero_button, self.point_button, self.equal_button, self.signinv_button)

	def buttonClick(self, numbers):
		self.display_box.icursor("end")
		self.operator = self.display_box.get() + str(numbers)
		self.text_input.set(self.operator)
		self.display_box.icursor("end")

	def clearButton(self):
		self.operator = ""
		self.text_input.set("")

	def equateButton(self):
		self.result = str(eval(self.operator.replace("×","*").replace("÷","/").replace("^","**").replace("²","**2").replace("⁻¹","**(-1)")))
		self.text_input.set(self.result)

	def signinv(self):
		self.text_input.set(str(-float(self.display_box.get())))

	def backspace(self):
		temp = self.display_box.get()[:-1]
		self.display_box.delete(0, tk.END)
		self.display_box.insert(tk.END, temp)
		del temp

	def keep_flat(self, event):
		if event.widget in self.button_list:
			event.widget.config(relief=tk.FLAT)

	def start(self):
		self.master.mainloop()

	def preferences(self):
		self.pref_window = PreferenceWindow(self.master, "User preferences", alpha=self.subwindows_alpha)

	def revert2default(self):
		PreferenceWindow.display_bg_color = DefaultValues.display_bg_color
		PreferenceWindow.display_fg_color = DefaultValues.display_fg_color
		PreferenceWindow.digits_bg_color = DefaultValues.digits_bg_color
		PreferenceWindow.digits_fg_color = DefaultValues.digits_fg_color
		PreferenceWindow.digits_bg_active_color = DefaultValues.digits_bg_active_color
		PreferenceWindow.math_operators_bg_color = DefaultValues.math_operators_bg_color
		PreferenceWindow.math_operators_fg_color = DefaultValues.math_operators_fg_color
		PreferenceWindow.math_operators_bg_active_color = DefaultValues.math_operators_bg_active_color
		PreferenceWindow.extra_funcs_bg_color = DefaultValues.extra_funcs_bg_color
		PreferenceWindow.extra_funcs_fg_color = DefaultValues.extra_funcs_fg_color
		PreferenceWindow.extra_funcs_bg_active_color = DefaultValues.extra_funcs_bg_active_color
		PreferenceWindow.mainwindow_alpha = DefaultValues.mainwindow_alpha
		PreferenceWindow.subwindows_alpha = DefaultValues.subwindows_alpha

		savedata = (PreferenceWindow.display_bg_color,
			PreferenceWindow.display_fg_color,
			PreferenceWindow.digits_bg_color,
			PreferenceWindow.digits_fg_color,
			PreferenceWindow.digits_bg_active_color,
			PreferenceWindow.math_operators_bg_color,
			PreferenceWindow.math_operators_fg_color,
			PreferenceWindow.math_operators_bg_active_color,
			PreferenceWindow.extra_funcs_bg_color,
			PreferenceWindow.extra_funcs_fg_color,
			PreferenceWindow.extra_funcs_bg_active_color,
			PreferenceWindow.mainwindow_alpha,
			PreferenceWindow.subwindows_alpha)

		pickle.dump(savedata, open("preferences.p", "wb"))

	def shortcuts(self):
		self.shortcuts_window = ShortcutsWindow(self.master, "Shortcuts", alpha=self.subwindows_alpha)

	def about_calc(self):
		self.about_window = AboutWindow(self.master, "Kaunsa c****ya banaaya yeh tatti?", alpha=self.subwindows_alpha)

	def show_menu(self, event):
		self.emptyMenu = None
		self.menubar = tk.Menu(self.master)

		self.optionsmenu = tk.Menu(self.menubar, tearoff=0)
		self.menubar.add_cascade(label="Options", menu=self.optionsmenu)
		self.optionsmenu.add_command(label="Preferences", command=self.preferences)
		self.optionsmenu.add_command(label="Revert to default settings", command=self.revert2default)
		self.optionsmenu.add_separator()
		self.optionsmenu.add_command(label="Hide menubar", command=self.hide_menu)

		self.helpmenu = tk.Menu(self.menubar, tearoff=0)
		self.menubar.add_cascade(label="Help", menu=self.helpmenu)
		self.helpmenu.add_command(label="Shortcuts", command=self.shortcuts)
		self.helpmenu.add_separator()
		self.helpmenu.add_command(label="About", command=self.about_calc)
		self.master.config(menu=self.menubar)

	def hide_menu(self):
		self.emptyMenu = tk.Menu(self.master)
		self.master.config(menu=self.emptyMenu)

	def hide_menu_binding(self, event):
		self.emptyMenu = tk.Menu(self.master)
		self.master.config(menu=self.emptyMenu)

	def config_gui(self):
		# Colors
		# backgrounds
		self.display_bg_color = PreferenceWindow.display_bg_color
		self.math_operators_bg_color = PreferenceWindow.math_operators_bg_color
		self.math_operators_bg_active_color = PreferenceWindow.math_operators_bg_active_color
		self.digits_bg_color = PreferenceWindow.digits_bg_color
		self.digits_bg_active_color = PreferenceWindow.digits_bg_active_color
		self.extra_funcs_bg_color = PreferenceWindow.extra_funcs_bg_color
		self.extra_funcs_bg_active_color = PreferenceWindow.extra_funcs_bg_active_color
		# foregrounds
		self.display_fg_color = PreferenceWindow.display_fg_color
		self.math_operators_fg_color = PreferenceWindow.math_operators_fg_color
		self.digits_fg_color = PreferenceWindow.digits_fg_color
		self.extra_funcs_fg_color = PreferenceWindow.extra_funcs_fg_color
		# Window transparency
		self.mainwindow_alpha = PreferenceWindow.mainwindow_alpha
		self.subwindows_alpha = PreferenceWindow.subwindows_alpha

		# Fonts
		self.LightFontface = font.Font(family='HelveticaNeueLT Com 25 UltLt', size=25, weight="normal")
		self.DisplayFontface = font.Font(family='HelveticaNeueLT Com 25 UltLt', size=40, weight="normal")
		self.smallLightFontface = font.Font(family='HelveticaNeueLT Com 25 UltLt', size=15, weight="normal")
		# self.LightFontface = font.Font(family='SF Pro Display', size=30, weight="normal")
		# self.DisplayFontface = font.Font(family='SF Pro Display', size=50, weight="normal")
		# self.smallLightFontface = font.Font(family='SF Pro Display', size=25, weight="normal")

		# Images
		# self.image_backspace_key = tk.PhotoImage(file=backspace_key_icon)

		self.master.configure(bd=0, bg=self.display_bg_color)
		self.master.title("Aashay's Calculator")
		self.master.resizable(False, False)
		self.master.attributes('-alpha', self.mainwindow_alpha)
		self.master.iconbitmap(app_icon)

	def create_widgets(self):
		# Set parameters
		self.normal_button_height = 1
		self.normal_button_width = 2
		self.button_padx = 1
		self.button_pady = 1

		# Frame for Display Box
		display_frame = tk.Frame(self.master)
		display_frame.grid(row=0, column=0, columnspan=5, sticky=tk.NSEW)

		# Display Box
		self.display_box = tk.Entry(display_frame, textvariable=self.text_input, insertbackground=self.math_operators_bg_color, width=11, relief=tk.FLAT, bg=self.display_bg_color, fg=self.display_fg_color, font=self.DisplayFontface, justify="right")
		self.display_box.grid(row=0, column=0, columnspan=5, sticky=tk.NSEW)
		# self.display_box.tag_configure("right", justify="right")

		# Row 1
		self.clear_button = tk.Button(self.master, text="C", height=self.normal_button_height, width=self.normal_button_width, font=self.smallLightFontface, relief=tk.FLAT, bg=self.extra_funcs_bg_color, activebackground=self.extra_funcs_bg_active_color, command=self.clearButton)
		self.clear_button.grid(row=1, column=0, sticky=tk.NSEW, padx=self.button_padx, pady=self.button_pady)
		self.master.bind('<Button-1>', self.keep_flat)

		self.backspace = tk.Button(self.master, text="DEL", height=self.normal_button_height, width=self.normal_button_width, font=self.smallLightFontface, relief=tk.FLAT, bg=self.extra_funcs_bg_color, activebackground=self.extra_funcs_bg_active_color, command=self.backspace)
		self.backspace.grid(row=1, column=1, sticky=tk.NSEW, padx=self.button_padx, pady=self.button_pady)
		self.master.bind('<Button-1>', self.keep_flat)

		self.square_button = tk.Button(self.master, text="x²", height=self.normal_button_height, width=self.normal_button_width, font=self.smallLightFontface, relief=tk.FLAT, bg=self.extra_funcs_bg_color,  activebackground=self.extra_funcs_bg_active_color, command=lambda: self.buttonClick("²"))
		self.square_button.grid(row=1, column=2, sticky=tk.NSEW, padx=self.button_padx, pady=self.button_pady)
		self.master.bind('<Button-1>', self.keep_flat)

		self.divide_button = tk.Button(self.master, text="÷", height=self.normal_button_height, width=self.normal_button_width, font=self.LightFontface, relief=tk.FLAT, command=lambda: self.buttonClick("÷"), bg=self.math_operators_bg_color, fg=self.math_operators_fg_color, activebackground=self.math_operators_bg_active_color, activeforeground=self.math_operators_fg_color)
		self.divide_button.grid(row=1, column=3, sticky=tk.NSEW, padx=self.button_padx, pady=self.button_pady)
		self.master.bind('<Button-1>', self.keep_flat)

		self.open_bracket = tk.Button(self.master, text="(", height=self.normal_button_height, padx=8, width=self.normal_button_width, font=self.smallLightFontface, relief=tk.FLAT, command=lambda: self.buttonClick("("), bg=self.extra_funcs_bg_color, fg=self.extra_funcs_fg_color, activebackground=self.extra_funcs_bg_active_color, activeforeground="#385646")
		self.open_bracket.grid(row=1, column=4, sticky=tk.NSEW, padx=self.button_padx, pady=self.button_pady)
		self.master.bind('<Button-1>', self.keep_flat)

		# Row 2
		self.seven_button = tk.Button(self.master, text="7", height=self.normal_button_height, width=self.normal_button_width, activebackground=self.digits_bg_active_color, bg=self.digits_bg_color, fg=self.digits_fg_color, font=self.LightFontface, relief=tk.FLAT, command=lambda: self.buttonClick(7))
		self.seven_button.grid(row=2, column=0, sticky=tk.NSEW, padx=self.button_padx, pady=self.button_pady)
		self.master.bind('<Button-1>', self.keep_flat)

		self.eight_button = tk.Button(self.master, text="8", height=self.normal_button_height, width=self.normal_button_width, activebackground=self.digits_bg_active_color, bg=self.digits_bg_color, fg=self.digits_fg_color, font=self.LightFontface, relief=tk.FLAT, command=lambda: self.buttonClick(8))
		self.eight_button.grid(row=2, column=1, sticky=tk.NSEW, padx=self.button_padx, pady=self.button_pady)
		self.master.bind('<Button-1>', self.keep_flat)

		self.nine_button = tk.Button(self.master, text="9", height=self.normal_button_height, width=self.normal_button_width, activebackground=self.digits_bg_active_color, bg=self.digits_bg_color, fg=self.digits_fg_color, font=self.LightFontface, relief=tk.FLAT, command=lambda: self.buttonClick(9))
		self.nine_button.grid(row=2, column=2, sticky=tk.NSEW, padx=self.button_padx, pady=self.button_pady)
		self.master.bind('<Button-1>', self.keep_flat)

		self.prod_button = tk.Button(self.master, text="×", height=self.normal_button_height, width=self.normal_button_width, font=self.LightFontface, relief=tk.FLAT, command=lambda: self.buttonClick("×"), bg=self.math_operators_bg_color, fg=self.math_operators_fg_color, activebackground=self.math_operators_bg_active_color, activeforeground=self.math_operators_fg_color)
		self.prod_button.grid(row=2, column=3, sticky=tk.NSEW, padx=self.button_padx, pady=self.button_pady)
		self.master.bind('<Button-1>', self.keep_flat)

		self.close_bracket = tk.Button(self.master, text=")", height=self.normal_button_height, padx=8, width=self.normal_button_width, font=self.smallLightFontface, relief=tk.FLAT, command=lambda: self.buttonClick(")"), bg=self.extra_funcs_bg_color, fg=self.extra_funcs_fg_color, activebackground=self.extra_funcs_bg_active_color, activeforeground="#385646")
		self.close_bracket.grid(row=2, column=4, sticky=tk.NSEW, padx=self.button_padx, pady=self.button_pady)

		# Row 3
		self.four_button = tk.Button(self.master, text="4", height=self.normal_button_height, width=self.normal_button_width, activebackground=self.digits_bg_active_color, bg=self.digits_bg_color, fg=self.digits_fg_color, font=self.LightFontface, relief=tk.FLAT, command=lambda: self.buttonClick(4))
		self.four_button.grid(row=3, column=0, sticky=tk.NSEW, padx=self.button_padx, pady=self.button_pady)
		self.master.bind('<Button-1>', self.keep_flat)

		self.five_button = tk.Button(self.master, text="5", height=self.normal_button_height, width=self.normal_button_width, activebackground=self.digits_bg_active_color, bg=self.digits_bg_color, fg=self.digits_fg_color, font=self.LightFontface, relief=tk.FLAT, command=lambda: self.buttonClick(5))
		self.five_button.grid(row=3, column=1, sticky=tk.NSEW, padx=self.button_padx, pady=self.button_pady)
		self.master.bind('<Button-1>', self.keep_flat)

		self.six_button = tk.Button(self.master, text="6", height=self.normal_button_height, width=self.normal_button_width, activebackground=self.digits_bg_active_color, bg=self.digits_bg_color, fg=self.digits_fg_color, font=self.LightFontface, relief=tk.FLAT, command=lambda: self.buttonClick(6))
		self.six_button.grid(row=3, column=2, sticky=tk.NSEW, padx=self.button_padx, pady=self.button_pady)
		self.master.bind('<Button-1>', self.keep_flat)

		self.minus_button = tk.Button(self.master, text="–", height=self.normal_button_height, width=self.normal_button_width, font=self.LightFontface, relief=tk.FLAT, command=lambda: self.buttonClick("-"), bg=self.math_operators_bg_color, fg=self.math_operators_fg_color, activebackground=self.math_operators_bg_active_color, activeforeground=self.math_operators_fg_color)
		self.minus_button.grid(row=3, column=3, sticky=tk.NSEW, padx=self.button_padx, pady=self.button_pady)
		self.master.bind('<Button-1>', self.keep_flat)

		self.raised_to = tk.Button(self.master, text="^", height=self.normal_button_height, padx=8, width=self.normal_button_width, font=self.smallLightFontface, relief=tk.FLAT, command=lambda: self.buttonClick("^"), bg=self.extra_funcs_bg_color, fg=self.extra_funcs_fg_color, activebackground=self.extra_funcs_bg_active_color, activeforeground="#385646")
		self.raised_to.grid(row=3, column=4, sticky=tk.NSEW, padx=self.button_padx, pady=self.button_pady)
		self.master.bind('<Button-1>', self.keep_flat)

		# Row 4
		self.one_button = tk.Button(self.master, text="1", height=self.normal_button_height, width=self.normal_button_width, activebackground=self.digits_bg_active_color, bg=self.digits_bg_color, fg=self.digits_fg_color, font=self.LightFontface, relief=tk.FLAT, command=lambda: self.buttonClick(1))
		self.one_button.grid(row=4, column=0, sticky=tk.NSEW, padx=self.button_padx, pady=self.button_pady)
		self.master.bind('<Button-1>', self.keep_flat)

		self.two_button = tk.Button(self.master, text="2", height=self.normal_button_height, width=self.normal_button_width, activebackground=self.digits_bg_active_color, bg=self.digits_bg_color, fg=self.digits_fg_color, font=self.LightFontface, relief=tk.FLAT, command=lambda: self.buttonClick(2))
		self.two_button.grid(row=4, column=1, sticky=tk.NSEW, padx=self.button_padx, pady=self.button_pady)
		self.master.bind('<Button-1>', self.keep_flat)

		self.three_button = tk.Button(self.master, text="3", height=self.normal_button_height, width=self.normal_button_width, activebackground=self.digits_bg_active_color, bg=self.digits_bg_color, fg=self.digits_fg_color, font=self.LightFontface, relief=tk.FLAT, command=lambda: self.buttonClick(3))
		self.three_button.grid(row=4, column=2, sticky=tk.NSEW, padx=self.button_padx, pady=self.button_pady)
		self.master.bind('<Button-1>', self.keep_flat)

		self.plus_button = tk.Button(self.master, text="+", height=self.normal_button_height, width=self.normal_button_width, font=self.LightFontface, relief=tk.FLAT, command=lambda: self.buttonClick("+"), bg=self.math_operators_bg_color, fg=self.math_operators_fg_color, activebackground=self.math_operators_bg_active_color, activeforeground=self.math_operators_fg_color)
		self.plus_button.grid(row=4, column=3, sticky=tk.NSEW, padx=self.button_padx, pady=self.button_pady)
		self.master.bind('<Button-1>', self.keep_flat)

		self.reciprocal = tk.Button(self.master, text="1/x", height=self.normal_button_height, padx=8, width=self.normal_button_width, font=self.smallLightFontface, relief=tk.FLAT, command=lambda: self.buttonClick("⁻¹"), bg=self.extra_funcs_bg_color, fg=self.extra_funcs_fg_color, activebackground=self.extra_funcs_bg_active_color, activeforeground="#385646")
		self.reciprocal.grid(row=4, column=4, sticky=tk.NSEW, padx=self.button_padx, pady=self.button_pady)
		self.master.bind('<Button-1>', self.keep_flat)

		# Row 5
		self.zero_button = tk.Button(self.master, text="0", padx=19, height=self.normal_button_height, activebackground=self.digits_bg_active_color, bg=self.digits_bg_color, fg=self.digits_fg_color, font=self.LightFontface, relief=tk.FLAT, command=lambda: self.buttonClick(0), anchor=tk.W)
		self.zero_button.grid(row=5, column=0, columnspan=2, sticky=tk.NSEW, padx=self.button_padx, pady=self.button_pady)
		self.master.bind('<Button-1>', self.keep_flat)

		self.point_button = tk.Button(self.master, text=".", height=self.normal_button_height, activebackground=self.digits_bg_active_color, bg=self.digits_bg_color, width=self.normal_button_width, fg=self.digits_fg_color, font=self.LightFontface, relief=tk.FLAT, command=lambda: self.buttonClick("."))
		self.point_button.grid(row=5, column=2, sticky=tk.NSEW, padx=self.button_padx, pady=self.button_pady)
		self.master.bind('<Button-1>', self.keep_flat)

		self.equal_button = tk.Button(self.master, text="=", height=self.normal_button_height, width=self.normal_button_width, font=self.LightFontface, relief=tk.FLAT, bg=self.math_operators_bg_color, fg=self.math_operators_fg_color, activebackground=self.math_operators_bg_active_color, activeforeground=self.math_operators_fg_color, command=self.equateButton)
		self.equal_button.grid(row=5, column=3, sticky=tk.NSEW, padx=self.button_padx, pady=self.button_pady)
		self.master.bind('<Button-1>', self.keep_flat)

		self.signinv_button = tk.Button(self.master, text="+/-", height=self.normal_button_height, padx=8, width=self.normal_button_width, font=self.smallLightFontface, relief=tk.FLAT, bg=self.extra_funcs_bg_color, fg=self.extra_funcs_fg_color, activebackground=self.extra_funcs_bg_active_color, command=self.signinv)
		self.signinv_button.grid(row=5, column=4, sticky=tk.NSEW, padx=self.button_padx, pady=self.button_pady)

		## ALL EXTRA KEY BINDINGS
		self.master.bind('<Alt_L>', self.show_menu)
		self.master.bind('<Control-Alt_L>', self.hide_menu_binding)

if __name__ == "__main__":
	app = MainApplication()
	app.start()