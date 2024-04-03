import subprocess
import os
import tqdm

def text_to_phonemes(language='fr', input_folder='part1_txt', output_file='phonemes_fr.txt'):
    results = []

    # Loop through all files in part1_txt
    # Sort all files in order
    for file in tqdm.tqdm(sorted(os.listdir(input_folder)), desc='Files', unit='file'):
        # Open the output file
        with open(input_folder+f"/{file}", 'r') as filetje:
            line = filetje.readlines()[0]

        # Command to generate phoneme data using espeak-ng, including amplitude and speed adjustments
        command = ['espeak', '-q', '-v', language, '--ipa', line]

        # Call espeak-ng and redirect the output to the file
        result = subprocess.run(command, capture_output=True, text=True)

        # Get rid of the newline character at the end of the output and in between the phonemes
        result.stdout = result.stdout.replace('\n', ' ')
        result.stdout = result.stdout.strip()

        new_result = file.replace('txt', 'wav') + '|' + result.stdout + '|0'

        results.append(new_result)

    results.append("")

    # Write the results to the output file
    with open(output_file, 'w') as file:
        file.write('\n'.join(results))

    return results

text_to_phonemes()