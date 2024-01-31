import sys

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage 1: python make_curly.py input.txt")
        print("Usage 2: python make_curly.py input.txt output.txt")
        sys.exit(1)

    if len(sys.argv) == 3:
        make_curly(sys.argv[1], sys.argv[2])
    else:
        make_curly(sys.argv[1], 'output.txt')

def make_curly(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input:
        content = input.read() # original content of input file
        text = []              # modified chars
        expect_open = True     # use open curly quotes

        for char in content:
            if char == '"': # replace double quotes
                if expect_open:
                    text.append('“')
                else:
                    text.append('”')
                expect_open = False
            elif char == "'": # replace single quotes
                if expect_open:
                    text.append('‘')
                else:
                    text.append('’')
                expect_open = False
            else:
                text.append(char) # add other text
                if char == ' ' or char == '\n':
                    expect_open = True
                else:
                    expect_open = False

        new_content = ''.join(text) # modified string
    
    with open(output_file_path, 'w') as output:
        output.write(new_content)

if __name__ == "__main__":
    main()