#### Prompt engineering review

Prompt engineering is the practice of designing effective inputs to guide AI models toward desired outputs. It involves:

- **Clarity**: Making instructions clear and unambiguous.
- **Context**: Providing necessary background information.
- **Constraints**: Specifying any limitations or formats.

When working with generative AI models, you'll encounter terms like **tokens**, **embeddings**, and **agents**. Here's a quick overview of these concepts:

- **Tokens**: Tokens are the smallest unit of text in a model. They can be words, characters, or subwords. Tokens are used to represent text data in a format that the model can understand.

- **Embeddings**: Embeddings are vector representations of tokens. They capture the semantic meaning of words and phrases, allowing models to understand relationships between words and generate contextually relevant responses.
	- nothing but an array of floats from a data perspective
	- not use LIKE anymore
	
- **Vector databases**: Vector databases are collections of embeddings that can be used to compare and analyze text data. They enable models to generate responses based on the context of the input data.

- **Agents**: Agents are AI components that interact with models to generate responses. They can be chatbots, virtual assistants, or other applications that use generative AI models to create content.

#### Semantic Kernel (SK)

Semantic Kernel is an open-source SDK that enables developers to integrate generative AI language models into their .NET applications. It provides abstractions for AI services and memory (vector) stores allowing creation of plugins that can be automatically orchestrated by AI. It even uses the OpenAPI standard enabling developers to create AI agents to interact with external APIs.

[![Figure: Semantic Kernel (SK) SDK.](https://github.com/mssa-ccad18/Generative-AI-for-beginners-dotnet/raw/main/01-IntroToGenAI/images/semantic-kernel.png)](https://github.com/mssa-ccad18/Generative-AI-for-beginners-dotnet/blob/main/01-IntroToGenAI/images/semantic-kernel.png)