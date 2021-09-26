import os
import threading
import PIL
import PIL.Image
import base64
try:
    import tkinter as tk
    import tkinter.filedialog
    import tkinter.messagebox
except:
    import Tkinter as tk
import tkinter.ttk as ttk


icon = """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"
"""
icondata= base64.b64decode(icon)
tempFile= "icon.ico"
iconfile= open(tempFile, "wb")
iconfile.write(icondata)
iconfile.close()


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.formats = ['BMP', 'DIB', 'EPS', 'GIF', 'ICO', 'IM', 'JFIF', 'JPEG', 'PCX', 'PNG', 'PPM', 
                        'SGI', 'TGA', 'TIFF']
        self.transparency_enabled = ['BMP', 'GIF', 'ICO', 'PNG', 'SVG', 'TIFF']

        # INPUT DIRECTORY
        self.input_directory = tk.StringVar()
        self.input_directory_label = tk.Label(root, text="Input Directory:")
        self.input_directory_box = tk.Entry(root, textvariable=self.input_directory, width=25)
        self.input_directory_button = tk.Button(root, text="Browse", command= lambda: 
                                                self.set_directory(self.input_directory))

        # OUTPUT DIRECTORY
        self.output_directory = tk.StringVar()
        self.output_directory_label = tk.Label(root, text="Output Directory:")
        self.output_directory_box = tk.Entry(root, textvariable=self.output_directory, width=25)
        self.output_directory_button = tk.Button(root, text="Browse", command= lambda: 
                                                self.set_directory(self.output_directory))

        # INPUT FILE
        self.input_file = tk.StringVar()
        self.input_file_label = tk.Label(text="Convert from:")
        self.input_file_extension = tk.OptionMenu(root, self.input_file, *self.formats, 
                                                command=self.check_transparency)

        # OUTPUT FILE
        self.output_file = tk.StringVar()
        self.output_file_label = tk.Label(text="Convert to:")
        self.output_file_extension = tk.OptionMenu(root, self.output_file, *self.formats)
        
        # QUALITY
        self.quality = tk.IntVar()
        self.quality.set(100)
        self.quality_label = tk.Label(text="Quality:")
        self.quality_box = tk.Entry(root, textvariable=self.quality, width=3)

        # DELETE ORIGINAL
        self.delete_original = tk.BooleanVar()
        self.delete_original.set(False)
        self.delete_original_button = tk.Checkbutton(root, text="Delete Original",
                                                    variable=self.delete_original)
        
        # TRANSPARENCY
        self.transparency = tk.BooleanVar()
        self.transparency.set(False)
        self.transparency_button = tk.Checkbutton(root, text="Preserve Transparency", 
                                                variable=self.transparency, 
                                                command=self.set_transparency)

        # RENAME
        self.rename = tk.BooleanVar()
        self.rename.set(False)
        self.rename_button = tk.Checkbutton(root, text="Rename Files", variable=self.rename,
                                            command=self.set_rename)
        self.new_name = tk.StringVar()
        self.namebox_label = tk.Label(root, text="Filename:", state='disabled')
        self.namebox = tk.Entry(root, textvariable=self.new_name, width=20, state='disabled')

        # RESIZE
        self.resize = tk.BooleanVar()
        self.resize.set(False)
        self.resize_button = tk.Checkbutton(root, text="Resize Files", variable=self.resize,
                                            command=self.set_resize)
        self.width = tk.IntVar()
        self.height = tk.IntVar()
        self.size_label_frame = tk.Frame(root)
        self.size_box_frame = tk.Frame(root)
        self.width_label = tk.Label(self.size_label_frame, text="Width:", state='disabled')
        self.height_label = tk.Label(self.size_label_frame, text="Height:", state='disabled')
        self.width_box = tk.Entry(self.size_box_frame, textvariable=self.width, width=5,
                                    state='disabled')
        self.height_box = tk.Entry(self.size_box_frame, textvariable=self.height, width=5,
                                    state='disabled')

        # ASPECT RATIO
        self.aspect_ratio = tk.BooleanVar()
        self.aspect_ratio.set(False)
        self.aspect_ratio_button = tk.Checkbutton(root, text="Preserve Aspect Ratio",
                                                variable=self.aspect_ratio, state='disabled')

        # OPTIMIZATION
        self.optimization = tk.BooleanVar()
        self.optimization.set(False)
        self.optimization_button = tk.Checkbutton(root, text="Optimize Files", 
                                                variable=self.optimization)
        
        # ANTIALIASING
        self.antialiasing = tk.BooleanVar()
        self.antialiasing.set(False)
        self.antialiasing_button = tk.Checkbutton(root, text="Antialiasing", 
                                                variable=self.antialiasing, state="disabled")

        # PROGRESS BAR
        self.progressbar = ttk.Progressbar(root, orient="horizontal", mode="determinate",
                                        length=420)

        # CONVERT AND CANCEL
        self.cancel = tk.BooleanVar()
        self.cancel.set(False)
        self.cc_frame = tk.Frame(root)
        self.convert_button = tk.Button(self.cc_frame, text="CONVERT", 
                                    command=self.confirm_convert)
        self.cancel_button = tk.Button(self.cc_frame, text="CANCEL", state="disabled", 
                                    command=lambda: self.cancel.set(True))

        
        # ROW 0
        self.input_directory_label.grid(sticky="W", row=0, column=0)
        self.input_directory_box.grid(sticky="W", row=0, column=1, padx=(15, 0))
        self.input_directory_button.grid(sticky="E", row=0, column=2)

        # ROW 1
        self.output_directory_label.grid(sticky="W", row=1, column=0)
        self.output_directory_box.grid(sticky="W", row=1, column=1, padx=(15, 0))
        self.output_directory_button.grid(sticky="E", row=1, column=2)

        # ROW 2
        self.input_file_label.grid(sticky="W", row=2, column=0, pady=(5, 0))
        self.input_file_extension.grid(sticky="W", row=2, column=1, padx=(15, 0))
        self.quality_label.grid(sticky="S", row=2, column=2)

        # ROW 3
        self.output_file_label.grid(sticky="W", row=3, column=0)
        self.output_file_extension.grid(sticky="W", row=3, column=1, padx=(15, 0))
        self.quality_box.grid(sticky="N", row=3, column=2)

        # ROW 4
        self.delete_original_button.grid(sticky="W", row=4, column=0, pady=(5, 0))
        self.transparency_button.grid(sticky="W", row=4, column=1, pady=(5, 0))
        self.rename_button.grid(sticky="W", row=4, column=2, pady=(5, 0))

        # ROW 5
        self.resize_button.grid(sticky="W", row=5, column=0)
        self.aspect_ratio_button.grid(sticky="W", row=5, column=1)
        self.optimization_button.grid(sticky="W", row=5, column=2)

        # ROW 6
        self.namebox_label.grid(sticky="W", row=6, column=0)
        self.size_label_frame.grid(sticky="W", row=6, column=1, columnspan=2)
        self.width_label.grid(row=6, column=1, padx=(21, 7))
        self.height_label.grid(row=6, column=2)
        self.antialiasing_button.grid(sticky="W", row=6, column=2)

        # ROW 7
        self.namebox.grid(sticky="W", row=7, column=0)
        self.size_box_frame.grid(sticky="W", row=7, column=1, columnspan=2)
        self.width_box.grid(row=7, column=1, padx=(25, 15))
        self.height_box.grid(row=7, column=2)

        # ROW 8
        self.progressbar.grid(row=8, column=0, columnspan=3, pady=(15, 10))

        # ROW 9
        self.cc_frame.grid(row=9, column=1, pady=(0, 10))
        self.convert_button.grid(sticky="W", row=9, column=0)
        self.cancel_button.grid(sticky="E", row=9, column=1)


    def set_directory(self, directory):
        """Prompts the user to input a directory through their GUI file explorer."""
        directory.set(tk.filedialog.askdirectory())


    def check_transparency(self, from_file):
        """Checks if the input file extension can have transparency and sets the transparency button
        accordingly."""
        if from_file in self.transparency_enabled:
            self.transparency_button['state'] = 'normal'
        else:
            self.transparency_button['state'] = 'disabled'
            self.transparency.set(False)
            self.set_transparency()


    def set_transparency(self):
        """Clears the current output file extension and changes the output file extension options
        based on the transparency variable."""
        if self.transparency.get():
            self.output_file.set(self.transparency_enabled[0])
            self.output_file_extension.grid_remove()
            self.output_file_extension = tk.OptionMenu(root, self.output_file, 
                                                    *self.transparency_enabled)
            self.output_file_extension.grid(sticky="W", row=3, column=1, padx=(15, 0))
        else:
            self.output_file_extension.grid_remove()
            self.output_file_extension = tk.OptionMenu(root, self.output_file, *self.formats)
            self.output_file_extension.grid(sticky="W", row=3, column=1, padx=(15, 0))


    def set_rename(self):
        """Updates the namebox GUI according to the rename variable."""
        if self.rename.get():
            self.namebox['state'] = self.namebox_label['state'] = 'normal'
        else:
            self.namebox['state'] = self.namebox_label['state'] = 'disabled'


    def set_resize(self):
        """Updates the resize GUI parameters according to the resize variable."""
        if self.resize.get():
            self.width_box['state'] = self.height_box['state'] = 'normal'
            self.width_label['state'] = self.height_label['state'] = 'normal'
            self.aspect_ratio_button['state'] = self.antialiasing_button['state'] = 'normal'
        else:
            self.width_box['state'] = self.height_box['state'] = 'disabled'
            self.width_label['state'] = self.height_label['state'] = 'disabled'
            self.aspect_ratio_button['state'] = self.antialiasing_button['state'] = 'disabled'
            self.antialiasing.set(False)


    def count_files(self):
        """Returns a cout of all files in the output file directory."""
        file_count = 0

        for i in os.listdir(self.input_directory.get()):
            if i.upper().endswith(self.input_file.get()):
                file_count += 1

        return file_count


    def thread(self):
        """Creates a new thread for the convert function. Avoids GUI crashes on large conversions."""
        thread = threading.Thread(target=self.convert)
        thread.start()


    def confirm_convert(self):
        """Prompts the user to confirm file conversion."""
        file_count = self.count_files()
        confirmation = tk.messagebox.askquestion("Info", "{} files will be converted. Do you wish to proceed?".format(file_count))
            
        if confirmation == 'yes':
            self.thread()
        else:
            return


    def gui_freeze(self):
        self.input_directory_box['state'] = self.input_directory_button['state'] = 'disabled'
        self.output_directory_box['state'] = self.output_directory_button['state'] = 'disabled'
        self.input_file_extension['state'] = self.output_file_extension['state'] = 'disabled'
        self.delete_original_button['state'] = self.transparency_button['state'] = 'disabled'
        self.rename_button['state'] = self.resize_button['state'] = 'disabled'
        self.namebox['state'] = self.width_box['state'] = self.height_box['state'] = 'disabled'
        self.aspect_ratio_button['state'] = 'disabled'
        self.optimization_button['state'] = self.antialiasing_button['state'] = 'disabled'
        self.quality_box['state'] = self.convert_button['state'] = 'disabled'
        self.width_box['state'] = self.height_box['state'] = 'disabled'

    def gui_unfreeze(self):
        self.input_directory_box['state'] = self.input_directory_button['state'] = 'normal'
        self.output_directory_box['state'] = self.output_directory_button['state'] = 'normal'
        self.input_file_extension['state'] = self.output_file_extension['state'] = 'normal'
        self.delete_original_button['state'] = self.transparency_button['state'] = 'normal'
        self.rename_button['state'] = self.resize_button['state'] = 'normal'
        if self.rename.get():
            self.namebox['state'] = 'normal'
        if self.resize.get():
            self.width_box['state'] = self.height_box['state'] = 'normal'
            self.antialiasing_button['state'] = self.aspect_ratio_button['state'] = 'normal'
        self.quality_box['state'] = self.convert_button['state'] = 'normal'    


    def convert(self):
        """Checks for conversion parameters and converts all files in the input directory to their
        equivalents on the output directory in the output file extension."""
        counter = 0
        
        try:
            self.progressbar.start()
            self.cancel_button['state'] = 'normal'
            self.gui_freeze()

            if self.input_file.get() in ['JPEG, JPG']:
                file_format = ('JPEG', 'JPG')
            else:
                file_format = self.input_file.get()

            for filename in os.listdir(self.input_directory.get()):
                if filename.upper().endswith(file_format):
                    im = PIL.Image.open(os.path.join(self.input_directory.get(), filename))
                    converted_file = "{}.{}".format(os.path.join(self.output_directory.get(), 
                                                    filename.split('.')[0]), self.output_file.get())

                    if self.cancel.get():
                        self.progressbar.stop()
                        self.cancel_button['state'] = 'disabled'
                        self.cancel.set(False)
                        self.gui_unfreeze()

                        tk.messagebox.showinfo("Info", "File conversion cancelled.")
                        return

                    if self.input_file.get() in ['JPEG, JPG']:
                        file_format = ['JPEG', 'JPG']
                    else:
                        file_format = self.input_file.get()

                    if self.transparency.get() == False:
                        try:
                            im = im.convert('RGB')
                        except Exception:
                            pass

                    if self.rename.get():
                        converted_file = "{}.{}".format(os.path.join(self.output_directory.get(), 
                                                        self.new_name.get() + str(counter)), 
                                                        self.output_file.get())
                        counter += 1

                    if self.resize.get():
                        if self.width.get() <= 0 or self.height.get() <= 0:
                            self.progressbar.stop()
                            self.cancel_button['state'] = 'disabled'
                            self.cancel.set(False)
                            self.gui_unfreeze()
                            tk.messagebox.showinfo("Info", "Output image size must exceed zero.")
                            return
                
                        if self.aspect_ratio.get():
                            width, height = im.size
                            ratio = min(self.width.get() / width, self.height.get() / height)

                            # Has to include int(), will be float otherwise.
                            new_width = int(width * ratio)
                            new_height = int(height * ratio)

                            if self.antialiasing.get():
                                im = im.resize((new_width, new_height), PIL.Image.ANTIALIAS)
                            else:
                                im = im.resize((new_width, new_height))
                        else:
                            im = im.resize((self.width.get(), self.height.get()))

                    try:
                        im.save(converted_file, format=self.output_file.get(), 
                                quality=self.quality.get(), optimize=self.optimization.get())
                    except Exception:
                        im.save(converted_file, quality=self.quality.get(),
                                optimize=self.optimization.get())

                    im.close()
                    
                    if self.delete_original.get():
                        os.remove(os.path.join(self.input_directory.get(), filename))
            

            tk.messagebox.showinfo("Info", "File conversion complete.")
    
        except Exception:
            tk.messagebox.showinfo("Info", "An error has occured. Aborting conversion.")

        self.progressbar.stop()
        self.cancel_button['state'] = 'disabled'
        self.gui_unfreeze()


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).grid()
    root.title("Batch File Converter")

    root.wm_iconbitmap(tempFile)

    root.geometry("+800+400")
    root.resizable(width=False, height=False)
    
    root.mainloop()
    
    os.remove(tempFile)
