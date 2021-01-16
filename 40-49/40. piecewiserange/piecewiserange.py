
class PiecewiseRange:

    def __init__(self, input_string):

        # convert to ints
        self.ranges = [
            tuple(map(int, item.strip().split('-'))) if '-' in item else int(item.strip())
            for item in input_string.split(',')
        ]

        # store condensed version
        self.ranges = self._condense()

        # calculate len once during init
        self.length = 0
        for item in self.ranges:
            if isinstance(item, int):
                self.length += 1
            else:
                self.length += (item[1] - item[0] + 1)

    def __iter__(self):
        for item in self.ranges:
            if isinstance(item, int):
                yield item
            else:
                yield from range(item[0], item[1] + 1)

    def __len__(self):
        return self.length

    def __getitem__(self, idx):
        if idx < 0:
            # deal with negative indices
            idx += len(self)

        for item in self.ranges:
            if isinstance(item, int):
                if idx == 0:
                    return item
                idx -= 1
            else:
                if idx <= (item[1] - item[0]):
                    return range(item[0], item[1] + 1)[idx]
                idx -= (item[1] - item[0] + 1)

    def _condense(self):
        condensed = []
        temp = None
        for item in self.ranges:
            if temp is None:
                temp = item
            elif isinstance(item, int):
                if isinstance(temp, int) and item == temp + 1:
                    temp = (temp, item)
                elif isinstance(temp, tuple) and item == temp[1] + 1:
                    temp = (temp[0], temp[1] + 1)
                else:
                    condensed.append(temp)
                    temp = item
            elif isinstance(item, tuple):
                if isinstance(temp, int) and item[0] == temp + 1:
                    temp = (temp, item[1])
                elif isinstance(temp, tuple) and item[0] == temp[1] + 1:
                    temp = (temp[0], item[1])
                else:
                    condensed.append(temp)
                    temp = item
        if temp:
            condensed.append(temp)
        return condensed

    def __repr__(self):
        condensed_str = []
        for item in self.ranges:
            if isinstance(item, int):
                condensed_str.append(f'{item}')
            else:
                condensed_str.append(f'{item[0]}-{item[1]}')
        return f'PiecewiseRange(\'{",".join(condensed_str)}\')'

    def __eq__(self, other):
        if not isinstance(other, PiecewiseRange):
            raise False
        return self.ranges == other.ranges
