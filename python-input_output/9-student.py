#!/usr/bin/python3
"""Module that defines a Student class.

The Student class stores a first name, a last name and an age, and can
return a dictionary description of itself for JSON serialization.
"""


class Student:
    """Class that defines a student by first name, last name and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student with a first name, last name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return the
cd ~/alu-higher_level_programming
mkdir -p python-input_output
cd python-input_output

cat > 0-read_file.py << 'EOF'
#!/usr/bin/python3
"""Module that defines a function to read a UTF8 text file."""


def read_file(filename=""):
    """Read a UTF8 text file and print its content to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
