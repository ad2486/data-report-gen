import matplotlib.pyplot as plt
from pathlib import Path


class PlotGenerator:
    def __init__(self, output_dir="plots"):
        self.output_dir = Path(__file__).resolve().parent / "outputs"
        self.output_dir.mkdir(exist_ok=True)

    def generate(self, df):
        image_paths = []

        image_paths += self._numeric_plots(df)
        image_paths += self._categorical_plots(df)

        return image_paths

    # -------------------------
    # NUMÉRICOS
    # -------------------------
    def _numeric_plots(self, df):
        paths = []

        numeric_cols = df.select_dtypes(include="number").columns

        for col in numeric_cols:
            if df[col].dropna().empty:
                continue

            plt.figure()

            data = df[col].dropna()

            plt.hist(data, bins=20)

            plt.title(f"Distribuição: {col}")
            plt.xlabel(col)
            plt.ylabel("Frequência")

            path = self.output_dir / f"{col}_numeric.png"
            plt.savefig(path)
            plt.close()

            paths.append(str(path))

        return paths

    # -------------------------
    # CATEGÓRICOS
    # -------------------------
    def _categorical_plots(self, df):
        paths = []

        cat_cols = df.select_dtypes(include="object").columns

        for col in cat_cols:
            if df[col].dropna().empty:
                continue

            plt.figure()

            top_values = df[col].value_counts().head(10)

            top_values.plot(kind="bar")

            plt.title(f"Top categorias: {col}")
            plt.xlabel(col)
            plt.ylabel("Frequência")

            path = self.output_dir / f"{col}_categorical.png"
            plt.savefig(path)
            plt.close()

            paths.append(str(path))

        return paths