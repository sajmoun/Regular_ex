import re

def check_dhcp_config(line: str) -> bool:
    pattern = r"([a-z]+\.[a-z]+\.[a-z]+)\s*ha=([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2}):ip=(\d+\.\d+\.\d+\.\d+):"
    return re.search(pattern, line.strip()) is not None

def transfer_dhcp_config(text: str) -> str:
    pattern = r"([a-z]+\.[a-z]+\.[a-z]+)\s*ha=([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2}):ip=(\d+\.\d+\.\d+\.\d+):"
    replacement = r"\nhost \1 {\n link address \2:\3:\4:\5:\6:\7;\n fix address \8;\n}\n"
    return re.sub(pattern, replacement, text.strip())
