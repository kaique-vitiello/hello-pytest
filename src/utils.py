def clean_string(s: str) -> str:
    """
    Remove espaços extras e converte para minúsculas.
    """
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return " ".join(s.strip().lower().split())