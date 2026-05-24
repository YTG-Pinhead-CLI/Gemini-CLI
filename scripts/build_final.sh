#!/bin/bash
OUTPUT="presentation.html"
rm -f $OUTPUT

echo "<!doctype html><html lang=\"ja\"><head><meta charset=\"utf-8\"><title>Reveal.js Standalone</title><style>" > $OUTPUT
cat lib/reveal.js/reset.css >> $OUTPUT
cat lib/reveal.js/reveal.css >> $OUTPUT
cat lib/reveal.js/theme/black.css >> $OUTPUT
cat lib/reveal.js/plugin/highlight/monokai.css >> $OUTPUT
echo "
:root { --r-main-color: #e0e0e0; --r-heading-color: #00ff41; --r-link-color: #00ff41; }
.reveal h1, .reveal h2, .reveal h3 { text-transform: none; }
.reveal pre code { border-radius: 8px; padding: 20px; font-family: monospace; }
</style></head><body><div class=\"reveal\"><div class=\"slides\">
<section><h1>Reveal.js</h1><p>Standalone Mode</p></section>
<section><h2>1 File</h2><p>Everything is inside.</p></section>
<section><h2>Code</h2><pre><code class=\"language-js\">console.log('Works!');</code></pre></section>
<section>
  <h2>Mermaid</h2>
  <div class=\"mermaid\">
    graph LR
      A[Start] --> B{Success?}
      B -- Yes --> C[Celebrate]
      B -- No --> D[Debug]
  </div>
</section>
</div></div><script>" >> $OUTPUT
cat lib/reveal.js/reveal.js >> $OUTPUT
echo "</script><script>" >> $OUTPUT
cat lib/reveal.js/plugin/notes.js >> $OUTPUT
echo "</script><script>" >> $OUTPUT
cat lib/reveal.js/plugin/markdown.js >> $OUTPUT
echo "</script><script>" >> $OUTPUT
cat lib/reveal.js/plugin/highlight.js >> $OUTPUT
echo "</script><script>" >> $OUTPUT
cat lib/mermaid.min.js >> $OUTPUT
echo "</script><script>
mermaid.initialize({ 
  startOnLoad: false, 
  theme: 'dark' 
});
Reveal.initialize({
  hash: true, center: true,
  plugins: [ RevealMarkdown, RevealHighlight, RevealNotes ]
});

function renderMermaid(slide) {
  const nodes = slide.querySelectorAll('.mermaid:not([data-processed="true"])');
  if (nodes.length > 0) {
    mermaid.run({ nodes: nodes });
  }
}

Reveal.on('ready', event => renderMermaid(event.currentSlide));
Reveal.on('slidechanged', event => renderMermaid(event.currentSlide));
</script></body></html>" >> $OUTPUT
