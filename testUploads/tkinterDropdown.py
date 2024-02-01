import tkinter as tk

window = tk.Tk()
frame = tk.Frame(master=window, width=500, height=500)
frame.pack()

desc = tk.Label(text="Location: California", master=frame, font=("Arial", 10, "bold"), bg='white')
desc.place(x=175, y=10)
greeting = tk.Label(text="Choose the restaurant options that you want", master=frame, font=("Arial", 15), bg='white')
greeting.place(x=50, y=50)
# entry = tk.Entry(fg="yellow", bg="blue", width=25, master=frame)
# entry.place(x=100, y=250)


# https://pythonbasics.org/tkinter-checkbox/

# c1 = tk.Checkbutton(window, text='A', onvalue=1, offvalue=0)  # command=print_selection, variable=var1,
# c1.pack()
# c2 = tk.Checkbutton(window, text='B', onvalue=1, offvalue=0)  # command=print_selection, variable=var2,
# c2.pack()

# restaurants in California only
# top 3 most popular restaurants in california in each category (sometimes only the top 1 restaurant match)
# # restaurant has to have the category food type as their main food type
# expensive restaurants are defined by googles $ sign search (example: expensive counts as $$$-$$$$, cheap counts as: $-$$)
# sources: google restaurant finder, yelp.com, bestthingsca.com
def submit():
    # Arbitrarily execute Python code
    # print("I chose:", clicked1.get())
    price = clicked1.get()
    cuisine = clicked2.get()

    # Render some text to the interface/screen)
    # the label has been placed on the interface on line 80
    # in this line, we set the text content of the label to whatever value that we want



    if price == 'Expensive' and cuisine == 'Pizza':
        results.config(text="Berri's Cafe, Five Restaurant, The Annex Kitchen")
    elif price == 'Expensive' and cuisine == 'Mexican':
        results.config(text="RED O 'Taste of Mexico'")
    elif price == 'Expensive' and cuisine == 'Fast Food':
        results.config(text="We could not find a restaurant that matches your description")
    elif price == 'Expensive' and cuisine == 'Desserts':
        results.config(text=" ")
    elif price == 'Expensive' and cuisine == 'Sushi':
        results.config(text="Sushi Gen, SUGARFISH by sushi nozawa, Matsuhisa")
    elif price == 'Expensive' and cuisine == 'Chinese':
        results.config(text="TAO, Mr Chow, Cheung Hing Seafood & Dimsum")
    elif price == 'Expensive' and cuisine == 'Burgers':
        results.config(text="Elbow Room Bar & Grill, The Lime Lite, Tommy's Restaurant")
    elif price == 'Expensive' and cuisine == 'Italian':
        results.config(text="Scopa Italian Roots, Bestia, Rossoblu")
    elif price == 'Expensive' and cuisine == 'Indian':
        results.config(text="Saffron - Burlingame, Spice Affair, All India Cafe")
    elif price == 'Cheap' and cuisine == 'Pizza':
        results.config(text="The Cheese Board Pizza, Bronx Pizza, 786 Degrees")
    elif price == 'Cheap' and cuisine == 'Mexican':
        results.config(text="El Toreo Cafe, El Huarache Azteca, La Super-Rica Taqueria")
    elif price == 'Cheap' and cuisine == 'Fast Food':
        results.config(text="In-N-Out, McDonald's, Chick-Fil-A")
    elif price == 'Cheap' and cuisine == 'Desserts':
        results.config(text=" ")
    elif price == 'Cheap' and cuisine == 'Sushi':
        results.config(text="Hide Sushi, Mrs. Fish, Noshi Sushi")
    elif price == 'Cheap' and cuisine == 'Chinese':
        results.config(text="Panda Express, Rice Bowl, P.F. Chang's")
    elif price == 'Cheap' and cuisine == 'Burgers':
        results.config(text="In-N-Out, McDonald's, Five Guys")
    elif price == 'Cheap' and cuisine == 'Italian':
        results.config(text="Maggiano's Little Italy, Buca di Beppo Italian Restaurant, Giuseppe's Cucina Rustica")
    elif price == 'Cheap' and cuisine == 'Indian':
        results.config(text="Heart Of India Bar & Restaurant, Kabana Restaurant, Cardamom")


# Text for "expensive or cheap"
priceText = tk.Label(text="Choose between cheap or expensive food", master=frame, font=("Arial", 10, "bold"))
priceText.place(x=100, y=100)

# https://www.geeksforgeeks.org/dropdown-menus-tkinter/#
# Dropdown menu options
optionsPrice = [
    "Expensive",
    "Cheap",
]

# text for "choosing a cuisine"
foodText = tk.Label(text="Choose a type of cuisine", master= frame, font=("Arial", 10, "bold" ))
foodText.place(x=155, y=250)

optionsCuisine = [
    "Pizza",
    "Mexican",
    "Fast Food",
    "Desserts",
    "Sushi",
    "Chinese",
    "Burgers",
    "Italian",
    "Indian"
]

clicked1 = tk.StringVar()  # datatype of menu text
clicked1.set("Choose a price")  # initial menu text

clicked2 = tk.StringVar()  # datatype of menu text
clicked2.set("Choose a cuisine")  # initial menu text


drop1 = tk.OptionMenu(window, clicked1, *optionsPrice)  # Create Dropdown menu
drop1.place(x=180, y=150)

drop2 = tk.OptionMenu(window, clicked2, *optionsCuisine)  # Create Dropdown menu
drop2.place(x=175, y=300)
###

results = tk.Label(window, text="", font=("Arial", 12, "bold"))
results.pack(pady=50)

button = tk.Button(window, text="Submit", command=submit).place(x=180, y=350)  # Button to change label text

# Create Label

window.mainloop()