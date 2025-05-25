# My PostgreSQL MCP Server

PostgreSQL MCP Server project for database management and operations.

## 🚀 Features

- 🔗 PostgreSQL database connections
- 📊 Query execution and analysis  
- 🗄️ Database schema management
- 🔒 Row-Level Security (RLS) support
- 📤 Data export/import functionality
- 🔍 Database monitoring and debugging
- 📈 Performance analysis tools

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/LeeInHaeng/my-postgres-mcp-server.git
cd my-postgres-mcp-server

# Install dependencies
pip install -r requirements.txt
```

## 🔧 Configuration

Set up your PostgreSQL connection:

```bash
export POSTGRES_CONNECTION_STRING="postgresql://username:password@localhost:5432/database"
```

## 💻 Usage

### Basic Database Operations
```python
# Connect to database
from postgres_mcp import PostgresMCP

server = PostgresMCP()
server.connect()

# Execute queries
result = server.execute_query("SELECT * FROM users;")
```

### Schema Management
```python
# Get table schema
schema = server.get_schema_info("users")

# Create tables
server.create_table("new_table", columns=[...])
```

## 📁 Project Structure

```
my-postgres-mcp-server/
├── src/
│   ├── postgres_mcp/
│   │   ├── __init__.py
│   │   ├── server.py
│   │   └── utils.py
├── tests/
├── requirements.txt
└── README.md
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

MIT License

---

**Last Updated**: 2025-05-25
