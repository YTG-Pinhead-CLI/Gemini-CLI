import os
import subprocess
import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich.live import Live
from rich.text import Text
from rich import box

console = Console()

def run(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, stderr=subprocess.DEVNULL).decode().strip()
    except:
        return ""

def get_git_info():
    branch = run("git branch --show-current") or "N/A"
    status = run("git status --short")
    last_commit = run("git log -n 1 --pretty=format:'%h %an %s'") or "No commits"
    
    staged = len([line for line in status.split('\n') if line.startswith(('A', 'M', 'D'))])
    unstaged = len([line for line in status.split('\n') if line.startswith(' ') and not line.startswith('??')])
    untracked = len([line for line in status.split('\n') if line.startswith('??')])
    
    return {
        "branch": branch,
        "last_commit": last_commit,
        "staged": staged,
        "unstaged": unstaged,
        "untracked": untracked
    }

def get_project_stats():
    todos = run("grep -rE 'TOD[O]|FIXM[E]' . --exclude-dir=node_modules --exclude-dir=.git --exclude-dir=lib --exclude='*.html' | wc -l")
    files = run("find . -maxdepth 2 -not -path '*/.*' | wc -l")
    return {
        "todos": todos,
        "files": files
    }

def make_layout():
    layout = Layout()
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="main"),
        Layout(name="footer", size=3)
    )
    layout["main"].split_row(
        Layout(name="left"),
        Layout(name="right")
    )
    return layout

def generate_dashboard():
    git = get_git_info()
    stats = get_project_stats()
    
    # Header
    header_text = Text(f"GEMINI CLI MISSION CONTROL - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", style="bold cyan")
    header_panel = Panel(header_text, box=box.DOUBLE_EDGE, border_style="bright_blue")
    
    # Left: Git
    git_table = Table(show_header=False, box=None)
    git_table.add_row("Branch", f"[bold green]{git['branch']}[/bold green]")
    git_table.add_row("Last Commit", f"[dim]{git['last_commit']}[/dim]")
    git_table.add_row("Staged", f"[bold cyan]{git['staged']}[/bold cyan]")
    git_table.add_row("Unstaged", f"[bold yellow]{git['unstaged']}[/bold yellow]")
    git_table.add_row("Untracked", f"[bold red]{git['untracked']}[/bold red]")
    git_panel = Panel(git_table, title="[bold]GIT STATUS[/bold]", border_style="green")
    
    # Right: Project
    proj_table = Table(show_header=False, box=None)
    proj_table.add_row("Total Files", f"[bold white]{stats['files']}[/bold white]")
    proj_table.add_row("TOD[O]/FIXM[E]", f"[bold magenta]{stats['todos']}[/bold magenta]")
    proj_table.add_row("Environment", "[bold blue]Codespaces[/bold blue]")
    proj_table.add_row("Health", "[bold reverse green] EXCELLENT [/bold reverse green]")
    proj_panel = Panel(proj_table, title="[bold]PROJECT STATS[/bold]", border_style="magenta")
    
    # Footer
    footer_text = Text("STATUS: READY | MODE: YOLO | USER: YTG-pinhead", style="bold white")
    footer_panel = Panel(footer_text, box=box.DOUBLE_EDGE, border_style="bright_blue")
    
    layout = make_layout()
    layout["header"].update(header_panel)
    layout["left"].update(git_panel)
    layout["right"].update(proj_panel)
    layout["footer"].update(footer_panel)
    
    return layout

if __name__ == "__main__":
    console.print(generate_dashboard())
