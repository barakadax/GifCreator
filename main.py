import tkinter
from tkinter import filedialog
from moviepy.editor import VideoFileClip

class GIF_creator():
    def __init__(self):
        self.my_clip = None
        self.new_gif_fps = 0
        self.font = "Calibri 15"
        self.new_file_dir_plus_name = ""
        self.file_name_and_dir_str = None
        self.file_name_and_dir_list = None
        self.window = tkinter.Tk(className=" GIF builder")
        self.window_mid_width_monitor = int(self.window.winfo_screenwidth()/2 - self.window.winfo_reqwidth()/2)
        self.window_mid_height_monitor = int(self.window.winfo_screenheight()/2 - self.window.winfo_reqheight()/2)
        self.window.geometry(f"+{self.window_mid_width_monitor}+{self.window_mid_height_monitor}")
        self.btn_upload = tkinter.Button(self.window, command=self.browse_for_file, font=self.font, text="Upload")
        self.btn_upload.pack(side=tkinter.LEFT)
        self.label_file_name_and_dir = tkinter.Label(self.window, text=f" File name:  ", font=self.font)
        self.label_file_name_and_dir.pack(side = tkinter.LEFT)
        self.label_amount_of_fps = tkinter.Label(self.window, text=" FPS:  ", font=self.font)
        self.label_amount_of_fps.pack(side = tkinter.LEFT)
        self.textfield_fps_value = tkinter.Entry(self.window, width=5, font=self.font, state="disabled")
        self.textfield_fps_value.pack(side=tkinter.LEFT)
        self.btn_create_gif = tkinter.Button(self.window, command=self.create_gif, font=self.font, text="Create", state="disabled")
        self.btn_create_gif.pack(side=tkinter.LEFT)
        

    def start(self):
        self.window.mainloop()


    def clean(self):
        self.my_clip = None
        self.new_gif_fps = 0
        self.new_file_dir_plus_name = ""
        self.file_name_and_dir_str = None
        self.file_name_and_dir_list = None


    def create_gif(self):
        self.my_clip = VideoFileClip(self.file_name_and_dir_str.name, audio=False)
        for i in range(0, len(self.file_name_and_dir_list) - 1):
            self.new_file_dir_plus_name += self.file_name_and_dir_list[i] + '/'
        self.new_file_dir_plus_name += "new_gif.gif"
        try :
            self.new_gif_fps = int(self.textfield_fps_value.get())
        except ValueError:
            self.new_gif_fps = self.my_clip.fps
        if self.new_gif_fps > self.my_clip.fps or self.new_gif_fps <= 0:
            self.new_gif_fps = self.my_clip.fps
        self.my_clip.write_gif(self.new_file_dir_plus_name, fps=self.my_clip.fps)
        self.textfield_fps_value.delete(0, 20)
        self.textfield_fps_value.configure(state="disabled")
        self.label_file_name_and_dir.configure(text=f" File name:  ")
        self.btn_create_gif.configure(state="disabled")
        self.clean()


    def browse_for_file(self):
        self.file_name_and_dir_str = filedialog.askopenfile(initialdir="/")
        if self.file_name_and_dir_str:
            self.textfield_fps_value.configure(state="normal")
            self.file_name_and_dir_list = self.file_name_and_dir_str.name.split('/')
            self.label_file_name_and_dir.configure(text=f" File name: {self.file_name_and_dir_list[len(self.file_name_and_dir_list) - 1]}  ")
            self.btn_create_gif.configure(state="normal")
        else:
            self.clean()
            self.btn_create_gif.configure(state="disabled")
            self.textfield_fps_value.configure(state="disabled")
            self.label_file_name_and_dir.configure(text=f" File name:  ")


if __name__ == "__main__":
    gif_creator_obj = GIF_creator()
    gif_creator_obj.start()
