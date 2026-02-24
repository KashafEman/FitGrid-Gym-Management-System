import customtkinter
from PIL import Image, ImageTk
import pyodbc
from tkinter import ttk, messagebox

app = customtkinter.CTk()
app.geometry("1000x700")
app.resizable(True, True)
customtkinter.set_appearance_mode("dark")
app.title("Fat Man Gym Management System")

tree = None
total_earnings_label = None
#function to display data
def fetch_and_display_data():
    global tree

 # Create a treeview to display the data
    columns = ["Expense ID", "Expense Description", "Amount", "Status"]
    tree = ttk.Treeview(app, columns=columns, show="headings")
    tree.tag_configure('mytag', font=('Helvetica', 40))

    # Add column headings
    for col in columns:
        # Update column heading from "Payment Plan" to "Expenses Plan"
        if col == "Expenses Plan":
            tree.heading(col, text="Expenses Plan")
        else:
            tree.heading(col, text=col)
        tree.column(col, width=150)  # Adjust the width as needed

    # Add column headings
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=220)  

    tree.place(relx=0.1, rely=0.2, anchor="nw")

fetch_and_display_data()

# FRAMES -----------------------------------------------------------------------------------------------------------------------------------------------------

# top frame
top_frame = customtkinter.CTkFrame(app, width=2000, height=80, fg_color="#34383e", corner_radius=0)
top_frame.grid(row=0, column=0, columnspan=2)

# Gym logo image
logo_image = customtkinter.CTkImage(light_image=Image.open("C:\\Users\\ZOR30\\OneDrive\\Desktop\\blacktm.png"), dark_image=Image.open("C:\\Users\\ZOR30\\OneDrive\\Desktop\\blacktm.png"), size=(55, 55))
logo_image_label = customtkinter.CTkLabel(top_frame, text="", image=logo_image)
logo_image_label.place(relx=0.03, rely=0.5, anchor="center")

# gym name label
gym_name_label = customtkinter.CTkLabel(top_frame, text="GYM - EXPENSES RECORDS",
                                        font=customtkinter.CTkFont("Doubledecker DEMO", 40, "bold"),
                                        bg_color='transparent', text_color="#3d85c6")
gym_name_label.place(relx=0.19, rely=0.5, anchor="center")

# Cash image
cash_image = customtkinter.CTkImage(light_image=Image.open("C:\\Users\\ZOR30\\OneDrive\\Desktop\\expenses.png"), dark_image=Image.open("C:\\Users\\ZOR30\\OneDrive\\Desktop\\expenses.png"),
                                    size=(600, 600))
cash_image_label = customtkinter.CTkLabel(app, text="", image=cash_image)
cash_image_label.place(relx=0.9, rely=0.8, anchor="center")





  


# Create "back" button
make_payment_button = customtkinter.CTkButton(app, text="Back")
make_payment_button.place(relx=0.3, rely=0.9, anchor="nw")

app.mainloop()