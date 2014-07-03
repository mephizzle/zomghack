import inspect


class IndentError(Exception):
    pass


def _is_valid_statement(line):
    stripped = line.strip()
    if not stripped:
        return False
    if stripped[-1] in ':,':
        return False
    if stripped[0] in '@':
        return False
    return True


def _wrap_exception_handling(line):
    if not _is_valid_statement(line):
        return line

    def _indentedline(line, level):
        return '{0}{1}'.format(' ' * level * 4, line)

    if line.startswith('\t'):
        raise TabIndentError('This module doesn\'t yet support tab-indented code')
    indent_spaces = len(line) - len(line.lstrip())
    if indent_spaces % 4:
        raise TabIndentError('This module only supports code indented by 4 space increments')

    base_indent_level = indent_spaces / 4
    return '\n'.join([
            _indentedline('try:', base_indent_level),
            _indentedline(line, base_indent_level + 1),
            _indentedline('except Exception as e:', base_indent_level),
            _indentedline('print e', base_indent_level + 1),
    ])


def hack_function(func):
    lines, _ = inspect.getsourcelines(func)
    if lines[0].lstrip().startswith('@'):
        lines = lines[1:]

    lines = [_wrap_exception_handling(line) for line in lines]
    new_code = '\n'.join(lines)
    exec new_code
    return locals()[func.__name__]
