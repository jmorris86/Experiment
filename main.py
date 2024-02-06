import numpy as np
import time
from tkinter import *
from tkinter import ttk, messagebox
import pandas
import random
from vendor_creator import Vendor

BACKGROUND_COLOR = "#B1DDC6"
people = ["A", "B"]
people_prob = [0.5, 0.5]
utility_multiplier = round(0.20, 2)
flat_fee = 2.50
rounds = 10
utility = 0
utility_a = 0
utility_b = 0
utility_c = 0
purchases_vendor_a = 0
purchases_vendor_b = 0
purchases_vendor_c = 0
offer_dist = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
accepted_offers = [0.05, .2, .2, .2, .2, .05, .04, .03, .02, 0.01, 0]
bad_accepted_offers = [.2, .25, .15, .15, .15, .04, .03, .02, 0.01, 0, 0]
counter = 0
experiment_round = 1
places = ["Belfast", "Bristol", "Cardiff", "Cambridge", "Chester", "Cork", "Dublin", "Edinburgh", "Glasgow", "Leeds",
		  "London", "Manchester", "Newport"]
name = ""
vendor_a = Vendor()
vendor_b = Vendor()
vendor_c = Vendor()
vendor_a_city = random.choice(places)
vendor_b_city = random.choice(places)
vendor_c_city = random.choice(places)
Type = np.random.choice(people, p=people_prob)
preferences = {
	"A": ["Specialist", "High Quality", "Low Quality"],
	"B": ["High Quality", "Low Quality", "Specialist"],
}
# instruction_text_1 = f"Thank you for agreeing to take part in this online experiment. \n\nThe experiment takes place" \
# 					 f" in an online marketplace where you will be randomly assigned to \nthe role of vendor or " \
# 					 f"purchaser.\n\nIn each of the {rounds} rounds, a purchaser buys a product from one of the " \
# 					 f"vendors. Each purchase \nis rated between 1 and 5 stars, where each star is equal to a payment " \
# 					 f"of £{utility_multiplier:.2f} to the purchaser \ni.e. 1 star equals £{utility_multiplier:.2f}, " \
# 					 f"2 stars equals £{2*utility_multiplier:.2f} etc.\n\nVendors display the average star rating of " \
# 					 f"their previous customers. Any vendor not chosen \nby the participant are chosen at random by " \
# 					 f"other purchasers, their average rating is then \nadded to the vendor history in the following " \
# 					 f"round. \n\nAt the end of round {rounds}, purchasers will see a summary of total payoff generated " \
# 					 f"from transactions\nwith each vendor. " \
# 					 f"Purchasers will then be asked to propose a one time take it or leave it offer\nto the vendor. " \
# 					 f"If a vendor rejects an offer, each participant will leave with nothing. If the vendor\naccepts, " \
# 					 f"the vendor will receive the amount offered, and purchasers will be paid the total payoff\nless " \
# 					 f"the amount given to the vendor."

instruction_text_1 = f"Thank you for agreeing to participate in this experiment.\n\nYou are in an online " \
					 f"marketplace. There are {rounds} rounds and you will be randomly assigned to be a vendor \nor " \
					 f"purchaser for the entire time.\n\nPurchasers\nIn each round you will be asked to choose a" \
					 f" product from one of several vendors. Each purchase is rated \nbetween 1 and 5 stars and you are" \
					 f" paid £{utility_multiplier:.2f} for each star.\n\nYou will see the average rating of each " \
					 f"vendor's previous customers. Vendors not chosen by you are \nchosen at random by other " \
					 f"purchasers, and their rating is added to the vendor history in the next round. \n\nAt the end " \
					 f"of round {rounds}, you will see a summary of total payoff generated from each vendor. You will " \
					 f"then \npropose a one time take it or leave it offer to each vendor. " \
					 f"If a vendor accepts an offer, you will be paid the \ntotal payoff less the amount given" \
					 f" to the vendor. If the vendor rejects, both you and the vendor will leave \nwith nothing.\n\n" \
					 f"Vendors\nYou will be shown the number of purchases and the average rating of the participant's " \
					 f"purchases from \nyou. The participant will then make you a take it or leave it offer. If you " \
					 f"choose to accept, you will be paid \nthe offer, and the purchaser will take the rest. If you " \
					 f"reject the offer, you both leave with nothing."

instruction_text_2 = f"The market consists of different purchaser and vendor types. The market share of each \ntype " \
					 f"is as follows:\n\nPurchaser Types and Market Share		Vendor Types and Market Share" \
					 f"\n\n                  Type A - 50%				High Quality - 40%\n	Type " \
					 f"B - 50%				 Low Quality - 40%\n					  Specialist Producers - 20%\n\n" \
					 f"Dependent on purchaser and vendor types, purchases have different average ratings. The\naverage" \
					 f" rating for the different types is as follows:\n\n" \
					 f"       Purchaser Type A				      Purchaser Type B\n\nSpecialty Producer - 4 Stars			" \
					 f"	High Quality - 3.5 Stars\nHigh Quality - 3.5 Stars				Low Quality - 2.5 Stars\n" \
					 f"Low Quality - 2.5 Stars				Specialist Producer - 2 Stars\n\nIf a product results " \
					 f"in a specific rating in a round, it may not result in the same rating in a\ndifferent round."


def next_page():
	global counter, experiment_round, utility, utility_a, utility_b, utility_c, purchases_vendor_a, \
		purchases_vendor_b, purchases_vendor_c, name
	# relationship_status = ""
	# partner_name = ""
	if counter == 0:
		canvas.itemconfig(card_title, text="Market Structure")
		canvas.itemconfig(card_info, text=instruction_text_2)
		next_button.grid(row=1, column=1)
		back_button.grid(row=1, column=0)
		counter += 1
	elif counter == 1:
		canvas.itemconfig(card_title, text="Personal Information")
		back_button.grid(row=1, column=0)
		canvas.itemconfig(card_info, text="")
		canvas.itemconfig(lbl_1, state='normal')
		canvas.itemconfig(lbl_2, state='normal')
		canvas.itemconfig(lbl_3, state='normal')
		canvas.itemconfig(ent_1, state='normal')
		canvas.itemconfig(ent_2, state='normal')
		canvas.itemconfig(ent_3, state='normal')
		entry_widget1.focus()
		counter += 1
	elif counter == 2:
		if entry_widget1.get() == "Name":
			messagebox.showwarning("Warning", "Please Enter Your Name.")
		elif entry_widget2.get() != "Single" and entry_widget3.get() == "N/A":
			messagebox.showwarning("Warning", "Please Enter Your Partner's Name.")
		elif entry_widget2.get() == "Single" and entry_widget3.get() != "N/A" and entry_widget3.get() != "":
			messagebox.showwarning("Warning", "You have entered your partner's name, but selected 'relationship"
											  " status' as single.\n\nPlease delete partner's name or amend"
											  " your relationship status.")
		else:
			name = entry_widget1.get()
			# relationship_status = entry_widget2.get()
			# partner_name = entry_widget3.get()
			if Type == "A":
				word_1 = "4 stars"
				word_2 = "3.5 stars"
				word_3 = "2.5 stars"
			else:
				word_1 = "3.5 stars"
				word_2 = "2.5 stars"
				word_3 = "2 stars"
			canvas.itemconfig(lbl_1, state='hidden')
			canvas.itemconfig(lbl_2, state='hidden')
			canvas.itemconfig(lbl_3, state='hidden')
			canvas.itemconfig(ent_1, state='hidden')
			canvas.itemconfig(ent_2, state='hidden')
			canvas.itemconfig(ent_3, state='hidden')
			canvas.itemconfig(card_title, text="Experiment Role and Type")
			canvas.moveto(card_title, 260, 70)
			canvas.itemconfig(card_info,
							  text=f"\n\n{name} you have been randomly assigned to the role of Purchaser\nand are Type"
								   f" {Type}.\n\nPlease remember, Type {Type} receives an average of {word_1} from "
								   f"\n{preferences[Type][0]} vendors, {word_2} from {preferences[Type][1]} vendors, "
								   f"and \n{word_3} from {preferences[Type][2]} vendors.", font=("Ariel", 14, "italic"))
			counter += 1
	elif counter == 3:
		text = f"It is important to guess the vendor Type based on each vendor's sale history.\n\nAs a type " \
			   f"{Type} purchaser, buying exclusively from {preferences[Type][0]} vendors will earn you on average " \
			   f"£{round(1.5*utility_multiplier*rounds)} more than buying exclusively from {preferences[Type][2]} " \
			   f"vendors.\n\nIf you would like to proceed to the experiment, click yes. To revisit the instructions, " \
			   f"click no."
		response = messagebox.askquestion("Important Information", text)
		if response == "yes":
			next_button.grid(row=1, column=0, columnspan=2)
			back_button.grid_forget()
			canvas.moveto(card_title, 260, 40)
			next_round()
			counter += 1
		else:
			back_button.grid_remove()
			next_button.grid(row=1, column=0, columnspan=2)
			canvas.moveto(card_title, 260, 40)
			canvas.itemconfig(card_title, text="Instructions")
			canvas.itemconfig(card_info, text=instruction_text_1, font=("Ariel", 12, "italic"))
			counter = 0
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
					f" any amount up to the total payoff generated from that vendor.\n\nVendors are real people and " \
					f"can reject offers. If an offer is rejected, you will\nreceive nothing. If the vendor accepts, you" \
					f" will be paid an amount equal to the \ntotal payoff from the vendor less the amount paid to " \
					f"them. \n\nYou need to consider both the likelihood of the offer being accepted and how\nmuch you" \
					f" are willing to give away."
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
		canvas.create_window(650, 175, window=offer_widget1)
		canvas.create_window(350, 260, window=label_offer2)
		canvas.create_window(350, 290, window=final_label2)
		canvas.create_window(650, 275, window=offer_widget2)
		canvas.create_window(350, 360, window=label_offer3)
		canvas.create_window(350, 390, window=final_label3)
		canvas.create_window(650, 375, window=offer_widget3)
		canvas.create_window(500, 450, window=label_offer4)
		label_offer4.configure(font=("Ariel", 12, "italic"))
		counter += 1
	elif counter == 7:
		text = f"{name}, you made the following offers to each vendor:\n\nVendor 1 - £{offer_widget1.get():.2f} out " \
			   f"of a total payoff of £{round(utility_a * utility_multiplier, 2):.2f}\n\nVendor 2 - " \
			   f"£{offer_widget2.get():.2f} out of a total payoff of £{round(utility_b * utility_multiplier, 2):.2f}\n\n" \
			   f"Vendor 3 - £{offer_widget3.get():.2f} out of a total payoff of " \
			   f"£{round(utility_c * utility_multiplier, 2):.2f}\n\nAre you happy to confirm these offers?"
		response = messagebox.askquestion("Offer Values", text)
		if response == "yes":
			if utility_a > 0:
				if vendor_a.vendor_type == 2:
					offers = bad_accepted_offers
				else:
					offers = accepted_offers
				if np.random.choice(offer_dist, p=offers) < (
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
				if vendor_b.vendor_type == 2:
					offers = bad_accepted_offers
				else:
					offers = accepted_offers
				if np.random.choice(offer_dist, p=offers) < (
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
				if vendor_c.vendor_type == 2:
					offers = bad_accepted_offers
				else:
					offers = accepted_offers
				if np.random.choice(offer_dist, p=offers) < (
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
			label_offer4.destroy()
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
		return f"You did not make any purchases from Vendor {vendor_num}."
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


def last_page():
	global counter
	if counter == 1:
		back_button.grid_remove()
		next_button.grid(row=1, column=0, columnspan=2)
		canvas.itemconfig(card_title, text="Instructions")
		canvas.itemconfig(card_info, text=instruction_text_1)
		counter -= 1
	elif counter == 2:
		counter -= 2
		canvas.itemconfig(lbl_1, state="hidden")
		canvas.itemconfig(lbl_2, state="hidden")
		canvas.itemconfig(lbl_3, state="hidden")
		canvas.itemconfig(ent_1, state="hidden")
		canvas.itemconfig(ent_2, state="hidden")
		canvas.itemconfig(ent_3, state="hidden")
		next_page()
	if counter == 3:
		canvas.moveto(card_title, 260, 40)
		canvas.itemconfig(card_info, font=("Ariel", 12, "italic"))
		counter -= 2
		next_page()


window = Tk()
window.title("Survey")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=1000, height=526)
card_img = PhotoImage(file='images/card_front.png')
canvas.create_image(500, 263, image=card_img)
card_title = canvas.create_text(500, 60, text="Instructions", anchor="center", font=("Ariel", 30, "italic"))
card_info = canvas.create_text(500, 280, text=instruction_text_1, anchor="center", font=("Ariel", 12, "italic"))
check_image = PhotoImage(file="images/right.png")
next_button = Button(text="Next Page", command=next_page)
next_button.grid(row=1, column=0, columnspan=2)
back_button = Button(text="Back", command=last_page)
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
lbl_1 = canvas.create_window(350, 160, window=label_widget1)
canvas.itemconfig(lbl_1, state='hidden')
lbl_2 = canvas.create_window(350, 260, window=label_widget2)
canvas.itemconfig(lbl_2, state='hidden')
lbl_3 = canvas.create_window(350, 360, window=label_widget3)
canvas.itemconfig(lbl_3, state='hidden')
ent_1 = canvas.create_window(650, 160, window=entry_widget1)
canvas.itemconfig(ent_1, state='hidden')
ent_2 = canvas.create_window(650, 260, window=entry_widget2)
canvas.itemconfig(ent_2, state='hidden')
ent_3 = canvas.create_window(650, 360, window=entry_widget3)
canvas.itemconfig(ent_3, state='hidden')
choice_values = ["Please Choose a Vendor", "Vendor 1", "Vendor 2", "Vendor 3"]
choice_widget2 = ttk.Combobox(window, width=30, values=choice_values, background=BACKGROUND_COLOR, state="readonly")
choice_widget2.grid(row=1, column=0)
choice_widget2.current(0)
choice_widget2.grid_remove()
label_offer1 = Label(window, text="How much of the available payoff would you like to offer to Vendor 1?",
					 background="white")
label_offer2 = Label(window, text="How much of the available payoff would you like to offer to Vendor 2?",
					 background="white")
label_offer3 = Label(window, text="How much of the available payoff would you like to offer to Vendor 3?",
					 background="white")
offer_widget1 = Scale(window, from_=0, to=round(utility_a * utility_multiplier, 2), orient=HORIZONTAL,
					  resolution=0.05, background="white")
offer_widget2 = Scale(window, from_=0, to=round(utility_b * utility_multiplier, 2), orient=HORIZONTAL,
					  resolution=0.05, background="white")
offer_widget3 = Scale(window, from_=0, to=round(utility_c * utility_multiplier, 2), orient=HORIZONTAL,
					  resolution=0.05, background="white")
label_offer4 = Label(window, text="Please click and slide each button to make an offer to the vendor",
					 background="white")
final_label1 = Label(window, text="", background="white")
final_label2 = Label(window, text="", background="white")
final_label3 = Label(window, text="", background="white")
window.mainloop()
