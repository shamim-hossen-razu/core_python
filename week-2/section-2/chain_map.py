from collections import ChainMap
import builtins

print("\nChainMap:")

# Creating a ChainMap
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'d': 5}

chain = ChainMap(dict1, dict2, dict3)

print(f"ChainMap: {chain}")

# Accessing values
print(f"\nAccessing values:")
print(f"chain['a']: {chain['a']}")  # From dict1
print(f"chain['b']: {chain['b']}")  # From dict1 (first occurrence)
print(f"chain['c']: {chain['c']}")  # From dict2
print(f"chain['d']: {chain['d']}")  # From dict3

# Checking membership
print(f"\nMembership:")
print(f"'a' in chain: {'a' in chain}")
print(f"'x' in chain: {'x' in chain}")

# Accessing keys, values, and items
print(f"\nKeys, values, and items:")
print(f"Keys: {list(chain.keys())}")
print(f"Values: {list(chain.values())}")
print(f"Items: {list(chain.items())}")

# Modifying the ChainMap
print(f"\nModifying the ChainMap:")
chain['b'] = 10  # This modifies dict1
print(f"After chain['b'] = 10: {chain}")
print(f"dict1: {dict1}")

chain['e'] = 6  # This adds to dict1
print(f"After chain['e'] = 6: {chain}")
print(f"dict1: {dict1}")

# Using maps attribute
print(f"\nUsing maps attribute:")
print(f"chain.maps: {chain.maps}")

# Creating a new ChainMap with an additional mapping
new_dict = {'f': 7}
new_chain = chain.new_child(new_dict)
print(f"\nNew ChainMap: {new_chain}")

# Accessing parents
print(f"\nAccessing parents:")
print(f"new_chain.parents: {new_chain.parents}")

# Updating and accessing first mapping
print(f"\nUpdating and accessing first mapping:")
chain.maps[0]['g'] = 8
print(f"After adding 'g': {chain}")

# Using ChainMap for command-line arguments, environment variables, and defaults
defaults = {'color': 'red', 'user': 'guest'}
import os, argparse
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v is not None}

combined = ChainMap(command_line_args, os.environ, defaults)
print(f"\nCombined ChainMap:")
print(f"color: {combined['color']}")
print(f"user: {combined['user']}")

# Using ChainMap with builtins
pylookup = ChainMap(locals(), globals(), vars(builtins))
print(f"\nPython lookup ChainMap:")
print(f"'len' in pylookup: {'len' in pylookup}")
print(f"'ChainMap' in pylookup: {'ChainMap' in pylookup}")