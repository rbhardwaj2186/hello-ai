from rich.console import Console
from rich.table import Table
import platform, sys, os, shutil

def main() -> None:
    console = Console()
    table = Table(title="Marine-AI System Check")
    table.add_column("Item", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Python", sys.version.split()[0])
    table.add_row("Machine", platform.machine())
    table.add_row("CPU cores", str(os.cpu_count()))
    table.add_row("Windows version", platform.version())

    disk = shutil.disk_usage("D:\\")
    free_gb = disk.free / 1024**3
    table.add_row("D: free space", f"{free_gb:.0f} GB")

    console.print(table)