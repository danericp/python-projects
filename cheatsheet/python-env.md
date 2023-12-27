# Python CLI and Modules Cheat Sheet

A collection of useful Python References for CLI and its modules.

## Table of Contents

- [Command Line Interface](#command-line-interface)
- [Module - HTTP Server](#module---http-server)
- [Module - Pip](#module---pip)
- [Module - Virtual Environment](#module---virtual-environment)
- [References](#references)

## Command Line Interface

| Command | Description |
|-|-|
| `py -0` | Show installed Python versions. |
| `py -3.9` <br> `py -3.12` | Open a specific version of Python. |

## Module - HTTP Server

| Command | Description |
|-|-|
| `python -m http.server 8000` <br> `python -m http.server 8000 --bind 127.0.0.1 ` | Start an HTTP Server (Python 3.x) |
| `python -m SimpleHTTPServer 8000`  | Start an HTTP Server (Python 2.x) |

### Python 3.x
Both port and bind address are optional. For more details, please read the [official docs](https://docs.python.org/3/library/http.server.html).

## Module - Pip

| Command | Description |
|-|-|
| `python3 -m pip check` | Check Package if compatible |
| `python3 -m pip freeze > requirements.txt` | Create Package List |
| `python3 -m pip show package_name` | Get Package Information |
| `python3 -m pip list` <br> `python3 -m pip list \| grep package_name` | List Packages |
| $ cd /path/to/your/local/python/package <br> python3 -m pip install -e . | Install Package - Editable Mode |
| `pip install package_name` <br>  `pip3 install package_name` <br> `python3 -m pip install package_name` <br> `python3 -m pip install django==2.2.26` <br> `python3.6 -m pip install package_name` | Install Package - From specific python module |
| `pip3 install --no-cache-dir -r requirements.txt` <br> `python3 -m pip install -r requirements.txt` | Install Modules - From file |
| `python3 -m pip search <search_term>` | Search Package (Deprecated) |
| `python3 -m pip freeze > requirements.txt && <br> python3 -m pip uninstall -r requirements.txt -y` <br> `python3 -m pip uninstall -y -r <(pip freeze)` | Uninstall Package - From list |
| `pip uninstall package_name` <br> `pip3 uninstall package_name` <br> `python3 -m pip uninstall package_name` <br> `python3.6 -m pip uninstall package_name` | Uninstall Package - From specific python module |
| `python3 -m pip install package_name --upgrade` | Upgrade a Package |

### Example File - requirements.txt

```
Flask==2.2.3
MarkupSafe==2.1.2
Werkzeug==2.2.3
itsdangerous==2.1.2
psutil==5.8.0
plotly==5.5.0
tenacity==8.0.1
boto3==1.9.148
kubernetes==10.0.1
```

## Module - Virtual Environment

| Command | Description |
|-|-|
| `venv\Scripts\activate` <br> `source venv\bin\activate` | Virtual Environment - Activate (Windows) <br> Virtual Environment - Activate (MAC/Linux) |
| `python -m venv <Environment Name>` <br> `python -m venv my-test` <br> `python -m venv venv` | Virtual Environment - Create |
| `deactivate` | Virtual Environment - Deactivate |
| (venv) `python -m pip install <package-name>` <br> (venv) `python -m pip install django==2.2.26` | Virtual Environment - Install a Package |

## References

- [PyPI](https://pypi.org/)
- [AnvilEight Blog](https://anvileight.com/blog/posts/simple-python-http-server/#google_vignette)