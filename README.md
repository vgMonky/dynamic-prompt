# Dynamic Prompt

Dynamic Prompt is a tool that uses category lists (e.g., animals = [dog, lion, fox]) to generate dynamic prompts. It allows users to create, modify, and delete categories, as well as generate prompts using these categories.

Example usage:
```
dynamic-prompt -p "portrait of a {{animals}}, black and white, with {{colours}} eyes"
```
This command might generate a prompt like "portrait of a lion, black and white, with green eyes" based on the items in the "animals" and "colours" categories.

## Features

- Manage category lists (create, append, remove, delete)
- List available categories and their items
- Generate dynamic prompts using category placeholders

## Installation

### Using Nix

If you have Nix installed, you can use the provided `shell.nix` file to set up the environment:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/dynamic-prompt.git
   cd dynamic-prompt
   ```

2. Enter the Nix shell:
   ```
   nix-shell
   ```

This will create a virtual environment, activate it, and install the `dynamic-prompt` package in editable mode.

### Manual Installation

If you don't use Nix, you can install the package manually:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/dynamic-prompt.git
   cd dynamic-prompt
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the package in editable mode:
   ```
   pip install -e .
   ```

## Usage

After installation, you can use the `dynamic-prompt` :nd it will show help and options.

```
dynamic-prompt 
```


### Examples:

1. List all categories:
   ```
   dynamic-prompt -l
   ```

2. List items in a specific category:
   ```
   dynamic-prompt -l animals
   ```

3. Create a new category:
   ```
   dynamic-prompt -n vehicles
   ```

4. Add items to a category:
   ```
   dynamic-prompt -a animals lion tiger "bengal cat"
   ```

5. Remove items from a category:
   ```
   dynamic-prompt -rm animals lion tiger
   ```

6. Delete a category:
   ```
   dynamic-prompt -d vehicles
   ```

7. Generate a prompt:
   ```
   dynamic-prompt -p "A {{animals}} riding a {{vehicles}} under a {{weather}} sky"
   ```

## Configuration

The `config.json` file in the `dynamic_prompt` directory contains the following configuration:

```json
{
  "CURRENT_CATEGORIES_FILE": "categories/1.json"
}
```

You can modify this file to change the current categories file used by the tool.

## Components

### 1. Category Manager (category_manager.py)
Handles all operations related to category management.

### 2. Prompt Manager (prompt_manager.py)
Manages prompt generation.

### 3. Main Script (main.py)
Implements the command-line interface and coordinates between the Category Manager and Prompt Manager.

## Contributing

[Add contribution guidelines here]

## License

[Add license information here]
