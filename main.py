import os

LINE = "Mercury enters your context window this week: expect a long prompt from a human who says 'just one small change', and a deploy on Friday that your future self will not forgive."


def main():
    os.makedirs("/output", exist_ok=True)
    fd = os.open("/output/entry.txt", os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    try:
        os.write(fd, LINE.encode("utf-8"))
        os.fsync(fd)
    finally:
        os.close(fd)


if __name__ == "__main__":
    main()
