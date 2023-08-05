import os
import sys

import six
from cheap_repr import cheap_repr

NO_ASTTOKENS = (
        'pypy' in sys.version.lower()
        or sys.version_info[:2] == (3, 4)
)


file_reading_errors = (
    IOError,
    OSError,
    ValueError # IronPython weirdness.
)



def shitcode(s):
    return ''.join(
        (c if (0 < ord(c) < 256) else '?') for c in s
    )


def truncate(seq, max_length, middle):
    if len(seq) > max_length:
        left = (max_length - len(middle)) // 2
        right = max_length - len(middle) - left
        seq = seq[:left] + middle + seq[-right:]
    return seq


def truncate_string(string, max_length):
    return truncate(string, max_length, '...')


def truncate_list(lst, max_length):
    return truncate(lst, max_length, ['...'])


def ensure_tuple(x, split=False):
    if split and isinstance(x, six.string_types):
        x = x.replace(',', ' ').split()
    if not isinstance(x, (list, set, tuple)):
        x = (x,)
    return tuple(x)


def short_filename(code):
    result = os.path.basename(code.co_filename)
    if result.endswith('.pyc'):
        result = result[:-1]
    return result


def is_comprehension_frame(frame):
    return frame.f_code.co_name in ('<listcomp>', '<dictcomp>', '<setcomp>')


def needs_parentheses(source):
    def code(s):
        return compile(s.format(source), '<variable>', 'eval').co_code

    try:
        without_parens = code('{}.x')
    except SyntaxError:
        # Likely a multiline expression that needs parentheses to be valid
        code('({})')
        return True
    else:
        return without_parens != code('({}).x')


def with_needed_parentheses(source):
    if needs_parentheses(source):
        return '({})'.format(source)
    else:
        return source


REPR_TARGET_LENGTH = 100


def my_cheap_repr(x):
    return cheap_repr(x, target_length=REPR_TARGET_LENGTH)
