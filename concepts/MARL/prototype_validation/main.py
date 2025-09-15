#!/usr/bin/env python3

import sys
from core.command_handler import CommandHandler

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python main.py validate <file_path>")
        print("  python main.py benchmark")
        print("  python main.py stats")
        print("  echo 'code' | python main.py validate -")
        return
    
    handler = CommandHandler()
    handler.execute(sys.argv[1:])

if __name__ == "__main__":
    main()