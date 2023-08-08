class List:
    def __init__(self, *args):
        self._main_data = dict({})
        for arg in args:
            self.append(arg)

    def __getitem__(self, item):
        return self._main_data[item]

    def __setitem__(self, key, value):
        self._main_data[key] = value

    def __delitem__(self, key):
        del self._main_data[key]
        self.__shift()

    def __iter__(self):
        return iter(self._main_data.values())

    def __repr__(self):
        string = "["
        for i in self._main_data.values():
            string += f" {i} "
        return string + "]"

    def __len__(self):
        return len(self._main_data)

    def __shift(self):
        new_dict = self._main_data.copy()
        self._main_data.clear()
        for item in new_dict.values():
            self.append(item)

    def append(self, arg):
        last_index = len(self._main_data)
        self._main_data[last_index] = arg

    def pop(self, key=None):
        if key is None:
            value = self._main_data[len(self) - 1]
            del self._main_data[len(self) - 1]
            return value
        else:
            del self._main_data[key]
            self.__shift()

    def remove(self, value):
        index = None
        for idx, val in enumerate(self._main_data.values()):
            if val == value:
                index = idx
                break
        else:
            assert ValueError("This value is not in the List.")
        self.pop(index)
        self.__shift()

    def insert(self, index, value):
        new_dict = self._main_data.copy()
        self._main_data.clear()
        for k in range(len(new_dict)):
            if k == index:
                self._main_data[k] = value
                break
            self._main_data[k] = new_dict[k]
            del new_dict[k]
        for i in new_dict.values():
            self.append(i)
