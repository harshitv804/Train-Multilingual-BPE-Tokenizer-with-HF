from pathlib import Path

VOCAB_SIZE = 64000
MIN_FREQUENCY = 2

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_TOKENIZER = BASE_DIR / "output" / "tokenizer.json"

CORPUS_DIR = BASE_DIR / "corpus"

METASPACE_CHAR = "▁"
UNK_TOKEN = "<UNK>"
SPECIAL_TOKENS = [
    "<PAD>",
    "<BOS>",
    "<EOS>",
    "<UNK>"
    ] + [f"<0x{i:02X}>" for i in range(256)]