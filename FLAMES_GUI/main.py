from tkinter import *

# function for removing common characters
def remove_match_char(list1, list2):

	for i in range(len(list1)) :
		for j in range(len(list2)) :

			if list1[i] == list2[j] :
				c = list1[i]

				# remove character from the list
				list1.remove(c)
				list2.remove(c)

				list3 = list1 + ["*"] + list2

				# return the concatenated list with True flag
				return [list3, True]


	list3 = list1 + ["*"] + list2
	return [list3, False]


# function for telling the relationship status
def tell_status() :
	
	p1 = Player1_field.get()

	p1 = p1.lower()

	p1.replace(" ", "")

	p1_list = list(p1)

	p2 = Player2_field.get()
	p2 = p2.lower()
	p2.replace(" ", "")
	p2_list = list(p2)

	proceed = True
	
	while proceed :

		ret_list = remove_match_char(p1_list, p2_list)

		con_list = ret_list[0]

		proceed = ret_list[1]

		star_index = con_list.index("*")

		p1_list = con_list[ : star_index]

		p2_list = con_list[star_index + 1 : ]


	# count total remaining characters
	count = len(p1_list) + len(p2_list)

	# list of FLAMES acronym
	result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

	while len(result) > 1 :

		split_index = (count % len(result) - 1)

		if split_index >= 0 :

			# list slicing
			right = result[split_index + 1 : ]
			left = result[ : split_index]

			# list concatenation
			result = right + left

		else :
			result = result[ : len(result) - 1]

	Status_field.insert(10, result[0])


# Function for clearing the
# contents of all text entry boxes
def clear_all() :
	Player1_field.delete(0, END)
	Player2_field.delete(0, END)
	Status_field.delete(0, END)

	Player1_field.focus_set()


if __name__ == "__main__" :

	root = Tk()

	root.configure(background = 'dark green')

	# Set the configuration of GUI window
	root.geometry("350x125")

	# set the name of tkinter GUI window
	root.title("Flames Game")
	
	# Create a Player 1 Name: label
	label1 = Label(root, text = "Player 1 Name: ",
				fg = 'black', bg = 'dark green')

	# Create a Player 2 Name: label
	label2 = Label(root, text = "Player 2 Name: ",
				fg = 'black', bg = 'dark green')
	
	# Create a Relation Status: label
	label3 = Label(root, text = "Relationship Status: ",
				fg = 'black', bg = 'red')

	label1.grid(row = 1, column = 0, sticky ="E")
	label2.grid(row = 2, column = 0, sticky ="E")
	label3.grid(row = 4, column = 0, sticky ="E")

	Player1_field = Entry(root)
	Player2_field = Entry(root)
	Status_field = Entry(root)

	Player1_field.grid(row = 1, column = 1, ipadx ="50")
	Player2_field.grid(row = 2, column = 1, ipadx ="50")
	Status_field.grid(row = 4, column = 1, ipadx ="50")

	button1 = Button(root, text = "Submit", bg = "red",
					fg = "black", command = tell_status)

	button2 = Button(root, text = "Clear", bg = "red",
					fg = "black", command = clear_all)

	button1.grid(row = 3, column = 1)
	button2.grid(row = 5, column = 1)

	root.mainloop()
