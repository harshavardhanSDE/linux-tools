from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from rich.console import Console

console = Console()

def main():
    languages = ['Python', 'JavaScript', 'Java', 'C++']
    completer = WordCompleter(languages)
    name = prompt("What is your name? ")
    language = prompt("What is your favorite programming language? ", completer=completer)
    console.print(f"Hello, [bold green]{name}[/bold green]! Your favorite programming language is [bold blue]{language}[/bold blue].")

if __name__ == '__main__':
    main()
