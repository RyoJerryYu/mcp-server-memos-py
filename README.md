# MCP Server Memos 📝

[![PyPI version](https://img.shields.io/pypi/v/mcp-server-memos.svg)](https://pypi.org/project/mcp-server-memos/)
[![Python Version](https://img.shields.io/pypi/pyversions/mcp-server-memos.svg)](https://pypi.org/project/mcp-server-memos/)
[![License](https://img.shields.io/github/license/RyoJerryYu/mcp-server-memos-py.svg)](https://github.com/RyoJerryYu/mcp-server-memos-py/blob/master/LICENSE)
[![smithery badge](https://smithery.ai/badge/@RyoJerryYu/mcp-server-memos-py)](https://smithery.ai/server/@RyoJerryYu/mcp-server-memos-py)

A Python package that provides LLM models with the ability to interact with [Memos](https://github.com/usememos/memos) server through the [MCP (Model Context Protocol)](https://modelcontextprotocol.io/introduction) interface.

## 🚀 Features

- 🔍 Search memos with keywords
- ✨ Create new memos with customizable visibility
- 📖 Retrieve memo content by ID
- 🏷️ List and manage memo tags
- 🔐 Secure authentication using access tokens

## 🛠️ Usage

You can include this package in your config file as bellow, just as you use other Python MCP plugins.

```jsonc
{
  ...,
  "mcpServers": {
    "fetch": { // other mcp servers
      "command": "uvx",
      "args": ["mcp-server-fetch"]
    },
    "memos": { // add this to your config
      "command": "uvx",
      "args": [
        "--prerelease=allow",
        "mcp-server-memos",
        "--host",
        "localhost",
        "--port",
        "5230",
        "--token",
        "your-access-token-here"
      ]
    }
  }
}
```

<details>
<summary>Other ways to use this package</summary>

### 📦 Installation

#### Installing via Smithery

To install mcp-server-memos-py for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@RyoJerryYu/mcp-server-memos-py):

```bash
npx -y @smithery/cli install @RyoJerryYu/mcp-server-memos-py --client claude
```

#### Installing Manually
```bash
pip install mcp-server-memos
```

### Command Line

```bash
mcp-server-memos --host localhost --port 8080 --token YOUR_ACCESS_TOKEN
```

### As a Library

```python
from mcp_server_memos import Config, serve_stdio

config = Config(
    host="localhost",
    port=8080,
    token="YOUR_ACCESS_TOKEN"
)

await serve_stdio(config=config)
```

</details>

## 🔧 Configuration

| Parameter | Description | Default |
|-----------|-------------|---------|
| `host` | Memos server hostname | `localhost` |
| `port` | Memos server port | `8080` |
| `token` | Access token for authentication | `""` |

## 🤝 Available Tools

This MCP server provides the following tools for interacting with Memos:

| Tool Name | Description | Parameters |
|-----------|-------------|------------|
| `list_memo_tags` | List all existing memo tags | - `parent`: The parent who owns the tags (format: memos/{id}, default: "memos/-")<br>- `visibility`: Tag visibility (PUBLIC/PROTECTED/PRIVATE, default: PRIVATE) |
| `search_memo` | Search for memos using keywords | - `key_word`: The keywords to search for in memo content |
| `create_memo` | Create a new memo | - `content`: The content of the memo<br>- `visibility`: Memo visibility (PUBLIC/PROTECTED/PRIVATE, default: PRIVATE) |
| `get_memo` | Get a specific memo by ID | - `name`: The name/ID of the memo (format: memos/{id}) |

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Memos](https://github.com/usememos/memos) - A lightweight, self-hosted memo hub
- [MCP (Model Context Protocol)](https://modelcontextprotocol.io/introduction) - Protocol for LLM model applications
