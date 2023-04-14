# Split Markdown Script

This script splits a Markdown file into separate files, with each file containing one line from the original file. This can be useful for breaking up long Markdown documents into smaller, more manageable files.

## Usage

1. Clone this repository to your local machine.
2. Open the `splitMd.py` file in a text editor.
3. Edit the `input_dir` and `output_dir` variables to specify the input and output directories, respectively. Note that the output directory must already exist.
4. Save the `splitMd.py` file.
5. In a terminal window, navigate to the directory containing the `splitMd.py` file.
6. Run the script by typing `python splitMd.py` and pressing Enter.

The script will read the input Markdown file and create a separate file for each line in the file. Each output file will be named with the format `<line_number>.md`, where `<line_number>` is the line number in the input file (starting from 0).

## License

This script is released under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use and modify it for your own purposes.
