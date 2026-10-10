from logic_utils import (
    check_guess,
    get_attempt_limit,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message  # regression: hint used to say HIGHER


def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_guess_compares_as_ints_not_strings():
    # regression: "9" > "10" as strings; secret was str on even attempts
    outcome, _ = check_guess(9, 10)
    assert outcome == "Too Low"


def test_parse_guess_valid_and_invalid():
    assert parse_guess("42") == (True, 42, None)
    assert parse_guess("") == (False, None, "Enter a guess.")
    assert parse_guess(None)[0] is False
    assert parse_guess("abc")[0] is False


def test_parse_guess_out_of_range():
    ok, _, err = parse_guess("500", 1, 100)
    assert not ok
    assert "between 1 and 100" in err


def test_hard_is_harder_than_normal():
    n_low, n_high = get_range_for_difficulty("Normal")
    h_low, h_high = get_range_for_difficulty("Hard")
    assert (h_high - h_low) > (n_high - n_low)
    assert get_attempt_limit("Hard") < get_attempt_limit("Easy")


def test_score_wrong_guesses_always_lose_points():
    # regression: Too High gave +5 on even attempts
    for attempt in (1, 2, 3, 4):
        assert update_score(0, "Too High", attempt) == -5
        assert update_score(0, "Too Low", attempt) == -5


def test_score_win_rewards_early_wins():
    assert update_score(0, "Win", 1) > update_score(0, "Win", 5)
    assert update_score(0, "Win", 20) == 10
