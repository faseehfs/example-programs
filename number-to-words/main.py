def partition(string: str) -> list[str]:
    """Partition the input string into substrings of three characters. Prepends zeros if needed to make the length divisible by 3."""
    formatted_string = (3 - len(string) % 3) * "0" + string

    strings = []
    start = 0

    for i in range(2, len(formatted_string), 3):
        strings.append(formatted_string[start : i + 1])
        start = i + 1

    return strings


def to_words(string: str) -> str:
    """Converts a 3-character numeric string to its English word representation. Assumes all characters are digits and handles numbers from 000 to 999. Returns an empty string on 000."""

    numbers = [
        "",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    numbers_second_place = [
        "",
        "ten",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]
    numbers_of_one = [
        "",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ]

    output = ""

    if string[0] != "0":
        output += numbers[int(string[0])] + " hundred "

    if string[1] != "0":
        if string[1] == "1" and string[2] != "0":
            output += numbers_of_one[int(string[2])] + " "
            return output
        else:
            output += numbers_second_place[int(string[1])] + " "

    if string[2] != "0":
        output += numbers[int(string[2])] + " "

    return output.strip()


SUFFIXES = [
    "",
    "thousand",
    "million",
    "billion",
    "trillion",
    "quadrillion",
    "quintillion",
    "sextillion",
    "septillion",
    "octillion",
    "nonillion",
    "decillion",
    "undecillion",
    "duodecillion",
    "tredecillion",
    "quattuordecillion",
    "quindecillion",
    "sexdecillion",
    "septendecillion",
    "octodecillion",
    "novemdecillion",
    "vigintillion",
    "unvigintillion",
    "duovigintillion",
    "trevigintillion",
    "quattuorvigintillion",
    "quinvigintillion",
    "sexvigintillion",
    "septenvigintillion",
    "octovigintillion",
    "novemvigintillion",
    "trigintillion",
    "untrigintillion",
    "duotrigintillion",
]

while True:
    number = input("Enter a number: ").strip().lower()

    if number == "":
        print("Bye!")
        break

    numbers_partitioned = partition(number)
    nums_in_words = [to_words(num) for num in numbers_partitioned]

    nums_in_words.reverse()
    num_in_words = ""
    for i in range(len(nums_in_words) - 1, -1, -1):
        if nums_in_words[i] != "":
            num_in_words += nums_in_words[i] + " " + SUFFIXES[i] + " "

    print(f"Number in words: {num_in_words}\n")
