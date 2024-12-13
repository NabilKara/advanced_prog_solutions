from rich.console import Console
console = Console()
word = input("Type some strings :  [press enter to exit]: ")
while(word != ""):
    console.print(f"[underline]{word}[/underline]")
    word = input()
    


