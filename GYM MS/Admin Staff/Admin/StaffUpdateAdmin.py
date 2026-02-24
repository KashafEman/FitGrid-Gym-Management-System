import customtkinter
from PIL import Image, ImageTk

app = customtkinter.CTk()
app.geometry("1000x700")
app.resizable(True, True)
customtkinter.set_appearance_mode("dark")
app.title("Staff Management")

# left frame
frameLeft = customtkinter.CTkFrame(app, width = 500, height = 700, fg_color='#0b5394', corner_radius=0)
frameLeft.grid(row = 0, column = 0, sticky = "nsew")

# right frame
frameRight = customtkinter.CTkFrame(app, width = 500, height = 700, fg_color='#24272C', corner_radius=0)
frameRight.grid(row = 0, column = 1, stick = "nsew")

# Set resizeable to full screen
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

# Login in page main image
login_page_image = customtkinter.CTkImage(light_image = Image.open("C:\\Users\\ZOR30\\Downloads\\Coaches-rafiki.png"), dark_image = Image.open("C:\\Users\\ZOR30\\Downloads\\Coaches-rafiki.png"), size = (400,400))
login_page_image_label = customtkinter.CTkLabel(frameLeft, text = "", image = login_page_image)
login_page_image_label.place(relx = 0.5, rely = 0.5, anchor = "center")

# Gym logo image
logo_image = customtkinter.CTkImage(light_image=Image.open("C:\\Users\\ZOR30\\OneDrive\\Desktop\\blacktm.png"), dark_image=Image.open("C:\\Users\\ZOR30\\OneDrive\\Desktop\\blacktm.png"), size = (65,65))
logo_image_label = customtkinter.CTkLabel(frameRight, text = "", image = logo_image)
logo_image_label.place(relx = 0.15, rely = 0.1, anchor = "center")

# gym name heading
heading_label = customtkinter.CTkLabel(frameRight, text = "FAT MAN GYM", font =customtkinter.CTkFont("Doubledecker DEMO", 50, "bold"), bg_color= 'transparent', text_color="#3d85c6")
heading_label.place(relx = 0.58, rely = 0.1, anchor = "center")

# heading line
heading_line = customtkinter.CTkFrame(frameRight, width = 275, height = 3, fg_color="white")
heading_line.place(relx = 0.58, rely = 0.15, anchor = "center")

# management system label
management_system_label = customtkinter.CTkLabel(frameRight, text = "Management System", font = customtkinter.CTkFont("Arial", 20), bg_color="transparent", text_color="#3d85c6", fg_color="transparent")
management_system_label.place(relx = 0.58, rely = 0.18, anchor = "center")

# sign up label
sign_up_label = customtkinter.CTkLabel(frameRight, text = "UPDATE STAFF", font = customtkinter.CTkFont("Arial", 30, "bold"), bg_color='transparent', text_color="#FFFFFF",cursor="hand2")
sign_up_label.place(relx = 0.5, rely = 0.27, anchor = "center")

# first name underline
first_name_line = customtkinter.CTkFrame(frameRight, width = 197, height = 3, fg_color="white")
first_name_line.place(relx = 0.75, rely = 0.38, anchor = "e")
first_name_line.update()

# last name underline
last_name_line = customtkinter.CTkFrame(frameRight, width = 197, height = 3, fg_color="white")
last_name_line.place(relx = 0.75, rely = 0.46, anchor = "e")

# first Name label
first_name_label = customtkinter.CTkLabel(frameRight, text = "First Name", font =customtkinter.CTkFont("Arial", 20), bg_color= 'transparent', text_color="#FFFFFF")
first_name_label.place(relx = 0.25, rely = 0.36, anchor = "center")

# last name label
last_name_label = customtkinter.CTkLabel(frameRight, text = "Last Name", font =customtkinter.CTkFont("Arial", 20), bg_color= 'transparent', text_color="#FFFFFF")
last_name_label.place(relx = 0.25, rely = 0.44, anchor = "center")

# first name entry field
first_name_entry = customtkinter.CTkEntry(frameRight, placeholder_text="e.g John", width = 200, height = 28, fg_color="#24272C", border_width=0, text_color="white")
first_name_entry.place(relx= 0.75, rely = 0.36, anchor = "e")

# last name entry field
last_name_entry = customtkinter.CTkEntry(frameRight, placeholder_text="e.g Doe", width = 200, height = 28, fg_color="#24272C", border_width=0,  text_color="white")
last_name_entry.place(relx= 0.75, rely = 0.44, anchor = "e")

# username label
username_label = customtkinter.CTkLabel(frameRight, text = "Username", font =customtkinter.CTkFont("Arial", 20), bg_color= 'transparent', text_color="#FFFFFF")
username_label.place(relx = 0.25, rely = 0.52, anchor = "center")

# username entry field
username_entry = customtkinter.CTkEntry(frameRight, placeholder_text="e.g johndoe", width = 200, height = 28, fg_color="#24272C", border_width=0, text_color="white")
username_entry.place(relx= 0.75, rely = 0.52, anchor = "e")

# username underline
username_line = customtkinter.CTkFrame(frameRight, width = 197, height = 3, fg_color="white")
username_line.place(relx = 0.75, rely = 0.54, anchor = "e")

#password label
username_label = customtkinter.CTkLabel(frameRight, text = "Password", font =customtkinter.CTkFont("Arial", 20), bg_color= 'transparent', text_color="#FFFFFF", )
username_label.place(relx = 0.25, rely = 0.60, anchor = "center")

# password entry field
username_entry = customtkinter.CTkEntry(frameRight, placeholder_text="e.g JohnDoe$1986", width = 200, height = 28, fg_color="#24272C", border_width=0, text_color="white", show="*")
username_entry.place(relx= 0.75, rely = 0.60, anchor = "e")

# username underline
username_line = customtkinter.CTkFrame(frameRight, width = 197, height = 3, fg_color="white")
username_line.place(relx = 0.75, rely = 0.62, anchor = "e")

#contact label
username_label = customtkinter.CTkLabel(frameRight, text = "Contact No", font =customtkinter.CTkFont("Arial", 20), bg_color= 'transparent', text_color="#FFFFFF")
username_label.place(relx = 0.25, rely = 0.68, anchor = "center")

# contact entry field
username_entry = customtkinter.CTkEntry(frameRight, placeholder_text="e.g 03001234567", width = 200, height = 28, fg_color="#24272C", border_width=0, text_color="white")
username_entry.place(relx= 0.75, rely = 0.68, anchor = "e")

# contact underline
username_line = customtkinter.CTkFrame(frameRight, width = 197, height = 3, fg_color="white")
username_line.place(relx = 0.75, rely = 0.70, anchor = "e")

#dob label
username_label = customtkinter.CTkLabel(frameRight, text = "Birth Date", font =customtkinter.CTkFont("Arial", 20), bg_color= 'transparent', text_color="#FFFFFF")
username_label.place(relx = 0.25, rely = 0.76, anchor = "center")

#dob day option menu
dob_day_option_menu = customtkinter.CTkOptionMenu(frameRight, values=[str(i) for i in range(1, 32)], width=60, fg_color="#000000", button_color="#000000")
dob_day_option_menu.set("1")
dob_day_option_menu.place(relx = 0.41, rely = 0.76, anchor = "center")

#dob month option menu
dob_month_option_menu = customtkinter.CTkOptionMenu(frameRight, values=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], width=100, fg_color="#000000", button_color="#000000")
dob_month_option_menu.set("January")
dob_month_option_menu.place(relx = 0.595, rely = 0.76, anchor = "center")

#dob year option menu
dob_year_option_menu = customtkinter.CTkOptionMenu(frameRight, values=[str(i) for i in range (1950, 2025)], width = 60, fg_color="#000000", button_color="#000000")
dob_year_option_menu.set("2000")
dob_year_option_menu.place(relx = 0.79, rely = 0.76, anchor = "center")

#gender label
username_label = customtkinter.CTkLabel(frameRight, text = "Gender", font =customtkinter.CTkFont("Arial", 20), bg_color= 'transparent', text_color="#FFFFFF")
username_label.place(relx = 0.25, rely = 0.84, anchor = "center")

#dob day option menu
dob_day_option_menu = customtkinter.CTkOptionMenu(frameRight, values=['Male', 'Female', 'Prefer Not To Say'], width = 100, fg_color="#000000", button_color="#000000")
dob_day_option_menu.set("Male")
dob_day_option_menu.place(relx = 0.35, rely = 0.84, anchor = "w")

# register button
update_button = customtkinter.CTkButton(frameRight, text = "UPDATE", corner_radius=35, fg_color="#0b5394",cursor="hand2")
update_button.place(relx = 0.29, rely = 0.91, anchor = "center")


# back button
back_button = customtkinter.CTkButton(frameRight, text = "Go Back", corner_radius=35, fg_color="#0b5394",cursor="hand2")
back_button.place(relx = 0.65, rely = 0.91, anchor = "center")


#designation label
desig_label = customtkinter.CTkLabel(frameRight, text = "Designation", font =customtkinter.CTkFont("Arial", 20), bg_color= 'transparent', text_color="#FFFFFF")
desig_label.place(relx = 0.63, rely = 0.84, anchor = "center")


#Designation
des_menu = customtkinter.CTkOptionMenu(frameRight, values=['Trainer', 'Non-Functional', 'Functional'], width = 100, fg_color="#000000", button_color="#000000")
des_menu.set("Trainer")
des_menu.place(relx = 0.75, rely = 0.84, anchor = "w")


app.mainloop()