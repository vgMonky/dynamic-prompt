import argparse
import sys
import json
from category_manager import CategoryManager
from prompt_manager import PromptManager

def load_config():
    with open('config.json', 'r') as f:
        return json.load(f)

def main():
    config = load_config()
    category_file = config['CURRENT_CATEGORIES_FILE']
    category_manager = CategoryManager(category_file)
    prompt_manager = PromptManager(category_manager)

    parser = argparse.ArgumentParser(
        description='''
Dynamic Prompt is a powerful tool for managing categories list and generating dynamic prompts based on thoes categories.
It allows you to create, modify, and delete categories, as well as generate prompts using these categories.

Usage examples:
  - List all categories:
    python main.py -l
  - List items in a specific category:
    python main.py -l animals
  - Create a new category:
    python main.py -n vehicles
  - Add an item to a category:
    python main.py -a animals lion
  - Remove an item from a category:
    python main.py -rm animals lion
  - Delete a category:
    python main.py -d vehicles
  - Generate a prompt:
    python main.py -p "A {{animals}} riding a {{vehicles}} under a {{weather}} sky"
        ''',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('-l', '--list', nargs='?', const=True, metavar='CATEGORY',
                        help='List all categories, or list items if CATEGORY is specified')
    parser.add_argument('-n', '--new', metavar='CATEGORY',
                        help='Create a new category')
    parser.add_argument('-a', '--append', nargs=2, metavar=('CATEGORY', 'ITEM'),
                        help='Append an item to an existing category')
    parser.add_argument('-rm', '--remove', nargs=2, metavar=('CATEGORY', 'ITEM'),
                        help='Remove an item from a category')
    parser.add_argument('-d', '--delete', metavar='CATEGORY',
                        help='Delete a category')
    parser.add_argument('-p', '--prompt', metavar='PROMPT',
                        help='Generate a dynamic prompt with {{category_name}} placeholders')

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    if args.list is not None:
        if args.list is True:
            categories = category_manager.get_all_categories()
            print("Available categories:", ', '.join(categories))
        else:
            items = category_manager.get_category(args.list)
            print(f"Items in category '{args.list}':", ', '.join(items))

    elif args.new:
        if category_manager.create_category(args.new):
            print(f"Category '{args.new}' created successfully.")
        else:
            print(f"Category '{args.new}' already exists.")

    elif args.append:
        category, item = args.append
        try:
            if category_manager.add_item(category, item):
                print(f"Item '{item}' added to category '{category}'.")
            else:
                print(f"Failed to add item. Category '{category}' might not exist.")
        except ValueError as e:
            print(str(e))

    elif args.remove:
        category, item = args.remove
        if category_manager.remove_item(category, item):
            print(f"Item '{item}' removed from category '{category}'.")
        else:
            print(f"Failed to remove item. Category '{category}' or item '{item}' might not exist.")

    elif args.delete:
        if category_manager.delete_category(args.delete):
            print(f"Category '{args.delete}' deleted successfully.")
        else:
            print(f"Failed to delete category. Category '{args.delete}' might not exist.")

    elif args.prompt:
        processed_prompt = prompt_manager.process_template_prompt(args.prompt)
        print("Processed prompt:", processed_prompt)

if __name__ == "__main__":
    main()
