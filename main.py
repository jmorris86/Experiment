import numpy as np
import time
from tkinter import *
from tkinter import ttk, messagebox
import pandas
import random
from vendor_creator import Vendor

BACKGROUND_COLOR = "#B1DDC6"
people = ["A", "B"]
people_prob = [0.3, 0.7]
utility_multiplier = round(0.20, 2)
flat_fee = 1
rounds = 10
utility = 0
utility_a = 0
utility_b = 0
utility_c = 0
purchases_vendor_a = 0
purchases_vendor_b = 0
purchases_vendor_c = 0
offer_dist = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
accepted_offers = [.05, .15, .15, .15, .15, .2, .05, .04, .03, .02, 0.01]
counter = 0
places = ["Belfast", "Bristol", "Cardiff", "Cambridge", "Chester", "Cork", "Dublin", "Edinburgh", "Glasgow", "Leeds",
		  "London", "Manchester", "Newport"]
name = ""
vendor_a = Vendor()
vendor_b = Vendor()
vendor_c = Vendor()
vendor_a_city = random.choice(places)
vendor_b_city = random.choice(places)
vendor_c_city = random.choice(places)
experiment_round = 1
Type = np.random.choice(people, p=people_prob)
preferences = {
	"A": ["Specialist", "High Quality", "Low Quality"],
	"B": ["High Quality", "Low Quality", "Specialist"],
}
instruction_text_1 = f"Thank you for agreeing to take part in this online experiment. \n\nThe experiment takes place" \
					 f" in an online marketplace where you will be randomly assigned\nto the role of vendor or " \
					 f"purchaser.\n\nIf you are a purchaser you will be randomly assigned to one of two equal sized " \
					 f"groups, A or B. \nAs a vendor you will be assigned to one of three groups, High Quality," \
					 f" Low Quality, or \nSpecialist Product - where 40% of the population are High Quality, 40% Low " \
					 f"Quality, and 20%\nSpecialist Producers." \
					 f"\n\nThe experiment consists of {rounds} rounds. In each round a purchaser must buy" \
					 f" a product from one\nof the vendors. Vendors display the average star rating of their previous " \
					 f"customers. Vendors\nnot chosen by the user are chosen at random by a purchaser of unknown type," \
					 f" their payoff\nis then added to the vendor history in the following round. " \
					 f"\n\nPurchasers receive payoff from buying a product of between 1 and 5 stars. Each purchase\n" \
					 f"results in a payoff of £{utility_multiplier:.2f} per star i.e. 1 star rating results in " \
					 f"£{utility_multiplier:.2f}, 2 star rating results in\n£{2 * utility_multiplier:.2f} etc."

instruction_text_2 = f"\n\nDependent on purchaser and vendor types, purchases have different probabilities of " \
					 f"being highly\nrated. For both type A and type B purchasers, " \
					 f"the average purchase from a High Quality vendor\nresults in 3.5 stars, whereas the average for" \
					 f" Low Quality vendors is 2.5 stars. \n\nType A purchasers enjoy Specialty products and these " \
					 f"types of purchases result in an average\nof 4 stars, whereas Type B purchasers dislike Specialty" \
					 f" products and these purchases result in\nan average of 2 stars.\n\nIf a product results in a " \
					 f"specific rating in a round, it may not result in the same rating in a different\nround. \n\nAt " \
					 f"the end of round {rounds}, purchasers will see a summary of total payoff generated from " \
					 f"transactions\nwith each vendor. Purchasers will then be asked to propose a one time take it or " \
					 f"leave it offer to the\nvendor. In the event that a vendor rejects an offer, each participant " \
					 f"will leave with nothing. If the\nvendor accepts the offer, purchasers will be " \
					 f"remunerated an amount equal to the total payoff less\nthe amount given to the vendor."


def next_page():
	global counter, experiment_round, utility, utility_a, utility_b, utility_c, purchases_vendor_a, \
		purchases_vendor_b, purchases_vendor_c, name
	relationship_status = ""
	partner_name = ""
	if counter == 0:
		canvas.itemconfig(card_title, text="Instructions (2 of 2)")
		canvas.itemconfig(card_info, text=instruction_text_2)
		counter += 1
	elif counter == 1:
		canvas.itemconfig(card_title, text="Personal Information")
		# canvas.moveto(card_title, 300, 50)
		# canvas.moveto(card_info, 250, 20)
		canvas.itemconfig(card_info, text="")
		canvas.create_window(350, 160, window=label_widget1)
		canvas.create_window(350, 260, window=label_widget2)
		canvas.create_window(350, 360, window=label_widget3)
		canvas.create_window(650, 160, window=entry_widget1)
		canvas.create_window(650, 260, window=entry_widget2)
		canvas.create_window(650, 360, window=entry_widget3)
		entry_widget1.focus()
		counter += 1
	elif counter == 2:
		if entry_widget1.get() == "Name":
			messagebox.showwarning("Warning", "Please Enter Your Name.")
		elif entry_widget2.get() != "Single" and entry_widget3.get() == "N/A":
			messagebox.showwarning("Warning", "Please Enter Your Partner's Name.")
		elif entry_widget2.get() == "Single" and entry_widget3.get() != "N/A":
			messagebox.showwarning("Warning", "You have entered your partner's name, but selected 'relationship"
											  " status' as single.\n\nPlease delete partner's name or amend"
											  " your relationship status.")
		else:
			name = entry_widget1.get()
			relationship_status = entry_widget2.get()
			partner_name = entry_widget3.get()
			entry_widget1.destroy()
			entry_widget2.destroy()
			entry_widget3.destroy()
			label_widget1.destroy()
			label_widget2.destroy()
			label_widget3.destroy()
			canvas.itemconfig(card_title, text="Experiment Role and Type")
			canvas.moveto(card_title, 260, 70)
			canvas.itemconfig(card_info,
							  text=f"\n\n{name} you have been randomly assigned to the role of Purchaser\nand "
								   f"are Type {Type}.\n\nPlease remember, on average Type {Type} receives the highest "
								   f"payoff from \n{preferences[Type][0]} vendors, the second highest payoff from "
								   f"{preferences[Type][1]} vendors,\nand the lowest amount from {preferences[Type][2]}"
								   f" vendors.", font=("Ariel", 14, "italic"))
			counter += 1
	elif counter == 3:
		next_button.grid(row=1, column=0, columnspan=2)
		next_round()
		counter += 1
	elif counter == 4:
		if choice_widget2.get() == "Please Choose a Vendor":
			messagebox.showwarning("Warning", "Please Choose a Vendor.")
		else:
			if experiment_round < rounds + 1:
				choice = choice_values.index(choice_widget2.get())
				if int(choice) == 1:
					utility_gen = vendor_a.vendor_utility(Type)
					utility_a += round(utility_gen, 2)
					purchases_vendor_a += 1
					vendor_b.vendor_utility(np.random.choice(people, p=people_prob))
					vendor_c.vendor_utility(np.random.choice(people, p=people_prob))
				elif int(choice) == 2:
					vendor_a.vendor_utility(np.random.choice(people, p=people_prob))
					utility_gen = vendor_b.vendor_utility(Type)
					vendor_c.vendor_utility(np.random.choice(people, p=people_prob))
					utility_b += round(utility_gen, 2)
					purchases_vendor_b += 1
				else:
					vendor_a.vendor_utility(np.random.choice(people, p=people_prob))
					vendor_b.vendor_utility(np.random.choice(people, p=people_prob))
					utility_gen = vendor_c.vendor_utility(Type)
					utility_c += round(utility_gen, 2)
					purchases_vendor_c += 1
				utility += round(utility_gen, 2)
				messagebox.showinfo("Purchase Payoff", f"Your purchase was rated as {utility_gen} stars "
													   f"and results in payoff of "
													   f"£{round(utility * utility_multiplier, 2):.2f}.\n\n"
													   f"Total payoff from purchases is now £"
													   f"{round(utility * utility_multiplier, 2):.2f}.")
				if experiment_round < rounds:
					experiment_round += 1
					next_round()
				else:
					counter += 1
					canvas.itemconfig(card_title, text="Purchase Summary")
					statement = f"{name} a summary of your purchases over the {rounds} rounds is as follows:\n\n" \
								f"{earnings_calculator(1, purchases_vendor_a, utility_a, utility_multiplier)}\n\n" \
								f"{earnings_calculator(2, purchases_vendor_b, utility_b, utility_multiplier)}\n\n" \
								f"{earnings_calculator(3, purchases_vendor_c, utility_c, utility_multiplier)}\n\n"
					canvas.itemconfig(card_info, text=statement)
					choice_widget2.destroy()

	elif counter == 5:
		counter += 1
		canvas.itemconfig(card_title, text="Sharing Payoff")
		statement = f"You will now be asked to make a one time take it or leave it offer to each vendor.\nYou can offer" \
					f" any amount up to the total payoff generated from that vendor.\n\nVendors are " \
					f"real people and can reject offers. If an offer is rejected, you will\nleave with nothing. If " \
					f"the vendor accepts, you will be paid an amount equal\nto the total payoff from the vendor less " \
					f"the amount paid to them. \n\nYou need to consider both the likelihood of the offer being " \
					f"accepted and how\nmuch you are willing to give away."
		canvas.itemconfig(card_info, text=statement)
	elif counter == 6:
		canvas.itemconfig(card_info, text="")
		canvas.itemconfig(card_title, text="Vendor Offers")
		final_label1.configure(text=f"{vendor_a.print_status(1, vendor_a_city, experiment_round)}")
		final_label2.configure(text=f"{vendor_b.print_status(2, vendor_b_city, experiment_round)}")
		final_label3.configure(text=f"{vendor_c.print_status(3, vendor_c_city, experiment_round)}")
		offer_widget1.configure(to=round(utility_a * utility_multiplier, 2))
		offer_widget2.configure(to=round(utility_b * utility_multiplier, 2))
		offer_widget3.configure(to=round(utility_c * utility_multiplier, 2))
		canvas.create_window(350, 160, window=label_offer1)
		canvas.create_window(350, 190, window=final_label1)
		canvas.create_window(650, 160, window=offer_widget1)
		canvas.create_window(350, 260, window=label_offer2)
		canvas.create_window(350, 290, window=final_label2)
		canvas.create_window(650, 260, window=offer_widget2)
		canvas.create_window(350, 360, window=label_offer3)
		canvas.create_window(350, 390, window=final_label3)
		canvas.create_window(650, 360, window=offer_widget3)
		counter += 1
	elif counter == 7:
		text = f"{name}, you made the following offers to each vendor:\n\n Vendor 1 - £{offer_widget1.get():.2f} out " \
			   f"of a total payoff of £{round(utility_a * utility_multiplier, 2):.2f}\n\nVendor 2 - " \
			   f"£{offer_widget2.get():.2f} out of a total payoff of £{round(utility_b * utility_multiplier, 2):.2f}\n\n " \
			   f"Vendor 3 - £{offer_widget3.get():.2f} out of a total payoff of " \
			   f"£{round(utility_c * utility_multiplier, 2):.2f}\n\nAre you happy to confirm these offers?"
		response = messagebox.askquestion("Offer Values", text)
		if response == "yes":
			earnings_a = 0
			earnings_b = 0
			earnings_c = 0
			if utility_a > 0:
				if np.random.choice(offer_dist, p=accepted_offers) < (
						offer_widget1.get() / round(utility_a * utility_multiplier, 2)):
					earnings_a = round((utility_a * utility_multiplier) - offer_widget1.get(), 2)
					statement_a = f"Your offer to Vendor 1 has been accepted, after Vendor payment, your\nearnings " \
								  f"from Vendor 1 are £{round(earnings_a, 2):.2f}."
				else:
					earnings_a = 0
					statement_a = f"Your offer to Vendor 1 has been rejected, as a result, your earnings from\nVendor " \
								  f"1 is £0."
			else:
				earnings_a = 0
				statement_a = "You did not make any purchases from Vendor 1."
			if utility_b > 0:
				if np.random.choice(offer_dist, p=accepted_offers) < (
						offer_widget2.get() / round(utility_b * utility_multiplier, 2)):
					earnings_b = round((utility_b * utility_multiplier) - offer_widget2.get(), 2)
					statement_b = f"Your offer to Vendor 2 has been accepted, after Vendor payment, your\nearnings " \
								  f"from Vendor 2 are £{round(earnings_b, 2):.2f}."
				else:
					earnings_b = 0
					statement_b = f"Your offer to Vendor 2 has been rejected, as a result, your earnings from\nVendor " \
								  f"2 is £0."
			else:
				earnings_b = 0
				statement_b = "You did not make any purchases from Vendor 2."
			if utility_c > 0:
				if np.random.choice(offer_dist, p=accepted_offers) < (
						offer_widget3.get() / round(utility_c * utility_multiplier, 2)):
					earnings_c = round((utility_c * utility_multiplier) - offer_widget3.get(), 2)
					statement_c = f"Your offer to Vendor 3 has been accepted, after Vendor payment, your\nearnings from" \
								  f" Vendor 3 are £{round(earnings_c, 2):.2f}."
				else:
					earnings_c = 0
					statement_c = f"Your offer to Vendor 3 has been rejected, as a result, your earnings from\nVendor " \
								  f"3 is £0."
			else:
				earnings_c = 0
				statement_c = "You did not make any purchases from Vendor 3."
			label_offer1.destroy()
			final_label1.destroy()
			offer_widget1.destroy()
			label_offer2.destroy()
			final_label2.destroy()
			offer_widget2.destroy()
			label_offer3.destroy()
			final_label3.destroy()
			offer_widget3.destroy()
			canvas.itemconfig(card_title, text="Summary")
			statement = f"{statement_a}\n\n{statement_b}\n\n{statement_c}\n\nIn addition to the flat fee of " \
						f"£{flat_fee:.2f}, this gives you total income of £" \
						f"{flat_fee + round(earnings_a + earnings_b + earnings_c, 2):.2f}. You will\nreceive the money " \
						f"into your bank account in the next 2-3 working days.\n\nThank you for taking part in this " \
						f"experiment. Have a good day!"
			canvas.itemconfig(card_info, text=statement)
			next_button.config(text="Finish", command=window.destroy)


def earnings_calculator(vendor_num, num_purchases, utility_from_purchases, multiplier):
	earnings = round(utility_from_purchases * multiplier, 2)
	if num_purchases == 0:
		return f"You didn't make any purchases from Vendor {vendor_num}."
	else:
		return f"You made {num_purchases} purchase(s) from Vendor {vendor_num} which resulted in a payoff of £" \
			   f"{earnings:.2f} at an \naverage rating of {round(utility_from_purchases / num_purchases, 1)} stars."


def next_round():
	canvas.itemconfig(card_title, text=f"\n\nRound {experiment_round}\n")
	canvas.itemconfig(card_info, text=f"{vendor_a.print_status(1, vendor_a_city, experiment_round)}\n\n"
									  f"{vendor_b.print_status(2, vendor_b_city, experiment_round)}\n\n"
									  f"{vendor_c.print_status(3, vendor_c_city, experiment_round)}")
	choice_widget2.grid()
	choice_widget2.current(0)


window = Tk()
window.title("Survey")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=1000, height=526)
card_img = PhotoImage(file='images/card_front.png')
canvas.create_image(500, 263, image=card_img)
card_title = canvas.create_text(500, 60, text="Instructions (1 of 2)", font=("Ariel", 30, "italic"))
card_info = canvas.create_text(500, 280, text=instruction_text_1, font=("Ariel", 12, "italic"))
check_image = PhotoImage(file="images/right.png")
next_button = Button(text="Next Page", command=next_page)
next_button.grid(row=1, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
entry_widget1 = Entry(window, width=30, background="white")
entry_widget1.insert(0, "Name")
values = ["Single", "Married", "Partner"]
entry_widget2 = ttk.Combobox(window, width=30, values=values, background="white", state="readonly")
entry_widget3 = ttk.Entry(window, width=30, background="white")
entry_widget2.current(0)
entry_widget3.insert(0, "N/A")
label_widget1 = Label(window, text="What is your first name?", background="white")
label_widget2 = Label(window, text="What is your relationship status?", background="white")
label_widget3 = Label(window, text="What is your partner's name?", background="white")
choice_values = ["Please Choose a Vendor", "Vendor 1", "Vendor 2", "Vendor 3"]
choice_widget2 = ttk.Combobox(window, width=30, values=choice_values, background=BACKGROUND_COLOR, state="readonly")
choice_widget2.grid(row=1, column=0)
choice_widget2.current(0)
choice_widget2.grid_remove()
label_offer1 = Label(window, text="How much of the available surplus would you like to offer to Vendor 1?",
					 background="white")
label_offer2 = Label(window, text="How much of the available surplus would you like to offer to Vendor 2?",
					 background="white")
label_offer3 = Label(window, text="How much of the available surplus would you like to offer to Vendor 3?",
					 background="white")
offer_widget1 = Scale(window, from_=0, to=round(utility_a * utility_multiplier, 2), orient=HORIZONTAL,
					  resolution=0.05, background="white")
offer_widget2 = Scale(window, from_=0, to=round(utility_b * utility_multiplier, 2), orient=HORIZONTAL,
					  resolution=0.05, background="white")
offer_widget3 = Scale(window, from_=0, to=round(utility_c * utility_multiplier, 2), orient=HORIZONTAL,
					  resolution=0.05, background="white")
final_label1 = Label(window, text="", background="white")
final_label2 = Label(window, text="", background="white")
final_label3 = Label(window, text="", background="white")
window.mainloop()
