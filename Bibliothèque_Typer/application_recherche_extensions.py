"""Application permetant de recherche ou de supprimer un fichier à travers son extension"""
from pathlib import Path
import time
import typer
from typing import Optional


app = typer.Typer()

@app.command("run")
def main(extension:str,
         directory: Optional[Path] = typer.Argument(None,help="Dossier dans lequel chercher."),
         delete: bool = typer.Option(False,help="Supprime les fichiers trouvés.")):


    if directory:
        directory = directory
    else:
        directory = Path.cwd()

    if not directory.exists():
        typer.secho(f"Le dossier {directory} n'existe pas.", fg=typer.colors.RED)
        raise typer.Exit()
    
    files = directory.rglob(f"*.{extension}")

    if delete:
        typer.confirm("Voulez-vous vraiment supprimer tous les fichiers trouvés ?", abort=True)
        for file in files:
            file.unlink()
            typer.secho(f"Suppression du fichier {file}.", fg=typer.colors.RED)
    else:
        typer.secho(f"Fichiers trouvés avec l'extension {extension} : " , fg=typer.colors.BLUE, bg=typer.colors.BLUE)
        with typer.progressbar(files) as progress:
            for file in progress:
                time.sleep(0.5)
                typer.echo(file)
    
@app.command("delete")
def delete_py(extension:str):
    """Commande pour supprimer les fichiers avec l'extension données."""
    main(delete=True, extension=extension, directory=None)  

@app.command("search")
def search_py(extension:str):
    """Commande pour rechercher les fichiers avec l'extension données."""
    main(delete=False, extension = extension, directory=None)        



if __name__ == "__main__":
    app()

    #typer.run(main)
    