import argparse
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    parser.add_argument('--text', required=True)
    args = parser.parse_args()

    if os.path.isfile(args.path):
        files = [args.path]
    else:
        files = [os.path.join(args.path, f) for f in os.listdir(args.path)]

    for filepath in files:
        filename = os.path.basename(filepath)
        with open(filepath) as f:
            lines = f.readlines()

        blocks = []
        cur_block = []
        line_number = 1
        start_line = 1
        for line in lines:
            if len(line) >= 10 and line[4] == '-' and line[7] == '-':
                if cur_block:
                    blocks.append((start_line, ''.join(cur_block)))
                cur_block = [line]
                start_line = line_number
            else:
                cur_block.append(line)
            line_number += 1
        if cur_block:
            blocks.append((start_line, ''.join(cur_block)))

        for start_line, block_text in blocks:
            if args.text in block_text:
                time = block_text[:23]
                words = block_text.split()
                try:
                    idx = words.index(args.text)
                    start_idx = max(0, idx - 5)
                    end_idx = min(len(words), idx + 6)
                    context = ' '.join(words[start_idx:end_idx])
                except ValueError:
                    pos = block_text.find(args.text)
                    start_pos = max(0, pos - 30)
                    end_pos = pos + len(args.text) + 30
                    context = block_text[start_pos:end_pos]
                print(f"Файл: {filename}, строка начала блока: {start_line}, время: {time} \n"
                      f"Контекст: {context}\n")


main()
