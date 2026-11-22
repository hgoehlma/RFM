<p align="center">
  <img src="./assets/RFM.png" width="80">
</p>

# Reasoning-First Methodology (RFM)

**Every complex project fails the same way: the thinking disappears.** Imagine you work on a project for a long period of time. Or a project where the complexity increases over time. You will work on a certain aspect and make decisions and get them right. And then you go back to another element of the project and you realize that you don't recall all the details anymore. Why did you start the project the way you did it? What motivated you in the first place? What choices did you reject and why? What were you assuming at the time? You come to realize that you can't remember it all.

All you have in front of you is what you created. And if you are lucky, some notes, photos, documents, slides maybe.

Next time you revisit your project or other parts of your project you will have to guess or try to remember or try to reconstruct. And the longer ago it was, the worse. And imagine a project with multiple people. If you have ever joined a project and had no idea why anything was built the way it was or if you have ever watched a team reconstruct a decision from scratch because nobody wrote down why they made it to begin with, this may be for you.

## What RFM does

Before any work starts you think it through. For this, RFM introduces an LLM as a strong partner. Jointly you start by writing down the why, your intentions, in a reasoning document. The actual outcome of your project - a slide deck or plan or software code - is created later.

This reasoning document has sections - like assumptions and what would break them, boundaries, but also open questions. It is essential that this document is honest. It does not defend, but describes what you think, so anyone can challenge it. It is a "living" document as it changes when conditions change or assumptions break. The reasoning documents retain the same section structure at every level, from the whole project down to each of its parts. You can compare it with a country map and a street map. They differ in resolution but they follow the same navigational rules and they still connect to each other.

## An example: a home battery

A practical example I used RFM with Claude for: should I buy a home battery as net metering stops in the Netherlands in 2027? I had the assumption that the charging pattern of my car was predictable enough to properly size the battery. This would break if my commute or the vehicle changed. And it broke when we decided to replace our fossil fuel car with a second electric one. Then one car would often be plugged in to receive extra solar power. I had the thinking ready. There was no need to start all over. I decided not to buy and the thinking ended in building nothing. Another argument that contributed to the decision was the limited efficiency versus the current costs of today's batteries. This example highlights that RFM is not only for larger projects but can also be used for smaller, everyday decisions.

## Why now, and why with an LLM

I think you need to shift your time investment from building to thinking. What used to take weeks to build can now be done in minutes via LLMs. That is why you need to invest in retaining your thinking and curating it continuously.

Because of how LLMs are trained today, they are faced with a pull to agree and produce. Yet, RFM asks the LLM to be a partner and push back on weak reasoning. At the same time you have your own pull: you are tempted to accept what reads well and move on when you would need to understand and challenge the thinking. RFM provides a guide for your side too ([`RFM_human_guide.md`](https://github.com/hgoehlma/RFM/blob/main/RFM_human_guide.md)).

Creating the result of the thinking is the second role of the LLM. The LLM hands a fresh LLM only your documents. The fresh LLM carries out the work and notes where it had to guess. Then the result is jointly discussed with the LLM in the main session and your documents are adjusted before any changes to the produced work.

## Background

Looking at recent developments people start to understand the importance of retaining the why because an LLM can only invent it. Several approaches have been developed whereby the LLM questions you to understand what you are working on. Some start out by writing the specs first and others record the decisions they have taken. The components are there, but they are not together ([`RFM_top_level_reasoning.md`](https://github.com/hgoehlma/RFM/blob/main/RFM_top_level_reasoning.md) shows how RFM brings them together). RFM tackles this problem by focusing on the source documents first. These reasoning documents bring the different sections together and are continuously updated. And they are the sources from which the results are derived. Furthermore, RFM aims to establish a partnership where you and the LLM both contribute and push back during the creation and curation of the source documents.

Simon Wardley emphasized that assumptions about position, movement and relationships need to be made visible. That is why RFM captures assumptions. RFM goes one step further and also captures what would break them. Peter Naur highlighted in 1985 that a program's theory only lives in the heads of the people who built it. When they leave the project, this knowledge will leave with them. He also believed that this theory cannot be fully written down. I think enough of the knowledge can be written down so that work can be created from it. And successful derivation shows it.

## Who it's for, and who it isn't

Do you want to build faster with ever more agents and ever-increasing agent autonomy? Likely RFM is not for you. RFM is a vehicle, not a prescription. The reasoning comes first. What you build on top of it is yours.

And in case you wonder: the acronym for the methodology was chosen deliberately. Anyone who recognizes the older expansion already knows what this methodology thinks you should do before touching anything.

## Where to start

Have a look at [`RFM_setup_guide.md`](https://github.com/hgoehlma/RFM/blob/main/RFM_setup_guide.md). I am using RFM successfully together with both Claude Code (Sonnet 5 or higher) and OpenAI's Codex (GPT models 5.5 or higher). The environment for RFM needs to run on your local computer and not in the cloud. If you want to learn more, have a look at [`RFM_glossary.md`](https://github.com/hgoehlma/RFM/blob/main/RFM_glossary.md) for the glossary and [`RFM_map.md`](https://github.com/hgoehlma/RFM/blob/main/RFM_map.md) for the list of all documents in the project.

The approach is in active development. Every document is living, versioned and continuously curated.

---

## License

[![CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

© 2026 Hinrich W.H. Göhlmann

*Developed in collaboration with Claude (Anthropic), acting as partner throughout.*
