import re

def phone_hide(persons_list: list[str]) -> list[str]:
    return [re.sub(r"\d{3}-", "***-", person) for person in persons_list]

def email_hide(persons_list: list[str]) -> list[str]:
    return [re.sub(r": ([a-z])[a-z.]+([a-z])@[a-z]+([a-z])", r": \1***\2@***\3", person) for person in persons_list]
