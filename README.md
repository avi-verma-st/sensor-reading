# Sensor Reading

Extract English text from an image using PaddleOCR. The script prints each detected text segment and its recognition confidence score to the terminal. It does not yet parse readings into structured sensor values or save results to a file.

## Prerequisites

- Python 3.10. The existing development environment uses Python 3.10.5; other Python versions have not been verified.
- Git, if you are cloning the repository.
- Internet access to install dependencies and download OCR models on the first run.

The commands below are for Windows PowerShell. Run them from the project folder.

## Get the Project

Clone the repository using its actual URL, then open the folder:

```powershell
git clone <repository-url>
cd sensor-reading
```

Replace `<repository-url>` with the repository's clone URL. If the project is already on your computer, open its folder in VS Code and select **Terminal > New Terminal** instead.

## First-Time Setup

Create your own virtual environment and install the dependencies:

```powershell
py -3.10 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

The virtual environment keeps this project's packages separate from other projects. Each person creates their own `.venv`; it is not shared through Git. Installation may take a while because OCR depends on machine-learning and image-processing packages.

## Run the Script

Make sure `test2.jpg` is in the project folder, then run:

```powershell
.\.venv\Scripts\python.exe main.py
```

This uses the virtual environment directly, so activation is not required. PaddleOCR may download models the first time it runs. Later runs can reuse the cached models.

Alternatively, activate the environment and use `python`:

```powershell
.\.venv\Scripts\Activate.ps1
python main.py
```

Activation applies to the current terminal session. In a new terminal, activate again or use the direct command above. Run `deactivate` to leave an activated environment.

## Read the Output

Each output line contains recognized text followed by its confidence score. For example, an illustrative result might look like:

```text
123.4 0.987
```

Scores are generally between 0 and 1; higher scores indicate greater model confidence, not a guarantee of accuracy. Check important readings against the original image. Startup and model-loading messages may also appear in the terminal.

## Use a Different Image

Open [main.py](main.py) and change the image path in this line:

```python
results = ocr.predict("test2.jpg")
```

For example, use the other included image:

```python
results = ocr.predict("test1.jpg")
```

Relative paths are resolved from the terminal's working directory, so run the script from the project root. For an image elsewhere on Windows, you can use an absolute path with forward slashes, such as `C:/images/reading.jpg`.

The current configuration uses English recognition and disables document orientation classification, document unwarping, and text-line orientation detection. Use a clear, upright image for best results.

## Project Files

| File | Purpose |
| --- | --- |
| [main.py](main.py) | Loads PaddleOCR, reads an image, and prints recognized text and confidence scores. |
| [requirements.txt](requirements.txt) | Records package versions for dependency installation. |
| [test1.jpg](test1.jpg), [test2.jpg](test2.jpg) | Included input images. The script uses `test2.jpg` by default. |
| [.gitignore](.gitignore) | Excludes the virtual environment and Python caches from Git. |

## Troubleshooting

- **`py` is not recognized or Python 3.10 is not found:** Install Python 3.10 with the Windows Python launcher, then reopen the terminal.
- **PowerShell blocks `Activate.ps1`:** Use `.\.venv\Scripts\python.exe main.py` instead. Activation and execution-policy changes are not needed for that command.
- **`ModuleNotFoundError` for PaddleOCR:** Install dependencies with `.\.venv\Scripts\python.exe -m pip install -r requirements.txt`, then run using that same interpreter.
- **The image cannot be found:** Check the filename in `ocr.predict(...)` and run from the project root.
- **Model download fails:** Check your internet connection and any proxy or firewall restrictions, then retry. Dependency installation and model downloads are separate steps.
- **Dependency installation fails:** Use Python 3.10 and read the first package error. The dependency list comes from the existing environment; installation on other operating systems or hardware has not been verified.

