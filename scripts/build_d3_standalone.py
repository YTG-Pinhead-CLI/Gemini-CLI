import os

def build():
    # Read all assets
    with open('reset.css', 'r') as f: reset_css = f.read()
    with open('reveal.css', 'r') as f: reveal_css = f.read()
    with open('black.css', 'r') as f: black_css = f.read()
    with open('reveal.js', 'r') as f: reveal_js = f.read()
    with open('d3.min.js', 'r') as f: d3_js = f.read()

    html_template = f"""<!doctype html>
<html lang="ja">
<head>
    <meta charset="utf-8">
    <title>D3.js + Reveal.js Standalone</title>
    <style>
    {reset_css}
    {reveal_css}
    {black_css}
    
    .reveal .slides section {{
        text-align: center;
        height: 100%;
    }}
    #d3-viz-container {{
        width: 1000px;
        height: 500px;
        margin: 0 auto;
        position: relative;
        background: rgba(255,255,255,0.02);
        border-radius: 15px;
        overflow: hidden;
    }}
    .d3-controls {{
        margin-bottom: 10px;
    }}
    .d3-controls button {{
        background: #334155; color: white; border: none; 
        padding: 8px 16px; border-radius: 5px; cursor: pointer;
        margin: 0 5px; font-size: 0.5em;
    }}
    .d3-controls button.active {{
        background: #3b82f6;
    }}
    .tooltip {{
        position: absolute; visibility: hidden; background: rgba(0,0,0,0.9);
        padding: 8px; border-radius: 4px; pointer-events: none; font-size: 14px;
        border: 1px solid #444; z-index: 1000; color: white;
    }}
    .label {{ font-size: 12px; fill: #94a3b8; pointer-events: none; text-anchor: middle; }}
    </style>
</head>
<body>
    <div class="reveal">
        <div class="slides">
            <!-- Slide 1 -->
            <section data-background-color="#0f172a">
                <h1 style="color: #60a5fa;">D3.js <span style="color: #fff;">+</span> Reveal.js</h1>
                <p>完全オフライン・データ駆動型スライド</p>
                <p style="font-size: 0.5em; color: #475569; margin-top: 50px;">Press &rarr; to see D3 in action</p>
            </section>

            <!-- Slide 2 -->
            <section data-background-color="#0f172a">
                <h2 style="font-size: 1.5em; margin-bottom: 20px;">移民の内訳比較 (2024)</h2>
                
                <div class="d3-controls">
                    <button id="btn-jp" class="active">JAPAN</button>
                    <button id="btn-uk">UNITED KINGDOM</button>
                </div>

                <div id="d3-viz-container">
                    <div class="tooltip" id="tooltip"></div>
                </div>
            </section>

            <!-- Slide 3 -->
            <section data-background-color="#1e293b">
                <h1>Conclusion</h1>
                <ul style="font-size: 0.8em; line-height: 1.8;">
                    <li>D3.js の自由な表現力</li>
                    <li>Reveal.js の構成力</li>
                    <li>インライン化による絶対的な可搬性</li>
                </ul>
                <p style="margin-top: 40px; color: #10b981;">This is the future of presentations.</p>
            </section>
        </div>
    </div>

    <script>
    {d3_js}
    </script>
    <script>
    {reveal_js}
    </script>
    <script>
        // Reveal.js Initializer
        Reveal.initialize({{
            hash: true,
            center: true,
            width: 1200,
            height: 800
        }}).then(() => {{
            initD3();
        }});

        function initD3() {{
            const data = {{
                jp: [
                    {{ name: "中国", value: 844, color: "#f87171" }},
                    {{ name: "ベトナム", value: 590, color: "#fb923c" }},
                    {{ name: "韓国", value: 410, color: "#fbbf24" }},
                    {{ name: "フィリピン", value: 336, color: "#facc15" }},
                    {{ name: "ブラジル", value: 210, color: "#a3e635" }},
                    {{ name: "ネパール", value: 207, color: "#2dd4bf" }},
                    {{ name: "インドネシア", value: 173, color: "#22d3ee" }},
                    {{ name: "その他", value: 1000, color: "#475569" }}
                ],
                uk: [
                    {{ name: "インド", value: 1000, color: "#60a5fa" }},
                    {{ name: "ポーランド", value: 900, color: "#818cf8" }},
                    {{ name: "パキスタン", value: 700, color: "#a78bfa" }},
                    {{ name: "ルーマニア", value: 550, color: "#c084fc" }},
                    {{ name: "ナイジェリア", value: 450, color: "#e879f9" }},
                    {{ name: "アイルランド", value: 400, color: "#f472b6" }},
                    {{ name: "イタリア", value: 300, color: "#fb7185" }},
                    {{ name: "その他", value: 7100, color: "#475569" }}
                ]
            }};

            const container = document.getElementById('d3-viz-container');
            const width = container.clientWidth;
            const height = container.clientHeight;

            const svg = d3.select("#d3-viz-container").append("svg")
                .attr("width", width)
                .attr("height", height);

            const tooltip = d3.select("#tooltip");

            function update(nodesData) {{
                const pack = d3.pack()
                    .size([width, height])
                    .padding(5);

                const root = d3.hierarchy({{ children: nodesData }})
                    .sum(d => d.value);

                const nodes = pack(root).leaves();

                const circles = svg.selectAll("circle")
                    .data(nodes, d => d.data.name);

                circles.exit()
                    .transition().duration(800)
                    .attr("r", 0)
                    .remove();

                const circlesEnter = circles.enter().append("circle")
                    .attr("r", 0)
                    .attr("cx", d => d.x)
                    .attr("cy", d => d.y)
                    .style("fill", d => d.data.color)
                    .on("mouseover", function(event, d) {{
                        d3.select(this).style("stroke", "#fff").style("stroke-width", 2);
                        tooltip.style("visibility", "visible")
                            .html(`<strong>${{d.data.name}}</strong><br>約 ${{d.data.value.toLocaleString()}},000人`);
                    }})
                    .on("mousemove", function(event) {{
                        const [x, y] = d3.pointer(event, container);
                        tooltip.style("top", (y - 40) + "px")
                               .style("left", (x + 10) + "px");
                    }})
                    .on("mouseout", function() {{
                        d3.select(this).style("stroke-width", 0);
                        tooltip.style("visibility", "hidden");
                    }});

                circles.merge(circlesEnter)
                    .transition().duration(1000)
                    .attr("cx", d => d.x)
                    .attr("cy", d => d.y)
                    .attr("r", d => d.r)
                    .style("fill", d => d.data.color);

                const labels = svg.selectAll(".label")
                    .data(nodes, d => d.data.name);

                labels.exit().remove();

                const labelsEnter = labels.enter().append("text")
                    .attr("class", "label")
                    .attr("dy", ".3em")
                    .style("opacity", 0);

                labels.merge(labelsEnter)
                    .transition().duration(1000)
                    .attr("x", d => d.x)
                    .attr("y", d => d.y)
                    .text(d => d.r > 25 ? d.data.name : "")
                    .style("opacity", 1);
            }}

            update(data.jp);

            d3.select("#btn-jp").on("click", function() {{
                d3.selectAll(".d3-controls button").classed("active", false);
                d3.select(this).classed("active", true);
                update(data.jp);
            }});

            d3.select("#btn-uk").on("click", function() {{
                d3.selectAll(".d3-controls button").classed("active", false);
                d3.select(this).classed("active", true);
                update(data.uk);
            }});
        }}
    </script>
</body>
</html>"""

    with open('d3_reveal_standalone.html', 'w') as f:
        f.write(html_template)
    print("Successfully built d3_reveal_standalone.html")

if __name__ == "__main__":
    build()
