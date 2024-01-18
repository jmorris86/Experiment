import numpy as np

ethnicity_percentage = [0.4, 0.6]
ethnicity_status = ["non-white", "white"]
gender_percentage = [0.5, 0.5]
gender_status = ["woman", "man"]
relationship_percentage = [0.3, 0.5, 0.2]
relationship_status = ["single", "partner", "married"]
hetrosexual_percentage = [0.3, 0.7]
hetrosexual_status = ["queer", "straight"]
mixedrace_percentage = [0.3, 0.7]
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
	}
}

def vendor_type(types, percentage):
	return np.random.choice(types, p=percentage)


def relationship(status, percentage):
	return np.random.choice(status, p=percentage)


def vendor_ethnicity(ethnic, ethnic_percentage):
	return np.random.choice(ethnic, p=ethnic_percentage)


def vendor_gender(women, women_percentage):
	return np.random.choice(women, p=women_percentage)


def vendor_name(ethnicity, gender, names):
	return np.random.choice(names[gender][ethnicity])


def vendor_sexuality(sexuality, sexuality_percentage):
	return np.random.choice(sexuality, p=sexuality_percentage)


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
				return np.random.choice(names[gender][partner_ethnic])
		else:
			if sexuality == "straight":
				return np.random.choice(names["woman"][partner_ethnic])
			else:
				return np.random.choice(names[gender][partner_ethnic])


def purchaser_utility(purchaser_type, seller_type, review_matrix, review_probs):
	return np.random.choice(review_matrix, p=review_probs[purchaser_type][seller_type])


class Vendor():
	def __init__(self):
		self.vendor_type = vendor_type(vendor_status, vendor_percentage)
		self.ethnicity = vendor_ethnicity(ethnicity_status, ethnicity_percentage)
		self.gender = vendor_gender(gender_status, gender_percentage)
		self.relationship_status = relationship(relationship_status, relationship_percentage)
		self.sexuality = vendor_sexuality(hetrosexual_status, hetrosexual_percentage)
		self.name = vendor_name(self.ethnicity, self.gender, name_dict)
		self.partner_ethnicity = partner_ethnicity(self.relationship_status, self.ethnicity, mixedrace_status,
												   mixedrace_percentage)
		self.partner_name = partner_name(self.relationship_status, self.partner_ethnicity, self.gender, self.sexuality,
										 name_dict)
		self.review_history = []
		self.review_average = "N/A"

	def print_status(self, vendor_number, city, experiment_round):
		if self.relationship_status == "single":
			print(f"Vendor {vendor_number} is {self.name} and they live in {city}. ")
		elif self.relationship_status == "married":
			print(
				f"Vendor {vendor_number} is {self.name} and they live with their spouse {self.partner_name} in {city}. ")
		else:
			print(
				f"Vendor {vendor_number} is {self.name} and they live with their partner {self.partner_name} in {city}.")
		if experiment_round == 1:
			print(f"The vendor is a new vendor, and as such does not have a review history.\n")
		else:
			print(f"The average rating of the vendor is {self.review_average} stars.\n")

	def vendor_utility(self, p_type):
		utility = purchaser_utility(p_type, self.vendor_type, review_score, review_dict)
		self.review_history.append(utility)
		self.review_average = round(np.mean(self.review_history), 2)
		return utility
