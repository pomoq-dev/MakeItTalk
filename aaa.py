from dataclasses import dataclass


@dataclass
class C:
    some_attr = 42


# c = C(some_attr=42)
c = 42

print(f'\\{c}\'')

target = f'absomet\'hing'


