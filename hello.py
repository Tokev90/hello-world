#!/usr/bin/env python3
"""hello-world 示例脚本"""


def greet(name: str = "GitHub") -> str:
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet())
