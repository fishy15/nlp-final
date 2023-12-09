# {'h-negation': 12, 'h-different': 16, 'h-specific': 14, 'h-general': 11, 'p-negation': 20, 'p-synonym': 6, 'p-number': 5, 'h-antonym': 23, 'p-different': 13, 'p-time': 1, 'h-synonym': 9, 'p-general': 9, 'p-specific': 13, 'h-direction': 3, 'p-direction': 1, 'p-removal': 1, 'h-number': 5, 'p-synoynm': 1, 'h-numbers': 1, 'p-antonym': 25, 'p-location': 1, 'h-time': 1, 'p-synonm': 1, 'h-tense': 1, 'pantonym': 1, 'pspecific': 1, 'hsynonym': 1, 'hnegation': 1, 'h-synonyms': 1, 'p-antonym/pgeneral': 1}

import os
import json

# assume cwd = dir
def split_dir_num():
    for i in range(1, 6):
        file_name = f'test-{i}.jsonl'
        with open(file_name, 'r') as orig:
            with open(f'test-{i}-0.jsonl', 'w') as f0, open(f'test-{i}-2.jsonl', 'w') as f2:
                for ex in orig:
                    if json.loads(ex)['origin'] == '0-0':
                        print(end=ex, file=f0)
                    else:
                        print(end=ex, file=f2)

def split_dir_typ():
    for i in range(1, 6):
        file_name = f'test-{i}.jsonl'
        with open(file_name, 'r') as orig:
            with open(f'test-{i}-h.jsonl', 'w') as f0, open(f'test-{i}-p.jsonl', 'w') as f2:
                for ex in orig:
                    try:
                        if json.loads(ex)['type'][0] == 'h':
                            print(end=ex, file=f0)
                        else:
                            print(end=ex, file=f2)
                    except:
                        # some invalid files
                        pass

for i in range(20, 180, 20):
    dir = f'split-{i}'
    os.chdir(dir)
    split_dir_num()
    split_dir_typ()
    os.chdir('..')
