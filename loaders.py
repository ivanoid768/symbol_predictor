def clean_text_for_pattern_letter(input_text: str, out_len: int = None):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', ' ', '.', ',', '"', '\'', '1']
    print(f'{len(letters)=}')

    input_list = list(input_text.lower())
    out_list = []

    for inp in input_list:
        if inp in letters:
            out_list.append(inp)
        elif inp == '\n':
            out_list.append(' ')

    if out_len is not None:
        out_list = out_list[:out_len]

    return ''.join(out_list)