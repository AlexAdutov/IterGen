nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

nested_list2 = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, [1,2,3,4], None],
]

class FlatIterItems:
    def __init__(self, input_list):
        self.list = self.flatten_list(input_list)

    def flatten_list(self, inp_list):
        result = []
        for elem in inp_list:
            result += self.flatten_list(elem) if isinstance(elem, list) else [elem]
        return result

class FlatIterator:
	def __init__(self, input_list):
		self.list = FlatIterItems(input_list).list

	def __iter__(self):
		self.cursor = -1
		return self

	def __next__(self):
		if self.cursor == len(self.list) - 1:
			raise StopIteration
		self.cursor += 1
		return self.list[self.cursor]


def flat_generator(input_list):
    flat_list = FlatIterItems(input_list).list
    count = 0
    while count < len(flat_list):
        yield flat_list[count]
        count += 1


if __name__ == '__main__':

	for item in FlatIterator(nested_list2):
		print(item)

	for item in flat_generator(nested_list2):
		print(item)

	flat_list = [item for item in FlatIterator(nested_list2)]
	print('\n', flat_list, '\n\n')
