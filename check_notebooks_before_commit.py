import nbformat
import shutil
import os 
import pathlib

def check_if_notebook_has_no_outputs(nb_path):
    has_no_output = all([cell['outputs'] == [] for cell in nbformat.read(nb_path, nbformat.NO_CONVERT)['cells'] if 'outputs' in cell])
    if not has_no_output:
        print(str(nb_path) + ' has cells with outputs')
    return has_no_output

if __name__== '__main__':
    path = pathlib.Path('./.git/hooks/pre-commit')
    if not path.exists():
        shutil.copy('./git_hooks/pre-commit', path)


    all_notebooks_have_no_output = all([check_if_notebook_has_no_outputs(str(path)) for path in pathlib.Path('./').glob('*.ipynb')])

    if all_notebooks_have_no_output:
        exit(0)
    else:
        exit(-1)