
import time

import typer


app = typer.Typer()


def main(delete : bool = typer.Option(False, help="Supprimer les fichier."),
         extension : str = typer.Argument("txt", help="Extension à chercher.")):
    """"" Afficher les fichiers trouvés avec l'extension données """

#    typer.echo(f"Recherche des fichiers avec l'extension {extension}.")
    #extension = typer.prompt("Quelle extension souhaitez-vous chercher? ")
    #print(extension)
    #if delete:
     #   do_delete = typer.confirm("Souhaitez-vous vraiment les supprimés ?")
      #  if not do_delete:
       #     typer.echo("On annule l'opération.")
        #    raise typer.Abort()

    #print("Suppressions des fichiers")


    #typer.echo(f"Recherche des fichiers avec l'extension {extension}.")
    #if delete:
    #    typer.echo("Suppressions des fichiers.")

#@app.command("search")
#def search_py():
 #   main(delete=False, extension="py")

#@app.command("delete")
#def delete_py():
 #   main(delete=True, extension="py")

    #prenom = typer.style("Bonjour", bg=typer.colors.RED)
    #typer.echo(f"{prenom} Cedric.")


    prenoms = range(100)
    with typer.progressbar(prenoms) as progress:
        for prenom in progress:
            time.sleep(0.5)

        print("c'est bon")
            
if __name__ == "__main__":
    typer.run(main)
#typer.run(main)
