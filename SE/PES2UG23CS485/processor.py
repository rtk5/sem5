def sanitize_string(data):
    """
    Removes special characters (!,@,#,$,%) and trims the input.
    Handles None, non-string, and empty inputs safely.
    """
    if not isinstance(data, str):
        return ""  # Return empty string for invalid input

    data = data.strip()
    if not data:
        return ""  # Empty string remains empty

    # Remove unwanted special characters
    for ch in ['!', '@', '#', '$', '%']:
        data = data.replace(ch, '')
    return data


def parse_int_list(csv_string):
    """
    Parses a CSV string of integers into a list of ints.
    Handles None, empty strings, and invalid numbers safely.
    """
    if not isinstance(csv_string, str) or not csv_string.strip():
        return []  # Return empty list for None or blank input

    parts = csv_string.split(',')
    result = []
    for p in parts:
        p = p.strip()
        if not p:
            continue  # Skip empty elements
        try:
            result.append(int(p))
        except ValueError:
            # Skip invalid numbers like "abc"
            continue
    return result


def reverse_words(sentence):
    """
    Reverses each word in a sentence.
    Handles None, non-string, and empty inputs safely.
    """
    if not isinstance(sentence, str):
        return ""  # Return empty string if input isn't a string

    sentence = sentence.strip()
    if not sentence:
        return ""  # Return empty string for blank input

    words = sentence.split()
    reversed_words = [w[::-1] for w in words]
    return ' '.join(reversed_words)


def main():
    print("==== Running sanitize_string ====")
    raw_string = input("Enter a string with special characters (!,@,#,$,%): ")
    clean_string = sanitize_string(raw_string)
    print("Sanitized String:", clean_string)

    print("\n==== Running parse_int_list ====")
    csv_input = input("Enter a CSV of integers (e.g. 1,2,3,4): ")
    int_list = parse_int_list(csv_input)
    print("Parsed Integer List:", int_list)

    print("\n==== Running reverse_words ====")
    sentence_input = input("Enter a sentence without punctuation: ")
    reversed_sentence = reverse_words(sentence_input)
    print("Reversed Words Sentence:", reversed_sentence)


if __name__ == "__main__":
    main()
