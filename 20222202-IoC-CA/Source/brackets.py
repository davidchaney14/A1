def remove_brakcets(string_with_brackets):
    string_without_brackets = str(string_with_brackets.strip('('))
    string_without_brackets = str(string_without_brackets.strip(')'))
    return string_without_brackets
