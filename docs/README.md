# Omega - Multi-Tool Python Project

This Python project is an all-encompassing toolkit designed to demonstrate various functionalities including authentication system, text compression, logging, quizzes, work with tect files and math tests. It features both console and graphical user interfaces, making it suitable for educational purposes and real-world application demonstrations.

## Features

- **Authentication System**: Secure login and registration functionality with both console and graphical interfaces.
- **Text Compression Tool**: Allows users to compress text files by replacing specified words with abbreviations through a GUI or console interface.
- **Logging**: Comprehensive logging system for tracking user activities and saving information.
- **Interactive Quizzes and Math Tests**: Provides interactive educational tools with support for multiple types of quizzes and math tests accessible via both GUI and console.
- **Text File Management**: Utilities to perform various operations on text files including reading, writing, and modifying content.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need Python installed on your machine. Python 3.6 or above is recommended. Install Python from [here](https://www.python.org/downloads/).

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/Prochyxd/Omega.git
```

Navigate to the project directory:

```bash
cd C:\Adam\Prochazka\Path\To\Omega
```

### Running the Application

Run the main application which provides access to all tools:

```bash
python main.py
```

## Design Patterns Used

- **Singleton**: LogManager class ensures a single logging instance across the application.
- **Factory Method**: Dynamic quiz creation in the quiz management system.
- **Command**: GUI actions in Tkinter are encapsulated as commands for easy management and extension.
- **Strategy**: Multiple validation strategies for authentication to ensure flexibility and security.
- **Decorator**: Logging functionality is enhanced with decorators to include timestamps and additional data.

## Contributing

Contributions to this project are welcome! Please refer to the contributing guidelines for more information on how to participate and submit pull requests.

## Authors

- **[Adam Procházka, C4c](https://github.com/Prochyxd)** - Initial creation and ongoing maintenance

## License

This project has no licence (I guess) (I did not make any)

