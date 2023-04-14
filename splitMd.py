import os

# Specify the input and output directories
input_dir = '<input_directory_path>'
output_dir = '<output_directory_path>'

# Open the input file and read its contents
with open(os.path.join(input_dir, '<input_file_name>'), 'r', encoding='utf-8') as f:
    contents = f.readlines()

# Loop through each line in the input file
for i, line in enumerate(contents):
    # Create a new file for each line
    filename = f'{i}.md'
    filepath = os.path.join(output_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(line)

