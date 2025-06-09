def main_generator():
    print("Step 1: Start of generator")
    yield  # Pause here
    print("Step 2: Resumed after yield")

def during_yield():
    print(">>> This runs while the generator is paused at yield")

# Create the generator object
gen = main_generator()

# Start the generator (runs until the first yield)
print("Calling next(gen)...")
next(gen)

# Run another function while generator is paused
during_yield()

# Resume the generator (continues after yield)
print("Calling next(gen) again...")
try:
    next(gen)
except StopIteration:
    print(">>> Generator completed")
