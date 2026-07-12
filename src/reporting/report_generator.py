"""
CircuitBench Report Generator
=============================

Generate publication-quality benchmark reports.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

from datetime import datetime

import pandas as pd


class ReportGenerator:
    @staticmethod
    def markdown(
        leaderboard: pd.DataFrame,
        title="CircuitBench Report",
    ):

        report = []

        report.append(f"# {title}")

        report.append("")

        report.append(f"Generated: {datetime.now().isoformat()}")

        report.append("")

        report.append("## Benchmark Results")

        report.append("")

        report.append(leaderboard.to_markdown(index=False))

        return "\n".join(report)

    @staticmethod
    def html(
        leaderboard,
        title="CircuitBench Report",
    ):

        html = f"""

<html>

<head>

<title>{title}</title>

<style>

body {{
font-family: Arial;
margin:40px;
}}

table {{
border-collapse: collapse;
}}

th,td {{
border:1px solid #ccc;
padding:6px;
}}

th {{
background:#eeeeee;
}}

</style>

</head>

<body>

<h1>{title}</h1>

<p>Generated:
{datetime.now().isoformat()}
</p>

{leaderboard.to_html(index=False)}

</body>

</html>

"""

        return html

    @staticmethod
    def latex(
        leaderboard,
        caption="Benchmark Results",
        label="tab:benchmark",
    ):

        return leaderboard.to_latex(
            index=False,
            caption=caption,
            label=label,
            escape=False,
        )

    @staticmethod
    def save_markdown(
        leaderboard,
        filename,
        title="CircuitBench Report",
    ):

        with open(
            filename,
            "w",
            encoding="utf-8",
        ) as f:
            f.write(
                ReportGenerator.markdown(
                    leaderboard,
                    title,
                )
            )

    @staticmethod
    def save_html(
        leaderboard,
        filename,
        title="CircuitBench Report",
    ):

        with open(
            filename,
            "w",
            encoding="utf-8",
        ) as f:
            f.write(
                ReportGenerator.html(
                    leaderboard,
                    title,
                )
            )

    @staticmethod
    def save_latex(
        leaderboard,
        filename,
    ):

        with open(
            filename,
            "w",
            encoding="utf-8",
        ) as f:
            f.write(
                ReportGenerator.latex(
                    leaderboard,
                )
            )
