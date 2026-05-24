#!/bin/bash

OUTPUT="presentation_standalone.html"

# Write Head
cat << 'HEAD_EOF' > $OUTPUT
<!doctype html>
<html lang="ja">
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
		<title>Reveal.js - Standalone</title>
		<style>
HEAD_EOF

# Inline CSS
cat lib/reveal.js/reset.css >> $OUTPUT
cat lib/reveal.js/reveal.css >> $OUTPUT
cat lib/reveal.js/theme/black.css >> $OUTPUT
cat lib/reveal.js/plugin/highlight/monokai.css >> $OUTPUT

# Custom CSS
cat << 'CSS_EOF' >> $OUTPUT
            :root {
                --r-main-color: #e0e0e0;
                --r-heading-color: #00ff41;
                --r-link-color: #00ff41;
                --r-selection-background-color: #00ff41;
            }
            .reveal h1, .reveal h2, .reveal h3 {
                text-transform: none;
                letter-spacing: -1px;
            }
            .reveal pre code {
                border-radius: 8px;
                padding: 20px;
                font-family: 'Fira Code', monospace;
            }
		</style>
	</head>
	<body>
		<div class="reveal">
			<div class="slides">
				<section>
                    <h1>Reveal.js <br><span style="color:white;">Standalone</span></h1>
                    <p>Powered by Copilot-CLI2</p>
                    <p style="font-size: 0.5em; color: #888;">Press Space to Start</p>
                </section>
				<section>
                    <h2>Why Standalone?</h2>
                    <ul>
                        <li class="fragment"><strong>Zero Dependencies</strong>: No folders, no internet.</li>
                        <li class="fragment"><strong>Portability</strong>: Just one .html file.</li>
                        <li class="fragment"><strong>Speed</strong>: Everything is local.</li>
                    </ul>
                </section>
                <section>
                    <h2>Code Highlighting</h2>
                    <pre><code class="language-javascript" data-trim data-line-numbers="1|3-5|7">
const message = "Hello, Standalone!";

function buildFuture() {
    console.log("Single file works.");
}

buildFuture();
                    </code></pre>
                </section>
                <section>
                    <h2>Ready to Go</h2>
                    <p>Send this file to anyone.</p>
                </section>
			</div>
		</div>
		<script>
BODY_EOF

# Inline JS
cat lib/reveal.js/reveal.js >> $OUTPUT
echo "</script><script>" >> $OUTPUT
cat lib/reveal.js/plugin/notes.js >> $OUTPUT
echo "</script><script>" >> $OUTPUT
cat lib/reveal.js/plugin/markdown.js >> $OUTPUT
echo "</script><script>" >> $OUTPUT
cat lib/reveal.js/plugin/highlight.js >> $OUTPUT

# Write Footer
cat << 'FOOTER_EOF' >> $OUTPUT
		</script>
		<script>
			Reveal.initialize({
				hash: true,
                center: true,
                transition: 'convex',
				plugins: [ RevealMarkdown, RevealHighlight, RevealNotes ]
			});
		</script>
	</body>
</html>
FOOTER_EOF

echo "Done: $OUTPUT"
