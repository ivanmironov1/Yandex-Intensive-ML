class Selector:
    def __init__(self, nums_list):
        self.nums_list = nums_list

    def get_odds(self):
        return list(filter(lambda x: x % 2 != 0, self.nums_list))

    def get_evens(self):
        return list(filter(lambda x: x % 2 == 0, self.nums_list))

    def add_number(self, num):
        self.nums_list.append(num)

    def __str__(self):
        return ' '.join(map(str, self.nums_list))

    def __call__(self):
        return self.nums_list


a = Selector([1, 2, 3, 4])
print(a.get_odds())
a.add_number(100)
print(a.get_evens())
print(a)
print(a())
