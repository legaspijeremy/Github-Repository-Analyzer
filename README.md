# GitHub Repository Analyzer

An AI-powered GitHub Repository Analyzer built with Python, the GitHub API, and static code analysis tools.

The application analyzes public GitHub repositories and generates insights about:

* Documentation quality
* Repository health
* Code quality
* Project complexity
* AI-generated project summaries

---

## Features

### Repository Analysis

* Fetch repository metadata
* Fetch README contents
* Count stars and forks
* Detect primary language
* Count contributors
* Count commits
* Generate repository file tree

### Documentation Analysis

* Documentation score (0-100)
* Installation section detection
* Usage section detection
* API documentation detection
* Examples detection
* Contributing guide detection
* License detection
* FAQ detection
* Roadmap detection
* README structure analysis
* Markdown heading analysis
* Code block analysis

### Code Quality Analysis (Upcoming)

* Cyclomatic Complexity
* Maintainability Index
* Lines of Code (LOC)
* Average Function Length
* Average Class Size
* Static Analysis Metrics

### Project Complexity Analysis (Upcoming)

* Complexity Score
* Complexity Classification
* Repository Size Analysis

### AI Summary Generation (Upcoming)

* Project Overview
* Technology Stack Detection
* Intended Users
* Key Features Summary

---

## Tech Stack

### Backend

* Python
* PyGithub
* python-dotenv

### Static Analysis

* Radon
* Pylint

### AI

* OpenAI API (Planned)
* Ollama (Planned)

### Frontend

* Streamlit (Planned)

---

## Project Roadmap

### Phase 1 — Repository Fetching

#### Status: Complete ✅

* [x] GitHub API integration
* [x] Repository URL parsing
* [x] Fetch repository metadata
* [x] Fetch README
* [x] Fetch stars
* [x] Fetch forks
* [x] Fetch primary language
* [x] Fetch contributors
* [x] Fetch commit count
* [x] Generate repository file tree

---

### Phase 2 — Documentation Score

#### Status: Complete ✅

* [x] Documentation scoring system
* [x] README analysis
* [x] Installation detection
* [x] Usage detection
* [x] API documentation detection
* [x] Example detection
* [x] Contributing guide detection
* [x] License detection
* [x] FAQ detection
* [x] Roadmap detection
* [x] Markdown heading analysis
* [x] Code block analysis

---

### Phase 3 — Code Quality Metrics

#### Status: In Progress 🚧

* [ ] Install Radon
* [ ] Install Pylint
* [ ] Download Python source files
* [ ] Calculate total files
* [ ] Calculate Python files
* [ ] Calculate Lines of Code (LOC)
* [ ] Calculate Average Function Length
* [ ] Calculate Average Class Size
* [ ] Calculate Cyclomatic Complexity
* [ ] Calculate Maintainability Index

---

### Phase 4 — Project Complexity Score

#### Status: Planned 📋

* [ ] Create complexity scoring engine
* [ ] Calculate complexity score
* [ ] Classify repositories:

  * [ ] Simple
  * [ ] Medium
  * [ ] Complex

---

### Phase 5 — AI Project Summary

#### Status: Planned 📋

* [ ] Integrate LLM
* [ ] Build summarization prompt
* [ ] Generate project overview
* [ ] Detect technologies
* [ ] Detect intended users
* [ ] Generate key feature summary

---

### Phase 6 — Streamlit Dashboard

#### Status: Planned 📋

* [ ] Build Streamlit UI
* [ ] Repository URL input
* [ ] Analysis dashboard
* [ ] Documentation report
* [ ] Code quality report
* [ ] Complexity report
* [ ] AI summary panel

---

## Example Output

```text
Repository Information
------------------------------
Name: flask

Repository Metrics
------------------------------
Stars: 71,000+
Forks: 16,000+
Language: Python
Contributors: 700+
Commit Count: 8,000+

Documentation Score: 75/100

Documentation Metrics
------------------------------
README Length: 8,000+
Headings: 14
Code Blocks: 8
```

---

## Installation

```bash
git clone https://github.com/your-username/github-repository-analyzer.git

cd github-repository-analyzer

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

---

## Usage

```bash
python app.py
```

Enter a repository URL:

```text
https://github.com/pallets/flask
```

---

## Future Improvements

* Support additional programming languages
* Repository comparison mode
* Repository health score
* Test coverage analysis
* Dependency analysis
* Security vulnerability scanning
* CI/CD quality checks
* Web deployment

