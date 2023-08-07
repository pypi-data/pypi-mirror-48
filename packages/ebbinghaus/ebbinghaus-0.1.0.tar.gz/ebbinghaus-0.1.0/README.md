# ebbinghaus
Ebbinghaus remembering framework, based on python3 and sqlite3.

# Install

```commandline
pip install ebbinghaus
```

# Usage

```python
import ebbinghaus

# Set the database to save data.
ebbinghaus.set_database(':memory:')

# Register a key to ebbinghaus.
ebbinghaus.register(3)
assert ebbinghaus.get_stage(3) == 0

# Remember the key.
ebbinghaus.remember(3)
assert ebbinghaus.get_stage(3) == 1

# Forget the key for one time.
ebbinghaus.forget(3)
assert ebbinghaus.get_stage(3) == 0

# Get random keys to review.
assert ebbinghaus.random(1) == [3]

```