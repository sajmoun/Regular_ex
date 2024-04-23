import re

def pick_numbers(text: str) -> list[int]:
    numbers = [int(num) for num in re.findall(r"\d+", text.replace(" ", "").replace("\t", ""))] #/t - tabulátor (mezery)
    return numbers
