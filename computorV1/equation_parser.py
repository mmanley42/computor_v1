import re

ERROR_STRING_SET = {
	"SpaceError":	"There should not be a space here: ",
	"WrongChar":	"Wrong character found.\nOnly these charaters are acceptable[xX\^+\-\*0-9. =]",
	"MultiplingX":	"Multipling x values is not supported at this moment.",
	"NoOperators":	"There shoud be an operator between these values."
}

class EquationParser:
	__slots__ = ["equ_data", "power"]
	def __init__(self):
		self.equ_data = []
		self.power = None

	def reason_to_correct_tuples(self, number, pow, op='+'):
		pass

	def __define_multipliers_and_discriminants(self, numbers):
		pass

	def _multipling_x_powered(self, equ_op):
		pass

	def zero_powered_data(self, equ_op):
		pass

	def n_powered_data(self, equ_op):
		pass

	def retrieve_equation_information(self, equ_list):
		pass
