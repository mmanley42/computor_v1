class EquationResolution:
	__slots__ = ["limit"]
	def __init__(self, limit):
		self.limit = limit
		self.degree_map = { 0: self.zero_degree_handling,
							1: self.first_degree_handling,
							2: self.second_dregree_handling}

	def input_data_validation(self, equ_data):
		"""check the degree limit and if the class can handle it"""
		pass

	def zero_degree_handling(self, equ_data):
		# keep list with 0 aspower. if multiplier different than 0 error.
		pass

	def first_degree_handling(self, equ_data):
		pass

	def second_dregree_handling(self, equ_data):
		pass

	def degree_dispatcher(self, equ_data):
		"""Pop list of multipliers equalto 0"""
		pass
