import click
from cookiecutter.main import cookiecutter


# Define the path to your cookiecutter template
@click.command()
@click.option(
    "--template_path",
    prompt="Template Path",
    default="template1",
    help="Path to your cookiecutter template.",
)
@click.option(
    "--project_name",
    prompt="Project Name",
    default="ml_project",
    help="Project directory name.",
)
@click.option(
    "--author",
    prompt="Author name",
    default="jimmfan",
    help="The name of the project author.",
)
@click.option(
    "--email",
    prompt="Author email",
    default="jimmfan@github.com",
    help="The email of the project author.",
)
@click.option(
    "--python_version",
    prompt="Python version",
    default="3.10",
    help="The Python version to use for the project.",
)
@click.option(
    "--output_dir",
    prompt="Output directory",
    default="../",
    help="Output directory to where to create the template.",
)
def create_project(
    template_path, 
    project_name, 
    author, email, 
    python_version, 
    output_dir
):
    print(f"Using template path: {template_path}")
    
    # Call cookiecutter to create the project using the collected inputs
    cookiecutter(
        template_path,
        output_dir=output_dir,
        no_input=True,
        extra_context={
            "project_name": project_name,
            "author": author,
            "email": email,
            "python_version": python_version
            # Add other variables to pass to cookiecutter here
        },
        overwrite_if_exists=True,
    )

    click.echo(f"Template created successfully.")


if __name__ == "__main__":
    create_project()
