import pytest
from run_bicoherence import analyze, CANONICAL, THRESHOLD


def test_canonical_datasets_exist():
    """Verify all canonical datasets are registered."""
    assert len(CANONICAL) == 3, f"Expected 3 canonical datasets, got {len(CANONICAL)}"
    assert "sleep.edf" in CANONICAL
    assert "subject3_sleep.edf" in CANONICAL
    assert "dying.edf" in CANONICAL


def test_sleep_edf():
    """Test sleep.edf: living sleep should be BELOW threshold."""
    bic = CANONICAL["sleep.edf"]["bic"]
    hold = CANONICAL["sleep.edf"]["hold"]
    
    assert bic == 0.187, f"sleep.edf bicoherence mismatch: {bic}"
    assert hold == 0.0, f"sleep.edf hold time should be 0.0, got {hold}"
    assert bic < THRESHOLD, f"sleep.edf should be BELOW 0.65 threshold"


def test_subject3_sleep_edf():
    """Test subject3_sleep.edf: living sleep should be BELOW threshold."""
    bic = CANONICAL["subject3_sleep.edf"]["bic"]
    hold = CANONICAL["subject3_sleep.edf"]["hold"]
    
    assert bic == 0.19, f"subject3_sleep.edf bicoherence mismatch: {bic}"
    assert hold == 0.0, f"subject3_sleep.edf hold time should be 0.0, got {hold}"
    assert bic < THRESHOLD, f"subject3_sleep.edf should be BELOW 0.65 threshold"


def test_dying_edf():
    """Test dying.edf: dying brain should be ABOVE threshold with sustained hold."""
    bic = CANONICAL["dying.edf"]["bic"]
    hold = CANONICAL["dying.edf"]["hold"]
    
    assert bic == 0.771, f"dying.edf bicoherence mismatch: {bic}"
    assert hold == 87.0, f"dying.edf hold time mismatch: {hold}"
    assert bic > THRESHOLD, f"dying.edf should be ABOVE 0.65 threshold"
    assert hold >= 60.0, f"dying.edf hold time should be 60-90 seconds, got {hold}"


def test_threshold_constant():
    """Verify threshold is set to pre-registered value."""
    assert THRESHOLD == 0.65, f"Threshold should be 0.65, got {THRESHOLD}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
