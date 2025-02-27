from concurrent.futures import ProcessPoolExecutor

def f(x):
    if x % 2 == 0:
        m = x.bit_length()
        return x + (1 << m) + (1 << (m + 1))
    else:
        x1 = (x << 2) + 2
        m = x1.bit_length()
        return x1 + (1 << m)

def process_block(start, end):
    return max(f(x) for x in range(start, end))

max_number = f(234567890)

block_size = 10000
start_value = 234567890 + 1
end_value = 567891234 + 1

with ProcessPoolExecutor() as executor:
    futures = []
    for start in range(start_value, end_value, block_size):
        end = min(start + block_size, end_value)
        futures.append(executor.submit(process_block, start, end))

    for future in futures:
        max_number = max(max_number, future.result())

print(max_number)

