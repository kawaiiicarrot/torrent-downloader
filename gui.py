import tkinter as tk
from tkinter import filedialog

torrent_file = ''
save_folder = ''

def uploadfile():
    temp_file = filedialog.askopenfilename(title='Select a Torrent file', filetypes=[('torrent files', '*.torrent')])
    global torrent_file
    torrent_file = temp_file
    for i in range(10):
        file.insert(tk.END, torrent_file)
        if i != 9:
            file.delete(0, tk.END)

def uploadfolder():
    temp_folder = filedialog.askdirectory(title='Select a Folder to download the torrent')
    global save_folder
    save_folder = temp_folder
    folder.insert(tk.END, save_folder)

def download(file, folder):
    magnet_uri = magnet.get()
    status.insert(tk.END, magnet_uri)
    print(magnet_uri)
    print(file)
    print(folder+'/')

#Root window
root = tk.Tk()
root.geometry('600x300')
root.title('Torrent Downloader')
root.iconbitmap('icon.ico')

#Main frame inside root window
main = tk.Frame(root)
main.pack(padx=10, pady=10, fill='x', expand=True)

#magnet_label
magnet_label = tk.Label(main, text='Paste the Magnet Link here')
magnet_label.pack(fill='x', expand=True)

#magnet_url entry
magnet_url = tk.StringVar()
magnet = tk.Entry(main, textvariable=magnet_url)
magnet.pack(fill='x', expand=True)

#or_label
or_label = tk.Label(main, text='OR')
or_label.pack(fill='x', expand=True)

#file_label
file_label = tk.Label(main, text='Select a Torrent file')
file_label.pack(fill='x', expand=True)

#browse_file button
browse_file_btn = tk.Button(main, text='Browse File', command=uploadfile)
browse_file_btn.pack(fill='x', expand=True)

#show file location text
file = tk.Text(main, height=1, bg=root.cget('background'))
file.pack(fill='x', expand=True)

#save_label
save_label = tk.Label(main, text='Select a folder to download the torrent')
save_label.pack(fill='x', expand=True)

#browse_folder button
browse_folder_btn = tk.Button(main, text='Browse Folder', command=uploadfolder)
browse_folder_btn.pack(fill='x', expand=True)

#show folder location text
folder = tk.Text(main, height=1, bg=root.cget('background'))
folder.pack(fill='x', expand=True)

#download button
download_btn = tk.Button(main, text='Download', command=lambda: download(torrent_file, save_folder))
download_btn.pack(fill='x', expand=True)

#show status text
status = tk.Text(main, height=1, bg=root.cget('background'))
status.pack(fill='x', expand=True, pady=5)

main.mainloop()