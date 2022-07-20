import re
from typing import Tuple

from pyspark.sql.types import StructType, StructField, LongType

from pyspark.sql import functions as F


def get_text_stats(text: str) -> Tuple[str]:
    char_count = len(text)
    blanks_fixed = re.sub(r'\s+', ' ', text).strip()
    word_count = 0
    if len(blanks_fixed) > 0:
        word_count = len(blanks_fixed.split(' '))
    return (word_count, char_count)
