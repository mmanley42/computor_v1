# import argParse
import re
import sys

import parse_prep
import computor_v1_2

def print_out_equation(equ, op=' + ', x='x', mult=''):
	simplified_eq.sort(key=lambda x: x[1], reverse=True)
	list_len = len(simplified_eq)
	for index, info in enumerate(simplified_eq):
		number = info[0]
		if number < 0:
			op = ' - ' if index != 0 else "-"
			number = number * -1
		if number == 1:
			number = ""
		if index == 0:
			print("".join([str(number), mult, x, str(info[1])]), end='')
		elif index == list_len - 1:
			print("".join([op, str(number), mult, x, str(info[1]), ' = 0']))
		else:
			print("".join([op, str(number), mult, x, str(info[1])]), end='')
		op = ' + '

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
		eq_p = computor_v1_2.EquationFormatting(False, "right")
		ep = parse_prep.EquationPars()
		simplified_eq = []
		for index, eq in enumerate(parsed_equ):
			side = True if index == 0 else False
			parsed_equ[index] = eq_p.format_equation(eq, right=side)
			if parsed_equ[index] is None:
				print('You have an error in your string')
				exit(0)
			simplified_eq = ep.retrieve_equation_information(parsed_equ[index])
			print(simplified_eq)
			print_out_equation(simplified_eq)
	else:
		print("Please input a valid second degree equation.")
