import click

@click.command()
@click.argument('name')
def main(name):
    click.echo("{}".format(name))

if __name__ == "__main__":
    main()