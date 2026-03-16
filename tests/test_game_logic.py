import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from logic_utils import check_guess, get_new_game_state


def test_hint_too_high_points_player_lower():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_hint_too_low_points_player_higher():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_new_game_state_resets_history_score_and_status():
    new_state = get_new_game_state(1, 100)
    assert new_state["history"] == []
    assert new_state["score"] == 0
    assert new_state["status"] == "playing"
    assert new_state["attempts"] == 0
    assert 1 <= new_state["secret"] <= 100


def test_submit_comparison_consistent_across_presses():
    # Simulates repeated submits against the same secret.
    # This guards against the old bug where secret type changed per attempt.
    first_outcome, _ = check_guess(20, 50)
    second_outcome, _ = check_guess(20, 50)
    assert first_outcome == "Too Low"
    assert second_outcome == "Too Low"
