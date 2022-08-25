"""
Unit tests for the text stats Python UDF.
"""

from text_stats import text_stats

def test_get_text_stats_empty() -> None:
    assert text_stats.get_text_stats('') == (0, 0)

def test_get_text_stats_nonempty() -> None:
    assert text_stats.get_text_stats('One two three four') == (4, 18)

def test_get_text_stats_multiple_blanks() -> None:
    assert text_stats.get_text_stats('   One two three four') == (4, 21)
    assert text_stats.get_text_stats('One    two three  four') == (4, 22)
    assert text_stats.get_text_stats('One two three four   ') == (4, 21)
    assert text_stats.get_text_stats('  One two three four   ') == (4, 23)
    assert text_stats.get_text_stats('    ') == (0, 4)
