import hashlib

def sha256_hash(key):
    return int(hashlib.sha256(key.encode('utf-8')).hexdigest(), 16) % 512

def sha1_hash(key):
    return int(hashlib.sha1(key.encode('utf-8')).hexdigest(), 16) % 512

def test_hash_function(hash_func, label):
    chash = ConsistentHash(hash_func=hash_func)
    # Add servers and measure load distribution
    # (Re-use the measure_load_distribution function from the previous step)

    # Add initial servers
    for i in range(3):
        chash.add_node(f"Server-{i}")

    # Measure load distribution
    count = measure_load_distribution()
    plot_distribution(count, f'Load Distribution with {label} Hash Function', f'load_distribution_{label.lower()}.png')

if __name__ == "__main__":
    test_hash_function(None, 'MD5')
    test_hash_function(sha256_hash, 'SHA-256')
    test_hash_function(sha1_hash, 'SHA-1')
