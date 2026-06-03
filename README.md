# Euro Monitor

Automated data acquisition pipeline · Python · Scrapy · Schedule · SMTPlib

---

## Overview

Scheduled web scraping pipeline that monitors the EUR/BRL exchange rate from Investing.com, extracts the current quote at configurable intervals, and delivers automated email alerts with the latest value. Demonstrates a complete autonomous data acquisition loop — polling, extraction, and notification — with no manual intervention required after startup. The architecture mirrors industrial sensor monitoring pipelines: periodic data collection, threshold-based or time-based alerting, and delivery to stakeholders.

---

## Technical Highlights

**Scheduled autonomous execution**
`schedule` drives periodic Scrapy crawl invocations at a configurable interval (default: 1 minute), running indefinitely without operator input. The same scheduler-over-worker pattern is used in industrial data collectors that poll field devices or OPC-UA servers on a fixed cycle.

**Scrapy-based data extraction**
A dedicated Scrapy spider handles HTTP request, HTML parsing, and data extraction from the Investing.com quote page. Scrapy's middleware stack provides automatic retry, throttling, and user-agent management — equivalent to robust communication layers in industrial protocol drivers (Modbus, OPC-UA) that handle retries and timeouts transparently.

**Automated email notification via SMTPlib**
Extracted values are dispatched by email using Python's native `smtplib`, with no external notification service dependency. Demonstrates the same alert delivery pattern used in industrial alarm management systems that route threshold breach notifications to maintenance teams.

**Process isolation via subprocess**
Each scheduled run launches the Scrapy spider as an independent OS process (`os.system`), isolating crawler state and preventing memory accumulation across long-running cycles. Mirrors watchdog-supervised process models in industrial edge software where worker processes are restarted cleanly on each cycle.

**Zero-dependency scheduler**
The orchestration layer uses only the Python standard library (`os`, `time`) plus `schedule`, keeping the runtime footprint minimal — suitable for deployment on resource-constrained industrial PCs or edge gateways.

---

## Stack

Python 3.x · Scrapy · schedule · smtplib · os · time

---

## Installation

```bash
git clone [https://github.com/YOUR_USER/euro-monitor](https://github.com/Phernando82/monitora_euro.git)
cd euro-monitor
pip install -r requirements.txt
```

Configure SMTP credentials and target email in the spider settings, then:

```bash
python scheduler.py
```

---

## Pipeline

```
scheduler.py starts
      │
      ▼
schedule.every(N).minutes
      │
      ▼  ← runs on each tick
os.system('scrapy crawl eurobot')
      │
      ▼
Scrapy spider → HTTP request → Investing.com
      │
      ▼
HTML parsed → EUR/BRL rate extracted
      │
      ▼
smtplib → email dispatched with current value
      │
      ▼
sleep(1) → back to schedule loop
```

---

## Configuration

| Parameter | Location | Description |
|---|---|---|
| Crawl interval | `scheduler.py` | `schedule.every(N).minutes` |
| Target URL | `euro_spider/spiders/` | Investing.com EUR/BRL page |
| SMTP host / port | Spider settings | Email server credentials |
| Recipient address | Spider settings | Notification target |

---

## Relevance to Industry 4.0

The polling → extract → notify pipeline demonstrated here is the foundational pattern of industrial condition monitoring systems:

- **Scheduled autonomous polling** → periodic reading of sensors, energy meters, or OPC-UA nodes without operator intervention; the basis of predictive maintenance data collection
- **Scrapy middleware stack** → mirrors protocol driver abstraction layers (Modbus TCP, OPC-UA) that handle retries, timeouts, and connection management transparently
- **Automated email alerting** → industrial alarm notification pipelines that route out-of-threshold events to maintenance or operations teams via email, SMS, or messaging platforms
- **Process isolation per cycle** → watchdog-supervised worker restart pattern used in industrial edge agents to prevent state accumulation and ensure clean execution on each poll cycle
- **Minimal runtime footprint** → deployment profile suitable for industrial PCs, Raspberry Pi gateways, or embedded Linux devices running alongside PLC communication software

---

## License

MIT · Data sourced exclusively from the public-facing Investing.com quote page.
