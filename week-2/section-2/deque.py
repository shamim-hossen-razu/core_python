from collections import deque

print("\n5. Deque:")
queue = deque(["a", "b", "c"])
print(f"Initial deque: {queue}")

# Append and appendleft
queue.append("d")
print(f"After append('d'): {queue}")
queue.appendleft("z")
print(f"After appendleft('z'): {queue}")

# Extend and extendleft
queue.extend(["e", "f"])
print(f"After extend(['e', 'f']): {queue}")
queue.extendleft(["y", "x"])
print(f"After extendleft(['y', 'x']): {queue}")

# Pop and popleft
popped = queue.pop()
print(f"Popped from right: {popped}")
print(f"After pop(): {queue}")
popped_left = queue.popleft()
print(f"Popped from left: {popped_left}")
print(f"After popleft(): {queue}")

# Count
print(f"Count of 'a': {queue.count('a')}")

# Index
print(f"Index of 'b': {queue.index('b')}")

# Insert
queue.insert(2, "m")
print(f"After insert(2, 'm'): {queue}")

# Remove
queue.remove("c")
print(f"After remove('c'): {queue}")

# Reverse
queue.reverse()
print(f"After reverse(): {queue}")

# Rotate
queue.rotate(2)
print(f"After rotate(2): {queue}")
queue.rotate(-1)
print(f"After rotate(-1): {queue}")

# Clear
queue.clear()
print(f"After clear(): {queue}")

# Maxlen
limited_queue = deque(maxlen=3)
limited_queue.extend([1, 2, 3, 4, 5])
print(f"Limited queue (maxlen=3): {limited_queue}")

# Copy
original = deque([1, 2, 3])
copied = original.copy()
print(f"Original: {original}, Copied: {copied}")