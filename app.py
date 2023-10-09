import os

from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_KEY")
openai.api_base = os.getenv("OPENAI_ENDPOINT")

# Define the supported languages
supported_languages = ["python", "javascript", "java", "c", "cpp", "ruby", "go", "swift", "typescript",
                       "php", "html", "css", "sql", "bash", "powershell", "perl", "r", "matlab", "scala",
                       "kotlin", "lua", "dart", "rust", "fortran", "prolog", "haskell", "groovy",
                       "elixir", "ocaml", "racket", "scheme", "julia", "pascal", "ada", "cobol", "lisp",
                       "erlang", "smalltalk", "forth", "verilog", "vhdl", "perl6", "apollos", "apl",
                       "autoit", "ballerina", "blitzmax", "c", "cadl", "cfm", "ceylon", "cil", "cjsx",
                       "clojure", "clorophy", "cobol", "coffeescript", "curry", "cweb", "cypher", "d",
                       "django", "dtd", "dylan", "ec", "ejs", "elm", "erlang", "f#", "factor", "fancy",
                       "fortran", "fsharp", "gcode", "gdscript", "genstat", "gml", "godotscript", "golo",
                       "gosu", "gql", "graphql", "groovy", "haml", "handlebars", "harbour", "haskell",
                       "haxe", "hcl", "html", "idl", "java", "javascript", "jsoniq", "julia", "jsx",
                       "julia", "kotlin", "kotlin", "latex", "less", "liquid", "lisp", "live", "lolcode",
                       "lua", "lsl", "markdown", "mathematica", "matlab", "moonscript", "nginx", "nim",
                       "nix", "nunjucks", "objective-c", "ocaml", "pascal", "perl", "php", "plpgsql",
                       "powershell", "pug", "puppet", "purescript", "python", "qml", "racket", "raku",
                       "razor", "reason", "red", "rexx", "ruby", "rust", "sas", "scss", "scala",
                       "scheme", "shell", "shen", "slash", "slim", "smarty", "snobol", "solidity",
                       "sparql", "sql", "stylus", "svelte", "svg", "swift", "systemverilog", "tcl",
                       "tex", "toml", "tsql", "twig", "typescript", "typescript", "vala", "vb.net",
                       "velocity", "verilog", "vhdl", "vim", "wasm", "wiki", "xeus", "xml", "yaml",
                       "yml", "zig", "zimbu"]

@app.route('/')
def index():
    return render_template('index.html', languages=supported_languages)

@app.route('/convert', methods=['POST'])
def convert():
    input_language = request.form['input-language']
    output_language = request.form['output-language']
    input_code = request.form['input-code']

    # Construct prompt for Chat Completions API

    # Construct prompt for Chat Completions API
    prompt = f"Translate this function from {input_language} into {output_language} ### {input_language} \n\n {input_code} \n\n ### {output_language}"

    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        temperature=0,
        max_tokens=1050,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["###"]
    )

    # Extract code from the response
    output_code = response.choices[0].text.strip()



    return output_code
if __name__ == '__main__':
    app.run(debug=True)