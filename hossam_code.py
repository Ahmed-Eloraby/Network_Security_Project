import tkinter as tk

def create_input_window():
    def submit_action():
        user_input = entry.get()
        # Do something with the user input
        print(f"User input: {user_input}")

    # Create the main application window
    window = tk.Tk()
    window.title("Input Window")
    window.geometry("300x150")

    # Configure window background color
    window.configure(bg="#f0f0f0")

    # Configure label style
    label_style = {"font": ("Arial", 12), "bg": "#f0f0f0", "fg": "#333333"}

    # Add a label
    label = tk.Label(window, text="Enter your input:", **label_style)
    label.pack(pady=10)

    # Add an entry field for input
    entry = tk.Entry(window, font=("Arial", 12))
    entry.pack(pady=5)

    # Add a submit button
    button = tk.Button(window, text="Submit", command=submit_action, font=("Arial", 12))
    button.pack(pady=10)

    # Start the event loop
    window.mainloop()

# Create and run the input window
create_input_window()