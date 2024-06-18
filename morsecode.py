import time
import winsound  # for Windows sound output
import tkinter as tk  # for GUI

# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-','!': '-.-.--'
}

# Function to encode text to Morse code
def encode_to_morse(text):
    if not text:
        raise ValueError("Input text is empty")
    morse_code = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
        else:
            morse_code += char + ' '  # Keep non-alphanumeric characters as they are
    return morse_code.strip()

# Function to decode Morse code to text
def decode_from_morse(morse_code):
    if not morse_code:
        raise ValueError("Input Morse code is empty")
    morse_code += ' '  # Add a space to signify the end of a Morse code sequence
    decoded_text = ''
    morse_char = ''
    for symbol in morse_code:
        if symbol != ' ':
            morse_char += symbol
        else:
            for key, value in MORSE_CODE_DICT.items():
                if morse_char == value:
                    decoded_text += key
                    break
            morse_char = ''
    return decoded_text

# Function to play Morse code as sound
def play_morse_code(morse_code, dot_duration=100, dash_duration=300, space_duration=1000):
    for symbol in morse_code:
        if symbol == '.':
            winsound.Beep(440, dot_duration)  # 440 Hz for dot
        elif symbol == '-':
            winsound.Beep(440, dash_duration)  # 440 Hz for dash
        elif symbol == ' ':
            time.sleep(space_duration / 1000)  # Wait for space duration

# Function to handle button click event in GUI
def on_encode_decode_click():
    input_text = input_entry.get().strip()
    if not input_text:
        output_label.config(text="Input text is empty", fg="red")
        return
    try:
        if encode_decode_var.get() == "Encode":
            morse_code = encode_to_morse(input_text)
            output_label.config(text="Morse code: " + morse_code, fg="black")
            play_morse_code(morse_code)
        else:
            decoded_text = decode_from_morse(input_text)
            output_label.config(text="Decoded text: " + decoded_text, fg="black")
    except ValueError as e:
        output_label.config(text=str(e), fg="red")

# GUI setup
root = tk.Tk()
root.title("Morse Code Converter")

input_label = tk.Label(root, text="Enter text or Morse code:")
input_label.pack()

input_entry = tk.Entry(root, width=50)
input_entry.pack()

encode_decode_var = tk.StringVar()
encode_decode_var.set("Encode")

encode_radio = tk.Radiobutton(root, text="Encode", variable=encode_decode_var, value="Encode")
encode_radio.pack()

decode_radio = tk.Radiobutton(root, text="Decode", variable=encode_decode_var, value="Decode")
decode_radio.pack()

encode_decode_button = tk.Button(root, text="Encode/Decode", command=on_encode_decode_click)
encode_decode_button.pack()

output_label = tk.Label(root, text="")
output_label.pack()

root.mainloop()
