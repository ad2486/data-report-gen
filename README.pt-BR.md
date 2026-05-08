# Data Report Generator

🇧🇷 Português | 🇺🇸 [English](README.md)

```text
██████╗  █████╗ ████████╗ █████╗       ██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗    ██████╗ ███████╗███╗   ██╗
██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗      ██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝   ██╔════╝ ██╔════╝████╗  ██║
██║  ██║███████║   ██║   ███████║█████╗██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║█████╗██║  ███╗█████╗  ██╔██╗ ██║
██║  ██║██╔══██║   ██║   ██╔══██║╚════╝██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║╚════╝██║   ██║██╔══╝  ██║╚██╗██║
██████╔╝██║  ██║   ██║   ██║  ██║      ██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║      ╚██████╔╝███████╗██║ ╚████║
╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝      ╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚═════╝ ╚══════╝╚═╝  ╚═══╝      
                                                                                                             by @ad2486
````

Pipeline automatizada de análise de dados com geração de relatórios em PDF utilizando IA.

---

# Features

* 📊 Carregamento automático de datasets CSV/XLSX
* 🧠 Insights gerados por IA usando LLMs
* 📈 Geração automática de gráficos com Matplotlib
* 📄 Relatórios profissionais em PDF com ReportLab
* 🧩 Arquitetura modular
* ⚙️ Pipeline estruturada de processamento
* 🔍 Análise de qualidade dos dados
* 🏷️ Análise categórica
* 📉 Visualização de distribuições numéricas
* 🔄 Arquitetura preparada para múltiplos provedores de LLM

---

# Requisitos

* Python 3.10+
* Uma API key de pelo menos um provedor suportado

---

# Instalação

## Clone o repositório

```bash
git clone https://github.com/ad2486/data-report-gen.git
cd data-report-gen
```

## Crie um ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate
```

## Instale as dependências

```bash
pip install -r requirements.txt
```

## Configure as variáveis de ambiente

```bash
cp .env.example .env
```

Exemplo:

```env
OPENROUTER_API_KEY=
GROQ_API_KEY=
```

---

# Uso

Coloque seus datasets dentro da pasta `data/`.

Formatos suportados:

* `.csv`
* `.xlsx`

Execute a pipeline:

```bash
python -m src.pipeline.run_pipeline
```

O sistema irá:

1. Carregar o dataset
2. Gerar métricas
3. Criar gráficos
4. Analisar os dados com IA
5. Gerar automaticamente um relatório em PDF

---

# Estrutura do Projeto

```text
src/
├── ai/
├── input/
├── pipeline/
├── processing/
├── report/
```

---

# Tecnologias Utilizadas

* Python
* Pandas
* Matplotlib
* ReportLab
* Rich
* OpenRouter API
* Integração com LLMs

---

# Exemplo de Saída

Os relatórios gerados incluem:

* Visão geral do dataset
* Análise de dados faltantes
* Análise categórica
* Gráficos
* Insights gerados por IA
* Recomendações

---

# Sobre

Olá! Eu sou Arthur Duarte, um estudante brasileiro do ensino médio apaixonado por programação, Linux e tecnologia em geral. Atualmente estou estudando mais desenvolvimento frontend, então fique de olho nos próximos projetos!

Esse projeto foi criado para estudar:

* Pipelines de processamento de dados
* Integração com LLMs
* Sistemas automatizados de relatórios
* Arquitetura de software
* Engenharia backend com Python

Ele se tornou um dos meus primeiros sistemas completos de automação ponta a ponta.

* 🐙 GitHub: @ad2486

---

# Licença

Esse projeto está licenciado sob a licença MIT.
Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

