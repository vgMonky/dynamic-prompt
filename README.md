# Dynamic Prompt

Dynamic Prompt is a tool that uses categories lists (e.g. animals = [dog,lion , fox] ) to generate dynamic prompts based on thoes categories. It allows users to create, modify, and delete categories, as well as generate prompts using these categories.

Example usage:

```

python main.py -p "portrait of a {{animals}}, black and white, with {{colours}} eyes"

```

This command might generate a prompt like "portrait of a lion, black and white, with green eyes" based on the items in the "animals" and "colours" categories.

## Features

- Manage category lists (create, append, remove, delete)
- List available categories and their items
- Generate dynamic prompts using category placeholders

## Installation

[Add installation instructions here]

## Usage

```
python main.py [OPTIONS]
```

### Options:

- `-h, --help`: Show the help message and exit
- `-l [CATEGORY], --list [CATEGORY]`: List all categories, or list items if CATEGORY is specified
- `-n CATEGORY, --new CATEGORY`: Create a new category
- `-a CATEGORY ITEM, --append CATEGORY ITEM`: Append an item to an existing category
- `-rm CATEGORY ITEM, --remove CATEGORY ITEM`: Remove an item from a category
- `-d CATEGORY, --delete CATEGORY`: Delete a category
- `-p PROMPT, --prompt PROMPT`: Generate a dynamic prompt with {{category_name}} placeholders

### Examples:

1. List all categories:
   ```
   python main.py -l
   ```

2. List items in a specific category:
   ```
   python main.py -l animals
   ```

3. Create a new category:
   ```
   python main.py -n vehicles
   ```

4. Add an item to a category:
   ```
   python main.py -a animals lion
   ```

5. Remove an item from a category:
   ```
   python main.py -rm animals lion
   ```

6. Delete a category:
   ```
   python main.py -d vehicles
   ```

7. Generate a prompt:
   ```
   python main.py -p "A {{animals}} riding a {{vehicles}} under a {{weather}} sky"
   ```

## Configuration

The `config.json` file in the `dynamic-prompt` directory contains the following configuration:

```json
{
  "CURRENT_CATEGORIES_FILE": "categories/1.json"
}
```

You can modify this file to change the current categories file used by the tool.

## Components

### 1. Category Manager (category_manager.py)

Handles all operations related to category management, including:
- Creating and deleting categories
- Adding and removing items from categories
- Retrieving category information

### 2. Prompt Manager (prompt_manager.py)

Manages prompt generation, including:
- Processing prompts with category placeholders
- Replacing placeholders with random items from the specified categories

### 3. Main Script (main.py)

Implements the command-line interface and coordinates between the Category Manager and Prompt Manager.

## Contributing

[Add contribution guidelines here]

## License

[Add license information here]
