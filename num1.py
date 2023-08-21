import time

start_time = time.time()
k = ""
for i in range(8000000):
    k += f"{i}\n"
print(k)
end_time = time.time()
Total = end_time - start_time
print(f"Total time: {Total}")