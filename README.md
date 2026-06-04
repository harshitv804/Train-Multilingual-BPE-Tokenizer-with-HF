# 🌍 Train Multilingual Character-Level BPE Tokenizer with Hugging Face

A multilingual **Character-Level BPE Tokenizer** built using the Hugging Face Tokenizers library, trained on **Tamil** and **English** text with a vocabulary size of **64,000 tokens**.

## ✨ Features

### 🔤 Character-Level BPE
- Uses a **Character-Level Byte Pair Encoding (BPE)** tokenizer.
- Starts from individual characters and learns merge rules during training.

### 🌐 Multilingual Training
- Trained on both:
  - 🇮🇳 Tamil
  - 🇬🇧 English
- Designed to handle mixed-language content effectively.

### 📚 64K Vocabulary
- Vocabulary size: **64,000 tokens**
- Provides a balance between compression efficiency and vocabulary coverage.

### 🧹 Regex-Based Preprocessing
- Includes custom **regex pre-tokenization** inspired by approaches used in:
  - DeepSeek models
  - GPT-family tokenizers
- Improves handling of:
  - Words
  - Numbers
  - Punctuation
  - Special symbols

### ▁ Metaspace Processing
- Uses **Metaspace (`▁`)** preprocessing similar to SentencePiece.
- Explicitly represents whitespace during tokenization.
- Automatically restores spaces during decoding.

### 🛡️ Byte Fallback Support
- Supports **Byte Fallback** for unseen or out-of-vocabulary characters.
- Ensures any Unicode text can be tokenized without producing unknown tokens.

### 🔠 Unicode-Based Initial Vocabulary
- Initializes training with:
  - All Tamil Unicode characters
  - All English characters
- Helps preserve important characters from the start of training.
- Leads to more meaningful and stable BPE merge rules.

## 🚀 Training the Tokenizer

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/harshitv804/Train-Multilingual-Character-Level-BPE-Tokenizer-with-HuggingFace.git
cd Train-Multilingual-Character-Level-BPE-Tokenizer-with-HuggingFace
```

### 2️⃣ Configure Training Parameters

Edit `config.py` and set the desired vocab size, minimum merge freq and special tokens:

### 3️⃣ Prepare Your Corpus

Create a folder named `corpus` in the project root:

```text
project/
├── corpus/
├── output/
├── config.py
├── trainer.py
└── ...
```

Copy all training data files into the `corpus` directory.

**Requirements:**
- Files must be in `.txt` format.
- You can include Tamil, English, or mixed-language text.
- Multiple text files are supported.

### 4️⃣ Start Training

Run:

```bash
python trainer.py
```

### 5️⃣ Training Output

After training completes, the tokenizer will be saved automatically to:

```text
output/tokenizer.json
```

## 📂 Example Directory Structure

```text
project/
├── corpus/
│   ├── tamil.txt
│   ├── english.txt
│   └── mixed.txt
├── output/
│   └── tokenizer.json
├── config.py
├── trainer.py
└── README.md
```

> 🤖 AI-assisted README.
