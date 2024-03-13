import sys

def reorder_table(file_path, dealer_position):
    """
    Reorders the poker table based on the new dealer position.
    
    :param file_path: Path to the file containing player statuses.
    :param dealer_position: The position number of the new dealer, as an integer.
    """
    # Read the current order and statuses from the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Create a dictionary to hold player statuses
    player_statuses = {}
    for line in lines:
        key, value = line.strip().split(':')
        player_statuses[int(key)] = value

    # Correct the dealer_index calculation
    dealer_index = dealer_position  # No need to subtract 1, assuming dealer_position is 1-based index

    # Correcting the logic for determining the new order
    # The list should start from the dealer position and wrap around correctly
    new_order = list(range(dealer_index, len(player_statuses) + 1)) + list(range(1, dealer_index))

    # Write the new order back to the file
    with open(file_path, 'w') as file:
        for player in new_order:
            # Ensure player key exists in player_statuses before writing to avoid KeyError
            if player in player_statuses:
                file.write(f"{player}:{player_statuses[player]}\n")

if __name__ == "__main__":
    if len(sys.argv) > 2:  # Check if both file path and dealer position are provided
        file_path = sys.argv[1]  # First argument is the file path
        dealer_position = int(sys.argv[2])  # Second argument is the dealer position
        reorder_table(file_path, dealer_position)
    else:
        print("Usage: python order.py <file_path> <dealer_position>")
