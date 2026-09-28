"""Module for processing sample data according to PEP 8 standard."""


def process_data(is_active, is_disabled, target_value, values, extra_offset):
    """Process input conditions and return calculated sum from list values."""
    if is_active and not is_disabled and target_value is None:
        first_item = values[0]
        base_offset = 1
        return first_item + extra_offset + base_offset

    return None


if __name__ == "__main__":
    process_data(True, False, None, [2], 3)