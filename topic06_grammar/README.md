# Grammar

<img src=img/meme.webp width=300px />

**Announcements (Monday 21 Oct):**

1. 6/14 homeworks submitted
    1. Mostly full credit; if not full credit, I left a note about why, and you have the opportunity to resubmit for full credit
    1. I'll start deducting late points on Tuesday@midnight

         $-10^5$/day after Tuesday

1. Project next steps:
    1. In 2 weeks (4 Nov) you'll submit to me your grading rubric
    1. You'll need a detailed list of:
        1. what tasks you will accomplish
        1. what percentage of your final grade each task is worth
    1. I will either approve it or suggest revisions
    1. This will be your "contract" so that you know what you need to do

1. 2-4 homeworks for this topic

**Learning Objectives:**

1. How to constrain LLM output
    1. e.g. force it to be JSON
    1. more general than LMQL
1. How to design a programming language
    1. create your own new language (like RASP/LMQL)
    1. understand existing languages
        1. standard languages like Python/SQL/JSON
        1. non-standard languages like RASP/LMQL
1. Speedrun of 2 semesters of standard CS curriculum
    1. CSCI081 - Computability and Logic
    1. CSCI132 - Compiler Design

## Homework: Whisper.cpp

**tl;dr**
Use whisper.cpp to create a "personal assistant" app.

**due date:** Sunday, 27 Oct

**learning objectives:**

1. learn how constraining model output with a CFG can improve performance
1. learn how to use non-python programs (Whisper.cpp is C/C++)

**background:**

1. 2022-09-21: OpenAI releases Whisper

    1. SOTA ASR (automatic speech recognition) supporting many languages

    1. official announcement: <https://openai.com/index/whisper/>

       github repo: <https://github.com/openai/whisper>

    1. last major open/non-commercial release from OpenAI

        1. 2024-10-04: OpenAI releases Whisper-v3-turbo <https://github.com/openai/whisper/discussions/2363>

        1. much faster than previous whisper models

1. Whisper.cpp is an open source alternative implementation

    1. github: <https://github.com/ggerganov/whisper.cpp>

    1. implemented in c/c++ 

    1. does inference on device (instead of in the cloud)

    1. optimized for Apple hardware (laptops/iphones) and CPU inference

    1. by the same author as llama.cpp
        1. originally designed for Meta's Llama models
        1. now supports most LLMs
        1. made by "a nobody" from Bulgaria who has become one of the most influential people in the LLM scene

            for his story, see: <https://www.reddit.com/r/LocalLLaMA/comments/1cf6b4y/what_is_the_story_behind_ggeranov_llamacpp/>

            <img src=img/ggeranov.png width=300px />

1. llama.cpp is (I think) the first LLM library to support restricting output to a *context free grammar* (CFG)

    1. a handful of other libraries began with regex restrictions

    1. 2023-02-24: Meta releases llama model weights <https://www.reddit.com/r/LocalLLaMA/comments/1dpjcju/timeline_of_llama_family_of_models_first/>

    1. 2023-03-10: llama.cpp first commit <https://github.com/ggerganov/llama.cpp/commits/master/?since=2023-03-10&until=2023-03-10>

    1. 2023-05-10: llama.cpp regex pr <https://github.com/ggerganov/llama.cpp/pull/1397>

    1. 2023-06-08: llama.cpp cfg pr <https://github.com/ggerganov/llama.cpp/pull/1773>

        1. supports JSON-only output and many other "languages"

        1. 2023-11-06: OpenAI adds "JSON mode" <https://openai.com/index/new-models-and-developer-products-announced-at-devday/>

            OpenAI still has no native support for non-JSON languages.

            External projects like LMQL provide support.

        1. NOTE: ggeranov didn't implement these features;

            but he still gets "most of the credit" for fostering an environment where people want to contribute these features
    
    1. 2023-08-30: whisper.cpp cfg pr (easy since it shares code base with llama.cpp) <https://github.com/ggerganov/whisper.cpp/pull/1229>

        AFAIK, no other service offers similar capabilities for ASR

1. Chess is a cool example of why we should care.

    1. local demo <https://github.com/ggerganov/whisper.cpp/tree/master/examples/wchess>

    1. online demo in wasm <https://whisper.ggerganov.com/wchess/>

    1. chess grammar <https://github.com/ggerganov/whisper.cpp/blob/master/grammars/chess.gbnf>

1. llama.cpp and whisper.cpp have python bindings, but ymmv <https://til.simonwillison.net/llms/llama-cpp-python-grammars>

**Tasks:**

1. Clone the whisper.cpp repo

1. Build the `command` program in whisper.cpp

    <https://github.com/ggerganov/whisper.cpp/tree/master/examples/command>

1. Run `command` with the assistant grammar

    <https://github.com/ggerganov/whisper.cpp/blob/master/grammars/assistant.gbnf>

    The pull request for adding cfgs to whisper.cpp shows an example of how to do this.

    You should be able to use the `tiny.en` model and have `command` recognize your commands.

    Without using the grammar, the `tiny.en` won't recognize your commands, but a larger/slower model might.

1. Modify the assistant grammar to include a new command

    `"kill all " things`

    where `things` can be any of `humans`, `animals`, `lifeforms`, or `robots`

    You might (or might not) find the guide for writing grammars helpful: <https://github.com/ggerganov/llama.cpp/blob/master/grammars/README.md>

1. Run `command` with your modified grammar, verifying that you can now issue commands like `kill all humans` and the command is registered.

1. Upload a video of you issuing your new commands to sakai.

## Homework 2

Details TBA

**Background:** See `example*.py`

<!--
## Part 0: What is Language?

## Part 1: Types of Languages

Noam Chomsky:
1. <https://en.wikipedia.org/wiki/Chomsky_hierarchy>

Regular languages:

1. regular expression

Context free:

1. Nested parentheses
1. $a^nb^n$
1. HTML <https://stackoverflow.com/a/1732454>

## Part 2: Language Controversies

1. <https://en.wikipedia.org/wiki/Linguistics_wars>

1. <https://www.astralcodexten.com/p/your-book-review-how-language-began#footnote-anchor-4-146070825>

1. Famous AI researcher Peter Norvig explains and challenges Chomsky's ideas: <https://norvig.com/chomsky.html>

## Part 3: 

Examples of constrained generation:

1. LMQL: <https://lmql.ai/>

1. Regular expressions: <https://github.com/r2d4/rellm>

Example grammars:

1. sqlite3 <https://www.sqlite.org/lang.html>

1. python3

    - in code: <https://docs.python.org/3/reference/grammar.html>
    - documentation: <https://docs.python.org/3/reference/lexical_analysis.html#other-tokens>

1. YAML has no reference grammar <https://github.com/yaml/yaml-grammar>

    YAML is notorious for lots of footguns

    1. <https://ruudvanasseldonk.com/2023/01/11/the-yaml-document-from-hell>
    1. <https://noyaml.com/>

    TOML is an alternative to YAML and does have a reference grammar <https://github.com/toml-lang/toml/blob/1.0.0/toml.abnf>

1. RASP <https://github.com/tech-srl/RASP/blob/main/RASP_support/RASP.g4>

1. url rfc <https://datatracker.ietf.org/doc/html/rfc3986#section-3>

1. json rfc <https://datatracker.ietf.org/doc/html/rfc7159#section-2>

1. jsonSchema <https://cswr.github.io/JsonSchema/spec/grammar/>
-->

<!--
## Homework 2

Use Lark to restrict LLM to CFG: <https://github.com/r2d4/parserllm/blob/main/examples/example.py>
-->
