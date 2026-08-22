# Risk Register

| Risk | Category | Severity | Control | Implemented |
|---|---|---|---|---|
| User submits malicious prompt injection | Security | High | validator.py — injection signal detection rejects the request before it reaches the LLM | ✓ |
| API rate limit hit during peak usage | Operational | High | retry.py — exponential backoff with full jitter, up to 4 attempts | ✓ |
| Primary model unavailable or over-budget | Operational | Medium | fallback.py — automatic degradation to cheaper model, logged per call | ✓ |
| Empty or oversized input passed to the LLM | Operational | Medium | validator.py — length and emptiness check rejects bad input before API call | ✓ |

## OWASP Top 10 Review

I compared the Commit Log Agent against the OWASP Top 10 for LLM Applications.

### Risks already partly addressed

- **Prompt Injection (LLM01):** `validator.py` checks for known prompt injection patterns and rejects the input before it reaches the LLM.
- **Excessive Agency (LLM06):** The Tool Gateway uses an allowlist so the LLM can only request approved functions.
- **Unbounded Consumption (LLM10):** The Cost Guard and input length limit help control excessive API usage and cost.

### Risks not fully addressed

- **Sensitive Information Disclosure (LLM02):** The system does not currently detect or remove personal or sensitive information from reviews before sending them to the external API.
- **Improper Output Handling (LLM05):** The system does not yet have a dedicated validation layer for checking the LLM's output.
- **System Prompt Leakage (LLM07):** The validator catches some obvious attempts, but it cannot guarantee that the system prompt will never be revealed.
- **Misinformation (LLM09):** The LLM could incorrectly classify a review, so the classification should not be treated as automatically correct.

This review shows that the current controls reduce some risks, but several OWASP risks remain open and require further controls.