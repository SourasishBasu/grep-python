import sys


def match_pattern(input_line, pattern):
    if len(input_line) == 0 and len(pattern) == 0:
        return True

    if not pattern:
        return True

    if len(pattern) >= 2 and pattern[1] == "?":
        element = pattern[0]
        if input_line:
            valid_string = input_line.split(" ")[0]

            if valid_string[0] == element:
                return match_pattern(input_line[1:], pattern[2:])
        return match_pattern(input_line, pattern[2:])

    if len(pattern) >= 2 and pattern[1] == ".":
        start, end = pattern[0], pattern[2]
        if input_line:
            valid_string = input_line.split(" ")[0]

            if valid_string[0] == start and valid_string[2] == end:
                return match_pattern(input_line[3:], pattern[3:])
            else:
                return False
        return match_pattern(input_line, pattern[3:])

    if not input_line:
        return False

    if pattern[len(pattern) - 1] == "$":
        valid_strings = input_line.split(" ")

        for x in valid_strings:
            if x.endswith(pattern[:-1]):
                return True
        else:
            return False

    elif len(pattern) >= 2 and pattern[1] == "+":
        element = pattern[0]
        valid_string = input_line.split(" ")[0]

        if valid_string[0] != element:
            return False
        else:
            for idx, x in enumerate(valid_string[1:]):
                if x != element:
                    return match_pattern(input_line[idx+1:], pattern[2:])
            return match_pattern(input_line[len(valid_string):], pattern[2:])

    if pattern[0] == input_line[0]:
        return match_pattern(input_line[1:], pattern[1:])

    elif pattern[:2] == "\\d":
        for i in range(len(input_line)):
            if input_line[i].isdigit():
                return match_pattern(input_line[i:], pattern[2:])
        return False

    elif pattern[:2] == "\\w":
        if input_line[0].isalnum():
            return match_pattern(input_line[1:], pattern[2:])
        else:
            return False

    elif pattern[:1] == "^":
        valid_strings = input_line.split(" ")

        for x in valid_strings:
            if x.startswith(pattern[1:]):
                return True
        else:
            return False

    elif pattern.startswith("[") and "]" in pattern:
        if pattern[1] == "^":
            invalid_chars = set(pattern[2:-2])
            for char in invalid_chars:
                if char in input_line:
                    return False
            return True
        else:
            valid_chars = set(pattern[1:-2])
            for char in valid_chars:
                if char in input_line:
                    return True
            return False

    elif pattern.startswith("(") and ")" in pattern:
        valid_strings = pattern[1:pattern.index(")")].split("|")
        valid_input = input_line.split(" ")[0]
        if valid_input in valid_strings:
            return match_pattern(input_line[len(valid_input):], pattern[pattern.index(")")+1:])
        else:
            return False

    else:
        return match_pattern(input_line[1:], pattern)


def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()

    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    if match_pattern(input_line, pattern):
        exit(0)
    else:
        exit(1)


if __name__ == "__main__":
    main()
