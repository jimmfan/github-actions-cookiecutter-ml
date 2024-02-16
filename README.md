### USAGE
name: Cookiecutter Template

on:
  workflow_dispatch:

steps:
- name: Checkout repo
  uses: actions/checkout@v2

- name: Create Cookiecutter Template
  uses: jimmfan/github-actions-cookiecuttter-ml@main
  with:
    project_name: 'My Project'
    author: jimmfan
    email: jimmfan@github.com
    python_version: '3.10'

### Requirements
TODO