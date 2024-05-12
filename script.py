import re

def main():
  file_path = "src/tactics.md"

  pattern = r'syntax "(.*?)".*?\[(.*)\]'

  replacement = r"# \1\nDefined in: `\2`\n"

  with open(file_path, 'r', encoding='utf-8') as file:
    # delete leading spaces
    content = "".join([re.sub(r'^\s\s', '', line) for line in file])

  # create markdown-style headers
  new_content = re.sub(pattern, replacement, content)

  # replace mere code blocks with lean code blocks
  new_content = re.sub(r'(^|.*:|[a-zA-Z]+\.)\n```\n', r'\1\n```lean\n', new_content)

  content_with_version = 'Lean version: `{{#include ../lean-toolchain}}`\n\n' + new_content

  with open(file_path, 'w', encoding='utf-8') as file:
    file.write(content_with_version)

if __name__ == '__main__':
  main()
