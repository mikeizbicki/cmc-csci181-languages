# LLM Evaluation

Last week:
1. Use RAG to improve response accuracy

    > **Aside:**
    > About half the class submitted last night.
    > We'll continue to have Sunday due dates + 2 day grace period until Tuesday + -1 letter grade for each day late after Tuesday.
    > If you need extensions, just let me know.

This week's question:
1. But how do we know if the response accuracy improved?

Answer:
1. Benchmarks

<!--
Read:
1. How I use LLMs (by Nicholas Carlini, famous Security/ML researcher) <https://nicholas.carlini.com/writing/2024/how-i-use-ai.html>
-->

<img height=250px src=img/llm-benchmark2.jpeg />

## News: OpenAI's o1-mini / o1-preview models

OpenAI Announcement:
1. <https://openai.com/index/learning-to-reason-with-llms/>
1. <https://openai.com/index/openai-o1-mini-advancing-cost-efficient-reasoning/>

### Background: OpenAI Drama

Very little information released in the announcement.
1. OpenAI used to be famous for publishing lots of research.
1. Now they are infamous for not publishing anything.

<img width=400px src=img/closed-ai.png />

<img width=400px src=img/closed-ai2.png />

(2024-03-01) [Elon Musk sues OpenAI for abandoning original mission for profit](https://www.reuters.com/legal/elon-musk-sues-openai-ceo-sam-altman-breach-contract-2024-03-01/)

(2024-06-12) [Elon Musk withdraws lawsuit against OpenAI](https://www.reuters.com/legal/elon-musk-withdraws-lawsuit-against-openai-2024-06-11/)

(2024-08-05) [Elon Musk revives lawsuit against Sam Altman and OpenAI, filing shows](https://www.reuters.com/technology/elon-musk-revives-lawsuit-against-sam-altman-openai-nyt-reports-2024-08-05/)

<img width=600px src=img/musk-altman.webp />

### Background: Chain of Thought (the main technique of o1/o1-mini/o1-preview)

<img src=img/cot.jpg width=300px />

Historical Overview: <https://deepgram.com/learn/chain-of-thought-prompting-guide>

Important papers:
1. (2022-01-28, Google Research Brain Team)[Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903)
1. (2022-03-21, Google Research Brain Team)[Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://arxiv.org/abs/2203.11171)
1. (2022-05-24, University of Tokyo) [Large Lange Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916) <!-- <https://chadrick-kwag.medium.com/paper-review-large-language-models-are-zero-shot-reasoners-e86ce0b4f025> -->
1. (2022-08-07, Amazon Web Services) [Automatic Chain of Thought Prompting in Large Language Models](https://arxiv.org/abs/2210.03493)

### Other links

The strawberry problem:

<img width=250px src=img/strawberry.webp />

In-depth Overview:
1. <https://simonwillison.net/2024/Sep/12/openai-o1/>
1. <https://github.com/hijkzzz/Awesome-LLM-Strawberry>

The g1 repo is COT on groq:
1. <https://github.com/bklieger-groq/g1>
1. <https://news.ycombinator.com/item?id=41550364>

Jailbreaking:
1. Example attempts:
    1. <https://www.reddit.com/r/LocalLLaMA/comments/1fh8n8k/is_this_a_way_to_reveal_o1s_thinking_steps/>
    1. <https://www.reddit.com/r/LocalLLaMA/comments/1fgp3b7/bypass_openai_thinking_policy_error/?share_id=ex7QNDbvH9r6L91HvbJ_B>
1. Result in account bans from openAI: <https://www.reddit.com/r/LocalLLaMA/comments/1fgo671/openai_sent_me_an_email_threatening_a_ban_if_i/>

### My take

Exponential growth is bad!!!

<img width=400px src=img/exp.png />

## Important Models

Factors in selecting a model:
1. Model size (bigger = better results, more expensive)
1. Training data
1. Context window
1. Open / closed model

Groq supported models: <https://console.groq.com/docs/models>

History of LLama models:
1. (old, but linked everywhere) <https://agi-sphere.com/llama-models/>
1. always up-to-date <https://en.wikipedia.org/wiki/Llama_(language_model)>

HuggingFace model downloads: <https://huggingface.co/models?other=LLM>

## Benchmarking

<img width=400px src=img/llm-benchmarks-too-many.jpg />

Classic Benchmarks:
1. paperswithcode.com
    1. MMLU ("the closest thing to a standard")<https://paperswithcode.com/sota/multi-task-language-understanding-on-mmlu>
        1. Metacalculus: <https://www.metaculus.com/questions/22056/highest-gpqa-diamond-scores/?sub-question=22057>
    1. all benchmarks: <https://paperswithcode.com/sota>
1. 🤗 HuggingFace Leaderboards:
    1. OpenLLM <https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard>
    1. BigCode <https://huggingface.co/spaces/bigcode/bigcode-models-leaderboard>
    1. BigCodeBench <https://huggingface.co/spaces/bigcode/bigcodebench-leaderboard>
1. Overview of coding benchmarks: <https://blog.continue.dev/an-introduction-to-code-llm-benchmarks-for-software-engineers/>

<img height=260px src=img/llm-benchmarks-be-like.webp />

Concerns about benchmarks:
1. (2023-12-04) Competition-Level Problems are Effective LLM Evaluators <https://arxiv.org/html/2312.02143v3>
1. (2024-05-03) A Careful Examination of Large Language Model Performance on Grade School Arithmetic <https://arxiv.org/abs/2405.00332>
    1. In blog form: <https://favtutor.com/articles/llm-overfit-public-benchmarks/>
1. (2024-02-01) When Benchmarks are Targets: Revealing the Sensitivity of Large Language Model Leaderboards <https://arxiv.org/abs/2402.01781>
    1. In tweet+reddit form: <https://www.reddit.com/r/LocalLLaMA/comments/1alryn6/when_benchmarks_are_targets_revealing_the/>

Betterish Benchmarks:
1. Livebench <https://livebench.ai/>
1. LiveCodeBench <https://livecodebench.github.io/>
1. Custom benchmark of random person:
    1. <https://www.reddit.com/r/LocalLLaMA/comments/1fhawvv/i_ran_o1preview_through_my_smallscale_benchmark/>
    1. <https://dubesor.de/benchtable>
1. Language Model Arena
    1. game: <https://lmarena.ai/>
    1. leaderboard: <https://lmarena.ai/?leaderboard>
1. Jailbreak arena
    1. game: <https://redarena.ai/>
    1. leaderboard: <https://redarena.ai/leaderboard>
1. ARC-AGI
    1. Critique of OpenAI o1-mini/preview <https://arcprize.org/blog/openai-o1-results-arc-prize>; <https://news.ycombinator.com/item?id=41535694>
    1. nearly-SOTA using GPT-4o: <https://redwoodresearch.substack.com/p/getting-50-sota-on-arc-agi-with-gpt>

<!--
scikit-learn predictor API: <https://scikit-learn.org/stable/developers/develop.html>
-->

## Homework

<img width=300px src=img/hw.jpg />

**Overview:**
You will use the [HairyTrumpet benchmark suite](https://github.com/mikeizbicki/hairy-trumpet) to evaluate your ragnews program and improve your LLM prompts.

**Details:** TBA

**Due:** ???

