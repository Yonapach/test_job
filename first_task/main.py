def task(array: str) -> int:
    """
    Algorithmic complexity: O(n)

    Return -1 on failure.
    """
    return array.find('0')


if __name__ == '__main__':
    print(task("111111111111111111111111100000000"))
