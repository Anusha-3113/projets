import tkinter as tk

# Create the main window.
window = tk.Tk()
window.title("Calculator")

# Create the display.
display = tk.Entry(window, width=30)
display.grid(row=0, column=0, columnspan=4)

# Create the buttons.
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['.', '0', '=', '+']
]

for row in range(4):
    for column in range(4):
        button = tk.Button(window, text=buttons[row][column])
        button.grid(row=row+1, column=column)

# Define the button click handler.
def button_click(button):
    if button == '=':
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(0, result)
        except:
            display.delete(0, tk.END)
            display.insert(0, "Error")
    elif button == '.':
        if '.' not in display.get():
            display.insert(tk.END, button)
    else:
        display.insert(tk.END, button)

# Bind the button click handler to the buttons.
for button in buttons:
    for b in button:
        button = tk.Button(window, text=b, command=lambda b=b: button_click(b))

# Start the main loop.
window.mainloop()