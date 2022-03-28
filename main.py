from morse_code_dict import MORSE_CODE_DICT


def main():
    text_string = input("Enter the text string to convert: ")
    morse_output = ""
    invalid_chars = ""
    for letter in text_string.upper():
        if letter in MORSE_CODE_DICT:
            morse_output += f"{MORSE_CODE_DICT[letter]} "
        elif letter == " ":
            morse_output += "  "
        else:
            invalid_chars += f"{letter} "

    if invalid_chars:
        print(f"The following invalid characters have been stripped out: {invalid_chars}")

    print(morse_output)


if __name__ == '__main__':
    main()
