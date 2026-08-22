## 1. Problem Statement
The serviced-apartment company receives customer reviews through platforms such as Booking.com. Manually reviewing and assessing a large number of reviews can take time and makes it difficult to quickly identify the overall sentiment of customer feedback. This system is intended to automatically analyse reviews and classify them as positive or negative, helping the organisation process customer feedback more efficiently and identify overall customer sentiment. Without such a system, reviews would continue to require more manual analysis, making it harder to process feedback consistently at larger volumes.

## 2. System Overview
The system is designed to analyse customer reviews and classify their sentiment as either positive or negative using an OpenAI language model. The application loads its API credentials, creates an OpenAI client, records the start of the API request, sends the review for analysis, and records the result or any error before exporting an execution trace. In the recorded test run, the API request was unsuccessful because the account had insufficient quota, and this failure was captured in `traces/run_latest.json`.

## 3. Component Breakdown
### 3.1 LLM Client

**What it does:**  
Sends structured prompts to the model API and returns completions.

**Implementation:**  
OpenAI Python SDK. API key loaded from an environment variable. Model specified at call time.

**Why this choice:**  
The OpenAI Python SDK provides a simple Python interface for authenticated API calls while keeping the underlying HTTP communication separate from the application logic.

**Failure mode:**  
AuthenticationError if the key is missing or expired. APIConnectionError on network failure.

**KSB evidence:**  
K8 — third-party API dependency with cost, uptime and data-handling implications.


### 3.2 Tool Gateway

**What it does:**  
Exposes an allowlisted set of callable functions to the LLM.

**Implementation:**  
JSON tool schemas passed in the API call. Only whitelisted function names are dispatched.

**Why this choice:**  
A schema-based tool gateway lets the model request only explicitly defined functions, while the application retains control over which functions are actually dispatched.

**Failure mode:**  
If the LLM requests an unlisted function, a tool_not_found response is returned to the model rather than allowing an unauthorised function to execute.

**KSB evidence:**  
K9 — function calling architecture. S27 — controlled tool exposure as a business control.


### 3.3 Cost Guard

**What it does:**  
Estimates cost before each API call and blocks calls that exceed the monthly budget.

**Implementation:**  
Reads the estimated token usage, calculates the cost using model pricing, and checks it against a defined budget threshold.

**Why this choice:**  
Cost is treated as an architectural constraint, allowing the system to estimate API costs and prevent usage from exceeding the defined budget.

**Failure mode:**  
BudgetExceededError is raised and the API call is not made. The error is logged and surfaced to the caller.

**KSB evidence:**  
K8 — cost as an architectural constraint. S27 — aligning capability with business constraints.


### 3.4 Usage Logger

**What it does:**  
Records prompt tokens, completion tokens, latency, cost and model for every API call.

**Implementation:**  
Appends a JSON line to usage.log after each call. The file path can be configured through an environment variable.

**Why this choice:**  
A structured usage log provides an audit trail of API calls, allowing the system to monitor token consumption, cost, latency and model usage for operational and cost management.

**Failure mode:**  
If the log directory is missing, the system falls back to stdout rather than failing the API call.

**KSB evidence:**  
S27 — operational observability as a system requirement.

## 4. Decisions and Trade-offs
### 4.1 LLM Client

**Chosen:** OpenAI Python SDK.

**Alternative considered:** Direct HTTP requests to the OpenAI API.

**Why:** The SDK provides a simpler Python interface and handles much of the API communication and request structure, allowing the application code to focus on the AI functionality.


### 4.2 Tool Gateway

**Chosen:** JSON-based function/tool schemas with an explicit allow-list.

**Alternative considered:** Allowing the model to directly determine which application functions could be executed.

**Why:** The schema and allow-list provide a controlled boundary between the LLM and the application. The model can request a defined tool, but the application remains responsible for deciding what can actually execute.


### 4.3 Cost Guard

**Chosen:** Estimate API costs before making calls and enforce a defined budget.

**Alternative considered:** Monitoring costs only after API calls had been made.

**Why:** Checking costs before execution provides an opportunity to prevent unexpected spending rather than discovering excessive usage after the cost has already been incurred.


### 4.4 Usage Logger

**Chosen:** Store structured usage information in a log.

**Alternative considered:** Relying only on the provider's usage dashboard.

**Why:** An application-level log connects token usage, model, latency and cost to individual application executions, providing more useful evidence for troubleshooting and auditing.

## 5. Open Questions and Risks
### 5.1 API Cost at Production Volume

The current cost estimate is based on an expected review volume of approximately 333 reviews per month. It is not yet known how costs will change if review volume increases significantly or if the average review length is substantially higher than estimated.


### 5.2 API Availability

The system currently depends on the availability of the external OpenAI API. The impact of prolonged API downtime on the review-analysis workflow has not yet been fully tested.


### 5.3 Sentiment Classification Accuracy

The accuracy of positive/negative classification on the company's real Booking.com reviews has not yet been validated because the API has not been used to process the production review dataset.


### 5.4 Data Protection and Third-Party Processing

The compliance implications of sending customer review text to an external AI provider require further investigation. It needs to be confirmed whether the review data can be processed by the chosen provider and whether any personal or sensitive information needs to be removed before processing.

## 6. Data Handling
### 6.1 Data Entering the System

The primary input is customer review text collected from Booking.com reviews for the serviced-apartment business. Reviews may contain customer opinions about their stay and could potentially include personal information if customers include names, contact details or other identifying information in their review.


### 6.2 Data Processing

The review text is passed from the Python application to the external OpenAI API for sentiment classification. The model is currently intended to return only a positive or negative classification, rather than generating additional analysis or storing unnecessary information.


### 6.3 Data Leaving the Environment

When the OpenAI API is used, the review text is transmitted from the application's environment to OpenAI for processing. This means the system has a third-party data-processing dependency that must be considered when assessing the organisation's data-protection and compliance requirements.


### 6.4 Data Minimisation and Compliance

Only the information required for sentiment classification should be sent to the AI service. Before using real customer reviews, the organisation should confirm the applicable data-protection requirements and whether personal or sensitive information should be removed or anonymised before the review is sent to the external provider.


### Input Validation

**Decision:** Use `validator.py` to reject empty, oversized and obvious prompt-injection inputs before they reach the LLM.

**Rejected alternative:** Allow all user input to reach the LLM and rely on the model to handle unsafe or invalid content.

**Reason:** The agent processes external content such as hotel reviews, so validating input before making an API call reduces security risk and prevents unnecessarily large requests from reaching the model.


### Retry Logic

**Decision:** Use a custom retry decorator with up to four attempts, exponential backoff and full jitter for temporary API failures.

**Rejected alternative:** Make one API attempt and immediately return an error when the API fails.

**Reason:** External APIs can temporarily return rate-limit or connection errors. Retrying automatically improves reliability without putting retry logic directly inside the LLM calling function.


### Model Fallback

**Decision:** Use `gpt-4o` as the primary model and `gpt-4o-mini` as the fallback model when the primary model is unavailable.

**Rejected alternative:** Stop the request when the primary model fails.

**Reason:** The agent should continue operating when the primary model is temporarily unavailable. The fallback also provides a lower-cost degradation path, while logging which model actually handled the request.