import tkinter as tk
from PIL import Image, ImageTk
import customtkinter  # Assuming you have a custom Tkinter library

# Create the main application window
app = customtkinter.CTk()
app.title("FATMAN GYM MANAGEMENT SYSTEM")

# Get the screen width and height
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

# Create a frame that occupies the full window
frame = customtkinter.CTkFrame(app, width=screen_width, height=screen_height, fg_color='#000000', corner_radius=0)
frame.grid(row=0, column=0, sticky="nsew")

# Make the frame resizable
frame.grid_propagate(False)

# Adjust the geometry of the main window
app.geometry(f"{screen_width}x{screen_height}+0+0")

#Gym Logo
logo_image = customtkinter.CTkImage(light_image=Image.open("C:\\Users\\ZOR30\\OneDrive\\Desktop\\blacktm.png"), dark_image=Image.open("C:\\Users\\ZOR30\\OneDrive\\Desktop\\blacktm.png"), size = (65,65))
logo_image_label = customtkinter.CTkLabel(frame, text = "", image = logo_image)
logo_image_label.place(relx = 0.05, rely = 0.08, anchor = "center")

#FATMAN GYM LABEL
heading_label = customtkinter.CTkLabel(frame, text = "USER HEALTH HISTORY", font =customtkinter.CTkFont("Doubledecker DEMO", 50, "bold"), bg_color= 'transparent', text_color="#3d85c6")
heading_label.place(relx = 0.32, rely = 0.09, anchor = "center")

#immunization picture
immunization_image=customtkinter.CTkImage(light_image=Image.open("C:\\Users\\ZOR30\\OneDrive\\Desktop\\Immunization.png"),dark_image=Image.open("C:\\Users\\ZOR30\\OneDrive\\Desktop\\Immunization.png"),size=(85,85))
immunization_image_label=customtkinter.CTkLabel(frame, text="",image=immunization_image)
immunization_image_label.place(relx=0.06,rely=0.25, anchor="center")

#immunization label
immunization_label = customtkinter.CTkLabel(frame, text = "Immunization", font =customtkinter.CTkFont("Arial", 15), bg_color= 'transparent', text_color="#FFFFFF")
immunization_label.place(relx = 0.06, rely = 0.32, anchor = "center")

#immunization entry 
immunization_entry = customtkinter.CTkEntry(frame, placeholder_text="e.g Polio", width = 230, height = 30, fg_color="#24272C", border_width=0, text_color="white")
immunization_entry.place(relx= 0.284, rely = 0.29, anchor = "e")

#immunization undreline
immunization_line = customtkinter.CTkFrame(frame, width = 220, height = 3, bg_color="white")
immunization_line.place(relx = 0.281, rely = 0.32, anchor = "e")

#medication picture
medication_image=customtkinter.CTkImage(light_image=Image.open("C:\\Users\\ZOR30\\OneDrive\\Desktop\\Medication.png"),dark_image=Image.open("C:\\Users\\ZOR30\\OneDrive\\Desktop\\Medication.png"),size=(85,85))
medication_image_label=customtkinter.CTkLabel(frame, text="",image=medication_image)
medication_image_label.place(relx=0.06,rely=0.45, anchor="center")

#medication label
medication_label = customtkinter.CTkLabel(frame, text = "Medication", font =customtkinter.CTkFont("Arial", 15), bg_color= 'transparent', text_color="#FFFFFF")
medication_label.place(relx = 0.06, rely = 0.52, anchor = "center")

#medication entry 
immunization_entry = customtkinter.CTkEntry(frame, placeholder_text="e.g  Amlodipine", width = 230, height = 30, fg_color="#24272C", border_width=0, text_color="white")
immunization_entry.place(relx= 0.284, rely = 0.49, anchor = "e")

#medication undreline
medication_line = customtkinter.CTkFrame(frame, width = 220, height = 3, bg_color="white")
medication_line.place(relx = 0.281, rely = 0.52, anchor = "e")

#allergy picture
allergy_image=customtkinter.CTkImage(light_image=Image.open("C:\\Users\\ZOR30\\OneDrive\\Desktop\\allergy.png"),dark_image=Image.open("C:\\Users\\ZOR30\\OneDrive\\Desktop\\allergy.png"),size=(85,85))
allergy_image_label=customtkinter.CTkLabel(frame, text="",image=allergy_image)
allergy_image_label.place(relx=0.06,rely=0.65, anchor="center")

#allergy label
medication_label = customtkinter.CTkLabel(frame, text = "Allergies", font =customtkinter.CTkFont("Arial", 15), bg_color= 'transparent', text_color="#FFFFFF")
medication_label.place(relx = 0.06, rely = 0.72, anchor = "center")

#allergy entry
allergy_entry = customtkinter.CTkEntry(frame, placeholder_text="e.g  Pollen allergy", width = 230, height = 30, fg_color="#24272C", border_width=0, text_color="white")
allergy_entry.place(relx= 0.284, rely = 0.69, anchor = "e")

#allergy underline
allergy_line = customtkinter.CTkFrame(frame, width = 220, height = 3, bg_color="white")
allergy_line.place(relx = 0.281, rely = 0.72, anchor = "e")

#injuries picture
injuries_image=customtkinter.CTkImage(light_image=Image.open("C:\\Users\\ZOR30\\OneDrive\\Desktop\\injuries.png"),dark_image=Image.open("C:\\Users\\ZOR30\\OneDrive\\Desktop\\injuries.png"),size=(85,85))
injuries_image_label=customtkinter.CTkLabel(frame, text="",image=injuries_image)
injuries_image_label.place(relx=0.4,rely=0.25, anchor="center")

#injuries label
injuries_label = customtkinter.CTkLabel(frame, text = "Injuries", font =customtkinter.CTkFont("Arial", 15), bg_color= 'transparent', text_color="#FFFFFF")
injuries_label.place(relx = 0.4, rely = 0.323, anchor = "center")

#injuries entry 
injuries_entry = customtkinter.CTkEntry(frame, placeholder_text="e.g Concussion", width = 230, height = 30, fg_color="#24272C", border_width=0, text_color="white")
injuries_entry.place(relx= 0.624, rely = 0.29, anchor = "e")

#injuries undreline
injuries_line = customtkinter.CTkFrame(frame, width = 220, height = 3, bg_color="white")
injuries_line.place(relx = 0.621, rely = 0.32, anchor = "e")

#emergency contact no picture
emergency_contact_no_image=customtkinter.CTkImage(light_image=Image.open("C:\\Users\\ZOR30\\OneDrive\\Desktop\\emergencycall.png"),dark_image=Image.open("C:\\Users\\ZOR30\\OneDrive\\Desktop\\emergencycall.png"),size=(85,85))
emergency_contact_no_image_label=customtkinter.CTkLabel(frame, text="",image=emergency_contact_no_image)
emergency_contact_no_image_label.place(relx=0.4,rely=0.45, anchor="center")

#emergency contact no label
emergency_contact_no_label = customtkinter.CTkLabel(frame, text = "Emergency Info", font =customtkinter.CTkFont("Arial", 15), bg_color= 'transparent', text_color="#FFFFFF")
emergency_contact_no_label.place(relx = 0.4, rely = 0.52, anchor = "center")

#emergency contact no entry 
emergency_contact_no_entry = customtkinter.CTkEntry(frame, placeholder_text="e.g 0332-8976543", width = 230, height = 30, fg_color="#24272C", border_width=0, text_color="white")
emergency_contact_no_entry.place(relx= 0.624, rely = 0.49, anchor = "e")

#emergency contact no undreline
emergency_contact_no_line = customtkinter.CTkFrame(frame, width = 220, height = 3, bg_color="white")
emergency_contact_no_line.place(relx = 0.621, rely = 0.52, anchor = "e")

#emergency contact name picture
emergency_contact_name_image=customtkinter.CTkImage(light_image=Image.open("C:\\Users\\ZOR30\\OneDrive\\Desktop\\emergencycontacname.png"),dark_image=Image.open("C:\\Users\\ZOR30\\OneDrive\\Desktop\\emergencycontacname.png"),size=(85,85))
emergency_contact_name_image_label=customtkinter.CTkLabel(frame, text="",image=emergency_contact_name_image)
emergency_contact_name_image_label.place(relx=0.4,rely=0.65, anchor="center")

#emergency contact name label
emergency_contact_name_label = customtkinter.CTkLabel(frame, text = "Emergency Info", font =customtkinter.CTkFont("Arial", 15), bg_color= 'transparent', text_color="#FFFFFF")
emergency_contact_name_label.place(relx = 0.4, rely = 0.72, anchor = "center")

#emergency contact name entry 
emergency_contact_name_entry = customtkinter.CTkEntry(frame, placeholder_text="e.g Lisa Evans", width = 230, height = 30, fg_color="#24272C", border_width=0, text_color="white")
emergency_contact_name_entry.place(relx= 0.624, rely = 0.69, anchor = "e")

#emergency contact name undreline
emergency_contact_name_line = customtkinter.CTkFrame(frame, width = 220, height = 3, bg_color="white")
emergency_contact_name_line.place(relx = 0.621, rely = 0.72, anchor = "e")
#----------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------

#user image on the left
user_image=customtkinter.CTkImage(light_image=Image.open("C:\\Users\\ZOR30\\OneDrive\\Desktop\\gymuserlogo.png"),dark_image=Image.open("C:\\Users\\ZOR30\\OneDrive\\Desktop\\gymuserlogo.png"),size=(90,90))
user_image_label=customtkinter.CTkLabel(frame, text="",image=user_image)
user_image_label.place(relx=0.8,rely=0.1, anchor="center")

#user info label
user_info_label = customtkinter.CTkLabel(frame, text = "User Information", font =customtkinter.CTkFont("Arial", 20,"bold"), bg_color= 'transparent', text_color="#FFFFFF")
user_info_label.place(relx = 0.8, rely = 0.2, anchor = "center")

#user ID Label
user_id_label = customtkinter.CTkLabel(frame, text = "User ID", font =customtkinter.CTkFont("Arial", 20,"bold"), bg_color= 'transparent', text_color="#FFFFFF")
user_id_label.place(relx = 0.7, rely = 0.3, anchor = "center")

#user ID display field
user_id_display=customtkinter.CTkLabel(app, text="User ID",font =customtkinter.CTkFont("Arial", 20), bg_color= '#000000', text_color="#FFFFFF")
user_id_display.place(relx=0.8,rely=0.307,anchor="center")

#username Label
username_label = customtkinter.CTkLabel(frame, text = "Name", font =customtkinter.CTkFont("Arial", 20,"bold"), bg_color= 'transparent', text_color="#FFFFFF")
username_label.place(relx = 0.7, rely = 0.4, anchor = "center")

#username display field
username_display=customtkinter.CTkLabel(app, text="Name",font =customtkinter.CTkFont("Arial", 20), bg_color= '#000000', text_color="#FFFFFF")
username_display.place(relx=0.8,rely=0.407,anchor="center")

#user BMI Label
user_BMI_label = customtkinter.CTkLabel(frame, text = "BMI", font =customtkinter.CTkFont("Arial", 20,"bold"), bg_color= 'transparent', text_color="#FFFFFF")
user_BMI_label.place(relx = 0.7, rely = 0.5, anchor = "center")

#user BMI display field
user_BMI_display=customtkinter.CTkLabel(app, text="BMI",font =customtkinter.CTkFont("Arial", 20), bg_color= '#000000', text_color="#FFFFFF")
user_BMI_display.place(relx=0.8,rely=0.510,anchor="center")

#user weight Label
user_weight_label = customtkinter.CTkLabel(frame, text = "Weight", font =customtkinter.CTkFont("Arial", 20,"bold"), bg_color= 'transparent', text_color="#FFFFFF")
user_weight_label.place(relx = 0.7, rely = 0.6, anchor = "center")

#user weight display field
user_weight_display=customtkinter.CTkLabel(app, text="Weight",font =customtkinter.CTkFont("Arial", 20), bg_color= '#000000', text_color="#FFFFFF")
user_weight_display.place(relx=0.8,rely=0.610,anchor="center")

#user email label
user_email_label = customtkinter.CTkLabel(frame, text = "Email", font =customtkinter.CTkFont("Arial", 20,"bold"), bg_color= 'transparent', text_color="#FFFFFF")
user_email_label.place(relx = 0.7, rely = 0.7, anchor = "center")

#user email display field
user_email_display=customtkinter.CTkLabel(app, text="Email",font =customtkinter.CTkFont("Arial", 20), bg_color= '#000000', text_color="#FFFFFF")
user_email_display.place(relx=0.8,rely=0.72,anchor="center")

#add button
add_button = customtkinter.CTkButton(frame, text="ADD", corner_radius=35, fg_color="#0b5394",width=150,height=30,cursor="hand2")
add_button.place(relx=0.31, rely=0.8, anchor="center")









# Run the Tkinter event loop
app.mainloop()
