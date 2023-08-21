import time

start_time = time.time()
for i in range(8000000):
    print(i)
end_time = time.time()
Total = end_time - start_time
print(f"Total time: {Total}")