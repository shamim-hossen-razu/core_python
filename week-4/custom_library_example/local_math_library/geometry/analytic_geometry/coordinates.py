def distance_between_points(x1, y1, x2, y2):
    """
    Calculate the Euclidean distance between two points in a 2D plane.

    Args:
        x1 (float): x-coordinate of the first point
        y1 (float): y-coordinate of the first point
        x2 (float): x-coordinate of the second point
        y2 (float): y-coordinate of the second point

    Returns:
        float: The distance between the two points
    """
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def midpoint(x1, y1, x2, y2):
    """
    Calculate the midpoint between two points in a 2D plane.

    Args:
        x1 (float): x-coordinate of the first point
        y1 (float): y-coordinate of the first point
        x2 (float): x-coordinate of the second point
        y2 (float): y-coordinate of the second point

    Returns:
        tuple: A tuple containing the x and y coordinates of the midpoint
    """
    return ((x1 + x2) / 2, (y1 + y2) / 2)
