import hashlib

class HashCracker:
    def __init__(self, hash_type, target_hash, wordlist):
        self.hash_type = hash_type.lower()
        self.target_hash = target_hash
        self.wordlist = wordlist

    def compute_hash(self, word):
        if self.hash_type == "md5":
            return hashlib.md5(word.encode()).hexdigest()
        elif self.hash_type == "sha1":
            return hashlib.sha1(word.encode()).hexdigest()
        elif self.hash_type == "sha256":
            return hashlib.sha256(word.encode()).hexdigest()
        else:
            raise ValueError("Unsupported hash type")

    def run(self):
        with open(self.wordlist, 'r') as f:
            for line in f:
                word = line.strip()
                hashed = self.compute_hash(word)
                if hashed == self.target_hash:
                    print(f"[+] Cracked! {self.hash_type.upper()} hash of '{word}' matches {self.target_hash}")
                    return word
        print("[-] Failed to crack the hash")
        return None
