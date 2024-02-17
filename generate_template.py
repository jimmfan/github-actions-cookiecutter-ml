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
    # Use a general 'projects' directory to hold all generated projects
    base_output_path = os.path.join(os.getcwd(), "generated-projects")
    os.makedirs(base_output_path, exist_ok=True)  # Ensure the base directory exists

    # Include the timestamp in the project's directory name to avoid conflicts
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    final_project_name = f"{project_name}_{timestamp}"
    output_path = os.path.join(base_output_path, final_project_name)
    print(f"Final output path for project: {output_path}")

    # No need to manually remove the directory as we're ensuring unique names with timestamp
    cookiecutter(
        TEMPLATE_PATH,
        no_input=True,
        extra_context={
            'project_name': project_name,
            'author': author,
            'email': email,
            'python_version': python_version
        },
        output_dir=base_output_path  # Specify the base directory for projects
    )

    click.echo(f'Project {final_project_name} created successfully in {output_path}.')

if __name__ == '__main__':
    create_project()
