# PlayWright

Playwright test project for checking Daraz product search results and prices.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install
```

## Run Tests

```powershell
pytest
```

Run the Daraz price comparison tests in Microsoft Edge:

```powershell
pytest .\tests\test_price_comparision.py --browser chromium --browser-channel msedge --headed
```
