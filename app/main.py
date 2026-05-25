import asyncio

from rich.console import Console

from app.agent import run_audit

console = Console()


def load_input() -> str:
    console.print("[bold cyan]Ecommerce Conversion Agent[/bold cyan]")
    console.print("Paste your ecommerce HTML, structure or UX description.")
    console.print("Press ENTER twice to run the audit.\n")

    lines = []

    while True:
        line = input()

        if line == "":
            break

        lines.append(line)

    return "\n".join(lines)


async def main():
    user_input = load_input()

    if not user_input.strip():
        console.print("[red]No input detected.[/red]")
        return

    console.print("\n[bold yellow]Running ecommerce audit...[/bold yellow]\n")

    audit = await run_audit(user_input)

    console.print(audit)

    with open("outputs/audit_output.md", "w", encoding="utf-8") as file:
        file.write(audit)

    console.print("\n[green]Audit saved to outputs/audit_output.md[/green]")


if __name__ == "__main__":
    asyncio.run(main())
