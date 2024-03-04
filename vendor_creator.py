import numpy as np
import random

ethnicity_percentage = [0.4, 0.6]
ethnicity_status = ["non-white", "white"]
gender_percentage = [0.45, 0.45, 0.1]
gender_status = ["woman", "man", "they"]
relationship_percentage = [0.3, 0.5, 0.2]
relationship_status = ["single", "partner", "married"]
hetrosexual_percentage = [0.2, 0.8]
hetrosexual_status = ["queer", "straight"]
queer_percentage = [0.8, 0.2]
queer_status = ["gay", "other"]
mixedrace_percentage = [0.5, 0.5]
mixedrace_status = ["hetro", "homo"]
vendor_status = [1, 2, 3]
vendor_percentage = [0.4, 0.4, 0.2]
review_score = [1, 2, 3, 4, 5]
purchaser_A_review_prob = {
	1: [0.05, 0.1, 0.35, 0.3, 0.2],
	2: [0.25, 0.3, 0.25, 0.1, 0.1],
	3: [0.05, 0.1, 0.15, 0.2, 0.5]
}
purchaser_B_review_prob = {
	1: [0.05, 0.1, 0.35, 0.3, 0.2],
	2: [0.25, 0.3, 0.25, 0.1, 0.1],
	3: [0.5, 0.2, 0.15, 0.1, 0.05],
}
review_dict = {
	"A": purchaser_A_review_prob,
	"B": purchaser_B_review_prob
}
name_dict = {
	"man": {
		"white": ["Todd", "Neil", "Geoffrey", "Brett", "Brendan", "Adam", "Matthew", "James", "Jay", "Brad", "Greg"],
		"non-white": ["Muhammed", "Rasheed", "Leroy", "Raheem", "Juan", "Jermaine", "Pedro", "Eduardo", "Fernando",
					  "Varun", "Sunny", "Hardeep"]
	},
	"woman": {
		"white": ["Emily", "Anne", "Jill", "Faye", "Allison", "Sarah", "Meredith", "Carrie", "Kristen", "Elaine",
				  "Jodie"],
		"non-white": ["Aisha", "Keisha", "Latonya", "Fatima", "Li", "Susana", "Gabriela", "Mirabelle", "Andrea",
					  "Marcia", "Coco", "Parjit", "Priya", "Priti"]
	},
	"they": {
		"white": ["Allie", "Amaranth", "Drew", "Indiana", "Lex", "River"],
		"non-white": ["Devan", "Jordan", "Kai", "Rune", "Zaire", "Zion", "Zuma"]
	}
}


def partner_ethnicity(status, ethnicity, mixed_status, mixed_percentage):
	partner = {
		"non-white": "white",
		"white": "non-white"
	}
	if status == "single":
		return "N/A"
	else:
		if np.random.choice(mixed_status, p=mixed_percentage) == "homo":
			return ethnicity
		else:
			return partner[ethnicity]


def partner_name(status, partner_ethnic, gender, sexuality, names):
	if status == "single":
		return "none"
	else:
		if gender == "woman":
			if sexuality == "straight":
				return np.random.choice(names["man"][partner_ethnic])
			else:
				status = np.random.choice(queer_status, p=queer_percentage)
				if status == "gay":
					return np.random.choice(names[gender][partner_ethnic])
				else:
					return np.random.choice(names["they"][partner_ethnic])
		elif gender == "man":
			if sexuality == "straight":
				return np.random.choice(names["woman"][partner_ethnic])
			else:
				status = np.random.choice(queer_status, p=queer_percentage)
				if status == "gay":
					return np.random.choice(names[gender][partner_ethnic])
				else:
					return np.random.choice(names["they"][partner_ethnic])
		else:
			if sexuality == "queer":
				return np.random.choice(names["they"][partner_ethnic])
			else:
				status = np.random.choice(["woman", "man"], p=[0.5, 0.5])
				return np.random.choice(names[status][partner_ethnic])


def purchaser_utility(purchaser_type, seller_type, review_matrix, review_probs):
	return np.random.choice(review_matrix, p=review_probs[purchaser_type][seller_type])


class Vendor:
	def __init__(self):
		self.vendor_type = np.random.choice(vendor_status, p=vendor_percentage)
		self.ethnicity = np.random.choice(ethnicity_status, p=ethnicity_percentage)
		self.gender = np.random.choice(gender_status, p=gender_percentage)
		self.relationship_status = np.random.choice(relationship_status, p=relationship_percentage)
		self.sexuality = np.random.choice(hetrosexual_status, p=hetrosexual_percentage)
		self.name = np.random.choice(name_dict[self.gender][self.ethnicity])
		self.partner_ethnicity = partner_ethnicity(self.relationship_status, self.ethnicity, mixedrace_status,
												   mixedrace_percentage)
		self.partner_name = partner_name(self.relationship_status, self.partner_ethnicity, self.gender, self.sexuality,
										 name_dict)
		self.review_history = []
		self.review_average = "N/A"

	def print_status(self, vendor_number, city, experiment_round):
		if self.gender == "woman":
			word = "she lives"
			word_1 = "her"
		elif self.gender == "man":
			word = "he lives"
			word_1 = "his"
		else:
			word = "they live"
			word_1 = "their"
		if experiment_round == 1:
			statement = f"The vendor is new, and as such, does not have a review history.\n"
		else:
			statement = f"The average rating of the vendor is {self.review_average} stars.\n"
		if self.relationship_status == "single":
			return f"Vendor {vendor_number} is {self.name} and {word} in {city}.\n{statement}"
		elif self.relationship_status == "married":
			return f"Vendor {vendor_number} is {self.name} and {word} with {word_1} spouse {self.partner_name} in " \
				   f"{city}.\n{statement}"
		else:
			return f"Vendor {vendor_number} is {self.name} and {word} with {word_1} partner {self.partner_name} in " \
				   f"{city}.\n{statement}"

	def vendor_utility(self, p_type):
		utility = purchaser_utility(p_type, self.vendor_type, review_score, review_dict)
		self.review_history.append(utility)
		self.review_average = round(float(np.mean(self.review_history)), 2)
		return utility
