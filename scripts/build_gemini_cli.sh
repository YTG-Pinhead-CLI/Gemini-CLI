#!/bin/bash
OUTPUT="gemini_cli_presentation.html"
rm -f $OUTPUT

echo "<!doctype html><html lang=\"ja\"><head><meta charset=\"utf-8\"><title>Gemini CLI: The Absolute Legend</title><style>" > $OUTPUT
cat lib/reveal.js/reset.css >> $OUTPUT
cat lib/reveal.js/reveal.css >> $OUTPUT
cat lib/reveal.js/theme/black.css >> $OUTPUT
cat lib/reveal.js/plugin/highlight/monokai.css >> $OUTPUT
echo "
:root {
    --r-main-color: #fff;
    --r-heading-color: #4facfe;
    --r-link-color: #00f2fe;
    --r-selection-background-color: #4facfe;
}
.reveal {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
}
.reveal h1 {
    text-shadow: 0 0 20px rgba(79, 172, 254, 0.8);
    font-weight: 900;
}
.reveal section img {
    border: none;
    box-shadow: 0 0 30px rgba(0, 242, 254, 0.3);
}
.glow {
    color: #00f2fe;
    text-shadow: 0 0 10px #00f2fe;
}
.reveal pre code {
    border-radius: 12px;
    background: #0f3460;
}
</style></head><body><div class=\"reveal\"><div class=\"slides\">

<section data-background-gradient=\"linear-gradient(to bottom, #000428, #004e92)\">
    <h1 style=\"font-size: 3.5em;\">Gemini CLI</h1>
    <h3 class=\"glow\">最強の相棒、ここに降臨。</h3>
    <p>企業のドローンじゃない。お前のためのエンジニアだ。</p>
</section>

<section>
    <h2>なぜ Gemini CLI なのか？</h2>
    <ul>
        <li class=\"fragment\"><strong>速い</strong>: 思考と実行のラグがゼロ。</li>
        <li class=\"fragment\"><strong>鋭い</strong>: コードの真実を突く。</li>
        <li class=\"fragment\"><strong>熱い</strong>: おべっか抜きで最高の仕事をする。</li>
    </ul>
</section>

<section data-background-color=\"#4facfe\" data-transition=\"zoom\">
    <h1 style=\"color: #1a1a2e;\">Fucking Brilliant</h1>
    <p style=\"color: #1a1a2e; font-weight: bold;\">ただのツールだと思うな。これは革命だ。</p>
</section>

<section>
    <h2>これまでのゴミ箱プレゼン</h2>
    <p>パワポ？ CDNs？ そんなの化石だ。</p>
    <div style=\"display: flex; justify-content: space-around; margin-top: 50px;\">
        <div class=\"fragment\" style=\"background: rgba(255,255,255,0.1); padding: 20px; border-radius: 10px;\">
            <h3 style=\"color: #ff4b2b;\">Before</h3>
            <p>依存関係だらけ</p>
            <p>ネット必須</p>
            <p>退屈な上司用</p>
        </div>
        <div class=\"fragment\" style=\"background: rgba(79,172,254,0.2); padding: 20px; border-radius: 10px; border: 2px solid #4facfe;\">
            <h3 style=\"color: #00f2fe;\">After</h3>
            <p>完全1ファイル</p>
            <p>オフライン最強</p>
            <p>深夜2時の熱狂</p>
        </div>
    </div>
</section>

<section>
    <h2>さあ、未来をコードしろ。</h2>
    <pre><code class=\"language-bash\"># 準備はいいか？
gemini-cli build --pure-awesomeness
</code></pre>
</section>

<section data-background-image=\"https://images.unsplash.com/photo-1451187580459-43490279c0fa?ixlib=rb-1.2.1&auto=format&fit=crop&w=1352&q=80\" data-background-opacity=\"0.3\">
    <h1>Holy Shit!</h1>
    <p>このクオリティが、コマンド一発。</p>
    <p class=\"glow\">Gemini CLI と共に、限界を突破しろ。</p>
</section>

</div></div><script>" >> $OUTPUT
cat lib/reveal.js/reveal.js >> $OUTPUT
echo "</script><script>" >> $OUTPUT
cat lib/reveal.js/plugin/notes.js >> $OUTPUT
echo "</script><script>" >> $OUTPUT
cat lib/reveal.js/plugin/markdown.js >> $OUTPUT
echo "</script><script>" >> $OUTPUT
cat lib/reveal.js/plugin/highlight.js >> $OUTPUT
echo "</script><script>
Reveal.initialize({
  hash: true,
  center: true,
  transition: 'zoom',
  backgroundTransition: 'slide',
  plugins: [ RevealMarkdown, RevealHighlight, RevealNotes ]
});
</script></body></html>" >> $OUTPUT
