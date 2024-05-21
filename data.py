def readData(file):
    lines = []
    with open(file, 'r', encoding='utf-8') as file:
        for line in file:
            lines.append(line.strip())  # strip() để loại bỏ ký tự xuống dòng (newline character)
    return lines
