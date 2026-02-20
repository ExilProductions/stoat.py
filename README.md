# Stoat.py

**Caution:** This project has **no connection** to [MCausc78/stoat.py](https://github.com/MCausc78/stoat.py).

*A Better Stoat Python Wrapper*

**This is W.I.P., it doesnt work until the first release!**
---

## Overview

Stoat.py is a Python wrapper designed for interacting with the Stoat API efficiently and reliably. It simplifies API calls, manages authentication, and provides structured responses using Python data models.

---

## Features

* Fully typed Python models using Pydantic
* Async and sync API calls
* Built-in error handling and validation
* Easy-to-use interface for common Stoat API endpoints

---

## Installation (Comming Soon)

```bash
pip install stoat.py
```

Or install directly from source:

```bash
git clone https://github.com/yourusername/stoat.py.git
cd stoat.py
pip install .
```

---

## Usage

```python
from stoat import StoatClient

client = StoatClient(api_key="YOUR_API_KEY")

# Example: Fetch some data
data = client.get_data("example_endpoint")
print(data)
```

### Async Usage

```python
import asyncio
from stoat import StoatClient

async def main():
    client = StoatClient(api_key="YOUR_API_KEY")
    data = await client.get_data_async("example_endpoint")
    print(data)

asyncio.run(main())
```

---

## Models

All responses are wrapped in Pydantic models. Example:

```python
from stoat.models import ResponseModel

response: ResponseModel = client.get_data("example_endpoint")
print(response.status, response.data)
```

---

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Create a pull request

---

## License

This project is licensed under the MIT License.