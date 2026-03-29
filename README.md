# FastAPI vs Django: Performance Benchmarking Study

## Comparative Analysis of Performance, Scalability, and Concurrency

---

## Overview

This repository presents a controlled benchmarking study comparing the performance characteristics of:

* **FastAPI** (ASGI-native, asynchronous)
* **Django** (primarily synchronous, with ASGI support)

The objective is to evaluate how both frameworks behave under varying levels of concurrent load in a standardized environment.

---

## Evaluation Metrics

The following metrics were measured:

* **Throughput** (requests per second)
* **Latency** (mean, median, 95th percentile)
* **Error rate**
* **Scalability under concurrent load**

---

## Key Findings

* FastAPI achieves **60–95% higher throughput** than Django
* Up to **9× lower tail latency**
* Near-zero error rates under high concurrency
* Django exhibits **saturation under high load** (single worker)
* Increasing worker count significantly improves Django performance

---

## Experimental Setup

| Component   | Specification  |
| ----------- | -------------- |
| CPU         | Intel i5-8350U |
| RAM         | 16 GB DDR4     |
| OS          | Windows 11     |
| Python      | 3.14.2         |
| Server      | Uvicorn        |
| Load Tool   | Locust         |
| Environment | Localhost      |

---

## Architecture Overview

### FastAPI

* ASGI-native architecture
* Async/await concurrency model
* Event-loop driven execution
* Pydantic-based validation

### Django

* Synchronous request handling (core)
* WSGI (default execution model)
* ASGI support via adapter
* Thread/process-based concurrency

---

## Repository Structure

```
.
├── fastapi_backend/
├── django_backend/
├── databases/
├── stats/
├── locustfile.py
└── README.md
```

---

## API Endpoints Tested

```
GET     /tasks
GET     /tasks/{id}
POST    /tasks
PUT     /tasks/{id}
PATCH   /tasks/{id}
DELETE  /tasks/{id}
```

---

## Running the Benchmark

### 1. Clone the Repository

```bash
git clone https://github.com/HimadriJoshii/lctresearch.git
cd lctresearch
```

### 2. Run FastAPI

```bash
cd fastapi_backend
uvicorn main:app --workers <num_workers>
```

### 3. Run Django

**ASGI:**

```bash
uvicorn project.asgi:application --workers <num_workers>
```

**WSGI:**

```bash
uvicorn project.wsgi:application --workers <num_workers>
```

### 4. Run Load Tests

```bash
cd locust_tests
locust
```

Open: http://localhost:8089

---

## Benchmark Configuration

| Parameter | Values       |
| --------- | ------------ |
| Users     | 10, 50, 100  |
| Workers   | 1, 4         |
| Ramp-up   | 10 users/sec |
| Duration  | ≥ 60 sec     |
| Runs      | 3            |

---

## Sample Results (100 Users)

| Framework     | Req/sec | 95th Latency | Errors |
| ------------- | ------: | -----------: | -----: |
| FastAPI       |   37.83 |       780 ms |     0% |
| Django (ASGI) |   19.98 |      5700 ms |  3.45% |
| Django (WSGI) |   19.35 |      7200 ms |  4.88% |

---

## Key Insights

* FastAPI efficiently handles concurrency via an event-driven model
* Django experiences request queue saturation under load
* Worker scaling is critical for improving Django throughput
* ASGI support does not make Django fully asynchronous

---

## Use Case Recommendations

### Use FastAPI for:

* High-performance APIs
* Machine learning model serving
* Microservices architectures
* Real-time systems

### Use Django for:

* Full-stack web applications
* Admin dashboards / CMS
* Rapid development workflows
* Moderate traffic systems

---

## Hybrid Architecture Recommendation

A practical production approach:

* **Django** → Admin panel, ORM, business logic
* **FastAPI** → High-performance and async APIs

---

## Research Paper

## Research Paper

A detailed report of this benchmarking study is available here:

🔗 [A Comparative Analysis of FastAPI and Django Frameworks](https://ijsrem.com/download/a-comparative-analysis-of-fastapi-and-django-frameworks-evaluating-performance-scalability-and-concurrency-efficiency-in-modern-web-applications/)

---

## Dataset

Benchmark results are available in:

```
/stats/
```

---

## Limitations

* No database performance benchmarking
* Localhost-only testing environment
* Limited worker configurations
* No authentication or middleware-heavy workloads

---

## Acknowledgments

* FastAPI
* Django
* Uvicorn
* Locust

---

## Contact

**Himadri Joshi**
GitHub: https://github.com/HimadriJoshii

---

## Support

If you find this work useful, consider giving the repository a ⭐
