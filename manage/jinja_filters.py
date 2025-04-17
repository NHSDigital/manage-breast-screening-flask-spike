from markupsafe import Markup, escape
from datetime import datetime

def no_wrap(value):
    return Markup(f'<span class="app-nowrap">{escape(value)}</span>' if value else "")

def as_hint(value):
    return Markup(f'<span class="app-text-grey">{value}</span>' if value else "")

def format_words(value, separator="_"):
    """
    Format separated words as a sentence, preserving acronyms
    * Example: 'in_progress' becomes 'In progress'
    * Example: 'not_in_PACS' becomes 'Not in PACS'
    """
    if not value:
        return ""

    parts = value.split(separator)
    result = []
    for part in parts:
        # Check for acronyms. Either:
        # - the whole thing is upper case
        # - there is an upper case character after the first letter
        if part == part.upper() or len(part) >= 2 and (part[1:].lower() != part[1:]):
            result.append(part)
        else:
            result.append(part.lower())

    return " ".join(parts)

def format_date(value):
    return value.strftime("%-d %B %Y")

def format_date_time(value):
    return value.strftime("%-d %B %Y, %H:%M")

def format_time(value):
    if value.minute == 0:
        if value.hour == 0:
            return "midnight"
        if value.hour == 12:
            return "midday"
        return value.strftime("%-I%p").lower()

    return value.strftime("%-I:%M%p").lower()

def format_time_range(value):
    start_time = format_time(value["start_time"])
    end_time = format_time(value["end_time"])
    return f"{start_time} to {end_time}"