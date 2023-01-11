from tkinter import *

morse_decode_dict = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9"}

morse_encode_dict = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"}


def morse_code_decoder(dictionary):
    text = input_txt.get()
    text_dict = text.split(" ")
    decoded = ""

    for morse in text_dict:
        try:
            decoded += dictionary[morse]
        except:
            if morse == "/":
                decoded += " "
            else:
                pass
    output.delete(0, END)
    output.insert(0, decoded)


def morse_code_encoder(dictionary):
    text = input_txt.get()
    text = text.lower()
    text = text.split()
    encoded = ""
    for word in text:
        counter = 0
        for letter in word:
            counter += 1  # Counting to check if we are on the last index of the word.
            encoded += dictionary[letter] + " "
            if counter == len(word):
                encoded += "/ "
    final_encoded = encoded[0:-2]  # Removing last "/ ", cause it is not supposed to be there.
    output.delete(0, END)
    output.insert(0, final_encoded)


def select_process():
    selection = var.get()
    if selection == 1:
        morse_code_decoder(morse_decode_dict)
    elif selection == 2:
        morse_code_encoder(morse_encode_dict)


window = Tk()
title = window.title("Morse Code Translator")
var = IntVar()
canvas = Canvas(window, width=800, height=500, background="lightgrey")
canvas.pack()

input_txt = Entry(window, width=50, font=('Times New Roman', 15), background="white")
input_msg = Label(window, text="Input the text or morse code to translate", font=('Times New Roman', 20), background="lightgrey")

canvas.create_window(400, 170, window=input_txt)
canvas.create_window(400, 100, window=input_msg)

button1 = Radiobutton(window, text="Morse to Text", variable=var, value=1, font=('Times New Roman', 15), background="lightgrey")
button2 = Radiobutton(window, text="Text to Morse", variable=var, value=2, font=('Times New Roman', 15), background="lightgrey")
translate = Button(window, text="Translate", command=select_process, font=('Times New Roman', 13), background="white")
output = Entry(window, width=50, font=('Times New Roman', 20), background="white")
canvas.create_window(400, 350, window=output)
canvas.create_window(400, 300, window=translate)
canvas.create_window(400, 200, window=button1)
canvas.create_window(400, 230, window=button2)

window.mainloop()
