#importing libraries
import time
import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import libtorrent as lt

#define paths
torrent_file = ''
save_folder = ''

#######################################################################################################################
#defining button functions
#######################################################################################################################
#upload file function
def uploadfile():
    temp_file = filedialog.askopenfilename(title='Select a Torrent file', filetypes=[('torrent files', '*.torrent')])
    global torrent_file
    torrent_file = temp_file
    file_str.set(torrent_file)

#select save folder function
def uploadfolder():
    temp_folder = filedialog.askdirectory(title='Select a Folder to download the torrent')
    global save_folder
    save_folder = temp_folder + '/'
    folder_str.set(save_folder)

#download start function
def download(file, folder):
    #get magnet uri from entry box
    magnet_uri = magnet.get()
    
    #create a torrent session
    ses = lt.session({'listen_interfaces': '0.0.0.0:6881'})

    #create torrent handle from magnet link or uploaded file
    if magnet_uri != '':
        params = lt.parse_magnet_uri(magnet_uri)
        params.save_path = folder
        handle = ses.add_torrent(params)

    else:
        params = {'save_path': folder}
        params['ti'] = lt.torrent_info(file)
        handle = ses.add_torrent(params)
    
    #store starting time
    begin = time.time()

    #printing status
    status_str.set('Starting....')
    main.update_idletasks()
    time.sleep(1)

    state_str = ['Queued', 'Checking', 'Downloading Metadata', 'Downloading...', 'Finished', 'Seeding', 'Allocating', 'Checking Fastresume']

    #download torrent data
    while not handle.status().is_seeding:
        s = handle.status()

        progress = str(round(s.progress * 100, 2))
        down_rate = str(round(s.download_rate / 1000000, 1))
        up_rate = str(round(s.upload_rate / 1000000, 1))
        peers = str(int(s.num_peers))
        state = str(state_str[s.state])
        stat = 'Download Speed: ' + down_rate + ' mb/s | Upload Speed: ' + up_rate + ' mb/s | Peers: ' + peers + ' | ' + state
        
        #printing status
        status_str.set(stat)
        pb['value'] = progress
        main.update_idletasks()
        time.sleep(1)
    
    #store ending time
    end = time.time()

    #calculate elasped time
    min = int((end-begin)//60)
    sec = int((end-begin)%60)
    timer = ' | Elasped Time: ' + str(min) + 'min : '+ str(sec) + 'sec'
    complete = 'Completed: ' + str(handle.status().name)
    final = complete + timer
    
    #printing status
    status_str.set(final)
    main.update_idletasks()
    messagebox.showinfo('Success', 'Download Complete')

#######################################################################################################################
#GUI
#######################################################################################################################
#Root window
root = tk.Tk()
root.geometry('700x300')
root.title('Torrent Downloader')
root.iconbitmap('icon.ico')

#Main frame inside root window
main = tk.Frame(root)
main.pack(padx=10, pady=10, fill='x', expand=True)

#magnet_label
magnet_label = tk.Label(main, text='Paste the Magnet Link here', font=('Courier', 16))
magnet_label.pack(fill='x', expand=True)

#magnet_url entry
magnet_url = tk.StringVar()
magnet = tk.Entry(main, textvariable=magnet_url)
magnet.pack(fill='x', expand=True)

#or_label
or_label = tk.Label(main, text='OR', font=('Courier', 16))
or_label.pack(fill='x', expand=True)

#file_label
file_label = tk.Label(main, text='Select a Torrent file', font=('Courier', 16))
file_label.pack(fill='x', expand=True)

#browse_file button
browse_file_btn = tk.Button(main, text='Browse File', command=uploadfile, font=('Courier', 16))
browse_file_btn.pack(fill='x', expand=True)

#file location label
file_str = tk.StringVar()
file_label = tk.Label(main, textvariable=file_str)
file_label.pack(fill='x', expand=True)

#save_label
save_label = tk.Label(main, text='Select a folder to download the torrent', font=('Courier', 16))
save_label.pack(fill='x', expand=True)

#browse_folder button
browse_folder_btn = tk.Button(main, text='Browse Folder', command=uploadfolder, font=('Courier', 16))
browse_folder_btn.pack(fill='x', expand=True)

#folder location label
folder_str = tk.StringVar()
folder_label = tk.Label(main, textvariable=folder_str)
folder_label.pack(fill='x', expand=True)

#download button
download_btn = tk.Button(main, text='Download', command=lambda: download(torrent_file, save_folder), font=('Courier', 16))
download_btn.pack(fill='x', expand=True)

#status_label
status_str = tk.StringVar()
status_label = tk.Label(main, textvariable=status_str)
status_label.pack(fill='x', expand=True)

# progressbar
pb = ttk.Progressbar(main, orient='horizontal', mode='determinate')
pb.pack(fill='x', expand=True)

main.mainloop()
