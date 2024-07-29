class CustomDict:
    def __init__(self, data=None):
        if data is None:
            data = {}
        self.data = data
        self.index = 0

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __len__(self):
        return len(self.data)

    def __contains__(self, key):
        return key in self.data

    def __iter__(self):
        self.index = 0
        self.keys = list(self.data.keys())
        return self

    def __next__(self):
        if self.index < len(self.keys):
            key = self.keys[self.index]
            self.index += 1
            return key
        else:
            raise StopIteration


if __name__ == "__main__":
    cd = CustomDict({"a": 1, "b": 2, "c": 3})

    print(cd["a"])
    cd["d"] = 4
    print(cd["d"])

    print(len(cd))

    print("a" in cd)
    print("e" in cd)

    for key in cd:
        print(key)
