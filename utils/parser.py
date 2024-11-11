def split_input(raw_input: str, sep: str = "\n") -> list[str]:
    """Split the input with a certain separetor."""
    return list(filter(None, raw_input.split(sep=sep)))
