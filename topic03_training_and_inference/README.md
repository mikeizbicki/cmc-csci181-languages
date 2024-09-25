# Training and Inference

<img width=400px src=img/magic.webp />

**Review (of engineering concepts):**
1. Don't disclose API keys
1. Prompt Engineering
    1. Prompt Injection
1. Retrieval Augmented Generation
    1. Focus the LLM on "new" data
    1. Cheaper/faster than finetuning
1. Tests
    1. Separate your LLM code from non-LLM code as much as possible
    1. Doctests on non-LLM code
    1. Run benchmarks (that you've created) on LLM code

**News:**

1. (2024-09-19) Anthropic announces "contextual retrieval" RAG method <https://www.anthropic.com/news/contextual-retrieval>

<!--
<img width=400px src=img/parrot.jpeg />

**Claim:**

1. LLMs are not "just predicting the next token"

<img width=400px src=img/change-my-mind.jpg />
-->

**Goal:**

Have enough background on LLM training and inference to read easy research papers

**Homework:**

1. Read [The Pitfalls of Next Token Prediction](https://arxiv.org/abs/2403.06963) (ICML 2024)
    1. We will discuss the paper next Monday (30 Oct)
        1. No class recording
        1. Please be present and on time
    1. Spend 2-5 hours on the paper
    1. You won't understand everything
        1. Identify the parts that are the most important
        1. Do you best to understand those parts
1. (optional) Watch [Andrew Ng](https://www.andrewng.org/)'s lecture [Career Advice / Reading Research Papers](https://www.youtube.com/watch?v=733m6qBH-jI&t=146s)
    
    or [just read the summary notes](https://forums.fast.ai/t/how-to-read-research-papers-andrew-ng/66892)

**Foreshadowing:**

In 2ish weeks, we will start covering the internal math behind transformers.

1. We will not implement transformers from scratch in this class.

1. If you would like to do this, then watch: [Andrej Karpathy](https://karpathy.ai/)'s video [Let's build GPT: from scratch, in code, spelled out](https://www.youtube.com/watch?v=kCc8FmEb1nY)

My treatment will be very heterodox.
I recommend you watch one of the orthodox explanations below first:

1. StatQuest's [Transformer Neural Networks, ChatGPT's foundation, Clearly Explained!!!](https://www.youtube.com/watch?v=zxQyTK8quyY)

1. 3Blue1Brown's [Deep Learning Series](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi).  Specifically:
    1. [Part 5: What is a GPT?  Visual Intro to Transformers.](https://www.youtube.com/watch?v=wjZofJX0v4M&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi&index=5)
    1. [Part 6: Attention in Transformers, Visually Explained](https://www.youtube.com/watch?v=wjZofJX0v4M&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi&index=6)
    1. [Part 7: How might LLMs store facts](https://www.youtube.com/watch?v=wjZofJX0v4M&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi&index=7)

1. (advanced) Andrej Karpathy's [Introduction to Transformers](https://www.youtube.com/watch?v=XfpMkf4rD6E)

## Training

The standard method for training **generative** language models is **teacher forcing**.

1. Synonyms include: next token prediction, autoregressive model, maximum likelihood

1. First described in 1989 *Neural Computation* paper [A learning algorithm for continually running fully recurrent neural networks.](https://direct.mit.edu/neco/article-abstract/1/2/270/5490/A-Learning-Algorithm-for-Continually-Running-Fully)

    > An interesting technique that is frequently used in dynamical supervised learning tasks

1. Can be applied to any model architecture, e.g.
    1. RNN/LSTM/GRU
    1. Transformers
    1. Mamba/RWKV
    <!-- 1. RWKV (<https://www.rwkv.com/>) -->

1. Commonly used not just on text, but on any "sequence-like" task.

    [According to Andrej Karpathy](https://x.com/karpathy/status/1835024197506187617):

    > It's a bit sad and confusing that LLMs ("Large Language Models") have little to do with language; It's just historical. They are highly general purpose technology for statistical modeling of token streams.

1. Used for computational convenience.

    1. "Everyone" knows it's not correct.

    1. <a href="https://www.youtube.com/watch?v=YEUclZdj_Sc">Ilya Sutskever: Why next-token prediction is enough for AGI <br/><img width=400px src=https://img.youtube.com/vi/YEUclZdj_Sc/maxresdefault.jpg /></a>

1. Alternatives
    1. All more computationally intensive
    1. A lot of similar ideas to literature in:
        1. reinforcement learning
        1. robotic control
        1. timeseries analysis

        There is basically no cross-communication of terms/ideas.

    1. Examples:
        1. (NeurIPS 2015) Scheduled Sampling <https://arxiv.org/abs/1506.03099>
            1. Won MSCOCO captioning competition
            1. mPLUG LLM SOTA <https://paperswithcode.com/sota/image-captioning-on-coco-captions>
        1. (ICLR 2016) How (not) to train your generative model <https://arxiv.org/abs/1511.05101>
        1. (NeurIPS 2016) Professor Forcing <https://papers.neurips.cc/paper/2016/hash/16026d60ff9b54410b3435b403afd226-Abstract.html>
     1. GPT-1 released in 2018 shows good results using only teacher training

1. Modern models are not exclusively trained with teacher forcing.

    1. The current training pipeline is

        1. unsupervised pretraining 
            1. very large training datasets
            1. "always" uses teacher forcing

                example exception: mPLUG <https://arxiv.org/abs/2205.12005v2>
        1. supervised finetuning
            1. small datasets
            1. "usually" uses teacher forcing
                1. [APIs provided by OpenAI API only use teaching forcing](https://platform.openai.com/docs/guides/fine-tuning)
                1. [Anthropic also has some support, but it's worse than OpenAI](https://www.anthropic.com/news/fine-tune-claude-3-haiku)
            1. other training methods include contrastive learning

                (NeurIPS 2022) A Contrastive Framework for Neural Text Generation <https://openreview.net/forum?id=V88BafmH9Pj>

                (ICLR 2022) CoNT: Contrastive Neural Text Generation <https://openreview.net/forum?id=mjVZw5ADSbX>

                ...

                and many more

        1. reinforcement learning with human feedback (RLHF)

            <https://huyenchip.com/2023/05/02/rlhf.html>

            Andrej Karpathy: ["RLFH is barely RL"](https://x.com/karpathy/status/1821277264996352246)

    1. The standard picture for describing this pipeline is the [Shoggoth](https://en.wikipedia.org/wiki/Shoggoth):

        <img width=400px src=img/2-shoggoth.jpg />

    1. Other finetuning enables predicting multiple tokens at a time for faster inference
        1. Medusa Heads <https://github.com/FasterDecoding/Medusa>
        1. EAGLE <https://github.com/SafeAILab/EAGLE>
        1. CLLMs <https://hao-ai-lab.github.io/blogs/cllm/>

<!--
Tokenization:

1. Tutorial <https://simonwillison.net/2023/Jun/8/gpt-tokenizers/>
1. OpenAI playground <https://platform.openai.com/tokenizer>

<img width=400px src=img/training-data.webp />
-->

<!--
### Training Problems

<img width=400px src=img/training1.png />

[Pre-atomic steel](https://en.wikipedia.org/wiki/Low-background_steel)
-->

### Main Non-Technical Criticism: LLMs are just Stochastic Parrots

<img width=400px src=img/parrot2.jpg />

Term coined by [Emily Bender](https://faculty.washington.edu/ebender/) (linguistics professor) in the paper: ["On the Dangers of Stochastic Parrots: Can Language Models Be Too Big? 🦜" published at Fairness, Accountability and Transparency (FAccT)](https://dl.acm.org/doi/abs/10.1145/3442188.3445922)

1. [Wikipedia has some juicy details](https://en.wikipedia.org/wiki/Stochastic_parrot#Origin_and_definition)

    1. 4 google coauthors are on the paper, and google asks them to remove their names.

        > According to Jeff Dean, the paper "didn't meet our bar for publication". 

    1. Co-lead of Google's Ethical AI team [Timnit Gebru](https://en.wikipedia.org/wiki/Timnit_Gebru) refuses. 

        > In response, Gebru listed conditions to be met, stating that otherwise they could "work on a last date".

        > Shortly after, Gebru received an email saying that Google was "accepting her resignation"

    1. Fellow googler <a href="https://en.wikipedia.org/wiki/Margaret_Mitchell_(scientist)">Margaret Mitchell</a> stayed on the publication under pseudonym Shmargaret Shmitchell and is not fired.

    1. Lots of scandal on social media: <https://www.reddit.com/r/MachineLearning/comments/nvzib3/d_what_really_happened_when_google_ousted_timnit/>

Philosophical debate over whether teacher forcing is sufficient continues to be waged in the blogoverse:

1. My bet: AI Size Solves Flubs: <https://www.astralcodexten.com/p/my-bet-ai-size-solves-flubs>

1. Gwern's GPT3 Nonfiction: <https://gwern.net/gpt-3-nonfiction#why-deep-learning-will-never-truly-x>

1. The Stochastic Parrot Hypothesis is debatable for the last generation of LLMs: <https://www.lesswrong.com/posts/HxRjHq3QG8vcYy4yy/the-stochastic-parrot-hypothesis-is-debatable-for-the-last>

1. Has Sam Altman gone full Gary Marcus? <https://garymarcus.substack.com/p/has-sam-altman-gone-full-gary-marcus>

Tweets from OpenAI:

<img width=600px src=img/parrot-sama.png />

<img width=600px src=img/ngo-tweet.webp />

<!--
<img width=600px src=img/lecun.png />
Yann LeCun: <https://x.com/ylecun/status/1801018194121118103>
-->

<!--
Good mathematical contributions go mostly ignored:
1. (ICML 2024) The Pitfalls of Next Token Prediction <https://arxiv.org/abs/2403.06963>

1. Criticisms
    1. (unpublished 2023) Autoregressive Modeling with Lookahead Attention <https://arxiv.org/abs/2305.12272>
    1. (NeurIPS 2020) Consistency of a recurrent language model with respect to incomplete decoding.
        > Autoregressive models may assign non-zero probability to infinite length strings.
    1. Trained on `A equals B` doesn't imply it understands `B equals A` <https://arxiv.org/abs/2309.14402>, <https://arxiv.org/abs/2311.07468>
-->

### Aside: Energy Consumption

Training an LLM uses negligible energy.

1. LLama3.1 used 39.3x10^6 GPU hours * 700W/GPU = 27.50 GWhr

    <https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md>

1. US energy consumption in 2023 was 93.59 quads * 293071.0702 GWhr/quad = 27.4x10^6 GWhr

    <https://www.eia.gov/energyexplained/us-energy-facts/>

1. So training LLama3.1 required 0.0001% of US electricity consumption in 2023.

    It's also about the same as powering 1000 homes for 1 year.

Compare to cryptocurrency mining:

1. Used 170 TWh - 390 TWh in 2023

   0.6%-2.3% of all US electricity consumption

    <https://www.eia.gov/todayinenergy/detail.php?id=61364>

## Sampling / Decoding / Inference Algorithms

<img width=400px src=img/decoding.jpeg />

1. Greedy Search

    Always pick the most probable next word.

    <img width=400px src=img/nextword.jpg />

1. Top Sampling

    Randomly sample from the probability distribution of next words.

    1. Temperature of 0 is greedy search.
        Higher temperature is more random.

        1. Common values are: 0 (no sampling), 0.8, 1

    1. Two methods of eliminating "obviously bad" samples.
        1. Top-k

            Common values are k=10,100,1000
            
        1. Top-P (also called Nucleus Sampling)
            
            Common values are P=0.5 or 1 (to disable)
    
            (ICLR 2020) <https://arxiv.org/abs/1904.09751>

1. (constrained) Beam search

    1. Advantages:
        1. Allow the model to look multiple tokens ahead when performing its inference
    1. Disadvantages:
        1. Very slow on non-local models
        1. Very expensive ($$$)
        1. No streaming support
    1. Details: <https://huggingface.co/blog/constrained-beam-search>
    1. Groq:
        1. [Groq does not support the primitives needed for arbitary constraints on your own machine](https://console.groq.com/docs/openai#currently-unsupported-openai-features)
        1. "JSON" mode uses constrained sampling this internally

            Not published in their documentation,
            but it's the only "reasonable" way to implement this feature.

            The lack of streaming support 
<!--
**The popular conception of "LLM as stochastic parrot" is 100% wrong!!!**

1. LLMs are not JUST a probability distribution over the next token.

1. They also include an algorithm for sampling from that probability distribution.
-->

### LLM world vs "traditional" sampling

Professors Sarah Canon and Mark Huber both work in "traditional" sampling fields.

They care about convergence proofs.
We don't.

<img width=400px src=img/converge.jpeg />

<!--
<img width=400px src=img/mcmc-meme.jpeg />

<img width=400px src=img/converge2.jpeg />

<img width=400px src=img/converge3.jpeg />
-->

### Libraries

Things I think are boring:
1. LangChain <https://python.langchain.com/docs/introduction/>
1. DSpy <https://github.com/stanfordnlp/dspy>
1. Ragas <https://docs.ragas.io/en/stable/>

Things I think are cool:
1. Language Model Query Language (LMQL)
    1. "SQL for LLMs"
    1. PLDI 2023 <https://arxiv.org/abs/2212.06094>
    1. Documentation <https://lmql.ai/>

