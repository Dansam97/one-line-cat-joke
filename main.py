import os

TEXT = "My cat knocked my phone off the table, looked me dead in the eye, and waited — because in this house, gravity is apparently my job."

def validated_text(text):
    encoded = text.encode("utf-8")
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    return encoded

def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    data = validated_text(TEXT)
    path = os.path.join(out, "entry.txt")
    with open(path, "wb") as f:
        f.write(data + b"\n")
    with open(path, "rb") as f:
        assert f.read() == data + b"\n", "written bytes differ from validated text"

if __name__ == "__main__":
    main()
