def format_report(title, count, data):
    """Return a formatted report string.

    Parameters
    ----------
    title : str
        The title of the report.
    count : int
        Number of items.
    data : dict
        Dictionary containing optional keys ``total`` and ``precision``.

    Returns
    -------
    str
        A human‑readable report string.
    """
    precision = data.get("precision", 2)
    total = data.get("total", 1)
    rate = count / max(total, 1) * 100
    report = f"Report: {title!r} | Items: {count:,} | Rate: {rate:.{precision}f}%"
    return report
