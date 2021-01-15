from io import DEFAULT_BUFFER_SIZE


# def last_lines(file):
#     with open(file, 'r') as f:
#         return f.readlines()[::-1]


# def last_lines(file):
#     with open(file, 'r') as f:
#         yield from f.readlines()[::-1]


def last_lines(file):
    with open(file, 'rb') as f:
        f.seek(0, 2)  # go to end of file
        leftover_data = b''
        while f.tell() > 0:
            # read DEFAULT_BUFFER_SIZE bytes, or the rest of the file if smaller
            num_bytes_to_read = min(f.tell(), DEFAULT_BUFFER_SIZE)

            # go backwards, read the data, then go backwards again :D
            # if there is leftover data from the previous read, add it here
            f.seek(-num_bytes_to_read, 1)
            data = f.read(num_bytes_to_read) + leftover_data
            f.seek(-num_bytes_to_read, 1)

            # split into lines, keeping line endings
            lines = data.splitlines(keepends=True)

            # if at the start of the file, there are no leftovers
            # if not, we are in the middle of a line, and the first item
            #   must be added to the next loop to obtain a complete line
            if f.tell() == 0:
                leftover_data = b''
            else:
                leftover_data = lines[0]
                lines = lines[1:]

            # yield backwards and decode from bytes to str
            yield from [line.decode() for line in lines[::-1]]
