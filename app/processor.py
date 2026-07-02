import re

def process_lines(text: str) -> list:
    results = []
    lines = text.splitlines()
    for line in lines:
        if m := re.match(r'(\w+)=(\d+)', line):
            results.append({'key': m.group(1), 'val': int(m.group(2))})
        elif chunk := line.strip():
            results.append({'raw': chunk})
    return results
