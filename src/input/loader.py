import pandas as pd
from pathlib import Path
from rich.markdown import Markdown
from rich.console import Console
from rich.table import Table

console = Console(force_terminal=True)

loaders = {
    'csv': pd.read_csv,
    'xlsx': pd.read_excel,
}

path = Path("data")

def select_file(path):
    files = list(path.iterdir())
    filtered_files = []
    
    for file in files:
        if ".csv" in file.suffix or ".xlsx" in file.suffix:
            filtered_files.append(file)

    table = Table(title="Available Files")
    table.add_column("ID", style="magenta", justify="left")
    table.add_column("File Name", style="cyan", justify="right")
    
    for i, file in enumerate(filtered_files):
        table.add_row(str(i), file.name)
    
    console.print(table)
    
    
    while True:
        file_choice = console.input("[bold green]Enter the ID or file name of the file you want to load\n>[/bold green] ")
        if file_choice.isdigit():
            try:
                file_choice = int(file_choice)
                return filtered_files[file_choice]
            except (IndexError, ValueError):
                console.print("[bold red]Invalid ID. Please try again.[/bold red]")
        else:        
            for file in filtered_files:
                if file.name == file_choice:
                    return file
    
        console.print("[bold red]Invalid choice. Please try again.[/bold red]")
    
def load_file(file):
    extension = file.suffix.lstrip(".").lower()
    
    if extension in loaders:
        loader = loaders[extension]
        df = loader(file)
        return df
    
    raise ValueError(f"Unsupported file type: {extension}")
    