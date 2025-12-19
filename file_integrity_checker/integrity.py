import hashlib
import os

def get_file_hash(filepath):
    # Standard SHA-256 hashing algorithm
    sha256_hash = hashlib.sha256()
    
    if not os.path.exists(filepath):
        return None

    try:
        with open(filepath, "rb") as f:
            # Read the file in chunks so it doesn't crash if the file is huge
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    path = input("Enter file path: ")
    print(f"Hash: {get_file_hash(path)}")
