import json
from pathlib import Path
from random import randint
import numpy as np

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', ' ', '.', ',', '"', '\'', '1']

def clean_text_for_pattern_letter(input_text: str, out_len: int = None):
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

def get_pattern_for_letter_without_collision(size: int = 32,
                                             cache: bool = True,
                                             dump_cache: bool = False,
                                             pattern_size: int = 2):
    cache_name = f'./data/letter_pattern_without_collision_cache_size_{size}.json'

    if not dump_cache:
        cache_file = Path(cache_name)
        if cache_file.is_file():
            with open(cache_file, "r") as read_file:
                letter_dict = json.load(read_file)

                for key in letter_dict:
                    letter_dict[key] = np.array(letter_dict[key], dtype='float64')

                print('a', int(letter_dict['a'].sum()), letter_dict['a'].astype('int').tolist())
                print('z', int(letter_dict['z'].sum()), letter_dict['z'].astype('int').tolist())

                return letter_dict

    letter_dict = {}

    slot_step = int(size / pattern_size)

    prev_pattern = np.zeros(size)

    for letter in letters:
        pattern = np.zeros(size)

        for slt_idx in range(0, size, slot_step):
            prev_slot = prev_pattern[slt_idx:slt_idx+slot_step]
            prev_slot_free_idx_arr: np.ndarray = np.where(prev_slot == 0)[0]

            new_pattern_idx = prev_slot_free_idx_arr[randint(0, prev_slot_free_idx_arr.size-1)]

            pattern[slt_idx + new_pattern_idx] = 1

        prev_pattern += pattern

        letter_dict[letter] = np.array(pattern, dtype='float64')
        print(letter, int(np.sum(pattern)), pattern.astype('int').tolist())

    if cache:
        output_file = open(cache_name, 'w')
        letter_dict_cache = {}

        for key in letter_dict:
            letter_dict_cache[key] = letter_dict[key].tolist()

        json.dump(letter_dict_cache, output_file)

    return letter_dict