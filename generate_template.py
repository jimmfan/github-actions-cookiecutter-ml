import click
import os
import shutil
from cookiecutter.main import cookiecutter
import datetime

def remove_if_exists(path):
    if os.path.exists(path) and os.path.isdir(path):
        print(f"Removing existing directory: {path}")
        shutil.rmtree(path)
    else:
        print(f"Directory does not exist, no need to remove: {path}")

TEMPLATE_PATH = 'ml-project-template'

@click.command()
@click.option('--project_name', prompt='Project Name', default='ml_project', help='Project Name, used as the project directory name.')
@click.option('--author', prompt='Author name', default='jimmfan', help='The name of the project author.')
@click.option('--email', prompt='Author email', default='jimmfan@github.com', help='The email of the project author.')
@click.option('--python_version', prompt='Python version', default='3.10', help='The Python version to use for the project.')

def create_project(project_name, author, email, python_version):
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    output_path = os.path.join(os.getcwd(), f"{project_name}_{timestamp}")
    print(f"Output path for project: {output_path}")
    
    remove_if_exists(output_path)  # Ensure the directory is removed before creating a new project

    cookiecutter(
        TEMPLATE_PATH,
        no_input=True,
        extra_context={
            'project_name': project_name,
            'author': author,
            'email': email,
            'python_version': python_version
        },
        output_dir=os.path.dirname(output_path)  # Set the output directory just above the project directory to avoid conflicts
    )

    click.echo(f'Project {project_name} created successfully in {output_path}.')

if __name__ == '__main__':
    create_project()
