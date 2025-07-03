from rps_game import determine_winner, is_valid_choice

def test_invalid_case_handling():
    assert is_valid_choice("banana") == False
    assert is_valid_choice("") == False
    assert is_valid_choice("Rock") == False  # case-sensitive check
    assert is_valid_choice("paper ") == False  # space

def test_edge_cases():
    assert determine_winner("rock", "rock") == "tie"
    assert determine_winner("paper", "paper") == "tie"
    assert determine_winner("scissors", "scissors") == "tie"

def test_user_win_cases():
    assert determine_winner("rock", "scissors") == "user"
    assert determine_winner("paper", "rock") == "user"
    assert determine_winner("scissors", "paper") == "user"

def test_computer_win_cases():
    assert determine_winner("scissors", "rock") == "computer"
    assert determine_winner("rock", "paper") == "computer"
    assert determine_winner("paper", "scissors") == "computer"
