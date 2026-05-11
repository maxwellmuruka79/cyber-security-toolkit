import hashlib
import os

def get_file_hash(filepath):
    sha256_hash = hashlib.sha256()

    if not os.path.exists(filepath):
        return None

    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)

    return sha256_hash.hexdigest()


original_hash = input("Enter original hash: ")
path = input("Enter file path: ")

current_hash = get_file_hash(path)

if current_hash is None:
    print("File not found.")

elif current_hash == original_hash:
    print("File integrity verified.")

else:
    print("WARNING: File has been modified!")
