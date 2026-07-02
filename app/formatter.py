def format_report(data: dict) -> str:
    title = data.get('title', 'Untitled')
    count = data.get('count', 0)
    # Complex f-string with nested quotes and expressions
    report = f"Report: {title!r} | Items: {count:,} | Rate: {count/max(data.get('total', 1), 1)*100:.{data.get('precision', 2)}f}%"
    return report

def format_list(items):
    return f"[{', '.join(f'{i}' for i in {*items,})}]"
