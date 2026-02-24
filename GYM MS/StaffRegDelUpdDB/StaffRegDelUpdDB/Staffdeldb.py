import customtkinter
import pyodbc
from PIL import Image, ImageTk

app = customtkinter.CTk()
app.geometry("1000x700")
app.resizable(True, True)
customtkinter.set_appearance_mode("dark")
app.title("Staff Management")

# Establish a connection to the SQL Server database
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=HP-PAVILION-360;DATABASE=staff;Trusted_Connection=yes;')

# Function to handle registration button click event
def delete_button_click():
    # Retrieve data entered by the user
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    username = username_entry.get()
    employeeid=userid_entry.get()
   
    # Construct SQL INSERT statement
    sql_delete = """
    DELETE FROM Staff 
    WHERE EmployeeID = ?
    """


    # Execute the INSERT statement
    cursor = conn.cursor()
    cursor.execute(sql_delete, (employeeid))
    conn.commit()
    cursor.close()


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

# delete label
sign_up_label = customtkinter.CTkLabel(frameRight, text = "DELETE STAFF", font = customtkinter.CTkFont("Arial", 30, "bold"), bg_color='transparent', text_color="#FFFFFF",cursor="hand2")
sign_up_label.place(relx = 0.5, rely = 0.31, anchor = "center")

# first name underline
first_name_line = customtkinter.CTkFrame(frameRight, width = 197, height = 3, fg_color="white")
first_name_line.place(relx = 0.75, rely = 0.47, anchor = "e")
first_name_line.update()

# last name underline
last_name_line = customtkinter.CTkFrame(frameRight, width = 197, height = 3, fg_color="white")
last_name_line.place(relx = 0.75, rely = 0.55, anchor = "e")

# first Name label
first_name_label = customtkinter.CTkLabel(frameRight, text = "First Name", font =customtkinter.CTkFont("Arial", 20), bg_color= 'transparent', text_color="#FFFFFF")
first_name_label.place(relx = 0.25, rely = 0.44, anchor = "center")

# last name label
last_name_label = customtkinter.CTkLabel(frameRight, text = "Last Name", font =customtkinter.CTkFont("Arial", 20), bg_color= 'transparent', text_color="#FFFFFF")
last_name_label.place(relx = 0.25, rely = 0.52, anchor = "center")

# first name entry field
first_name_entry = customtkinter.CTkEntry(frameRight, placeholder_text="e.g John", width = 200, height = 28, fg_color="#24272C", border_width=0, text_color="white")
first_name_entry.place(relx= 0.75, rely = 0.44, anchor = "e")

# last name entry field
last_name_entry = customtkinter.CTkEntry(frameRight, placeholder_text="e.g Doe", width = 200, height = 28, fg_color="#24272C", border_width=0,  text_color="white")
last_name_entry.place(relx= 0.75, rely = 0.52, anchor = "e")

# username label
username_label = customtkinter.CTkLabel(frameRight, text = "Username", font =customtkinter.CTkFont("Arial", 20), bg_color= 'transparent', text_color="#FFFFFF")
username_label.place(relx = 0.25, rely = 0.60, anchor = "center")

# username entry field
username_entry = customtkinter.CTkEntry(frameRight, placeholder_text="e.g johndoe", width = 200, height = 28, fg_color="#24272C", border_width=0, text_color="white")
username_entry.place(relx= 0.75, rely = 0.60, anchor = "e")

# username underline
username_line = customtkinter.CTkFrame(frameRight, width = 197, height = 3, fg_color="white")
username_line.place(relx = 0.75, rely = 0.62, anchor = "e")

# delete button
delete_button = customtkinter.CTkButton(frameRight, text = "DELETE", corner_radius=35, fg_color="#0b5394",cursor="hand2",command=delete_button_click)
delete_button.place(relx = 0.29, rely = 0.85, anchor = "center")

# back button
back_button = customtkinter.CTkButton(frameRight, text = "Go Back", corner_radius=35, fg_color="#0b5394",cursor="hand2")
back_button.place(relx = 0.65, rely = 0.85, anchor = "center")

# user id label
userid_label = customtkinter.CTkLabel(frameRight, text = "User Id", font =customtkinter.CTkFont("Arial", 20), bg_color= 'transparent', text_color="#FFFFFF")
userid_label.place(relx = 0.25, rely = 0.70, anchor = "center")

#user id entry field
userid_entry = customtkinter.CTkEntry(frameRight, placeholder_text="e.g 1", width = 200, height = 28, fg_color="#24272C", border_width=0, text_color="white")
userid_entry.place(relx= 0.75, rely = 0.68, anchor = "e")

#user id  undreline
userid_line = customtkinter.CTkFrame(frameRight, width = 197, height = 3, fg_color="white")
userid_line.place(relx = 0.75, rely = 0.70, anchor = "e")


app.mainloop()