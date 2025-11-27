# Git & GitHub Workshop - Python Project

Welcome to the Git & GitHub Workshop! This repository contains a basic Python project structure designed to help you learn and practice version control with Git and collaboration with GitHub.

## Quick Start

New to the workshop? Follow these steps to get started in 5 minutes:

```bash
# 1. Clone the repository (replace <repository-url> with actual URL)
git clone <repository-url>
cd workshop-git

# 2. Set up Python virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run a sample script to verify everything works
python src/data_analysis.py

# 5. Run tests to see everything is working
pytest tests/ -v

# 6. Create your first branch and start coding!
git checkout -b feature/my-first-feature
```

That's it! You're ready to start learning Git and GitHub.

## Project Structure

```
workshop-git/
├── src/                # Source code directory
│   ├── data_analysis.py   # Pandas/NumPy examples
│   ├── visualization.py   # Matplotlib/Seaborn charts
│   └── utils.py           # Utility functions
├── scripts/            # Utility scripts
│   ├── setup_environment.sh
│   └── run_tests.sh
├── tests/              # Unit tests
│   ├── test_data_analysis.py
│   └── test_utils.py
├── data/               # Data files directory
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── .gitignore         # Git ignore rules
```

## Detailed Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd workshop-git
```

### 2. Create a Virtual Environment

This project uses Python 3.10 or higher. Create a virtual environment:

```bash
python3 -m venv venv
```

### 3. Activate the Virtual Environment

**On Linux/Mac:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## Workshop Exercises

### Exercise 1: Basic Git Commands
- Check the status of your repository: `git status`
- View commit history: `git log`
- Create a new branch: `git branch feature/your-feature-name`
- Switch to your branch: `git checkout feature/your-feature-name`

### Exercise 2: Making Changes
- Modify one of the Python scripts in the `src/` directory
- Stage your changes: `git add <file>`
- Commit your changes: `git commit -m "Descriptive message"`
- Push to GitHub: `git push origin feature/your-feature-name`

### Exercise 3: Collaboration
- Create a Pull Request on GitHub
- Review someone else's Pull Request
- Merge a Pull Request

### Exercise 4: Handling Conflicts
- Practice resolving merge conflicts
- Use `git diff` to see changes
- Use `git merge` or `git rebase`

## Useful Git Commands

```bash
# Check status
git status

# View changes
git diff

# View commit history
git log --oneline --graph

# Create and switch to new branch
git checkout -b branch-name

# Stage files
git add .

# Commit changes
git commit -m "Your message"

# Push to remote
git push origin branch-name

# Pull latest changes
git pull origin main

# View remote repositories
git remote -v

# Stash changes
git stash
git stash pop
```

## Running the Example Scripts

The repository includes several example Python scripts that you can run to practice Git:

### Data Analysis Script
```bash
python src/data_analysis.py
```
This script demonstrates data manipulation with pandas and numpy, including:
- Generating sample datasets
- Computing statistics and aggregations
- Filtering and analyzing data

### Visualization Script
```bash
python src/visualization.py
```
Creates beautiful charts using matplotlib and seaborn:
- Time series plots
- Distribution histograms
- Correlation heatmaps

### Utility Functions
```bash
python src/utils.py
```
Demonstrates common utility functions:
- Currency formatting
- Percentage calculations
- Date range generation
- JSON file operations

### Running Tests
```bash
# Run all tests
pytest tests/ -v

# Run with coverage report
pytest tests/ --cov=src --cov-report=term

# Or use the provided script
bash scripts/run_tests.sh
```

## Resources

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Python Documentation](https://docs.python.org/3/)

## License

This project is for educational purposes.

## Questions?

Feel free to open an issue or reach out during the workshop!
