from app import factory
from pathlib import Path
from dotenv import load_dotenv
from os import environ as env

load_dotenv()

if __name__ == '__main__':
    # list of all files in the project, so flask knows where to look for changes
    extra_files = [str(p.resolve()) for p in Path('./').glob('**/*')]
    factory.app.run(extra_files=extra_files, debug=bool(env.get("debug", False)))
