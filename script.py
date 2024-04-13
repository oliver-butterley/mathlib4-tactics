import re

def main():
  file_path = "tactics.md"

  pattern = r'syntax "(.*?)".*?\[(.*)\]'

  replacement = r"# \1\nDefined in: `\2`\n"

  with open(file_path, 'r', encoding='utf-8') as file:
    content = "".join([re.sub(r'^\s\s', '', line) for line in file])

  new_content = re.sub(pattern, replacement, content)

  with open(file_path, 'w', encoding='utf-8') as file:
    file.write(new_content)

if __name__ == '__main__':
  main()