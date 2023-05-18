# import required modules
from tkinter import *
from tkinter.ttk import *
from datetime import datetime, timedelta
from hijridate import Hijri, Gregorian
from reportlab.pdfgen import canvas
import tkinter.font as TkFont
from tkinter import scrolledtext
import time
import sqlite3
import database
import pygame
import sys
import os
import threading
import webbrowser


# get the base directory of the bundled resources
if getattr(sys, 'frozen', False):
    # if the application is run as a bundle, use the special _MEIPASS
    # attribute to get the path to the bundled resources
    bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
else:
    # if the application is not run as a bundle, use the standard
    # directory structure
    bundle_dir = os.path.abspath(os.path.dirname(__file__))

# variables to assign the adhaan_file_path, adhaan_fajr_file_path, app_logo_file_path and theme_file_path
adhaan_file_path = os.path.join(bundle_dir, 'E:/prayer_time_app/resources/Adhaan.mp3')
adhaan_fajr_file_path = os.path.join(bundle_dir, 'E:/prayer_time_app/resources/Adhaan Fajr.mp3')
app_logo_file_path = os.path.join(bundle_dir, 'E:/prayer_time_app/resources/mosque.ico')
theme_file_path = os.path.join(bundle_dir, 'E:/prayer_time_app/resources/azure/azure.tcl')

# create root window
root = Tk()

# add root title
root.title('Prayer Times - Sri Lanka')
root.iconbitmap(app_logo_file_path)

# set the font for the entire application
default_font = TkFont.nametofont("TkDefaultFont")
default_font.configure(family='Circular Std Bold', size=20)
root.option_add("*Font", default_font)

# add root geometry
root.geometry('750x650')

# create a menubar
menubar = Menu(root, font=('Circular Std Bold','10','bold'))
root.config(menu=menubar)

# create menus
file_menu = Menu(menubar, tearoff=False, font=('Circular Std Bold','10','bold'))
tools_menu = Menu(menubar, tearoff=False, font=('Circular Std Bold','10','bold'))
settings_menu = Menu(menubar, tearoff=False, font=('Circular Std Bold','10','bold'))
help_menu = Menu(menubar, tearoff=False, font=('Circular Std Bold','10','bold'))

# add a menu item to the file menu
file_menu.add_command(
    label='Exit',
    command=root.destroy)

# create style to customize when needed
s=Style()

# create a connection to the database
conn = sqlite3.connect('prayer_time.db')
cursor_theme = conn.cursor()

cursor_theme.execute('''CREATE TABLE IF NOT EXISTS app_settings
             (id INTEGER PRIMARY KEY,
             theme TEXT)''')

conn.commit()

# Function to save the current theme to the database
def save_theme(theme):
    cursor_theme.execute("INSERT INTO app_settings (theme) VALUES (?)", (theme,))
    conn.commit()

# Function to retrieve the last saved theme from the database
def get_last_theme():
    cursor_theme.execute("SELECT theme FROM app_settings ORDER BY id DESC LIMIT 1")
    row = cursor_theme.fetchone()
    if row:
        return row[0]
    else:
        return None

def set_theme(theme):
    # importing the custom theme azure if not imported
    try:
        root.call("source", theme_file_path)
    except:
        pass
    
    # set current theme
    root.call("set_theme", theme)

    s.configure('TNotebook.Tab', font=('Circular Std Bold','15','bold'))
    s.configure('my.TButton', font=('Circular Std Bold', 20, 'bold'))
    s.configure("Bold.TLabel", font=('Circular Std Bold', 20, 'bold'))
    s.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Circular Std Bold', 11))
    s.configure("mystyle.Treeview.Heading", font=('Circular Std Bold', 15, 'bold'))

    bigfont = TkFont.Font(family="Circular Std Bold", size=20)
    root.option_add("*TCombobox*Listbox*Font", bigfont)
    month_chosen.configure(font=bigfont)

    save_theme(theme)

# add a menu item to settings menu
settings_menu.add_command(label='Dark Theme', command=lambda: set_theme("dark"))
settings_menu.add_command(label='Light Theme', command=lambda: set_theme("light"))

user_manual = '''User Manual: Prayer Times - Sri Lanka

1. Introduction
The App is a prayer time and adhaan notification application. It provides users with the ability to view prayer times, customize the theme, and receive audio notifications for each prayer. This user manual will guide you through the features and functionalities of the App.

2. Installation and Setup
To install and set up the App, follow these steps:

- Download the executable file (`.exe`) for the App.
- Run the executable file to install the App on your system.
- Once installed, launch the App by double-clicking the desktop icon or selecting it from the Start menu.

3. Application Interface
The App's interface is divided into several tabs, each offering specific functionality. The following sections describe the features available on each tab.

3.1 Home Tab
The Home tab displays the current date, time, and prayer times for today and tomorrow.

- Gregorian Date Label: Displays the current date in the Gregorian calendar format.
- Hijri Date Label: Displays the current date in the Hijri calendar format.
- Current Time: Shows the current time.
- Prayer Times for Today: Displays the prayer times for today.
- Prayer Times for Tomorrow: Displays the prayer times for tomorrow.

3.2 Settings Tab
The Settings tab allows users to customize the App's appearance and preferences.

- Theme Selection: Choose a theme for the App from the available options. The default theme is "Light" when the App is opened for the first time.
- Save Theme: Save the currently selected theme for future use.
- Retrieve Last Theme: Retrieve the previously saved theme.

3.3 Help Tab
The Help tab provides information and assistance related to the App.

- About: Displays information about the App, including the version and credits.
- User Manual: Opens this user manual.

3.4 Monthly Timings Tab
The Monthly Timings tab allows users to explore the prayer times for a specific month.

- Select Month: Choose a month from the dropdown list.
- Prayer Timings: Displays the prayer times for the selected month.

4. Audio Notifications
The App provides adhaan (Islamic call to prayer) notifications for each prayer time. The notifications can be toggled on or off for each prayer.

- Prayer Toggle Buttons: Each prayer time has an associated toggle button. If the button is toggled "🔔", the adhaan will be played when it reaches the time for the respective prayer. If the button is toggled "🔕", a popup notification will inform the user about the prayer time.
- Play Adhaan: If the prayer toggle button is "🔔" and the prayer time is reached, the adhaan audio for the respective prayer will play automatically.
- Stop Adhaan: During the adhaan playback, users have the option to stop the adhaan manually by clicking the "Stop Adhaan" button.
- Automatic Playback: If the adhaan is played, users can choose to let it play until the adhaan is over or manually stop it.

5. Additional Features
The App includes additional features to enhance the user experience.

- Theme Customization: Users can customize the theme of the App according to their preferences. The default theme is "Light" when the App is opened for the first time.
- Real-Time Updates: The App updates the time-related variables every second to ensure accurate time display.
- Special Days: On special days, such as the month of Ramadan, additional buttons and functionalities may appear.
- Popup Window: When a prayer time is reached and the prayer toggle button is "🔕", a popup window will appear to notify the user about the prayer time.

6. Conclusion
This user manual provided an overview of the App's features and functionalities. We hope this guide helps you navigate and utilize the App effectively. If you have any further questions or issues, please refer to the Help tab for assistance or contact our support team. Thank you for choosing our App!'''
def open_user_manual(user_manual):
    # Create the popup window
    popup = Toplevel()
    popup.title("User Manual")
    popup.iconbitmap(app_logo_file_path)
    popup.geometry('450x500')

    # Create a canvas to hold the label and scrollbar
    canvas = Canvas(popup)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    # Create a scrollbar
    scrollbar = Scrollbar(popup, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Configure the canvas to work with the scrollbar
    canvas.config(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to hold the label
    frame = Frame(canvas)

    # Add the frame to the canvas
    canvas.create_window((0, 0), window=frame, anchor='nw')

    # Create a label to display the user manual text
    label = Label(frame, text=user_manual, justify=LEFT, wraplength=400, font=("Circular Std Bold", 15, 'bold'))
    label.pack(fill=BOTH, expand=True, padx=10, pady=10)

    # Bind mouse scroll to the scrollbar
    canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))

    popup.focus()

    # Run the popup window's event loop
    popup.mainloop()

def open_github(event):
    webbrowser.open("https://github.com/milenek-x")

def open_about():
    # Create the popup window
    popup = Toplevel()
    popup.title("About")
    popup.iconbitmap(app_logo_file_path)

    # Create a label with the app information
    label_row_1 = Label(popup, text="\n\nApp Name: Prayer Times - Sri Lanka\nApp Version: 1.0\nDeveloper: milenek-x", justify=CENTER, font=("Circular Std Bold", 15, 'bold'))
    label_row_1.pack(padx=10)
    label_row_2 = Label(popup, text="For more information, visit my GitHub page: ", font=("Circular Std Bold", 15, 'bold'))
    label_row_2.pack(padx=10)
    # Create a label for the GitHub link
    github_label = Label(popup, text="https://github.com/milenek-x", cursor="hand1", font=("Circular Std Bold", 15, 'bold underline'))
    github_label.pack( padx=10)
    github_label.bind("<Button-1>", open_github)
    label_row_3 = Label(popup, text="\n\n")
    label_row_3.pack(padx=10)

    popup.focus()

    # Run the popup window's event loop
    popup.mainloop()



# add a menu item to help menu
help_menu.add_command(label='User Manual', command=lambda: open_user_manual(user_manual))
help_menu.add_command(label='About', command=open_about)

# add menus to the menubar
menubar.add_cascade(label="File", menu=file_menu)
#menubar.add_cascade(label='Tools', menu=tools_menu)
menubar.add_cascade(label="Settings", menu=settings_menu)
menubar.add_cascade(label='Help', menu=help_menu)


# customize notebook
s.configure('TNotebook.Tab', font=('Circular Std Bold','15','bold'))

# create notebook
tab_collection = Notebook(root)

# create tabs
home_tab = Frame(tab_collection)
monthly_timings_tab = Frame(tab_collection)

# adding tabs
tab_collection.add(home_tab, text='Home')
tab_collection.add(monthly_timings_tab, text='Monthly Timings')
tab_collection.pack(expand=1, fill=BOTH)

# create items in home_tab
# create gregorian date label
gregorian_date_label = Label(home_tab, text='', font=('Circular Std Bold', 20, 'bold'))
gregorian_date_label.pack(anchor=CENTER, fill=X, padx=20, pady=5)

# create hijri date label
hijri_date_label = Label(home_tab, text='', font=('Circular Std Bold', 20, 'bold'))
hijri_date_label.pack(anchor=CENTER, fill=X, padx=20, pady=5)

# show current time
time_label = Label(home_tab, text='', font=('Circular Std Bold', 24, 'bold'))
time_label.pack(anchor=CENTER, fill=X, padx=20, pady=5)

# create a cursor object to execute a query for prayer times for today
cursor_today = conn.cursor()
cursor_today.execute("SELECT * FROM prayer_times WHERE date = (?)", (datetime.now().strftime('%d-%m'),))

# get date of tomorrow by today's date
tomorrow_date = (datetime.now() + timedelta(days=1)).strftime('%d-%m')

# create a cursor object to execute a query for prayer times for tomorrow
cursor_tomorrow = conn.cursor()
cursor_tomorrow.execute("SELECT * FROM prayer_times WHERE date = (?)", (tomorrow_date,))

# fetch prayer times for today and tomorrow
rows_today=cursor_today.fetchall()
rows_tomorrow = cursor_tomorrow.fetchall()

# get the prayer times for today
sahr_end_time_today = datetime.strptime(rows_today[0][1], "%H:%M").time()
fajr_time_today = datetime.strptime(rows_today[0][2], "%H:%M").time()
sunrise_time_today = datetime.strptime(rows_today[0][3], "%H:%M").time()
luhr_time_today = datetime.strptime(rows_today[0][4], "%H:%M").time()
asr_time_today = datetime.strptime(rows_today[0][5], "%H:%M").time()
maghrib_time_today = datetime.strptime(rows_today[0][6], "%H:%M").time()
isha_time_today = datetime.strptime(rows_today[0][7], "%H:%M").time()

# get the prayer times for tomorrow
sahr_end_time_tomorrow = (datetime.strptime(rows_tomorrow[0][1], "%H:%M")).time()
fajr_time_tomorrow = (datetime.strptime(rows_tomorrow[0][2], "%H:%M")).time()

# customize button and label
s.configure('my.TButton', font=('Circular Std Bold', 20, 'bold'))
s.configure("Bold.TLabel", font=('Circular Std Bold', 20, 'bold'))

# create a labelframe for prayer times of today and customize it
prayer_time_labelframe = Label(text="Prayer Times Today : ", style="Bold.TLabel")
prayer_time_frame = LabelFrame(home_tab, labelwidget=prayer_time_labelframe)
prayer_time_frame.pack(anchor=CENTER, fill=X, padx=20, pady=5)

# create a variable to hold alarm on and off for each prayer time
sahr_end_bell = f'🔕'
sunrise_bell = f'🔕'

cursor_adhaan = conn.cursor()

# Execute a SELECT query to fetch the values
try:
    cursor_adhaan.execute("SELECT * FROM adhaan_settings WHERE id = 1")
    row = cursor_adhaan.fetchone()
except:
    row = None

if row is not None:
    fajr_bell = row[1]
    luhr_bell = row[2]
    asr_bell = row[3]
    maghrib_bell = row[4]
    isha_bell = row[5]
else:
    # Handle the case when the row doesn't exist
    fajr_bell = '🔕'
    luhr_bell = '🔕'
    asr_bell = '🔕'
    maghrib_bell = '🔕'
    isha_bell = '🔕'

# create a definition to play Fajr adhaan
def fajr_adhaan():
    global fajr_bell
    if fajr_bell == f'🔕':
        fajr_bell = f'🔔'
        fajr_button.config(text=f'Fajr\t{fajr_bell}\n{fajr_time_today.strftime("%I:%M %p")}')
    else:
        fajr_bell = f'🔕'
        fajr_button.config(text=f'Fajr\t{fajr_bell}\n{fajr_time_today.strftime("%I:%M %p")}')

# create a definition to play Luhr adhaan
def luhr_adhaan():
    global luhr_bell
    if luhr_bell == f'🔕':
        luhr_bell = f'🔔'
        luhr_button.config(text=f'Luhr\t{luhr_bell}\n{luhr_time_today.strftime("%I:%M %p")}')
    else:
        luhr_bell = f'🔕'
        luhr_button.config(text=f'Luhr\t{luhr_bell}\n{luhr_time_today.strftime("%I:%M %p")}')

# create a definition to play Asr adhaan
def asr_adhaan():
    global asr_bell
    if asr_bell == f'🔕':
        asr_bell = f'🔔'
        asr_button.config(text=f'Asr\t{asr_bell}\n{asr_time_today.strftime("%I:%M %p")}')
    else:
        asr_bell = f'🔕'
        asr_button.config(text=f'Asr\t{asr_bell}\n{asr_time_today.strftime("%I:%M %p")}')

# create a definition to play Maghrib adhaan
def maghrib_adhaan():
    global maghrib_bell
    if maghrib_bell == f'🔕':
        maghrib_bell = f'🔔'
        maghrib_button.config(text=f'Maghrib\t{maghrib_bell}\n{maghrib_time_today.strftime("%I:%M %p")}')
    else:
        maghrib_bell = f'🔕'
        maghrib_button.config(text=f'Maghrib\t{maghrib_bell}\n{maghrib_time_today.strftime("%I:%M %p")}')

# create a definition to play Isha adhaan
def isha_adhaan():
    global isha_bell
    if isha_bell == f'🔕':
        isha_bell = f'🔔'
        isha_button.config(text=f'Isha\t{isha_bell}\n{isha_time_today.strftime("%I:%M %p")}')
    else:
        isha_bell = f'🔕'
        isha_button.config(text=f'Isha\t{isha_bell}\n{isha_time_today.strftime("%I:%M %p")}')

# create buttons to display for prayer times for today
fajr_button = Button(prayer_time_frame, text=f'Fajr\t{fajr_bell}\n{fajr_time_today.strftime("%I:%M %p")}', style='my.TButton', command=fajr_adhaan)
sunrise_button = Button(prayer_time_frame, text=f'Sunrise\t{sunrise_bell}\n{sunrise_time_today.strftime("%I:%M %p")}', style='my.TButton')
luhr_button = Button(prayer_time_frame, text=f'Luhr\t{luhr_bell}\n{luhr_time_today.strftime("%I:%M %p")}', style='my.TButton', command=luhr_adhaan)
asr_button = Button(prayer_time_frame, text=f'Asr\t{asr_bell}\n{asr_time_today.strftime("%I:%M %p")}', style='my.TButton', command=asr_adhaan)
maghrib_button = Button(prayer_time_frame, text=f'Maghrib\t{maghrib_bell}\n{maghrib_time_today.strftime("%I:%M %p")}', style='my.TButton', command=maghrib_adhaan)
isha_button = Button(prayer_time_frame, text=f'Isha\t{isha_bell}\n{isha_time_today.strftime("%I:%M %p")}', style='my.TButton', command=isha_adhaan)

# create a labelframe for next prayer time and customize it
next_prayer_time_labelframe = Label(text="Next Prayer Time : ", style="Bold.TLabel")
next_prayer_time_frame = LabelFrame(home_tab, labelwidget=next_prayer_time_labelframe)
next_prayer_time_frame.pack(anchor=CENTER, fill=X, padx=20, pady=5)

# create a button to display the next prayer time
next_prayer_time_button = Button(next_prayer_time_frame, text='', style='my.TButton')
next_prayer_time_button.pack(anchor=CENTER, fill=X, padx=20, pady=5)

# create a button to display the time left for the next prayer time
next_prayer_time_left_button = Button(next_prayer_time_frame, text='', style='my.TButton')
next_prayer_time_left_button.pack(anchor=CENTER, fill=X, padx=20, pady=5)

# Initialize Pygame
pygame.init()

# Create a flag to keep track of whether the audio is currently playing
is_audio_playing = False

# Function to stop playing the Adhaan
def stop_adhaan():
    pygame.mixer.music.stop()
    popup.destroy()

# Function to play the Adhaan    
def play_adhaan(current_prayer):
    global is_audio_playing
    # Check if the audio is not already playing
    if not is_audio_playing:
        is_audio_playing = True
        # path to the adhaan audio file
        adhaan_file_path = "E:/prayer_time_app/resources/Adhaan.mp3"

        # load the adhaan audio file
        pygame.mixer.music.load(adhaan_file_path)

        # play the audio
        pygame.mixer.music.play(loops=0, start=5)

        # set audio duration to a variable
        audio_duration = 155.002

        # create a popup window
        global popup
        popup = Toplevel()
        popup.title(f"{current_prayer} Adhaan")
        popup.iconbitmap(app_logo_file_path)
        popup.geometry("300x150")

        # Disable the close button ('x')
        popup.protocol("WM_DELETE_WINDOW", lambda: None)


        # add a label
        label = Label(popup, text=f"Playing: {current_prayer} Adhaan", font=('Circular Std Bold', 20, 'bold'))
        label.pack(pady=10)

        # Add a stop button
        stop_button = Button(popup, text="Stop Adhaan", command=stop_adhaan, style='my.TButton')
        stop_button.pack(pady=10)

        popup.focus()

        # Check the current position of the audio periodically
        while pygame.mixer.music.get_busy():
            current_pos = pygame.mixer.music.get_pos() / 1000  # Convert milliseconds to seconds
            if current_pos >= audio_duration:
                popup.destroy()
                break

            popup.update()  # Update the popup window

# Function to play the Adhaan    
def play_adhaan_fajr(current_prayer):
    global is_audio_playing
    # Check if the audio is not already playing
    if not is_audio_playing:
        is_audio_playing = True
        # path to the adhaan audio file
        adhaan_file_path = "E:/prayer_time_app/resources/Adhaan Fajr.mp3"

        # load the adhaan audio file
        pygame.mixer.music.load(adhaan_file_path)

        # play the audio
        pygame.mixer.music.play(loops=0, start=5)

        # set audio duration to a variable
        audio_duration = 197.159

        # create a popup window
        global popup
        popup = Toplevel()
        popup.title(f"{current_prayer} Adhaan")
        popup.iconbitmap(app_logo_file_path)
        popup.geometry("300x150")

        # Disable the close button ('x')
        popup.protocol("WM_DELETE_WINDOW", lambda: None)

        # disable the maximize/minimize button
        popup.resizable(False, False)

        # add a label
        label = Label(popup, text=f"Playing: {current_prayer} Adhaan", font=('Circular Std Bold', 20, 'bold'))
        label.pack(pady=10)

        # Add a stop button
        stop_button = Button(popup, text="Stop Adhaan", command=stop_adhaan, style='my.TButton')
        stop_button.pack(pady=10)

        popup.focus()

        # Check the current position of the audio periodically
        while pygame.mixer.music.get_busy():
            current_pos = pygame.mixer.music.get_pos() / 1000  # Convert milliseconds to seconds
            if current_pos >= audio_duration:
                popup.destroy()
                break

            popup.update()  # Update the popup window

def create_popup(current_prayer):
    global popup_notification
    popup_notification = Toplevel()
    popup_notification.title(f"{current_prayer} Adhaan")
    popup_notification.iconbitmap(app_logo_file_path)
    popup_notification.geometry("300x150")

    # disable the close button ('x')
    popup_notification.protocol("WM_DELETE_WINDOW", lambda: None)

    # disable the maximize/minimize button
    popup_notification.resizable(False, False)

    # add a label
    label = Label(popup_notification, text=f"{current_prayer} has arrived", font=('Circular Std Bold', 20, 'bold'))
    label.pack(pady=10)

    # Add a dismiss button
    dismiss_button = Button(popup_notification, text="Dismiss", command=stop_adhaan, style='my.TButton')
    dismiss_button.pack(pady=10)

    # Schedule the popup to be destroyed after 5 seconds
    popup_notification.after(10000, popup_notification.destroy)

c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS adhaan_settings
             (id INTEGER PRIMARY KEY,
             fajr_bell TEXT,
             luhr_bell TEXT,
             asr_bell TEXT,
             maghrib_bell TEXT,
             isha_bell TEXT)''')
conn.commit()

def update_adhaan_settings():
    # Get the current values of the bells from the buttons
    fajr_bell_value = fajr_button["text"].split("\t")[1].split("\n")[0]
    luhr_bell_value = luhr_button["text"].split("\t")[1].split("\n")[0]
    asr_bell_value = asr_button["text"].split("\t")[1].split("\n")[0]
    maghrib_bell_value = maghrib_button["text"].split("\t")[1].split("\n")[0]
    isha_bell_value = isha_button["text"].split("\t")[1].split("\n")[0]

    # Check if the row with id=1 exists in the table
    c.execute("SELECT * FROM adhaan_settings WHERE id = 1")
    row = c.fetchone()

    if row is None:
        # If the row doesn't exist, insert a new row with id=1 and the bell values
        c.execute("INSERT INTO adhaan_settings (id, fajr_bell, luhr_bell, asr_bell, maghrib_bell, isha_bell) VALUES (1, ?, ?, ?, ?, ?)",
                  (fajr_bell_value, luhr_bell_value, asr_bell_value, maghrib_bell_value, isha_bell_value))
    else:
        # If the row exists, update the bell values
        c.execute("UPDATE adhaan_settings SET fajr_bell = ?, luhr_bell = ?, asr_bell = ?, maghrib_bell = ?, isha_bell = ? WHERE id = 1",
                  (fajr_bell_value, luhr_bell_value, asr_bell_value, maghrib_bell_value, isha_bell_value))

    conn.commit()
    root.destroy()

# create a function to update time related variables each second
def update_time():
    # get current time, date and datetime
    current_time = datetime.now().strftime("%I:%M:%S %p")
    current_date = datetime.now().date()
    current_datetime = datetime.now().time()

    # get current hijri date
    current_day_strf = str(datetime.now().strftime("%A"))
    current_year_strf = int(datetime.now().strftime("%Y"))
    current_month_strf = int(datetime.now().strftime("%m"))
    current_date_strf = int(datetime.now().strftime("%d"))


    # convert gregorian to hijri and get hijri year, month, date seperately
    hijri_format = Gregorian(current_year_strf, current_month_strf, current_date_strf).to_hijri()
    hijri_year = int((str(hijri_format)).split('-')[0])
    hijri_month = int((str(hijri_format)).split('-')[1])
    hijri_date = int((str(hijri_format)).split('-')[2])

    # create a dictionary to hold the Arabic names for the days of the week
    days_of_week = {
        "Sunday": "Al-Ahad",
        "Monday": "Al-Ithnayn",
        "Tuesday": "Ath-Thulatha'",
        "Wednesday":  "Al-Arbi'a",
        "Thursday": "Al-Khamees",
        "Friday": "Al-Jummu'ah",
        "Saturday": "As-Sabt",
        }

    # create a dictionary to hold the Arabic names for the months in Islamic Calendar
    months_in_islam = {
        1: "Muharram",
        2: "Safar",
        3: "Rabi' Al-Awwal",
        4: "Rabi' Al-Thani",
        5: "Jumada Al-Ula",
        6: "Jumada Al-Akhirah",
        7: "Rajab",
        8: "Sha'ban",
        9: "Ramadan",
        10: "Shawwal",
        11: "Dhu Al-Qadah",
        12: "Dhu Al-Hijjah"
    }


    # create variables to hold current day and month using the dictionary
    if current_day_strf in days_of_week:
        current_day_hijri = days_of_week[current_day_strf]
    if hijri_month in months_in_islam:
        current_month_hijri = months_in_islam[hijri_month]

    # show current date in Gregorian and Hijri formats
    gregorian_date_formatted = datetime.now().strftime("%A, %B %d, %Y")
    hijri_date_formatted = f"{current_day_hijri}, {current_month_hijri} {hijri_date}, {hijri_year}"

    # update gregorian date and hijri date labels
    gregorian_date_label.config(text=gregorian_date_formatted)
    hijri_date_label.config(text=hijri_date_formatted)

    # create a definition to find if today is a day in month of Ramadan
    def is_ramadan_month_today():
        if hijri_month == 9: #####################################
            return True
        else:
            return False

    # create a definition to find if today is a day between 2 to 7 in month of Shawwal
    def is_days_2_to_7_of_shawwal_today():
        if hijri_month == 10 and 2<=hijri_date<=7:
            return True
        else:
            return False

    # create a definition to find if tomorrow is a day in month of Ramadan
    def is_ramadan_month_tomorrow():
        if hijri_month == 8 and 29<=hijri_date<=30:
            return True
        elif hijri_month == 9:
            if hijri_date <30:
                return True
            else:
                return False
        else:
            return False

    # create a definition to find if today is a day between 2 to 7 in month of Shawwal
    def is_day_2_of_shawwal_tomorrow():
        if hijri_month == 10 and 1<=hijri_date<=6:
            return True
        else:
            return False

    # check if today is a day in month of Ramadan, or a day between 2 to 7 in month of Shawwal
    is_special_day_today = is_ramadan_month_today() or is_days_2_to_7_of_shawwal_today()

    # check if tomorrow is a day in month of Ramadan, or a day between 2 to 7 in month of Shawwal
    is_special_day_tomorrow = is_ramadan_month_tomorrow() or is_day_2_of_shawwal_tomorrow()

    # add the Sahr End button if it's a special day
    if is_special_day_today:
        global sahr_end_bell
        sahr_end_button = Button(prayer_time_frame, text=f'Sahr End\t{sahr_end_bell}\n{sahr_end_time_today.strftime("%I:%M %p")}', style='my.TButton')
        sahr_end_button.grid(row=0, column=0, padx=20, pady=5)

        # Shift the other buttons to the right
        fajr_button.grid(row=0, column=1, padx=20, pady=5)
        sunrise_button.grid(row=0, column=2, padx=20, pady=5)
        luhr_button.grid(row=0, column=3, padx=20, pady=5)
        asr_button.grid(row=1, column=0, padx=20, pady=5)
        maghrib_button.grid(row=1, column=1, padx=20, pady=5)
        isha_button.grid(row=1, column=2, padx=20, pady=5)

        root.geometry('1000x650')
    else:
        # No special day, display buttons without Sahr End
        fajr_button.grid(row=0, column=0, padx=20, pady=5)
        sunrise_button.grid(row=0, column=1, padx=20, pady=5)
        luhr_button.grid(row=0, column=2, padx=20, pady=5)
        asr_button.grid(row=1, column=0, padx=20, pady=5)
        maghrib_button.grid(row=1, column=1, padx=20, pady=5)
        isha_button.grid(row=1, column=2, padx=20, pady=5)


    # update the time label with the current time
    time_label.config(text=current_time)
    
    # check if it is past Isha adhaan time
    if current_datetime >= isha_time_today:
        if str(current_datetime).split('.')[0] == str(isha_time_today):
            if isha_bell == f'🔔':
                # Play the Adhaan in a separate thread
                current_prayer = 'Isha'
                threading.Thread(target=play_adhaan, args=(current_prayer,)).start()
            else:
                threading.Thread(target=create_popup, args=(current_prayer,)).start()
        # check if it is a special day
        if is_special_day_tomorrow:
            # display sahr end time for tomorrow if it is a special day
            next_prayer_time = datetime.combine(current_date + timedelta(days=1), sahr_end_time_tomorrow)
            next_prayer = "Sahr End for Tomorrow"
        else:
            # display Fajr adhaan time for tomorrow if it is not a special day
            next_prayer_time = datetime.combine(current_date + timedelta(days=1), fajr_time_tomorrow)
            next_prayer = "Fajr Adhaan for Tomorrow"
    # check if it is past Maghrib adhaan time
    elif current_datetime >= maghrib_time_today:
        if str(current_datetime).split('.')[0] == str(maghrib_time_today):
            if maghrib_bell == f'🔔':
                # Play the Adhaan in a separate thread
                current_prayer = 'Maghrib'
                threading.Thread(target=play_adhaan, args=(current_prayer,)).start()
            else:
                threading.Thread(target=create_popup, args=(current_prayer,)).start()
        next_prayer_time = datetime.combine(current_date, isha_time_today)
        next_prayer = "Isha Adhaan"
    # check if it is past Asr adhaan time
    elif current_datetime >= asr_time_today:
        if str(current_datetime).split('.')[0] == str(asr_time_today):
            if asr_bell == f'🔔':
                # Play the Adhaan in a separate thread
                current_prayer = 'Asr'
                threading.Thread(target=play_adhaan, args=(current_prayer,)).start()
            else:
                threading.Thread(target=create_popup, args=(current_prayer,)).start()    
        next_prayer_time = datetime.combine(current_date, maghrib_time_today)
        next_prayer = "Maghrib Adhaan"
    # check if it is past Luhr adhaan time
    elif current_datetime >= luhr_time_today:
        if str(current_datetime).split('.')[0] == str(luhr_time_today):
            if luhr_bell == f'🔔':
                # Play the Adhaan in a separate thread
                current_prayer = 'Luhr'
                threading.Thread(target=play_adhaan, args=(current_prayer,)).start()
            else:
                threading.Thread(target=create_popup, args=(current_prayer,)).start()
        next_prayer_time = datetime.combine(current_date, asr_time_today)
        next_prayer = "Asr Adhaan"
    # check if it is past Sunrise time
    elif current_datetime >= sunrise_time_today:
        next_prayer_time = datetime.combine(current_date, luhr_time_today)
        next_prayer = "Luhr Adhaan"
    # check if it is past Fajr adhaan time
    elif current_datetime >= fajr_time_today:
        if str(current_datetime).split('.')[0] == str(fajr_time_today):
            current_prayer = 'Fajr'
            if fajr_bell == f'🔔':
                # Play the Adhaan in a separate thread
                threading.Thread(target=play_adhaan_fajr, args=(current_prayer,)).start()
            else:
                threading.Thread(target=create_popup, args=(current_prayer,)).start()
        next_prayer_time = datetime.combine(current_date, sunrise_time_today)
        next_prayer = "Sunrise"
    # check if it is before Fajr adhaan time
    elif current_datetime < fajr_time_today:
        next_prayer_time = datetime.combine(current_date, fajr_time_today)
        next_prayer = "Fajr Adhaan"

    # calculate the time between now and the next prayer
    time_until_next_prayer = next_prayer_time - datetime.combine(current_date, current_datetime)

    # update the next prayer time buttons
    next_prayer_time_button.config(text=f"{next_prayer} at {next_prayer_time.strftime('%I:%M %p')}.")
    next_prayer_time_left_button.config(text=f"Time left for {next_prayer} is {((str(time_until_next_prayer)).split('.'))[0]}.")

    # schedule the next update
    time_label.after(1000, update_time)

# call out the update time function
update_time()

# create items in monthly_timings tab
# create a frame to hold basic items
select_month_frame = Frame(monthly_timings_tab)
select_month_frame.pack(fill=X)

# create a label for select month
select_month_label = Label(select_month_frame, text='Select Month : ', font=('Circular Std Bold', 20, 'bold'))
select_month_label.pack(side=LEFT, padx=10)


bigfont = TkFont.Font(family="Circular Std Bold",size=20)
root.option_add("*TCombobox*Listbox*Font", bigfont)

# create a combobox to select the month
n = StringVar()
month_chosen = Combobox(select_month_frame, width=10, textvariable=n, state='readonly')
month_chosen.configure(font=bigfont)
month_chosen.pack(side=LEFT)

# adding combobox drop down list
month_chosen['values'] = (' January', 
                          ' February',
                          ' March',
                          ' April',
                          ' May',
                          ' June',
                          ' July',
                          ' August',
                          ' September',
                          ' October',
                          ' November',
                          ' December')

s.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Circular Std Bold', 11))
s.configure("mystyle.Treeview.Heading", font=('Circular Std Bold', 15, 'bold'))

prayer_view_scrollbar = Scrollbar(monthly_timings_tab)
prayer_view_scrollbar.pack(side=RIGHT, fill=Y)

# create a treeview to display prayer times
prayer_view = Treeview(monthly_timings_tab, style='mystyle.Treeview', height=22, yscrollcommand=prayer_view_scrollbar.set)
prayer_view['columns'] = ('Date','Sahr End', 'Fajr', 'Sunrise', 'Luhr', 'Asr', 'Maghrib', 'Isha')


prayer_view.column("#0", width = 0, stretch = "no")
prayer_view.column('Date', width=60, anchor=CENTER)
prayer_view.column('Sahr End', width=100, anchor=CENTER)
prayer_view.column('Fajr', width=100, anchor=CENTER)
prayer_view.column('Sunrise', width=100, anchor=CENTER)
prayer_view.column('Luhr', width=100, anchor=CENTER)
prayer_view.column('Asr', width=100, anchor=CENTER)
prayer_view.column('Maghrib', width=100, anchor=CENTER)
prayer_view.column('Isha', width=100, anchor=CENTER)

prayer_view.heading('Date', text='Date')
prayer_view.heading('Sahr End', text='Sahr End')
prayer_view.heading('Fajr', text='Fajr')
prayer_view.heading('Sunrise', text='Sunrise')
prayer_view.heading('Luhr', text='Luhr')
prayer_view.heading('Asr', text='Asr')
prayer_view.heading('Maghrib', text='Maghrib')
prayer_view.heading('Isha', text='Isha')
prayer_view.pack(fill=X, padx=10, pady=20)

prayer_view_scrollbar.configure(command=prayer_view.yview)



current_month_combobox = int(datetime.now().strftime("%m"))

# set current month as the chosen month
month_chosen.current(current_month_combobox - 1)

# function to check if sahr end should be viewed for the selected month
def view_sahr_end(month_selected):
    # get the current year
    this_year = int(datetime.now().strftime("%Y"))

    # Calculate the start date of the selected month in the Hijri calendar
    first_of_month = Gregorian(this_year, month_selected+1, 1).to_hijri()

    # Calculate the end date of the selected month in the Hijri calendar
    try:
        last_of_month = Gregorian(this_year, month_selected+1, 31).to_hijri()
    except:
        try:
            last_of_month = Gregorian(this_year, month_selected+1, 30).to_hijri()
        except:
            try:
                last_of_month = Gregorian(this_year, month_selected+1, 29).to_hijri()
            except:
                last_of_month = Gregorian(this_year, month_selected+1, 28).to_hijri()

    # extract the month and day from the start and end dates
    start_month = int((str(first_of_month)).split('-')[1])
    end_month = int((str(last_of_month)).split('-')[1])
    start_day = int((str(first_of_month)).split('-')[2])
    end_day = int((str(last_of_month)).split('-')[2])

    # check if the month has a day in Ramadan
    if start_month == 9 or end_month == 9:
        # set the width of the 'Sahr End' column to 100
        prayer_view.column('Sahr End', width=100, anchor=CENTER, stretch="no")
    # check if the month has a day within the first 7 days of Shawwal
    elif start_month == 10 and 1<=start_day<=7 or end_month == 10 and 1<=end_day<=7:
        # set the width of the 'Sahr End' column to 100
        prayer_view.column('Sahr End', width=100, anchor=CENTER, stretch="no")
    # if not a month to view sahr end
    else:
        # hide the 'Sahr End' column by setting its width to 0
        prayer_view.column('Sahr End', width=0, anchor=CENTER, stretch="no")
    
def prayer_times_for_month(event):
    # create a cursor object to execute a quert for prayer times for the current month
    cursor_month = conn.cursor()
    selected_month = month_chosen.current()
    keyword = '%-' + str(selected_month+1).zfill(2)
    
    def is_leap_year(year):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    # Check if it is a leap year
    year = datetime.now().year
    is_leap = is_leap_year(year)
    
    cursor_month.execute("SELECT * FROM prayer_times WHERE date LIKE (?)", (keyword,))
    monthly_prayers = cursor_month.fetchall()

    # Adjust the number of days in February based on leap year
    if selected_month == 1:
        if is_leap:
            pass
        else:
            monthly_prayers = monthly_prayers[:-1]
    else:
        pass
    
    # clear existing data in the treeview
    prayer_view.delete(*prayer_view.get_children())

    # scroll the treeview to the top
    prayer_view.yview_moveto(0)

    for date_prayers in monthly_prayers:
        date = date_prayers[0].split('-')[0]
        prayer_times = date_prayers[1:]
        prayers = (date,) + prayer_times
        prayer_view.insert("", "end", values=prayers)

    view_sahr_end(selected_month)


# Bind the combobox event to update the treeview
month_chosen.bind('<<ComboboxSelected>>', prayer_times_for_month)

# get prayer times for current month
prayer_times_for_month(current_month_combobox)

# Check if there is a last saved theme and set it
last_theme = get_last_theme()
if last_theme:
    set_theme(last_theme)
else:
    set_theme('light')

root.protocol("WM_DELETE_WINDOW", update_adhaan_settings)

# create mainloop
root.mainloop()

# close the connection to the database
conn.close()
