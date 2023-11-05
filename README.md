# genClientFAKE

Generate SQLite database with fake client

# Version

![](https://img.shields.io/badge/Version%3A-1.0-success)

# Release date

![](https://img.shields.io/badge/Release%20date-Sep%2C%2017%2C%202023-9cf)

# License

![](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)

# Programming language

<img src="https://img.icons8.com/?size=512&id=13441&format=png" width="50"/>

# OS

<img src="https://img.icons8.com/?size=512&id=17842&format=png" width="50"/> <img src="https://img.icons8.com/?size=512&id=122959&format=png" width="50"/> <img src="https://img.icons8.com/?size=512&id=108792&format=png" width="50"/>

# Requirements

```bash
pip install sqlite3 random pycountry faker
```

```python
import sqlite3
import random
import pycountry
from faker import Faker
```

## How to run

```python
  databasename = "fakeClientDATA.db"

  createFakeCustomers(databasename, max_clients=100, max_age=60)
```
