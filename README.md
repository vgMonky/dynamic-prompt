# dynamic-prompt

dynamic-prompt is a command-line tool for generating dynamic prompts using category lists as variables. It allows users to create and manage categories, then use them to generate dynamic prompts.

Example usage:
```
dynamic-prompt -p "portrait of a {animals}, black and white, with {colours} eyes"
```
This command might generate a prompt like "portrait of a lion, black and white, with green eyes" based on the items in the "animals" and "colours" categories.

## Project Structure

```
dynamic-prompt/
├── dynamic-prompt/
│   ├── categories/
│   │   ├── 1.json
│   │   └── 2.json
│   ├── main.py
│   ├── category_manager.py
│   ├── prompt_manager.py
│   └── config.py
├── README.md
└── shell.nix
```

## Features

- Generate dynamic prompts using category lists as variables
- Manage category lists (create, append, remove items, delete)
- List available categories and their items
- Generate prompts with random categories

## Components

### 1. Categories Storage

Categories are stored in JSON files within the `dynamic-prompt/categories/` directory. Each file (e.g., `1.json`) can contain multiple category lists. The structure of a category file is as follows:

```json
{
  "animals": ["dog", "cat", "lion", "elephant"],
  "colours": ["red", "blue", "green", "purple"],
  "styles": ["impressionist", "cubist", "surrealist"]
}
```

### 2. category_manager.py

This module handles all operations related to category management. It includes the following functions:

- `create_category(category_name)`
- `append_items(category_name, items)`
- `remove_items(category_name, items)`
- `delete_category(category_name)`
- `get_random_item(category_name)`
- `get_random_category()`
- `list_categories()`
- `list_items(category_name)`
- `get_category(category_name)`

### 3. prompt_manager.py

This module handles prompt generation. It includes the following functions:

- `dynamic_prompt(prompt_template)`
  - Example: `dynamic_prompt("portrait of a {animals}, black and white, with {colours} eyes")`
- `dynamic_prompt_random(n)`
  - Generates a prompt with `n` random categories
  - Example: If n is 3, it might generate `"{animals}, {colours}, {styles}"`

Both functions will include error handling for cases where specified categories don't exist.

### 4. config.json

This module will define some variables. For example:

```json
{
  "USE_CATEGORIES_FROM": ["categories/1.json", "categories/2.json"],
  "SAVE_CATEGORIES_TO": "categories/2.json"
}
```

All other scripts will use this configuration to determine which categories file to use and where to save when creating categories.

### 5. main.py

The main script that implements the command-line interface:

```
python dynamic-prompt.py [OPTIONS]

Options:
  -h, --help                Show this help message and exit
  -p, --prompt PROMPT       Define a dynamic prompt with {category_name} variables
  -r [N], --random [N]      Generate a dynamic prompt with N random {category_name} variables
  -l, --list [CATEGORY]     List available categories, or list items if CATEGORY is specified
  -n, --new CATEGORY        Create a new category list
  -a, --append CATEGORY     Append item(s) to an existing category
  -rm, --remove CATEGORY         Remove item(s) from a category
  -d, --delete CATEGORY     Delete a category list
```

## Future Considerations

1. File I/O and Caching: Consider implementing a caching mechanism to optimize file read/write operations.

2. Data Validation: Implement validation for category names and item content (e.g., disallowing empty strings or duplicates).

## Installation

[Add installation instructions here]

## Contributing

[Add contribution guidelines here]

## License

[Add license information here]
