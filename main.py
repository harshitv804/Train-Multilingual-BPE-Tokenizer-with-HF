import config
from trainer import create_tokenizer, create_trainer, get_corpus_files


def main():
    corpus_files = get_corpus_files()

    tokenizer = create_tokenizer()

    trainer = create_trainer()

    tokenizer.train(
        corpus_files,
        trainer,
    )

    tokenizer.save(str(config.OUTPUT_TOKENIZER))

    print(f"Tokenizer saved to {config.OUTPUT_TOKENIZER}")


if __name__ == "__main__":
    main()
