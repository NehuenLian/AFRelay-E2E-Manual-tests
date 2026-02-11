from datetime import datetime


def get_date_today() -> str:
    """
    Format: AAAAMMDD
    """
    return datetime.now().strftime("%Y%m%d")