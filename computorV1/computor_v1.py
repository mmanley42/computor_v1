# import argParse
import re
import sys

import parse_prep

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
		eq_p = parse_prep.EquationPrep()
		ep = parse_prep.EquationParser()
		for index, eq in enumerate(parsed_equ):
			side = True if index == 0 else False
			parsed_equ[index] = eq_p.basic_pre_parsing(eq, right=side)
			if parsed_equ[index] is None:
				print('You have an error in your string')
				exit(0)
			ep.retrieve_equation_information(parsed_equ[index])
	else:
		print("Please input a valid second degree equation.")
