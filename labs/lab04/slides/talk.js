import Inspire from "../../slides/talk.js";
import "https://elements.colorjs.io/src/color-swatch/color-swatch.js";

let canonicalIds = ["html", "js"];
function getLanguage (element) {
	let language = Prism.util.getLanguage(element);
	let def = Prism.languages[language];
	let canonical = canonicalIds.find(id => Prism.languages[id] === def);
	return canonical ?? language;
}

function populateResultIframes () {
	for (let iframe of document.querySelectorAll("iframe.browser[data-result]")) {
		let parent = iframe.parentElement;
		let codes = [...parent.querySelectorAll("pre > code")].map(code => ({ language: getLanguage(code), code: code.textContent }));
		let code = Object.groupBy(codes, o => o.language);

		for (let language in code) {
			code[language] = code[language].map(o => o.code).join("\n");
		}

		let html = code.html ?? iframe.closest("[data-result-html]")?.dataset.resultHtml ?? "";
		let css = `<style>
			:root {
				font-size: 200%;
			}

			button, input, textarea, select {
				font-size: inherit;
			}
			${code.css ?? ""}
		</style>`;
		let js = code.js ? `<script type="module">${code.js}</script>` : "";

		iframe.srcdoc = `${ css }${ js }${ html }`;
	}
}

document.addEventListener("DOMContentLoaded", populateResultIframes);
