class CreatedFunctions:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, item):
        return self.data[item]

    def my_sum(self):
        summary = 0
        for item in self.data:
            summary += item
        return summary

    def my_min(self):
        return min(self.data)


my_list = CreatedFunctions([1,2,3,4,5])

print(("Довжина списку ", len(my_list)))
print("Сума ", my_list.my_sum())
print("Мінімальне значення ", my_list.my_min())
