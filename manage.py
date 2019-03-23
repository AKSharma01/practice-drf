#!/usr/bin/env python
import os
import sys
import re

key_value_pair_pattern = r'\A((?P<key>[^~`_!@#$%^&*()_+=]\w+(\d*|\s*|(A-Z|a-z)*)*)=(?P<val>.*))\Z'
with open(".env") as file:
    lines = file.read().splitlines()
    for line in lines:
        key_value = re.match(key_value_pair_pattern, line)
        if key_value:
            key, value = key_value['key'], key_value['val']
            m1 = re.match(r"\A'(.*)'\Z", value)
            if m1:
                value = m1.group(1)
            m2 = re.match(r'\A"(.*)"\Z', value)
            if m2:
                value = re.sub(r'\\(.)', r'\1', m2.group(1))
            os.environ.setdefault(key.strip(" "), value.strip(" "))


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "practicedrf.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
