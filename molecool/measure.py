"""
This file containts functions relevant to measure properties of molecules.
"""


import numpy as np


def calculate_distance(rA, rB):
    """
    This function calculates the distance between two atoms in space
    given its Cartesian coordinates

    Parameters
    ----------
    rA: float
        Position of the first atom

    rB: float
        Position of the second atom

    Returns
    -------
    distance : float
    """

    d = rA - rB

    dist = np.linalg.norm(d)
    return dist


def calculate_angle(rA, rB, rC, degrees=False):
    # Calculate the angle between three points. Answer is given in radians by default, but can be given in degrees
    # by setting degrees=True
    AB = rB - rA
    BC = rB - rC
    theta = np.arccos(np.dot(AB, BC) / (np.linalg.norm(AB) * np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta
