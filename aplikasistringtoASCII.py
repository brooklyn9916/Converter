import tkinter as tk


def string_to_ascii(string):
    ascii_list = []
    for char in string:
        ascii_list.append(ord(char))
    return ascii_list


def convert_base(number, base):
    if base == 2:
        return bin(number)[2:]
    elif base == 8:
        return oct(number)[2:]
    elif base == 10:
        return str(number)
    elif base == 16:
        return hex(number)[2:]


def convert_number(number, current_base, target_base):
    if current_base == target_base:
        return str(number)

    if current_base == 2:
        number = int(str(number), 2)
    elif current_base == 8:
        number = int(str(number), 8)
    elif current_base == 10:
        number = int(str(number), 10)
    elif current_base == 16:
        number = int(str(number), 16)

    if target_base == 2:
        return bin(number)[2:]
    elif target_base == 8:
        return oct(number)[2:]
    elif target_base == 10:
        return str(number)
    elif target_base == 16:
        return hex(number)[2:]


def convert_string():
    string = input_text.get()
    ascii_list = string_to_ascii(string)
    ascii_output.config(text=f"ASCII values: {ascii_list}")

    choice = base_var.get()
    target_base = 2 if choice == "Binary" else (
        8 if choice == "Octal" else (10 if choice == "Decimal" else 16))
    converted_list = [convert_base(number, target_base)
                      for number in ascii_list]
    base_output.config(text=f"{choice}-converted values: {converted_list}")


def convert_number_func():
    number = int(number_text.get())
    current_base = int(current_base_var.get())
    target_base = int(target_base_var.get())
    converted_number = convert_number(number, current_base, target_base)
    number_output.config(
        text=f"{current_base}-converted to {target_base}: {converted_number}")


# Create the main window
root = tk.Tk()
root.title("Conversion Tool")
root.geometry("700x400")

# Create string conversion widgets
input_label = tk.Label(root, text="Enter a string:")
input_label.grid(row=0, column=0)

input_text = tk.Entry(root)
input_text.grid(row=0, column=1)

ascii_output = tk.Label(root, text="")
ascii_output.grid(row=1, column=0, columnspan=2)

base_var = tk.StringVar(value="Binary")

base_label = tk.Label(root, text="Convert ASCII values to:")
base_label.grid(row=2, column=0)

binary_radio = tk.Radiobutton(
    root, text="Binary", variable=base_var, value="Binary")
binary_radio.grid(row=2, column=1)

octal_radio = tk.Radiobutton(
    root, text="Octal", variable=base_var, value="Octal")
octal_radio.grid(row=4, column=1)

decimal_radio = tk.Radiobutton(
    root, text="Decimal", variable=base_var, value="Decimal")
decimal_radio.grid(row=5, column=1)

hex_radio = tk.Radiobutton(root, text="Hexadecimal",
                           variable=base_var, value="Hexadecimal")
hex_radio.grid(row=6, column=1)

base_button = tk.Button(root, text="Convert", command=convert_string)
base_button.grid(row=7, column=0, columnspan=2)

base_output = tk.Label(root, text="")
base_output.grid(row=3, column=0, columnspan=2)

number_label = tk.Label(root, text="Enter a number:")
number_label.grid(row=8, column=0)

number_text = tk.Entry(root)
number_text.grid(row=8, column=1)

current_base_var = tk.StringVar(value="10")

current_base_label = tk.Label(root, text="Target base:")
current_base_label.grid(row=10, column=0)

current_base_menu = tk.OptionMenu(root, current_base_var, "2", "8", "10", "16")
current_base_menu.grid(row=9, column=1)

target_base_var = tk.StringVar(value="2")

target_base_label = tk.Label(root, text="Current base:")
target_base_label.grid(row=9, column=0)

target_base_menu = tk.OptionMenu(root, target_base_var, "2", "8", "10", "16")
target_base_menu.grid(row=10, column=1)

number_button = tk.Button(root, text="Convert", command=convert_number_func)
number_button.grid(row=11, column=0, columnspan=2)

number_output = tk.Label(root, text="")
number_output.grid(row=12, column=0, columnspan=2)

root.mainloop()
