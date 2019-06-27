# WeatherAppPython

The point of this project is a python scraper that gets the weather from `https://weather.com`.

## Requirements

- Will be using a virtual env
  - To setup the env, use the following 
  ```bash
  python -m venv weatherterm
  ```
  - This will create the virtual env called weatherterm in your current directory
  - To activate you virtual env, run the activate script in the scripts folder of the new folder (Windows)
  - Install packages in the requirements.txt file, using the following: (Once the env is activated)
  ```bash
  pip install -r requirements.txt
  ```
- Besides python dependencies, we will be making use of phantomjs, downloaded from: `http://phantomjs.org/download.html` and extracted 
  to the folder phantomjs (In case a re-download is required).

## Code layout

The logic for the application will reside in the `weatherApp` directory.
It contains:
  - core
  - parsers

### Usage

