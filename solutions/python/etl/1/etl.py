def transform(legacy_data):
    new_format = {}
    for score, letters in legacy_data.items():
        for letter in letters:
            new_format[letter.lower()] = score
    return new_format
