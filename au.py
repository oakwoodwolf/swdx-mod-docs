# Script to generate markdown table from filenames and descriptions
def generate_markdown_table(filename):
    try:
        # Read the file content
        with open(filename, 'r') as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        # Check if the number of lines is even (each filename should have a description)
        if len(lines) % 2 != 0:
            raise ValueError("The file should have an even number of lines (filename followed by description).")

        # Start the markdown table
        markdown = "| Filename          | Description                      |\n"
        markdown += "|-------------------|----------------------------------|\n"

        # Pair each filename with its description
        for i in range(0, len(lines), 2):
            filename = lines[i]
            description = lines[i + 1]
            markdown += f"| {filename:<17} | {description:<32} |\n"

        # Write the markdown output to a file
        with open('output.md', 'w') as output_file:
            output_file.write(markdown)

        print("Markdown table generated successfully in 'output.md'.")

    except Exception as e:
        print(f"Error: {e}")

# Run the function with your filenames and descriptions file
generate_markdown_table('filenames_and_descriptions.txt')
