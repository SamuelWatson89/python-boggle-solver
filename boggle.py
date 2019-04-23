def make_grid(width, height):
    """
    Creates a grid that holds boggle tiles
    """
    return {(row, col): " " for row in range(height)
            for col in range(width)
            }
