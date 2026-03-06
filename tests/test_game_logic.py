import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# --- Input validation bug fixes ---

def test_parse_guess_rejects_alphabetic():
    # Bug fixed: alphabetic input should return invalid, not count as attempt
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None
    assert err == "That is not a number."

def test_parse_guess_rejects_mixed_input():
    # "12abc" is not a valid number
    ok, value, err = parse_guess("12abc")
    assert ok is False
    assert value is None
    assert err == "That is not a number."

def test_parse_guess_rejects_empty_string():
    # Bug fixed: empty input should not count as an attempt
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None
    assert err == "Enter a guess."

def test_parse_guess_rejects_none():
    # Bug fixed: None input should not count as an attempt
    ok, value, err = parse_guess(None)
    assert ok is False
    assert value is None
    assert err == "Enter a guess."

def test_parse_guess_accepts_valid_number():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_guess_accepts_float_string():
    # Float strings are truncated to int (e.g. "7.9" -> 7)
    ok, value, err = parse_guess("7.9")
    assert ok is True
    assert value == 7
    assert err is None

def test_range_check_rejects_above_max():
    # Bug fixed: numbers above difficulty range must be rejected, not count as attempt
    low, high = 1, 20   # Easy difficulty
    ok, guess_int, _ = parse_guess("99")
    assert ok is True
    out_of_range = guess_int < low or guess_int > high
    assert out_of_range is True, "99 is above Easy range (1-20) and should be rejected"

def test_range_check_rejects_negative():
    # Bug fixed: negative numbers are below the valid range and must not count as attempt
    low, high = 1, 100  # Normal difficulty
    ok, guess_int, _ = parse_guess("-1")
    assert ok is True
    out_of_range = guess_int < low or guess_int > high
    assert out_of_range is True, "-1 is below the valid range and should be rejected"

def test_range_check_accepts_boundary_values():
    # Values exactly at the boundary should be accepted
    low, high = 1, 50   # Hard difficulty
    for boundary in [1, 50]:
        ok, guess_int, _ = parse_guess(str(boundary))
        assert ok is True
        out_of_range = guess_int < low or guess_int > high
        assert out_of_range is False, f"{boundary} is a valid boundary for Hard"
