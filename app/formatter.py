def format_report(title, count, data):
    """Return a formatted report string.

    Parameters
    ----------
    title : str
        The title of the report.
    count : int
        Number of items.
    data : dict
        Dictionary containing optional ``total`` and ``precision`` keys.
    """
    # Safely extract values with defaults
    total = data.get("total", 1)
    precision = data.get("precision", 2)

    # Compute the rate, guarding against division by zero
    rate = count / max(total, 1) * 100

    # Build the report string using a single f‑string with a simple format specifier
    report = f"Report: {title!r} | Items: {count:,} | Rate: {rate:.{precision}f}%"
    return report
