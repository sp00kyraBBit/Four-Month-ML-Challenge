import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, type, value, traceback):
        end = time.perf_counter()
        print(f"Time taken: {end - self.start:.4f} seconds")


with Timer():
    total = sum(range(10_000_000))

# Ref: https://medium.com/@DahlitzF/how-to-create-your-own-timing-context-manager-in-python-a0e944b48cf8