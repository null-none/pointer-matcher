# pointer-matcher

```python
from pointer_matcher.utils import PointMatcher

# Sample data
a = [(2.0, 4.0), (3.0, 3.0), (3.0, 4.0), (3.0, 5.0), (4.0, 2.0), (4.0, 3.0), (4.0, 4.0), (4.0, 5.0), (4.0, 6.0), (5.0, 3.0), (5.0, 5.0)]
b = [(3.4, 2.3), (3.4, 3.4), (3.4, 5.3)]

# Initialize matcher with tolerance
matcher = PointMatcher(a, b, eps=1)

print("Exact match:", matcher.exact_match())   # False
print("Fuzzy match:", matcher.fuzzy_match())   # True

# Show plot
matcher.plot()
```