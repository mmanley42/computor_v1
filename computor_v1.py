# import argParse
import re
import sys

class EquationParser:
	__slots__ = ["equ_data", "power", "pow_data", "zero_pow_data"]
	def __init__(self):
		self.equ_data = []
		self.pow_data = []
		self.zero_pow_data = []
		self.power = -1

	def _change_signs(self, items_to_change):
		for index, elem in enumerate(items_to_change):
			go = re.sub('\A', '-', elem)
			go = re.sub('--', '', go)
			items_to_change[index] = go
		return items_to_change

	def _possible_error_cases(self, data_to_check):
		if re.findall("\d +\d", data_to_check):
			return None
		# Add checks you can think of

	@staticmethod
	def basic_pre_parsing(data, right=True):
		if _possible_error_cases(data) is None:
			return None
		lower_case_eq = data.lower()
		simplified = re.sub(' *- *', ' + -', lower_case_eq)
		simpli = re.sub('x\^ *', 'x', simplified)
		groups = simpli.split('+')
		trim_groups = [grp.strip() for grp in groups]
		if not right:
			trim_groups = self._change_signs(trim_groups)
		return trim_groups

	def put_number_in_correct_tuple(self, number, pow, op='+'):
		if not self.equ_data:
			self.equ_data.append([number, pow])
		else:
			for tup in self.equ_data:
				print()
				if tup[1] == pow:
					tup[0] = tup[0] * number if op != '+' else tup[0] + number
		if not any(tup[1] == pow for tup in self.equ_data):
			self.equ_data.append([number, pow])
		print(self.equ_data)

	def zero_powered_data(self, data):
		c = eval(data)
		number = float(c)
		self.put_number_in_correct_tuple(number, 0)

	def powered_data(self, data):
		self.pow_data.append(data)
		dt = re.sub(" *\*? x", "x", data)
		if dt.count('x') > 1:

			print('deal with it', dt)
		else:
			post_eval, powr = dt.split('x')
			post_eval = '1' if not post_eval else post_eval
			number = eval(post_eval)
			print('Sending to put :', post_eval, powr)
			self.put_number_in_correct_tuple(number, eval(powr))

	def retrieve_equation_information(self, equation):
		for index, item in enumerate(equation):
			if item == '':
				continue
			elif 'x' in item:
				self.powered_data(item)
			else:
				self.zero_powered_data(item)

def multplication_in_args(file_name, args):
	return [item if item != file_name else '*' for item in args]

if __name__ == "__main__":
	if len(sys.argv) > 1:
		new_arg_list = multplication_in_args(sys.argv[0], sys.argv[1:])
		equation = "".join(new_arg_list)
		parsed_equ = " ".join(equation.split()).split('=')

		if len(parsed_equ) > 2:
			print("Make sure this is a valid equation for this program!")
			exit(1)
		if len(parsed_equ) < 2:
			resp = input("There is no equal sign, do you wish to continu ? n/Y")
			if resp in ['Y', 'y', 'yes']:
				parsed_equ.append('0')
			else:
				exit(0)
		print(parsed_equ)
		ep = EquationParser()
		for index, eq in enumerate(parsed_equ):
			side = True if index == 0 else False
			parsed_equ[index] = ep.basic_pre_parsing(eq, right=side)
			if parsed_equ[index] is None:
				print('You have an error in your string')
				exit(0)
			ep.retrieve_equation_information(parsed_equ[index])
	else:
		print("Please input a valid second degree equation.")
