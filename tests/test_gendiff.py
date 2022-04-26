from pathlib import Path
from gendiff import generate_diff


def test_generate_diff():
    get_path = Path('tests/fixtures', 'generate_diff.txt').resolve()
    with open(get_path) as data_str:
        result_str = data_str.read()

    assert generate_diff('file1.json', 'file2.json') == result_str
