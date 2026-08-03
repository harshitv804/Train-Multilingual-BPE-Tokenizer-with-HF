from pathlib import Path

VOCAB_SIZE = 64000
MIN_FREQUENCY = 5

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_TOKENIZER = BASE_DIR / "output" / "tokenizer.json"

CORPUS_DIR = BASE_DIR / "corpus"
# CORPUS_DIR = Path("FULL_PATH") # For custom location

SPECIAL_TOKENS = [
    "<|pad|>",
    "<|bos|>",
    "<|eos|>"
] + [f"<|unused{i}|>" for i in range(50)]
