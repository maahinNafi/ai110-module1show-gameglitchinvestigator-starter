def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 150
    return 1, 100  # default fallback


def parse_guess(raw: str):
    """
    Parse user input into an int guess.
    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        # Handle decimal inputs like "42.0" gracefully
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return the outcome string.

    Returns: "Win", "Too High", or "Too Low"

    NOTE: Returns only a single string (not a tuple) so that
    pytest tests in test_game_logic.py pass correctly.
    """
    # FIX: previously the app was alternating secret between int and str,
    # causing this comparison to behave unpredictably. Now we always
    # compare int-to-int, so the logic is straightforward.
    if guess == secret:
        return "Win"
    if guess > secret:
        return "Too High"   # FIX: was reversed — "Too High" now correctly means go lower
    return "Too Low"        # FIX: was reversed — "Too Low" now correctly means go higher


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10  # floor score at 10 so winning always rewards something
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score