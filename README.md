# Curly quotes

A program that converts straight quotes to curly quotes. I use this to convert quick notes taken on my phone to more professional-looking, typographically correct text for documents or emails.

## Usage

1. Navigate to the directory from command line: `cd .../curly-quotes`
2. Save a text file in the `curly-quotes` directory to give as input to the program
2. Run the program:
    - `python curly.py input.txt` reads the specified text file and writes a file called “output.txt” in the same directory as the program
    - `python curly.py input.txt output.txt` instead writes a file with the name given as the final argument

## Updates

Most recent change(s):
- Added a tuple for the exception to expect open quotes if the previous char is a space, newline, or em dash
- Used map from straight to curly quotes
- Updated file name to `curly.py` as distinct from the `make_curly` method
- Updated comments