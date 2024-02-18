import sys

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage 1: python curly.py input.txt")
        print("Usage 2: python curly.py input.txt output.txt")
        sys.exit(1)

    if len(sys.argv) == 3:
        make_curly(sys.argv[1], sys.argv[2])
    else:
        make_curly(sys.argv[1], 'output.txt')

def make_curly(input_file_path, output_file_path):

    # Read input file's content and make a list of modified chars
    with open(input_file_path, 'r', encoding='utf-8') as input:
        content = input.read()
        text = []

        quotes = {'"': ('“', '”'), "'": ('‘', '’')}
        expect_open = True
        exceptions = (' ','\n','—')
        
        for char in content:

            # Replace quotes
            if char in quotes:
                if expect_open:
                    text.append(quotes[char][0])
                else:
                    text.append(quotes[char][1])
                expect_open = False
            
            # Keep chars that aren't quotes
            else:
                text.append(char)
                if char in exceptions:
                    expect_open = True
                else:
                    expect_open = False

        new_content = ''.join(text)
    
    with open(output_file_path, 'w', encoding='utf-8') as output:
        output.write(new_content)

if __name__ == "__main__":
    main()