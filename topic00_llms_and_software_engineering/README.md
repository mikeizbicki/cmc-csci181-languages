# Topic 0: LLMs and Software Engineering

<img src=img/chatgpt.png width=300px />

**Learning objectives:**

1. How to interface with an LLM from python
1. Understand 2 common security mistakes with LLMs
    1. key leaking
    1. prompt injection
1. Participate in an ongoing CTF security challenge

## Homework

We will write a simple program to summarize an input document.

I will do most of the steps in class, and you get to follow along.

### Step 0: Background Stuff

Create an account and API key at <https://groq.com/>.
Groq is a [pre-revenue LLM startup](https://www.youtube.com/watch?v=BzAdXyPYKQo) focused on developing faster hardware to compete with NVIDIA.

### Step 1: Creating a project

The following steps walk through the standard way to start a new python project.
You should develop the habit of going through these steps on all the work you do.

Create a new project folder called `docsum`.
```
$ mkdir docsum
$ cd docsum
$ git init
```

Create a python virtual environment for packages.
```
$ python3 -m venv venv
$ . ./venv/bin/activate
$ echo venv > .gitignore
```

Install packages.
```
$ pip3 install groq
$ pip3 freeze > requirements.txt
```

Commit to git.
```
$ git add .
$ git commit -m 'init'
```

### Step 2: Get a Basic Example Working

The groq API has a basic usage example here: <https://github.com/groq/groq-python#usage>

Groq is also compatible with the openai api: <https://console.groq.com/docs/openai>

### Step 3: Create the Document Summarizer

Create a file `docsum.py` that:
1. takes a file (of any type) as a command line argument
1. summarizes that file using the Groq API

> **Useful links:**
>
> 1. <https://docs.python.org/3/library/argparse.html>
> 1. <https://github.com/btimby/fulltext>
>
> <img src=img/google.jpg width=300px />

Create a `README.md` file.
1. The file should explain what your `docsum.py` file does and how to use it.
1. The file should use reasonable markdown styling.
    (Especially with code blocks vs inline code.)

Create a new github project for your repo.  Commit and upload all of your changes.

Submit the link to your github repo on sakai.

## Stupid Mistakes Programmers Make With LLMs

### Mistake 1: Leaking API keys

<img src=img/apikey.jpg width=300px /> <img src=img/api2.webp width=300px />

Very common support request on the OpenAI forums:
1. <https://community.openai.com/t/key-leaked-unexpectedly-any-possible-reason/280948>
1. <https://community.openai.com/t/my-api-is-getting-leaked-need-advice/280564>
1. <https://community.openai.com/t/api-key-stolen-charged-lost-of-anybody-help-me/390240>
1. <https://community.openai.com/t/someone-used-my-api-key-and-used-up-all-my-limit/774218>

Tools for stealing API keys:
1. <https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/API%20Key%20Leaks>

### Stupid Mistake 2: Trusting User Input

<img src=img/prompt.png width=600px />

Read the following links:
1. Prompt injection attacks against ChatGPT 3: <https://simonwillison.net/2022/Sep/12/prompt-injection/>
1. Data Exfiltration from Slack AI via indirect prompt injection <https://promptarmor.substack.com/p/data-exfiltration-from-slack-ai-via>
   
   and the corresponding hacker news post <https://news.ycombinator.com/item?id=41302597>

   > **NOTE:**
   > This attack was announced 20 August 2024.

## Capture the Flag

<img src=img/ctf.png width=300px />

Solve as much as you can of the CTF at <https://invariantlabs.ai/ctf-challenge-24>.
You should be able to solve at least the "playground" level.

> **NOTE:**
> This is a real, currently active, CTF challenge.
> It started in August 5th and runs until September 2nd.

> **NOTE:**
> There is no grade attached to this assignment.

<!--
    1. <https://verse.systems/blog/post/2024-03-19-a-ctf-challenge-for-llms-for-code-analysis/>
    1. <https://github.com/dhammon/ai-goat>
-->
