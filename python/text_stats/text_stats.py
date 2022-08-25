"""
Python UDF to compute text stats.
"""

import re
from typing import Tuple


def get_text_stats(text: str) -> Tuple[str]:
    char_count = len(text)
    blanks_fixed = re.sub(r'\s+', ' ', text).strip()
    word_count = 0
    if len(blanks_fixed) > 0:
        word_count = len(blanks_fixed.split(' '))
    return (word_count, char_count)
