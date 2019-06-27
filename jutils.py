def i_lines(inp):
    for line in inp:
        line = line.strip()
        if line.startswith('#'):
            continue
        if not line:
            continue
        yield line


