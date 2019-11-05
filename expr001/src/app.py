import argparse

from pathlib import Path


def do_work(input1, input2, output1):
    result = "result: " + str(input1) + " + " + str(input2)
    with open(output1, 'w') as f:
        f.write(result)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='My program description')
    parser.add_argument('--input1', type=str, help='input1 value')  # Paths should be passed in, not hardcoded
    parser.add_argument('--input2', type=str, help='input2 value')  # Paths should be passed in, not hardcoded
    parser.add_argument('--output1', type=str, help='output1 dir')  # Paths should be passed in, not hardcoded
    args = parser.parse_args()
    Path(args.output1).parent.mkdir(parents=True, exist_ok=True)
    do_work(args.input1, args.input2, args.output1)


