if command -v pipenv 2>/dev/null; then
    pipenv run python runExperiment.py
else
    echo "install pipenv before using: pip install pipenv"
fi