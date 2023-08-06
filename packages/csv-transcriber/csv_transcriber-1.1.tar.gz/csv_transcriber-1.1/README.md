# CSV-Transcriber
Breaks down a CSV file into text files containing the contents of each row.

## Installation
You can use PIP to install the package. Type the following command into your terminal to install the package.
```bash
pip install csv_transcriber
```

## Usage
The package contains a transcribe function, which takes in the path to a CSV file, and an output to a directory. A typical use of the function is as follows:

```bash
import csv_transcriber

csv_transcriber.transcribe('./data.csv', './users/')
```

## License
A short snippet describing the license (MIT, Apache etc)

MIT © Jad Khalili 2019.
