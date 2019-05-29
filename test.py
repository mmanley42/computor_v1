from computorV1 import equation_formatter

EF = equation_formatter.EquationFormatting

equations = {
	1: ["2x^1  * 4 + x2 - 3 + 4x0 = -2", [[1, 2], [8, 1], [3, 0]], [["x2", "8x1", "-3", "4x0", "2"]]],
	2: ["2x^1  * 4 + x2 - 3 + 4x0 = -2 + x1", [[1, 2], [8, 1], [3, 0]], ["x2", "7x1", "3x0"]],
	3: ["x^1 * 2 * 4 + x2 - 3 + 4x0 = -2", [[1, 2], [8, 1], [3, 0]], "x2 + 8x1 + 3x0 = 0"],
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

def test_format_equation_function_returns():
	equ_f = EF(False, "left")
	for key, equation in equations.items():
		result = equ_f.equation_dispatcher(equation[0])
		print(result, equation[2])
		for elem in equation[2][0]:
			assert elem in result[0], "EquationFormatting class did not send the correct data back. elem {0}".format(elem)
			result[0].remove(elem)
		print(result)
		assert result == [[]], "More data then expected sent back"
