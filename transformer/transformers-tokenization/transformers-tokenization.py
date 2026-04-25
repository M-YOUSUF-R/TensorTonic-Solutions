import numpy as np
from typing import List, Dict

class SimpleTokenizer:
    """
    A word-level tokenizer with special tokens.
    """
    
    def __init__(self):
        self.word_to_id: Dict[str, int] = {}
        self.id_to_word: Dict[int, str] = {}
        self.vocab_size = 0
        
        # Special tokens
        self.pad_token = "<PAD>"
        self.unk_token = "<UNK>"
        self.bos_token = "<BOS>"
        self.eos_token = "<EOS>"
    
    def build_vocab(self, texts: List[str]) -> None:
        """
        Build vocabulary from a list of texts.
        Add special tokens first, then unique words.
        """
        # YOUR CODE HERE.
        vocab:list = list()
        special_token:list = [
          self.pad_token,
          self.unk_token,
          self.bos_token,       
          self.eos_token    
        ]
        for token in special_token:
          self.word_to_id[token] = self.vocab_size
          self.id_to_word[self.vocab_size] = token
          self.vocab_size += 1
          vocab.append(token)
        print(f"{vocab=}")
        text_vocab = set()
        for item in texts:
          for word in item.split(" "):
            text_vocab.add(word.lower())
        text_vocab:list = sorted(text_vocab)
        print(f"{text_vocab=}")
        vocab = vocab + text_vocab
        print(f"{vocab=}")

        for word in vocab:
          if word not in self.word_to_id :
            self.word_to_id[word] = self.vocab_size
            self.id_to_word[self.vocab_size] = word
            self.vocab_size += 1
    def encode(self, text: str) -> List[int]:
        """
        Convert text to list of token IDs.
        Use UNK for unknown words.
        """
        # YOUR CODE HERE
        token = []
        # token.append(self.word_to_id[self.bos_token])
        for word in text.lower().split(" "):
          if word == "" or len(word) <= 0:
            return []
          word = word.lower()
          if word in self.word_to_id:
            token.append(self.word_to_id[word])
          else:
            token.append(self.word_to_id[self.unk_token])
        # token.append(self.word_to_id[self.eos_token])
        return token
    
    def decode(self, ids: List[int]) -> str:
        """
        Convert list of token IDs back to text.
        """
        # YOUR CODE HERE
        words = []
        for n in ids:
          word = self.id_to_word.get(n,self.unk_token)
          if word in [self.bos_token,self.eos_token,self.pad_token]:
            continue
          words.append(word)
        return " ".join(words)