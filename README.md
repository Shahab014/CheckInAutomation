# Check-In Automation

Automate the check-in process for a web application using Selenium.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

- Python 3.11
- Selenium library
- Pillow library
- Pyinstaller library

## Getting Started

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/check-in-automation.git
   cd check-in-automation
   ```

2. Install dependencies:

   ```bash
   pip install selenium, pillow, pyinstaller
   ```

### Usage

Run the application:

```bash
python main_app.py
```

Build the exe:

```bash
pyinstaller --noconsole --onefile --clean --icon=assets\clock.ico --add-data 'assets;assets' --add-data 'data;data'  --name=CheckInAutomation main.py
```
