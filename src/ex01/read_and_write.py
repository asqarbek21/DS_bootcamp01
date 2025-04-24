def read_and_write():
    with open("ds.csv", "r") as csv_file:
        lines = csv_file.readlines()

    with open("ds.tsv", "w") as tsv_file:
        for line in lines:
            new_line = ""
            inside_quotes = False
            for char in line:
                if char == '"':
                    inside_quotes = not inside_quotes
                    new_line += char
                elif char == ',' and not inside_quotes:
                    new_line += '\t'
                else:
                    new_line += char
            tsv_file.write(new_line)

if __name__ == '__main__':
    read_and_write()