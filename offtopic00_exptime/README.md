# OpenAI's o1 models and exponential runtime

**tl;dr:**
There exists a trivial algorithm that achieves the same runtime performance benefits of OpenAI's new o1 series models.

### Background

OpenAI [recently released the o1 series of models](https://openai.com/index/learning-to-reason-with-llms/).
Their blog post leads with the following plot,
which shows how these new models can improve performance by 

<img width=600px src=img/compute.webp />

Lots of folk have observed problems with this graph.
The ARC-AGI folks notably [observed that the runtime is exponential, and exponential is really bad](https://arcprize.org/blog/openai-o1-results-arc-prize).

### The new algorithm

Rejection sampling in the context of LLMs looks something like:
```
while True:
    text = model.random_sample()
    if passes_test_cases(text):
        return text
```

### Open Problems

1. What are the conditions that the `random_sample()` method needs to satisfy in order to run in sub-exponential time?

   1. Can any transformer/RNN/etc-based sampling strategy satisfy these requirements?
   1. Is it reasonable that a human might satisfy these requirements? 
