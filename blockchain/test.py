import hashlib

# i = 42
# string = str(i).encode()
# raw_hash = hashlib.sha256(string)
# hex_hash = raw_hash.hexdigest()

# print(type(raw_hash))
# print(raw_hash)
# print(type(hex_hash))
# print(hex_hash)

# index = int(hex_hash[:6], 16)
# print(hex_hash[:6])
# print(index)


def hash_cache(capacity, attempts):
    cache = [None] * capacity

    for i in range(attempts):
        raw_hash = hashlib.sha256(str(i).encode())
        hex_hash = raw_hash.hexdigest()
        index = int(hex_hash[:2], 16)
        cache[index] = str(i)
        # print(index)

    count = sum(1 for i in cache if i is not None)
    print(f'coverage: {count/capacity:.5f}')
    return cache

cache_of_hashes = hash_cache(100, 100)

# print(int('FF', 16))
