import os

TEXT = "Tip: A fresh context window fixes your AI in seconds. Sleep fixes you in hours. Reset the one you can right now — then seriously consider the other."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
