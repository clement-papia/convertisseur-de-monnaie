import tkinter as tk 
import requests  


def converti():
    url = "https://api.exchangerate-api.com/v4/latest/EUR"
    response = requests.get(url)
    data = response.json()
    exchange = data["rates"]["USD"]

    original = float(amount_entry.get())
    converted = original * exchange

    result_label.config(text=f"{converted:.2f} USD")
    
    test = open("test.txt","a")
    test.write(f"{converted:.2f} USD\n")
    test.close()

windows = tk.Tk()
windows.title("Convertisseur euro/dollar")
windows.geometry('320x420')

amount_entry = tk.Entry(windows)
amount_entry.pack()

converti_button = tk.Button(windows, text="Convertir", command=converti)
converti_button.pack()

result_label = tk.Label(windows, text="")
result_label.pack()

windows.mainloop()