import re

ERROR_STRING_SET = {
	"SpaceError":	"There should not be a space here: ",
	"WrongChar":	"Wrong character found.\nOnly these charaters are acceptable[xX\^+\-\*0-9. =]",
	"MultiplingX":	"Multipling x values is not supported at this moment.",
	"NoOperators":	"There shoud be an operator between these values."
}

class EquationFormatting:
	"""Class that will parse a second degree formated string.
	It will only accept two strings per instances as for the two sides of an equation.
	"""
	__slots__ = ["error_message"]
	def __init__(self):
		self.error_message = ERROR_STRING_SET


	def change_equation_signs(self, items_to_change):
		"""Change the signs of equation part sent"""
		elem_to_pop = []
		for index, elem in enumerate(items_to_change):
			if elem:
				elem_neg = re.sub('\A', '-', elem)
				elem_pos = re.sub('--', '', elem_neg)
				items_to_change[index] = elem_pos
			else:
				elem_to_pop.append(index)

		for ind in elem_to_pop:
			items_to_change.pop(ind)
		return items_to_change

	def change_multipliers_side(self, equ_data):
		"""Puts the multipliler in front of the x it is attached to."""
		items = equ_data.split(' * ')
		mult_disc = items[0].split('x')
		if mult_disc[0] == '-' or not mult_disc[0]:
			first = -1 if mult_disc[0] == '-' else 1
		else:
			first = eval(mult_disc[0])
		items[1] = str(first * eval(items[1]))
		return "".join([items[1], 'x', mult_disc[1]])

	# TODO: Does not work correctly!!!
	def multiple_multipliers(self, equ_data):
		"""Handles multiple multipliers"""
		check = re.search("-?\d*x\d+ \* \d+.?\d*", equ_data)
		if check is not None:
			nb_multiplier = equ_data
			while re.search("-?\d*x\d+ \* \d+.?\d*", nb_multiplier) is not None:
				nb_multiplier = self.change_multipliers_side(nb_multiplier)
				print(check.group(), equ_data)
				d_chck = re.sub(check.group(), "", equ_data)
				print("Want to change multiple multipliers order.", d_chck)
			equ_data = nb_multiplier
		return equ_data

	def format_multipling_xs(self, equ):
		"""Spcial format to handle multiplication between xs"""
		reg_multipling_xs = "(?<=x\^[0-9]) *\* *(\d*x)"
		reg_srch_xs = "x\^[0-9] \* \d*x"

		x_multiply_change = equ
		for _ in re.finditer(reg_srch_xs, equ):
			x_multiply_change = re.sub(reg_multipling_xs, " ** \g<1>", x_multiply_change)
		return x_multiply_change

	def _x_formatting(self, data):
		"""Formats for x parts"""
		reg_power_char = "x *\^ *"
		reg_solo_x = "x(?= ?[\*\+-]|$| ?=)"

		print("Post solo: ", data)
		solo_x = re.sub(reg_solo_x, "x^1", data)
		print("Solo x: ", solo_x)
		x_multiply_change = self.format_multipling_xs(solo_x)
		print(x_multiply_change)
		remove_power_char = re.sub(reg_power_char, 'x', x_multiply_change)
		return remove_power_char

	def _operator_formatting(self, equation):
		"""The basic operators formatting"""
		trimed = equation.strip()
		lower_cased = trimed.lower()

		space_cut = re.sub(" +", " ", lower_cased)
		equal_space = re.sub(" *= *", "=", space_cut)
		plus_space = re.sub(" *\+ *", " + ", equal_space)
		minus_space = re.sub(" *-", " -", plus_space)
		multiply_space = re.sub(' *\* *', ' * ', minus_space)

		minus_format = re.sub('(?<!\*) +- *', ' + -', multiply_space)
		first_minus = minus_format
		if re.match(" \+ -", first_minus):
			minus_format = re.sub("\A \+ -", "-", first_minus)

		power_char_space = re.sub("x *\^ *", "x^", minus_format)
		add_power_char = re.sub("x *(\d+)", "x^\g<1>", power_char_space)

		return add_power_char

	def basic_input_check(self, data_to_check):
		operator_check = re.findall("(\d+ +\d+)|(x\d+ *x\d)", data_to_check)
		if operator_check:
			# highlight_error(data_to_check, operator_check)
			print(self.error_message["SpaceError"], *operator_check)
			return None
		char_check = re.search("[^xX\^+\-\*0-9. =]+", data_to_check)
		if char_check is not None:
			print(self.error_message["WrongChar"], 'found : ', char_check.group())
			return None
		error = re.search("x[^\^] *[\d]", data_to_check)
		if error is not None:
			print(self.error_message["NoOperators"], 'found : ', error.group())
			return None
		#  Multiple multipliers check
		return data_to_check

	def check_for_multipling_multipliers(self, equ_list):
		if not equ_list:
			return False
		for item in equ_list:
			try:
				if 'x' not in item and item:
					eval(item)
				elif re.search("-?\d* ?\*? ?\d*x\d+", item) is None:
					raise SyntaxError
			except SyntaxError as error:
				print("Error caught during final check: <", error, ">\nFound: {0}".format(item))
				return False
		return True

	def is_equation(self, equation):
		"""Sends equation through the EquationFormatter.
		Returns:
			False: If formatted errors.
			True : If no formatted errors. Does not mean the equation is valid.
		"""
		if self.format_equation(equation)is not None:
			return True
		else:
			return False

	def is_equation_format(self, equation):
		"""Checks if the string passed has a first glance equation format.
		Returns:
			-1	:	Not an equation
			0	:	Is an equation
			1	:	Is a valid equation side, assumes a '= 0' at the end if No '=' provided
		"""
		char_check = self.basic_input_check(equation)
		if char_check is None:
			return -1
		if re.search("=", equation) is None:
			return 1
		else:
			return 0

	def format_inputed_equation(self, equation):
		pass

	def _add_equation_format(self, equation):
		""" If is_equation_format == 1 will add the = 0 at the end and goes on formatting.
			If is_equation_format == -1 returns None
			If is_equation_format == 0 continues with regular formatting
		"""
		is_equ = self.is_equation_format(equation)
		if is_equ != -1:
			if is_equ == 1:
				equation = "".join([equation, " = 0"])
			spaced_parsed_equ_list = " ".join(equation.split()).split('=')
			print("_add_equation_format : ", spaced_parsed_equ_list)
			return spaced_parsed_equ_list
		return None

	def format_equation(self, equation):
		"""Used to have a flexible equation format. This version will have the
		same output as cmp_v1_reformating. Although it can accept multiple
		equation formats

		Args:
			equation <str>:	A flexible second degree formated equation
		Returns:
			A specific format for EquationParser. [str]
		"""
		end_equ_parts = []
		equation = self._add_equation_format(equation)
		if equation is None:
			return None
		for index, equ_side in enumerate(equation):
			op_change = self._operator_formatting(equ_side)
			print("Basic parse", op_change)
			x_formated = self._x_formatting(op_change)
			print("X formatting", x_formated)
			if self.basic_input_check(x_formated) is None:
				return None

			print("\nStart working with lists of the equation :\n")
			# exit(0)
			plus_split = x_formated.split('+')
			trim_equ_parts = [grp.strip() for grp in plus_split]
			if index == 1:
				trim_equ_parts = self.change_equation_signs(trim_equ_parts)
			for index, equ_part in enumerate(trim_equ_parts):
				trim_equ_parts[index] = self.multiple_multipliers(equ_part)
			print("Trimmed equation parts: ", trim_equ_parts)
			if not self.final_check(trim_equ_parts):
				return None
			end_equ_parts.extend(trim_equ_parts)
		print(end_equ_parts)
		return end_equ_parts


	def equation_from_args(self, args):
		"""This function as the sole purpose of handling the list of arguments
		passed if computor v1 is called with user arguments or inputs.
		Need to put flag args to True.
		This function will see all arguments as creating one single equation.

		Args:
			args (List):	List of arguments to join together.
		"""
		file_name = args[0]
		equ_elements = [item if item != file_name else '*' for item in args[1:]]
		equation = "".join(equ_elements)
		return self.format_equation(equation)


	def equation_dispatcher(self, equation_data, args=False):
		"""Equation dispatcher self explanitory.
		Agrs:
			equation_data <[strings]>:	A list of equations, can send a string equation it will put it in a list.
			args <boolean>:				For the single purpose of formatting main arguments.
		Returns:
			if from args:	List of strings of equation parts
			else:			List of lists of strings equation parts
		"""
		if equation_data is not None:
			if isinstance(equation_data, str):
				equation_data = [equation_data]
			if args:
				return self.equation_from_args(equation_data)
			else:
				all_formatted_equ = []
				for equation in equation_data:
					print(equation_data)
					all_formatted_equ.append(self.format_equation(equation))
					print(all_formatted_equ)
				return all_formatted_equ
