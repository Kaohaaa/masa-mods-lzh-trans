# I’ll confess frankly: this code was written by AI because I'm not really good at it...
# You know, I just care about the translation of this resoursepack project:)

import os
import sys
import zipfile
import json
import datetime

def load_params():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    params_path = os.path.join(script_dir, 'params.json')
    with open(params_path, 'r', encoding='utf-8') as f:
        return json.load(f), script_dir

def package(dirname):
    params, script_dir = load_params()
    output_name_tpl = params.get('output_name', '{type}{version}.zip')
    output_dir = params.get('output_dir', '.')
    if not os.path.isabs(output_dir):
        output_dir = os.path.normpath(os.path.join(script_dir, output_dir))
    os.makedirs(output_dir, exist_ok=True)

    params_for_format = dict(params)
    params_for_format['timestamp'] = datetime.datetime.now().strftime('%Y%m%d%H%M')

    try:
        output_name = output_name_tpl.format(**params_for_format)
    except Exception:
        output_name = f"{params.get('type','')}{params.get('version','')}_{params_for_format['timestamp']}.zip"

    output_path = os.path.join(output_dir, output_name)

    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(dirname):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, start=dirname)
                zf.write(file_path, arcname)

    print(f"Created: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python package.py <directory-to-package>")
        sys.exit(2)

    dirname = sys.argv[1]
    if not os.path.isdir(dirname):
        print(f"Error: {dirname} is not a valid directory.")
        sys.exit(1)

    package(dirname)