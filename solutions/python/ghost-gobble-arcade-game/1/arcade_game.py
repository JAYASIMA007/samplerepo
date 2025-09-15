"""Functions for implementing the rules of the classic arcade game Pac-Man."""

def eat_ghost(power_pellet_active, touching_ghost):
    """Return True if Pac-Man can eat a ghost.

    :param power_pellet_active: bool - whether Pac-Man has an active power pellet.
    :param touching_ghost: bool - whether Pac-Man is touching a ghost.
    :return: bool - True if Pac-Man can eat the ghost, False otherwise.
    """
    return power_pellet_active and touching_ghost


def score(touching_power_pellet, touching_dot):
    """Return True if Pac-Man scores.

    :param touching_power_pellet: bool - whether Pac-Man is touching a power pellet.
    :param touching_dot: bool - whether Pac-Man is touching a dot.
    :return: bool - True if Pac-Man scores, False otherwise.
    """
    return touching_power_pellet or touching_dot


def lose(power_pellet_active, touching_ghost):
    """Return True if Pac-Man loses.

    :param power_pellet_active: bool - whether Pac-Man has an active power pellet.
    :param touching_ghost: bool - whether Pac-Man is touching a ghost.
    :return: bool - True if Pac-Man loses, False otherwise.
    """
    return not power_pellet_active and touching_ghost


def win(eaten_all_dots, power_pellet_active, touching_ghost):
    """Return True if Pac-Man wins.

    :param eaten_all_dots: bool - whether all dots have been eaten.
    :param power_pellet_active: bool - whether Pac-Man has a power pellet.
    :param touching_ghost: bool - whether Pac-Man is touching a ghost.
    :return: bool - True if Pac-Man wins, False otherwise.
    """
    return eaten_all_dots and not lose(power_pellet_active, touching_ghost)
