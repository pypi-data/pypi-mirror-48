# packed

## Installation

```sh
pip3 install packed
```

## Usage

```python
from packed import packable

@packable  # 1) register class
class EqualMatcher:
    def __init__(self, expected):
        self._expected = expected

    def match(self, actual):
        return actual == self._expected

    def __packed__(self):  # 2) pick fields
        return {"expected": self._expected}
```

**client**

```python
from packed import pack

matcher = EqualMatcher("banana")
packed = pack(matcher)
# -> send «packed» over network
```

**server**

```python
from packed import unpack

# <- recieve «packed» as binary
matcher = unpack(packed)
assert matcher.match("banana") is True
```
