#!/usr/bin/env python3
"""Тестовая программа для сборки EXE"""

def main():
    print("=" * 50)
    print("🎉 Привет от GitHub Actions!")
    print("=" * 50)
    print("\nЭта программа собрана автоматически через:")
    print("  • Python 3.11")
    print("  • PyInstaller")
    print("  • GitHub Actions (Windows runner)")
    print("\nСобрано: $(date)")
    print("=" * 50)
    
    input("\nНажмите Enter для выхода...")

if __name__ == "__main__":
    main()
