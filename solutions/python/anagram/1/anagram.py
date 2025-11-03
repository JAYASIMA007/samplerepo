def find_anagrams(target, candidates):
    target_lower = target.lower()
    sorted_target = sorted(target_lower)

    result = []
    for word in candidates:
        if word.lower() == target_lower:
            continue  # Skip identical word
        if sorted(word.lower()) == sorted_target:
            result.append(word)
    return result