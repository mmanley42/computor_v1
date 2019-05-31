from computorV1 import equation_formatter

EF = equation_formatter.EquationFormatting


start_format_management = {
	# Valid weirdly shaped equations
	"Weirdly_shaped_equation_1": ["    -  1+ 2 *x^1 - 4.3*         -x = 3.3x^2",		"-1 + 2 * x1 + -4.3 * -x1=3.3x2"],
	"Weirdly_shaped_equation_2": ["1+ 2 *-3x   ^    1+ 4.3*         -x = x^2 * 3.3",	"1 + 2 * -3x1 + 4.3 * -x1=x2 * 3.3"],
	"Weirdly_shaped_equation_3": ["1+ 2 * -3x    1+ 4.3*         -x = x^2 * 3.3",		"1 + 2 * -3x1 + 4.3 * -x1=x2 * 3.3"],
	"Weirdly_shaped_equation_4": [" 1+ 2 *-3x^    1+ 4.3 *  -x = x^2 * 3.3   ",			"1 + 2 * -3x1 + 4.3 * -x1=x2 * 3.3"],
	"Weirdly_shaped_equation_5": ["-1+2*-3x^1+4.3*-x-5x2*2x1=x^2*3.3",					"-1 + 2 * -3x1 + 4.3 * -x1 + -5x2 ** 2x1=x2 * 3.3"],
	"Weirdly_shaped_equation_6": [" 1 + 2 * -3x^1 + 4.3 * -x -5x2 * x = x^2 * 3.3",	"1 + 2 * -3x1 + 4.3 * -x1 + -5x2 ** x1=x2 * 3.3"],

	# A plus sign after a multiplication
	"Wrongly_shaped_1": ["-1 +2*- 3x^1  +4.3*+ x  +5x2*x^1=x^ * -3.3"],
	# Wrong characters
	"Wrongly_shaped_2": ["-1ABC +t2*-() 3x^1 // +4.3*+ x  +5x%^2*x^1=x^2 * -3.3"],
}

multiplier_management = {
	"base_format":							["2 * x^2 = 0",	[["2 * x2", "-0"]],		[2, 2]],
	"no_power_sign":						["2 * x2 = 0",	[["2 * x2", "-0"]],		[2, 2]],
	"no_multiplication":					["2x^2 = 0",	[["2 * x2", "-0"]],		[2, 2]],
	"no_multiplication_nor_power":			["2x2 = 0",		[["2 * x2", "-0"]],		[2, 2]],

	"multiplier_to_multiple_x":				["5 * 3x1",		[["5 * 3x1", "-0"]],	[15, 1]],
	"multiplier_to_multiple_x_with_power":	["5 * 3x^1",	[["5 * 3x1", "-0"]],	[15, 1]],

	"inverted_multiplier_to_multiple_x":	["3x1 * 5",		[["5 * 3x1", "-0"]],	[15, 1]],
	"inverted_multiplier_to_multiple_x":	["x1 * 5",		[["5 * x1", "-0"]],		[5, 1]],

	"multiplier_to_multiple_x_neg":			["5 * -1x1",	[["5 * -1x1", "-0"]],	[-5, 1]],
	"multiplier_to_multiple_neg_x":			["5 * -x1",		[["5 * -1x1", "-0"]],	[-5, 1]],
}

base_equs = {
	"base_1_no_equal": ["2 * x^2", [["2 * x2", "-0"]], [[2, 2]]],
	"base_1_no_equal_neg": ["-2 * x^2", [["-2 * x2", "-0"]], [[-2, 2]]],

	"base_2_simple": ["2 * x^2 = 0", [["2 * x2", "-0"]], [[2, 2]]],
	"base_2_simple_neg": ["2 * -x^2 = 0", [["2 * -1x2", "-0"]], [[-2, 2]]],
	"base_2_no_power": ["2 * x2 = 0", [["2 * x2", "-0"]], [[2, 2]]],
	"base_2_no_power_multi": ["2x2 = 0", [["2 * x2", "-0"]], [[2, 2]]],
	"base_2_solo_x": ["x = 0", [["x1", "-0"]], [[1, 1]]],

	"base_3_equal_neg": ["2 * x^2 = -2", [["2x2", "2"]], [[2, 2], [2, 0]]],
	"base_3_equal_neg_multiplier": ["2 * x^2 = -2x2", [["2x2", "2"]], [[2, 2], [2, 0]]],

	"base_4_other_disc": ["2 * x^2 + x1 = 0", [["2x2", "x1"]], [[2, 2], [1, 1]]],
	"base_5_complete": ["2 * x^2 + 3 * x^1 + 5 = 0", [["2x2", "3x1", "5"]], [[2, 2], [-3, 1], [5, 0]]],
	"base_6_neg_complete": ["-2 * x^2 - 3 * x^1 - 5 = 0", [["-2x2", "-3x1", "-5"]], [[-2, 2], [-3, 1], [-5, 0]]],
}

equations = {
	1: ["2x^1  * 4 + x2 - 3 + 4x0 = -2", [[1, 2], [8, 1], [3, 0]], [["x2", "8x1", "-3", "4x0", "2"]]],
	2: ["2x^1  * 4 + x2 - 3 + 4x0 = -2 + x1", [[1, 2], [8, 1], [3, 0]], [["x2", "8x1", "-3", "4x0", "2", "-x1"]]],
	3: ["x^1 * 2 * 4 + x2 - 3 + 4x0 =x2 * -2", [[1, 2], [8, 1], [3, 0]], "x2 + 8x1 + 3x0 = 0"],
	4: ["x^1 * 2 * 4 + x  ^ 2 - 3 + 4 *  1x0 = -2", [[1, 2], [8, 1], [3, 0]], "x2 + 8x1 + 3x0 = 0"],
	5: ["x^1 * 2 * x1 + x2 - 3 + 4x0 = -2", [[3, 2], [0, 1], [3, 0]], "3x2 + 0x1 + 3x0 = 0"],
	6: ["x * 4x^1 +   x ^ 1 - 3 + 4x0 = 2", [[4, 2], [1, 1], [-1, 0]], "4x2 + 1x1 + -x0 = 0"],
	7: ["-x^1 * 2x2 + x2 - 3 + 4  x^0 = -2x1", [[-2, 3], [1, 2], [2, 1], [1, 0]], "-2x3 + x2 + 2x1 + x0 = 0"],
	8: ["x1 * 2 * 4 + x2 - 3 + 4x0 = -2", [[1, 2], [8, 1], [3, 0]], "x2 + 8x1 + 3x0 = 0"],
}

invalid_equ = {
	1: "2x ^  + 7 * x0  = 0",
	2: "2x ^ 2 - * x0 = 0",
	3: "2x ^1  +  x0 = 0",
	4: "2x^  = 0",
	5: "2x0  x1 = 0",
	6: "x * 3.5 x1 = 0",
	7: "(2x0 - x1) = 0",
	8: "--2x0 + x1 = 0",
	9: "* 2x0 + x1 = 0",
	10: "2x0 ++ x1 = 0",
	11: "2x^ 3 x1 = 0",
	12: "2x0  x1 = 0",
	13: "-2 * x0 + 15 - x1 * x^ 2x = 0",
	14: "-2 * x0 + 15 - x1 * x^1 2  x = 0",
}

# def test_format_equation_function_returns():
# 	equ_f = EF(False, "left")
# 	for key, equation in equations.items():
# 		result = equ_f.equation_dispatcher(equation[0])
# 		print("Post result: ", result, equation[2])
# 		for elem in equation[2][0]:
# 			assert elem in result[0], "EquationFormatting class did not send the correct data back. elem {0}".format(elem)
# 			result[0].remove(elem)
# 		print(result)
# 		assert result == [[]], "More data then expected sent back"



def test_start_format_management_1():
	equ_f = EF()
	start_str = start_format_management["Weirdly_shaped_equation_1"][0]
	end_str = start_format_management["Weirdly_shaped_equation_1"][1]

	result = equ_f._operator_formatting(start_str)
	result = equ_f._x_formatting(result)
	print(result)
	assert result == end_str, "\nWRONG ANSWER: \"{0}\" != \"{1}\"".format(result, end_str)

def test_start_format_management_2():
	equ_f = EF()
	start_str = start_format_management["Weirdly_shaped_equation_2"][0]
	end_str = start_format_management["Weirdly_shaped_equation_2"][1]

	result = equ_f._operator_formatting(start_str)
	result = equ_f._x_formatting(result)
	print(result)
	assert result == end_str, "\nWRONG ANSWER: \"{0}\" != \"{1}\"".format(result, end_str)

def test_start_format_management_3():
	equ_f = EF()
	start_str = start_format_management["Weirdly_shaped_equation_3"][0]
	end_str = start_format_management["Weirdly_shaped_equation_3"][1]

	result = equ_f._operator_formatting(start_str)
	result = equ_f._x_formatting(result)
	print(result)
	assert result == end_str, "\nWRONG ANSWER: \"{0}\" != \"{1}\"".format(result, end_str)

def test_start_format_management_4():
	equ_f = EF()
	start_str = start_format_management["Weirdly_shaped_equation_4"][0]
	end_str = start_format_management["Weirdly_shaped_equation_4"][1]

	result = equ_f._operator_formatting(start_str)
	result = equ_f._x_formatting(result)
	print(result)
	assert result == end_str, "\nWRONG ANSWER: \"{0}\" != \"{1}\"".format(result, end_str)

def test_start_format_management_5():
	equ_f = EF()
	start_str = start_format_management["Weirdly_shaped_equation_5"][0]
	end_str = start_format_management["Weirdly_shaped_equation_5"][1]

	result = equ_f._operator_formatting(start_str)
	result = equ_f._x_formatting(result)
	print(result)
	assert result == end_str, "\nWRONG ANSWER: \"{0}\" != \"{1}\"".format(result, end_str)

def test_start_format_management_6():
	equ_f = EF()
	start_str = start_format_management["Weirdly_shaped_equation_6"][0]
	end_str = start_format_management["Weirdly_shaped_equation_6"][1]

	result = equ_f._operator_formatting(start_str)
	result = equ_f._x_formatting(result)
	print(result)
	assert result == end_str, "\nWRONG ANSWER: \"{0}\" != \"{1}\"".format(result, end_str)

def test_start_format_management_invalid_1():
	equ_f = EF()
	start_str = start_format_management["Wrongly_shaped_1"][0]

	result = equ_f.is_equation_format(start_str)
	print(result)
	assert result == -1, "\nWRONG ANSWER: Result should be == -1 not {0}".format(result)

def test_start_format_management_invalid_2():
	equ_f = EF()
	start_str = start_format_management["Wrongly_shaped_2"][0]

	result = equ_f.is_equation_format(start_str)
	print(result)
	assert result == -1, "\nWRONG ANSWER: Result should be == -1 not {0}".format(result)

#
# def test_base_equs_no_equal_01():
# 	equ_f = EF(False, "left")
# 	try:
# 		result = equ_f.equation_dispatcher(base_equs["base_1_no_equal"][0])
# 	except SystemExit as sys_error:
# 		print("System exit error: ", sys_error)
# 	print(result)
# 	assert result == base_equs["base_1_no_equal"][1], "The result does not match the awaited answer: res: {0}	answer: {1}".format(result, base_equs["base_1_no_equal"][1])
#
#
# def test_base_equs_no_equal_neg_02():
# 	equ_f = EF(False, "left")
# 	result = equ_f.equation_dispatcher(base_equs["base_1_no_equal_neg"][0])
# 	print(result)
# 	assert result == base_equs["base_1_no_equal_neg"][1], "The result does not match the awaited answer: res: {0}	answer: {1}".format(result, base_equs["base_1_no_equal_neg"][1])
#
#
# def test_base_equs_simple_03():
# 	equ_f = EF(False, "left")
# 	result = equ_f.equation_dispatcher(base_equs["base_2_simple"][0])
# 	print(result)
# 	assert result == base_equs["base_2_simple"][1], "The result does not match the awaited answer: res: {0}	answer: {1}".format(result, base_equs["base_2_simple"][1])
#
# def test_base_equs_simple_neg_04():
# 	equ_f = EF(False, "left")
# 	result = equ_f.equation_dispatcher(base_equs["base_2_simple_neg"][0])
# 	print(result)
# 	assert result == base_equs["base_2_simple_neg"][1], "The result does not match the awaited answer: res: {0}	answer: {1}".format(result, base_equs["base_2_simple_neg"][1])
