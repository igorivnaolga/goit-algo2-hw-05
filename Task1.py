from bloom import BloomFilter


def check_password_uniqueness(
    bloom_filter: BloomFilter, passwords: [str]
) -> (str, str):
    results = {}

    for password in passwords:
        if bloom_filter.contains(password):
            results[password] = "already used"
        else:
            results[password] = "unique"
    return results


if __name__ == "__main__":
    # Initialize Bloom filter
    bloom = BloomFilter(size=1000, num_hashes=3)

    # Add existing passwords
    existing_passwords = ["password123", "admin123", "qwerty123"]
    for password in existing_passwords:
        bloom.add(password)

    # Check new passwords
    new_passwords_to_check = ["password123", "newpassword", "admin123", "guest"]
    results = check_password_uniqueness(bloom, new_passwords_to_check)

    # Print results
    for password, status in results.items():
        print(f"Password '{password}' - {status}.")
