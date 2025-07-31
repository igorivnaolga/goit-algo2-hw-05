import json
import timeit

from datasketch import HyperLogLog


def upload_data(path: str) -> list:
    data: list = []

    with open(path, "r", encoding="UTF-8") as f:
        for line in f:
            if line == "\n" or line == "" or (not json.loads(line)["remote_addr"]):
                continue
            data.append(json.loads(line))

    return data


def count_unique_ip_set(data: list):
    my_set = set()

    for item in data:
        my_set.add(item["remote_addr"])
    return len(my_set)


def count_unique_ip_hll(data: list):
    hll = HyperLogLog(p=10)

    for item in data:
        hll.update(item["remote_addr"].encode("utf-8"))
    return hll.count()


def compare_unique_ip():
    data = upload_data("lms-stage-access.log")

    # Exact counting
    exact_count = count_unique_ip_set(data)
    exact_time = timeit.timeit(lambda: count_unique_ip_set(data), number=100)

    # Counting using HyperLogLog
    hll_count = count_unique_ip_hll(data)
    hll_time = timeit.timeit(lambda: count_unique_ip_hll(data), number=100)

    # Formatted output of results
    print("Comparison Results:")
    print(f"{'':<20} | {'Exact Count':<20} | {'HyperLogLog':<20}")
    print(f"{'-'*70}")
    print(f"{'Unique Elements':<20} | {exact_count:<20} | {hll_count:<20}")
    print(f"{'Execution Time (sec)':<20} | {exact_time:<20.2f} | {hll_time:<20.2f}")


if __name__ == "__main__":
    compare_unique_ip()
