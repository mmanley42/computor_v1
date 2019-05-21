import re

ERROR_STRING_SET = {
	"SpaceError":	"There should not be a space here: ",
	"WrongChar":	"Wrong character found.\nOnly these charaters are acceptable[xX\^+\-\*0-9. =]",
	"MultiplingX":	"Multipling x values is not supported at this moment."
}

def highlight_error(original, match_set):
	my_set = []
	for tup in match_set:
		if not my_set:
			my_set = set(tup)
		else:
			for val in tup:
				my_set.add(val)
	my_set.remove('')
	print(my_set)
	# for match in re.finditer()

class EquationPrep:
	__slots__ = ["error_message"]
	def __init__(self):
		self.error_message = ERROR_STRING_SET

	def _change_signs(self, items_to_change):
		for index, elem in enumerate(items_to_change):
			go = re.sub('\A', '-', elem)
			go = re.sub('--', '', go)
			items_to_change[index] = go
		return items_to_change

	def change_multipliers_side(self, data):
		items = data.split(' * ')
		stuff = items[0].split('x')
		if stuff[0] == '-' or not stuff[0]:
			first = -1 if stuff[0] == '-' else 1
		else:
			first = eval(stuff[0])
		items[1] = str(first * eval(items[1]))
		return "".join([items[1], 'x', stuff[1]])

	def situational_parsing(self, data):
		chack = re.search("-?\d*x\d+ \* \d+.?\d*", data)
		print('Situational parsing: ', chack)
		if chack is not None:
			return self.change_multipliers_side(self, data)
		return data

	def _possible_error_cases(self, data_to_check):
		operator_check = re.findall("(\d+ \d+)|(x\d+ ?x\d)", data_to_check)
		if operator_check:
			# highlight_error(data_to_check, operator_check)
			print(self.error_message["SpaceError"], *operator_check)
			return None
		char_check = re.search("[^xX\^+\-\*0-9. =]+", data_to_check)
		if char_check is not None:
			print(self.error_message["WrongChar"], 'found : ', char_check.group())
			return None
		return data_to_check

	def basic_pre_parsing(self, data, right=True):
		lower_case_eq = data.lower()
		minus_change = re.sub(' *- *', ' + -', lower_case_eq)
		multiply_change = re.sub(' *\* *', ' * ', minus_change)
		x_multi = re.sub("(?<=x\^[0-9]) *\* *(\d+x)", " ** \g<1>", multiply_change)
		simpli = re.sub('x *\^ *', 'x', x_multi)
		if self._possible_error_cases(simpli) is None:
			return None
		groups = simpli.split('+')
		trim_groups = [grp.strip() for grp in groups]
		if not right:
			trim_groups = self._change_signs(trim_groups)
		return trim_groups

class EquationParser:
	__slots__ = ["equ_data", "power", "pow_data", "zero_pow_data"]
	def __init__(self):
		self.equ_data = []
		self.pow_data = []
		self.zero_pow_data = []
		self.power = -1

	def put_number_in_correct_tuple(self, number, pow, op='+'):
		if not self.equ_data:
			self.equ_data.append([number, pow])
		else:
			for tup in self.equ_data:
				if tup[1] == pow:
					tup[0] = tup[0] * number if op != '+' else tup[0] + number
		if not any(tup[1] == pow for tup in self.equ_data):
			self.equ_data.append([number, pow])
		print(self.equ_data)

	def _define_multipliers_and_discriminants(self, numbers):
		if numbers[0] and numbers[1]:
			number, disc = numbers[0], numbers[1]
		elif numbers[0] and not numbers[1]:
			number, disc = numbers[0], '1'
		elif not numbers[0] and numbers[1]:
			number, disc = '1', numbers[1]
		else:
			number, disc = '1', '1'
		number = "-1" if number == '-' else number
		return number, disc

	def multipling_x_values(self, data):
		xs_values = data.split('**')
		start = [1, 0]
		for x in xs_values:
			x = x.strip()
			numbers = x.split('x')
			number, disc = self._define_multipliers_and_discriminants(numbers)
			start = [start[0] * eval(number), start[1] + eval(disc)]
		self.put_number_in_correct_tuple(start[0], start[1])

	def zero_powered_data(self, data):
		c = eval(data)
		number = float(c)
		self.put_number_in_correct_tuple(number, 0)

	def powered_data(self, data):
		self.pow_data.append(data)
		print('Post parsing', data)
		dt = re.sub(" +\*? x", "x", data)
		print(dt)
		if dt.count('x') > 1:
			self.multipling_x_values(dt)
		else:
			dt = EquationPrep.situational_parsing(EquationPrep, dt)
			post_eval, powr = dt.split('x')
			post_eval = '1' if not post_eval else post_eval
			number = eval(post_eval)
			self.put_number_in_correct_tuple(number, eval(powr))

	def retrieve_equation_information(self, equation):
		for index, item in enumerate(equation):
			if item == '':
				continue
			elif 'x' in item:
				self.powered_data(item)
			else:
				self.zero_powered_data(item)
		return self.equ_data
