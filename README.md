# Data Report Generator

🇺🇸 English | 🇧🇷 [Português](README.pt-BR.md)

```text
██████╗  █████╗ ████████╗ █████╗       ██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗    ██████╗ ███████╗███╗   ██╗
██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗      ██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝   ██╔════╝ ██╔════╝████╗  ██║
██║  ██║███████║   ██║   ███████║█████╗██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║█████╗██║  ███╗█████╗  ██╔██╗ ██║
██║  ██║██╔══██║   ██║   ██╔══██║╚════╝██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║╚════╝██║   ██║██╔══╝  ██║╚██╗██║
██████╔╝██║  ██║   ██║   ██║  ██║      ██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║      ╚██████╔╝███████╗██║ ╚████║
╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝      ╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚═════╝ ╚══════╝╚═╝  ╚═══╝      
                                                                                                             by @ad2486
````

AI-powered automated data analysis and PDF reporting pipeline.

---

# Features

* 📊 Automatic CSV/XLSX dataset loading
* 🧠 AI-generated insights using LLMs
* 📈 Automatic chart generation with Matplotlib
* 📄 Professional PDF reports with ReportLab
* 🧩 Modular architecture
* ⚙️ Structured processing pipeline
* 🔍 Data quality analysis
* 🏷️ Categorical data analysis
* 📉 Numeric distribution visualization
* 🔄 Multi-provider LLM-ready architecture

---

# Requirements

* Python 3.10+
* An API key for at least one supported LLM provider

---

# Installation

## Clone the repository

```bash
git clone https://github.com/ad2486/data-report-gen.git
cd data-report-gen
```

## Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Configure environment variables

```bash
cp .env.example .env
```

Example:

```env
OPENROUTER_API_KEY=
GROQ_API_KEY=
```

---

# Usage

Place your datasets inside the `data/` folder.

Supported formats:

* `.csv`
* `.xlsx`

Run the pipeline:

```bash
python -m src.pipeline.run_pipeline
```

The system will:

1. Load the dataset
2. Generate metrics
3. Create charts
4. Analyze the data with AI
5. Generate a PDF report automatically

---

# Project Structure

```text
src/
├── ai/
├── input/
├── pipeline/
├── processing/
├── report/
```

---

# Technologies Used

* Python
* Pandas
* Matplotlib
* ReportLab
* Rich
* OpenRouter API
* LLM Integration

---

# Example Output

Generated reports include:

* Dataset overview
* Missing data analysis
* Categorical analysis
* Visual charts
* AI-generated insights
* Recommendations

---

# About

Hi! I'm Arthur Duarte, a Brazilian high school student passionate about programming, linux, etc, computer-related things. Currently I'm learning more about frontend development so keep an eye for my next projects!

This project was built to study:

* Data processing pipelines
* LLM integration
* Automated reporting systems
* Software architecture
* Python backend engineering

It became one of my first complete end-to-end automation systems.

* 🐙 GitHub: @ad2486

---

# License

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.

