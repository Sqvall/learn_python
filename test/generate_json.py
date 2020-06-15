from pathlib import Path

p = Path('.')
result_folder = p.joinpath('generate_json_input')
result_folder.mkdir()

input_file = p.joinpath('./generate_json_input.json')
input_text = input_file.read_text()

for i in range(0, 10):
    file = result_folder.joinpath(f'file_{i}.json')
    file.write_text(input_text)
