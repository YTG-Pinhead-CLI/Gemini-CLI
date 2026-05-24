import os

def build():
    # Read assets
    with open('reset.css', 'r') as f: reset_css = f.read()
    with open('reveal.css', 'r') as f: reveal_css = f.read()
    with open('black.css', 'r') as f: black_css = f.read()
    with open('reveal.js', 'r') as f: reveal_js = f.read()
    with open('chart.js', 'r') as f: chart_js = f.read()

    html_template = f"""<!doctype html>
<html lang="ja">
<head>
    <meta charset="utf-8">
    <title>Immigration Data Standalone</title>
    <style>
    {reset_css}
    {reveal_css}
    {black_css}
    .reveal .slides section {{ text-align: center; }}
    .chart-container {{ width: 800px; height: 450px; margin: 0 auto; background: rgba(255,255,255,0.05); padding: 20px; border-radius: 10px; }}
    </style>
</head>
<body>
    <div class="reveal">
        <div class="slides">
            <section data-background-color="#111">
                <h1 style="color: #ef4444;">IMMIGRATION</h1>
                <p>Standalone Reveal.js + Chart.js</p>
                <p style="font-size: 0.6em; color: #666;">Press &rarr; to continue</p>
            </section>
            <section data-background-color="#111">
                <h3>日本 vs イギリス：流入数</h3>
                <div class="chart-container">
                    <canvas id="immChart"></canvas>
                </div>
            </section>
            <section data-background-color="#222">
                <h3>Success!</h3>
                <p>Everything is inlined in this single HTML file.</p>
            </section>
        </div>
    </div>
    <script>
    {chart_js}
    </script>
    <script>
    {reveal_js}
    </script>
    <script>
    Reveal.initialize({{ hash: true, center: true }}).then(() => {{
        const ctx = document.getElementById('immChart').getContext('2d');
        new Chart(ctx, {{
            type: 'line',
            data: {{
                labels: ['2014', '16', '18', '20', '22', '24'],
                datasets: [
                    {{ label: 'Japan', data: [21, 25, 30, 10, 14, 66], borderColor: '#ef4444', tension: 0.4 }},
                    {{ label: 'UK', data: [63, 59, 61, 60, 110, 120], borderColor: '#3b82f6', tension: 0.4 }}
                ]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{ legend: {{ labels: {{ color: 'white' }} }} }},
                scales: {{
                    y: {{ ticks: {{ color: '#888' }}, grid: {{ color: '#333' }} }},
                    x: {{ ticks: {{ color: '#888' }}, grid: {{ display: false }} }}
                }}
            }}
        }});
    }});
    </script>
</body>
</html>"""

    with open('standalone_presentation.html', 'w') as f:
        f.write(html_template)
    print("Successfully built standalone_presentation.html")

if __name__ == "__main__":
    build()
