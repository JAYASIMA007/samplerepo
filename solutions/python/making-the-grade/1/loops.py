"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores."""
    return [round(score) for score in student_scores]


def count_failed_students(student_scores):
    """Count the number of failing students (score <= 40)."""
    return len([score for score in student_scores if score <= 40])


def above_threshold(student_scores, threshold):
    """Return scores that are >= threshold."""
    return [score for score in student_scores if score >= threshold]


def letter_grades(highest):
    """Return the lower threshold of each letter grade interval."""
    # The failing score is <= 40.
    minimum_passing = 41

    # We need 4 intervals: D, C, B, A
    # Range of scores from 41 → highest
    interval_size = (highest - 40) // 4

    # Create the starting points of D, C, B, A
    return [
        minimum_passing,
        minimum_passing + interval_size,
        minimum_passing + interval_size * 2,
        minimum_passing + interval_size * 3
    ]


def student_ranking(student_scores, student_names):
    """Return list of ranked students as strings."""
    ranked_list = []

    for index, (name, score) in enumerate(zip(student_names, student_scores), start=1):
        ranked_list.append(f"{index}. {name}: {score}")

    return ranked_list


def perfect_score(student_info):
    """Return the first [name, score] list where score == 100."""
    for item in student_info:
        name, score = item
        if score == 100:
            return item
    return []
