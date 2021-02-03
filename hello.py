#!/usr/bin/env python3

def hello(name: str) -> str:
    return f'Hello, {name}!'


print(hello('world'))
print(hello(5))
print(hello([10, 20, 30]))
