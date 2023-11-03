"""Check the access nested function"""
from utils import access_nested_map

nested_map={"a": 1} 
path=("a",)
print(access_nested_map(nested_map, path))
nested_map={"a": {"b": 2}} 
path=("a",)
print(access_nested_map(nested_map, path))
nested_map={"a": {"b": 2}} 
path=("a", "b")
print(access_nested_map(nested_map, path))
