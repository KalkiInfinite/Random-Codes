def center_string(string, width):
    if len(string) >= width:
        return string
    else:
        padding = width - len(string)
        left_pad = padding // 2
        right_pad = padding - left_pad
        return "-" * left_pad + string + "-" * right_pad

string = "Hello, World!"
terminal_width = 20
centered_string = center_string(string, terminal_width)
print(centered_string)