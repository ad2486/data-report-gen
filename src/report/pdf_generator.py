from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
import matplotlib.pyplot as plt
import os


def plot_category(data, tile, output_path):
    plt.figure()
    
    names = list(data.keys())
    values = list(data.values())
    
    plt.bar(names, values)
    plt.title(tile)
    
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def plot_numeric(data, title, output_path):
    plt.figure()

    plt.hist(data, bins=20)
    plt.title(title)

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def generate_all_plots(df, metrics, output_dir="output"):
    os.makedirs(output_dir, exist_ok=True)

    images = []

    # CATEGÓRICOS
    categorical = metrics.get("categorical_analysis", {})

    for col, data in categorical.items():
        path = f"{output_dir}/{col}_cat.png"
        plot_category(data, col, path)
        images.append(path)

    # NUMÉRICOS
    numeric_cols = df.select_dtypes(include=["number"]).columns

    for col in numeric_cols:
        path = f"{output_dir}/{col}_num.png"
        plot_numeric(df[col].dropna(), col, path)
        images.append(path)

    return images



from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(ai_output, image_paths=None, output_path="report.pdf"):
    doc = SimpleDocTemplate(output_path)
    styles = getSampleStyleSheet()

    story = []

    # título
    story.append(Paragraph("<b>RELATÓRIO DE DADOS (IA)</b>", styles["Title"]))
    story.append(Spacer(1, 12))

    # =========================
    # IA SECTIONS (schema fixo)
    # =========================

    story.append(Paragraph("<b>Dataset Overview</b>", styles["Heading2"]))
    story.append(Paragraph(ai_output["dataset_overview"], styles["Normal"]))
    story.append(Spacer(1, 10))

    story.append(Paragraph("<b>Data Quality Issues</b>", styles["Heading2"]))
    story.append(Paragraph(ai_output["data_quality_issues"], styles["Normal"]))
    story.append(Spacer(1, 10))

    story.append(Paragraph("<b>Key Insights</b>", styles["Heading2"]))
    story.append(Paragraph(ai_output["key_insights"], styles["Normal"]))
    story.append(Spacer(1, 10))

    story.append(Paragraph("<b>Recommendations</b>", styles["Heading2"]))
    story.append(Paragraph(ai_output["recommendations"], styles["Normal"]))
    story.append(Spacer(1, 15))

    # =========================
    # GRÁFICOS
    # =========================

    if image_paths:
        story.append(Paragraph("<b>GRÁFICOS</b>", styles["Heading2"]))
        story.append(Spacer(1, 10))

        numeric_imgs = [img for img in image_paths if "_num" in img]
        cat_imgs = [img for img in image_paths if "_cat" in img]

        if cat_imgs:
            story.append(Paragraph("Distribuições Categóricas", styles["Heading3"]))
            story.append(Spacer(1, 6))

            for img in cat_imgs:
                story.append(Image(img, width=400, height=250))
                story.append(Spacer(1, 10))

        if numeric_imgs:
            story.append(Paragraph("Distribuições Numéricas", styles["Heading3"]))
            story.append(Spacer(1, 6))

            for img in numeric_imgs:
                story.append(Image(img, width=400, height=250))
                story.append(Spacer(1, 10))

    doc.build(story)