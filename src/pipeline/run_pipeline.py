from src.input.loader import select_file, load_file
from src.processing.metrics import generate_metrics
from src.processing.plots import PlotGenerator  
from src.ai.llm import LLMClient
from src.ai.analyzer import analyze_with_ai
from src.report.pdf_generator import generate_pdf_report
from pathlib import Path


def run_pipeline():
    # 1. seleção de arquivo
    file = select_file(Path("data"))

    # 2. carregar dados
    df = load_file(file)

    # 3. métricas
    metrics = generate_metrics(df)

    # 4. gráficos (vai retornar lista de paths)
    image_paths = PlotGenerator().generate(df)
    # 5. IA
    llm = LLMClient()
    ai_output = analyze_with_ai(metrics, llm)

    # 6. PDF final
    generate_pdf_report(
        ai_output=ai_output,
        image_paths=image_paths,
        output_path="report.pdf"
    )


if __name__ == "__main__":
    run_pipeline()