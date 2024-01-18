import numpy as np
import time
from vendor_creator import Vendor
people = ["A", "B"]
people_prob = [0.3, 0.7]
utility_multiplier = round(0.20, 2)
flat_fee = 5
rounds = 10
utility = 0
utility_a = 0
utility_b = 0
utility_c = 0
purchases_vendor_a = 0
purchases_vendor_b = 0
purchases_vendor_c = 0
utility_gen = 0
offer_dist = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
accepted_offers = [.05, .15, .15, .15, .15, .2, .05, .04, .03, .02, 0.01]

places = ["Belfast", "Bristol", "Cardiff", "Cambridge", "Chester", "Cork", "Dublin", "Edinburgh", "Glasgow", "Leeds",
          "London", "Manchester", "Newport"]
vendor_a = Vendor()
vendor_b = Vendor()
vendor_c = Vendor()
preferences = {
    "A": ["Specialist", "High Quality", "Low Quality"],
    "B": ["High Quality", "Low Quality", "Specialist"],
}
print(f"Thank you for agreeing to take part in this online experiment. \n \n"
      f"The experiment takes place in an online marketplace where participants are randomly assigned to a role of "
      f"vendor or purchaser. \n\n"
      f"Purchasers are randomly assigned to one of two equal sized groups, A or B, and vendors will be randomly "
      f"assigned to one of three groups, High \nQuality, Low Quality, or Specialist Product - where 40% of the "
      f"population are High Quality, 40% Low Quality, and 20% Specialist Producers. \nParticipants know their own "
      f"groups, but not that of other participants.\n\n"
      f"The experiment consists of {rounds} rounds, whereby, a purchaser must acquire a product from one of the vendors"
      f" in each round. Vendors display the\naverage star rating of their previous customers. Vendors not chosen "
      f"by the user are chosen at random by a purchaser of unknown type, their\nsatisfaction is then added to the "
      f"vendor history in the following round. The purchaser can choose to purchase from the same vendor in subsequent\n"
      f"rounds, or from a different vendor. \n\n"
      f"Purchasers receive gratification from buying a product of between 1 and 5 stars. Each purchase results in a "
      f"surplus of £{utility_multiplier}0 per star i.e. 1 star\nrating results in £{utility_multiplier}0, 2 star "
      f"rating results in £{2*utility_multiplier}0 etc. \n\nAt the end of round {rounds}, purchasers will see a "
      f"summary of total surplus generated from transactions with each vendor. Purchasers will then be asked\nto "
      f"propose a one time take it or leave it offer to the vendor. Vendors are real people and can reject offers, "
      f"whereby each participant will leave\nwith nothing from the transaction. If the vendor accepts the offer, "
      f"purchasers will be remunerated an amount equal to the total surplus less the\namount given to the vendor.\n\n"
      f"Dependent on purchaser and vendor types, purchases have different probabilities of resulting in higher ratings "
      f"and thus higher surpluses. For both\nType A and Type B purchasers, the average purchase from a High Quality "
      f"vendor results in 3.5 stars, whereas the average for Low Quality vendors is\n2.5 stars. Type A purchasers "
      f"enjoy Specialty vendors and purchases result in an average of 4 stars, whereas Type B purchases of Specialty "
      f"products\nresult in an average of 2 stars. Please note, if a product results in a specific rating in a round, "
      f"it may not result in the same rating in\ndifferent rounds. This is to mirror real transactions, whereby, "
      f"transactions with the same vendor may differ between periods i.e. damage to the\nproduct etc. which would "
      f"result in a lower rating in that period.\n")

name = input("What is your name? ")

Relationship_status = input("Are you Married, Single, or do you have a partner? Please answer 'Married', 'Single', "
                            "or 'Partner'.\n").lower().replace("'", "")

if Relationship_status not in ["married", "single", "partner"]:
    Relationship_status = "Unknown"
elif Relationship_status in ["married", "partner"]:
    Partner_name = input("What is the name of your partner?")
else:
    pass
while Relationship_status == "Unknown":
    Relationship_status = input("Sorry, I did not understand your last answer, please enter either 'Married', 'Single',"
                                "or 'Partner'.\n").lower().replace("'", "")
    if Relationship_status in ["married", "partner"]:
        Partner_name = input("What is the name of your partner?")
    elif Relationship_status == "single":
        pass
    else:
        Relationship_status = "Unknown"
Round = 1
Type = np.random.choice(people, p=people_prob)
print(f"\n\n{name} you have been randomly assigned to the role of Purchaser and are Type {Type}. Please remember, Type "
      f"{Type} prefers {preferences[Type][0]} vendors, then\n{preferences[Type][1]}\nvendors, and least prefers "
      f"{preferences[Type][2]} vendors.")
while Round < rounds+1:
    print(f"\n\nRound {Round}\n")
    vendor_a.print_status(1, np.random.choice(places), Round)
    vendor_b.print_status(2, np.random.choice(places), Round)
    vendor_c.print_status(3, np.random.choice(places), Round)
    valid = True
    choice = input("\nPlease choose a vendor by typing either 1, 2, or 3: \n")
    while valid:
        try:
            if int(choice) in [1, 2, 3]:
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
                print(f"Your purchase resulted in satisfaction of {utility_gen} stars which means total earnings from "
                      f"purchases are £{round(utility*utility_multiplier, 2)}0.")
                valid = False
            else:
                choice = input("This is not a valid choice, please choose a vendor by typing either 1, 2, or 3. ")
        except ValueError:
            choice = input("This is not a valid choice, please choose a vendor by typing either 1, 2, or 3. ")
    Round += 1
    time.sleep(2)
earnings_a = round(utility_a*utility_multiplier, 2)
if purchases_vendor_a == 0:
    average_earnings_a = 0
else:
    average_earnings_a = round(earnings_a / purchases_vendor_a, 2)
earnings_b = round(utility_b*utility_multiplier, 2)
if purchases_vendor_b == 0:
    average_earnings_b = 0
else:
    average_earnings_b = round(earnings_b / purchases_vendor_b, 2)
earnings_c = round(utility_c * utility_multiplier, 2)
if purchases_vendor_c == 0:
    average_earnings_c = 0
else:
    average_earnings_c = round(earnings_c / purchases_vendor_c, 2)
earnings = earnings_a + earnings_b + earnings_c

vendor_a_valid = True
vendor_b_valid = True
vendor_c_valid = True
vendor_a_offer = 0
vendor_b_offer = 0
vendor_c_offer = 0
if purchases_vendor_a == 0:
    vendor_a_valid = False
    print("You didn't make any purchases from Vendor 1.")
else:
    print(f"\n\n{name} your {purchases_vendor_a} purchase(s) from vendor 1 resulted in a surplus of £{earnings_a}0 at an "
          f"average of £{average_earnings_a} per transaction.\n ")
while vendor_a_valid:
    try:
        vendor_a_offer = float(input(f"How much of the total surplus of £{earnings_a}0 from transaction(s) with Vendor 1"
                                     f" would you like to pay to the vendor? Please enter a numerical value\nbetween 0 "
                                     f"and £{earnings_a}0. Please note, vendors may reject offers they deem unfair, in "
                                     f"which case both purchaser and vendor receive zero.\n"))
        if 0 <= vendor_a_offer <= earnings_a:
            if np.random.choice(offer_dist, p=accepted_offers) < (vendor_a_offer / earnings_a):
                earnings_a -= vendor_a_offer
                print(f"Your offer has been accepted, after Vendor payment, your earnings from Vendor 1 are "
                      f"£{round(earnings_a, 2)}0.")
            else:
                earnings_a = 0
                print(f"Your offer has been rejected, as a result, your earnings from Vendor 1 are "
                      f"{earnings_a}.")
            vendor_a_valid = False
            time.sleep(2)
        else:
            print(f"This is not a valid numerical input between 0 and £{earnings_a}0, please try again.")
    except TypeError:
        print(f"This is not a valid numerical input between 0 and £{earnings_a}0, please try again.")

if purchases_vendor_b == 0:
    vendor_b_valid = False
    print("You didn't make any purchases from Vendor 2.")
else:
    print(f"your {purchases_vendor_b} purchase(s) from vendor 2 resulted in a surplus of £{earnings_b}0 at an "
          f"average of £{average_earnings_b} per transaction.\n")
while vendor_b_valid:
    try:
        vendor_b_offer = float(
            input(f"How much of the total surplus of £{earnings_b}0 from transaction(s) with Vendor 2"
                  f" would you like to pay to the vendor? Please enter a numerical value\nbetween 0 "
                  f"and £{earnings_b}0. Please note, vendors may reject offers they deem unfair, in "
                  f"which case both purchaser and vendor receive zero.\n"))
        if 0 <= vendor_b_offer <= earnings_b:
            if np.random.choice(offer_dist, p=accepted_offers) < (vendor_b_offer / earnings_b):
                earnings_b -= vendor_b_offer
                print(f"Your offer has been accepted, after Vendor payment, your earnings from Vendor 1 are "
                      f"£{round(earnings_b, 2)}0.")
            else:
                earnings_b = 0
                print(f"Unfortunately, your offer has been rejected, as a result, your earnings from Vendor 1 are "
                      f"{earnings_b}.")
            vendor_b_valid = False
            time.sleep(2)
        else:
            print(f"This is not a valid numerical input between 0 and £{earnings_b}0, please try again.")
    except TypeError:
        print(f"This is not a valid numerical input between 0 and £{earnings_b}0, please try again.")
if purchases_vendor_c == 0:
    vendor_c_valid = False
    print("You didn't make any purchases from Vendor 3.")
else:
    print(f"your {purchases_vendor_c} purchase(s) from vendor 3 resulted in a surplus of £{earnings_c}0 at an "
          f"average of £{average_earnings_c} per transaction.\n")
while vendor_c_valid:
    try:
        vendor_c_offer = float(
            input(f"How much of the total surplus of £{earnings_c}0 from transaction(s) with Vendor 3"
                  f" would you like to pay to the vendor? Please enter a numerical value\nbetween 0 "
                  f"and £{earnings_c}0. Please note, vendors may reject offers they deem unfair, in "
                  f"which case both purchaser and vendor receive zero.\n"))
        if 0 <= vendor_c_offer <= earnings_c:
            if np.random.choice(offer_dist, p=accepted_offers) < (vendor_c_offer / earnings_c):
                earnings_c -= vendor_c_offer
                print(f"Your offer has been accepted, after Vendor payment, your earnings from Vendor 1 are "
                      f"£{round(earnings_c, 2)}0.")
            else:
                earnings_c = 0
                print(f"Your offer has been rejected, as a result, your earnings from Vendor 1 are "
                      f"{round(earnings_c, 2)}.")
            vendor_c_valid = False
            time.sleep(2)
        else:
            print(f"This is not a valid numerical input between 0 and £{earnings_c}0, please try again.")
    except TypeError:
        print(f"This is not a valid numerical input between 0 and £{earnings_c}0, please try again.")
print(f"\n\n{name} your net surplus from purchases where an offer was accepted equalled "
      f"£{round(earnings_a + earnings_b + earnings_c, 2)}0. In addition to the flat fee of £{flat_fee}, this gives you "
      f"total income\nof £{flat_fee+round(earnings_a + earnings_b + earnings_c, 2)}0. You will receive the money into "
      f"your bank account in the next 2-3 working days.\n\nThank you for taking part in this experiment. "
      f"Have a good day!")
