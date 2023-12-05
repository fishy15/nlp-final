import json

def main():
    files = [[None] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            file = open(f'{i}-{j}.jsonl', 'w+')
            file.write(f'label {i}, predicted {j}\n')
            files[i][j] = file

    with open('eval_predictions.jsonl', 'r') as f:
        for line in f:
            j = json.loads(line)
            label = j['label']
            pred = j['predicted_label']
            files[label][pred].write(line)

    for row in files:
        for f in row:
            f.close()

if __name__ == '__main__':
    main()
