# Comprehensive Guide to Set and Frozen Set in Python

# 1. Creating Sets
print("1. Creating Sets:")
set1 = {1, 2, 3, 4, 5}
set2 = set([3, 4, 5, 6, 7])
empty_set = set()
print(f"set1: {set1}")
print(f"set2: {set2}")
print(f"empty_set: {empty_set}")

# 2. Set Operations
print("\n2. Set Operations:")
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference (set1 - set2): {set1 - set2}")
print(f"Symmetric Difference: {set1 ^ set2}")

# 3. Adding and Removing Elements
print("\n3. Adding and Removing Elements:")
set1.add(6)
set1.update([7, 8])
print(f"After adding elements: {set1}")
set1.remove(8)
set1.discard(9)  # Doesn't raise an error if element is not present
print(f"After removing elements: {set1}")

# 4. Set Methods
print("\n4. Set Methods:")
print(f"Is set1 subset of set2? {set1.issubset(set2)}")
print(f"Is set1 superset of set2? {set1.issuperset(set2)}")
print(f"Do set1 and set2 have no elements in common? {set1.isdisjoint(set2)}")

# 5. Set Comprehension
print("\n5. Set Comprehension:")
squared_set = {x**2 for x in range(10)}
print(f"Squared set: {squared_set}")

# 6. Frozen Sets
print("\n6. Frozen Sets:")
frozen_set = frozenset([1, 2, 3, 4, 5])
print(f"Frozen set: {frozen_set}")
# frozen_set.add(6)  # This would raise an AttributeError

# 7. Set vs Frozen Set
print("\n7. Set vs Frozen Set:")
print("Set:")
print("- Mutable (can be changed after creation)")
print("- Supports methods that modify the set (add, remove, update, etc.)")
print("- Cannot be used as dictionary keys or elements of another set")
print("\nFrozen Set:")
print("- Immutable (cannot be changed after creation)")
print("- Does not support methods that modify the set")
print("- Can be used as dictionary keys or elements of another set")
print("- Useful for creating constant set of values")

# 8. Set Performance
print("\n8. Set Performance:")
print("- Average time complexity for add/remove/check membership: O(1)")
print("- Worst-case time complexity (rare): O(n)")
print("- Space complexity: O(n)")

# 9. Sets vs Lists vs Tuples
print("\n9. Sets vs Lists vs Tuples:")
print("- Sets: unordered, mutable, no duplicates")
print("- Lists: ordered, mutable, allows duplicates")
print("- Tuples: ordered, immutable, allows duplicates")

# 10. Real-world Use Cases
print("\n10. Real-world Use Cases:")
print("- Removing duplicates from a collection")
print("- Membership testing")
print("- Mathematical set operations")

# 11. Set with Different Data Types
print("\n11. Set with Different Data Types:")
mixed_set = {1, "hello", (1, 2, 3)}
print(f"Mixed set: {mixed_set}")

# 12. Set Iteration
print("\n12. Set Iteration:")
for item in set1:
    print(item, end=" ")
print()  # New line

# 13. Set Comparison
print("\n13. Set Comparison:")
set3 = {1, 2, 3, 4, 5}
print(f"set1 == set3: {set1 == set3}")
print(f"set1 != set2: {set1 != set2}")

# 14. Copying Sets
print("\n14. Copying Sets:")
set_copy = set1.copy()
print(f"Copied set: {set_copy}")

# 15. Clearing a Set
print("\n15. Clearing a Set:")
set_copy.clear()
print(f"Cleared set: {set_copy}")

# 16. Using Sets for Data Deduplication
print("\n16. Using Sets for Data Deduplication:")
duplicates = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(duplicates))
print(f"Original list: {duplicates}")
print(f"Deduplicated list: {unique}")

# 17. Frozen Set as Dictionary Key
print("\n17. Frozen Set as Dictionary Key:")
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([4, 5, 6])
fs_dict = {fs1: "Group 1", fs2: "Group 2"}
print(f"Dictionary with frozen set keys: {fs_dict}")

# This comprehensive guide covers all major aspects of working with sets and frozen sets in Python,
# including creation, operations, methods, and real-world use cases, as well as the key differences
# between sets and frozen sets.

