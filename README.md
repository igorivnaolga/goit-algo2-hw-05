# Task 1. Checking Password Uniqueness Using a Bloom Filter

### Create a function to check the uniqueness of passwords using a Bloom filter. This function should determine whether a password has been used before without the need to store the passwords themselves.

## Technical Requirements
 1. Implement the BloomFilter class, which supports adding elements to the filter and checking whether an element is in the filter.
 2. Implement the function check_password_uniqueness, which uses an instance of BloomFilter to check a list of new passwords for uniqueness. It should return the result of the check for each password.
 3. Ensure proper handling of all data types. Passwords should be handled simply as strings, without hashing. Empty or invalid values must also be properly handled.
 4. The function and class must work with large datasets using minimal memory.


# Task 2. Comparing the Performance of HyperLogLog with Exact Unique Element Counting

### Create a script to compare exact counting of unique elements and approximate counting using HyperLogLog.

## Technical Requirements
1. Load the dataset from the real log file `lms-stage-access.log`, which contains IP address information.
2. Implement a method for **exact counting** of unique IP addresses using a `set`.
3. Implement a method for **approximate counting** of unique IP addresses using `HyperLogLog`.
4. Compare the methods based on execution time.