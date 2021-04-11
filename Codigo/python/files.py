def read_lines(file):
    lines = []
    with open("./files/" + file, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip().isnumeric():
                lines.append(int(line))
            else:
                lines.append(line.strip())
    return lines

def write_lines(file, lines):
    with open("./files/" + file, "w", encoding="utf-8") as f:
        for line in lines:
            if type(line) is not str:
                line = str(line)
            f.write(line + "\n")


def run():
    print("========")
    print("LEYENDO numbers.txt")
    print(read_lines("numbers.txt"))
    print("========")
    print("LEYENDO names.txt")
    print(read_lines("names.txt"))

    print("========")
    print("ESCRIBIENDO numbers.txt")
    new_numbers = [12,23,34,45,56]
    write_lines("numbers.txt", new_numbers)
    print("NUEVOS NUMEROS: " + ", ".join([str(number) for number in new_numbers]))

if __name__ == '__main__':
    run()