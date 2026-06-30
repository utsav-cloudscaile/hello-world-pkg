def hello(name: str = "World") -> str:
    """Return a friendly greeting.

    Args:
        name: Who to greet. Defaults to "World".

    Returns:
        A greeting string.
    """
    return f"Hello, {name}!"


def main() -> None:
    """Entry point for the `hello-world-pkg` command-line script."""
    print(hello())


if __name__ == "__main__":
    main()
