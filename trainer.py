import unicodedata
import config
from tokenizers import Tokenizer, Regex, decoders, normalizers, pre_tokenizers, trainers
from tokenizers.models import BPE

def get_corpus_files():
    if not config.CORPUS_DIR.exists():
        raise FileNotFoundError(
            f"Corpus directory does not exist: {config.CORPUS_DIR}"
        )

    corpus_files = [
        str(file)
        for file in config.CORPUS_DIR.iterdir()
        if file.is_file()
    ]

    if not corpus_files:
        raise ValueError(
            f"No corpus files found in {config.CORPUS_DIR}"
        )

    return corpus_files

def build_initial_alphabet():
    tamil_chars = [
        chr(cp)
        for cp in range(0x0B80, 0x0C00)
        if unicodedata.category(chr(cp)) != "Cn"
    ]

    english_chars = list(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz"
        "0123456789"
        ".,!?;:'\"-()[]{}"
    )

    return (
        tamil_chars +
        english_chars +
        [config.METASPACE_CHAR]
    )

def create_tokenizer():
    tokenizer = Tokenizer(BPE(unk_token=config.UNK_TOKEN,
                              byte_fallback=True))

    tokenizer.normalizer = normalizers.NFKC()

    tokenizer.pre_tokenizer = pre_tokenizers.Sequence(
        [
            pre_tokenizers.Split(
                pattern=Regex(r"\p{N}{1,3}"),
                behavior="isolated",
            ),
            pre_tokenizers.Split(
                pattern=Regex(r"[一-龥぀-ゟ゠-ヿ]+"),
                behavior="isolated",
            ),
            pre_tokenizers.Split(
                pattern=Regex(
                    r"""[!"#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~][A-Za-z]+"""
                    r"""|[^\r\n\p{L}\p{P}\p{S}]?[\p{L}\p{M}]+[\p{P}\p{S}]*"""
                    r"""| ?[\p{P}\p{S}]+[\r\n]*"""
                    r"""|\s*[\r\n]+"""
                    r"""|\s+(?!\S)"""
                    r"""|\s+"""
                ),
                behavior="isolated",
            ),
            pre_tokenizers.Metaspace(
                replacement=config.METASPACE_CHAR,
                prepend_scheme="first",
            ),
            pre_tokenizers.Digits(
                individual_digits=False,
            ),
        ]
    )

    tokenizer.decoder = decoders.Sequence(
        [
            decoders.ByteFallback(),
            decoders.Metaspace(
                replacement=config.METASPACE_CHAR,
                prepend_scheme="first",
            ),
        ]
    )

    return tokenizer

def create_trainer():
    trainer = trainers.BpeTrainer(
        vocab_size=config.VOCAB_SIZE,
        min_frequency=config.MIN_FREQUENCY,
        initial_alphabet=build_initial_alphabet(),
        special_tokens=config.SPECIAL_TOKENS,
        show_progress=True)
    
    config.OUTPUT_TOKENIZER.parent.mkdir(
    parents=True,
    exist_ok=True,)

    return trainer