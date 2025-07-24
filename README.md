# StackScribe AI

A smart note-taking system that automatically suggests relevant links between your markdown notes using vector search and semantic similarity.

## Features

- **Automatic Link Suggestions**: Uses AI to suggest relevant connections between your notes
- **Vector Search**: Leverages Qdrant vector database for fast semantic search
- **Cross-Encoder Reranking**: Improves suggestion quality with advanced reranking
- **Heuristic Boosting**: Applies domain-specific rules to enhance suggestions
- **Markdown Support**: Works with your existing markdown note collection

## Prerequisites

- Python 3.8+
- Docker Desktop
- Git

## Setup

### 1. Clone and Setup Environment

```bash
git clone <your-repo-url>
cd stackscribe-ai

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install qdrant-client sentence-transformers nltk markdown tqdm
```

### 2. Setup Qdrant Database

The project uses Qdrant as a vector database. You need to run it in Docker:

```bash
# Start Qdrant container with proper port binding
docker run -d -p 6333:6333 -p 6334:6334 --name qdrant qdrant/qdrant:latest
```

**Important**: Make sure the ports are properly bound. If you see `Ports: {}` when running `docker ps`, the ports aren't exposed and you'll get connection errors.

To verify Qdrant is running correctly:
```bash
# Check if container is running with proper port binding
docker ps | grep qdrant
# Should show: 0.0.0.0:6333-6334->6333-6334/tcp

# Test connection
curl -X GET http://localhost:6333/collections
```

### 3. Index Your Notes

Before using the link suggester, you need to index your markdown notes:

```bash
# Make sure your virtual environment is activated
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux

# Run the indexing script
python index_notes.py
```

This will:
- Create a `note_chunks` collection in Qdrant
- Process all `.md` files in the `my_notes/` directory
- Split notes into chunks and create vector embeddings
- Store everything in the vector database

## Usage

### Using IPython for Interactive Link Suggestions

1. **Start IPython**:
```bash
# Make sure your virtual environment is activated
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux

# Start IPython
ipython
```

2. **Import and Use the Link Suggester**:
```python
from link_suggester import suggest_links

# Example usage
para = "a method is a function that a class can execute."
suggestions = suggest_links(para, current_note="Method.md")
print(suggestions)

# For a different example
para2 = "polymorphism allows objects to be treated as instances of their parent class"
suggestions2 = suggest_links(para2, current_note="Polymorphism.md")
print(suggestions2)
```

### Understanding the Output

The `suggest_links()` function returns a list of tuples:
- Each tuple contains: `(note_filename, confidence_score)`
- Higher scores indicate more relevant suggestions
- The function automatically excludes the current note from suggestions

Example output:
```python
[
    ('Method.md', 0.85),
    ('Class.md', 0.72),
    ('Function.md', 0.68),
    ('Object.md', 0.45)
]
```

### Configuration

You can modify the behavior by editing the constants in `link_suggester.py`:

- `THRESHOLD`: Minimum confidence score (default: 0.05)
- `TOP_K`: Maximum number of suggestions (default: 8)
- `COLLECTION`: Qdrant collection name (default: "note_chunks")
- `EMBED_MODEL`: Embedding model (default: "nomic-ai/nomic-embed-text-v1")

## Project Structure

```
stackscribe-ai/
├── my_notes/           # Your markdown notes
├── index_notes.py      # Script to index notes into Qdrant
├── link_suggester.py   # Main link suggestion logic
├── hueristics.py       # Heuristic rules for boosting suggestions
├── venv/              # Virtual environment
└── README.md          # This file
```

## Troubleshooting

### Connection Issues

If you get `[WinError 10061] No connection could be made`:

1. **Check if Qdrant is running**:
   ```bash
   docker ps | grep qdrant
   ```

2. **Verify port binding**:
   ```bash
   docker inspect qdrant | grep -i port
   ```
   Should show port mappings, not empty `Ports: {}`

3. **Restart Qdrant with proper ports**:
   ```bash
   docker stop qdrant
   docker rm qdrant
   docker run -d -p 6333:6333 -p 6334:6334 --name qdrant qdrant/qdrant:latest
   ```

### Collection Not Found

If you get `Collection 'note_chunks' doesn't exist`:

1. **Run the indexing script**:
   ```bash
   python index_notes.py
   ```

2. **Verify the collection exists**:
   ```bash
   curl -X GET http://localhost:6333/collections
   ```

### Virtual Environment Issues

Make sure you're using the correct Python environment:
```bash
# Check which Python you're using
which python  # macOS/Linux
where python  # Windows

# Should point to your venv directory
```

## Advanced Usage

### Custom Heuristics

You can modify `hueristics.py` to add custom rules for boosting suggestions based on your specific domain or note structure.

### Different Embedding Models

Change the `EMBED_MODEL` in `link_suggester.py` to use different embedding models. Popular alternatives:
- `sentence-transformers/all-MiniLM-L6-v2` (faster, smaller)
- `BAAI/bge-large-en-v1.5` (higher quality)

### Batch Processing

For processing multiple paragraphs at once, you can create a simple script:

```python
from link_suggester import suggest_links

paragraphs = [
    "a method is a function that a class can execute.",
    "polymorphism allows objects to be treated as instances of their parent class",
    "encapsulation hides internal state and requires all interaction through an object's methods"
]

for i, para in enumerate(paragraphs):
    print(f"Paragraph {i+1}: {para}")
    suggestions = suggest_links(para, current_note="test.md")
    print(f"Suggestions: {suggestions}\n")
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

[Add your license here] 