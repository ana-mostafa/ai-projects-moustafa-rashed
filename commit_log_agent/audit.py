# commit_log_agent/audit.py

from datetime import datetime


# ─── Component registry ────────────────────────────────────────────────────
# Each entry is one architectural component of your agent.
# Fill in the why_this_choice field for each one — that becomes
# Section 3 (Component Breakdown) and Section 4 (Decisions) of your ADD.

COMPONENTS = [
    {
        "name": "LLM Client",
        "what_it_does": "Sends structured prompts to the model API and returns completions.",
        "implementation": "OpenAI Python SDK. API key loaded from environment variable. Model specified at call time.",
        "why_this_choice": "The OpenAI Python SDK provides a simple Python interface for authenticated API calls while keeping the underlying HTTP communication separate from the application logic.",
        "failure_mode": "AuthenticationError if key is missing or expired. APIConnectionError on network failure.",
        "ksb_evidence": "K8 — third-party API dependency with cost, uptime and data-handling implications.",
    },
    {
        "name": "Tool Gateway",
        "what_it_does": "Exposes an allowlisted set of callable functions to the LLM.",
        "implementation": "JSON tool schemas passed in the API call. Only whitelisted function names are dispatched.",
        "why_this_choice": "A schema-based tool gateway lets the model request only explicitly defined functions, while the application retains control over which functions are actually dispatched.",
        "failure_mode": "LLM requests an unlisted function → tool_not_found returned to the model, not raised.",
        "ksb_evidence": "K9 — function calling architecture. S27 — controlled tool exposure as a business control.",
    },
    {
        "name": "Cost Guard",
        "what_it_does": "Estimates cost before each API call and blocks calls that exceed the monthly budget.",
        "implementation": "Reads token estimate from the prompt, calculates cost at current model pricing, checks against threshold.",
        "why_this_choice": "Cost is treated as an architectural constraint, so the system can estimate the cost of an API call and prevent usage from exceeding the defined budget.",
        "failure_mode": "BudgetExceededError raised — the call is not made. Error is logged and surfaced to caller.",
        "ksb_evidence": "K8 — cost as an architectural constraint. S27 — aligning capability with business constraints.",
    },
    {
        "name": "Usage Logger",
        "what_it_does": "Records prompt tokens, completion tokens, latency, cost and model for every call.",
        "implementation": "Appends a JSON line to usage.log after each call. File path configurable via environment variable.",
        "why_this_choice": "A structured usage log provides an audit trail of API calls, allowing the system to monitor token consumption, cost, latency and model usage for operational and cost management.",
        "failure_mode": "If the log directory is missing, falls back to stdout. Does not fail the API call.",
        "ksb_evidence": "S27 — operational observability as a system requirement.",
    },
]


def run_audit():
    print("\n" + "═" * 64)
    print("  COMMIT LOG AGENT — ARCHITECTURE AUDIT")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("═" * 64 + "\n")

    print("SECTION 3 — COMPONENT BREAKDOWN\n")
    incomplete = []

    for i, comp in enumerate(COMPONENTS, 1):
        has_rationale = bool(comp["why_this_choice"].strip())
        marker = "✓" if has_rationale else "□  add decision rationale"
        if not has_rationale:
            incomplete.append(comp["name"])

        print(f"{i}. {comp['name']}  [{marker}]")
        print(f"   What it does:    {comp['what_it_does']}")
        print(f"   How:             {comp['implementation']}")
        if has_rationale:
            print(f"   Why this choice: {comp['why_this_choice']}")
        print(f"   If it fails:     {comp['failure_mode']}")
        print(f"   KSB evidence:    {comp['ksb_evidence']}")
        print()

    print("─" * 64)

    if incomplete:
        print("\nDECISIONS NEEDING RATIONALE (for ADD Section 4)\n")
        for name in incomplete:
            print(f"  • Why did you choose this implementation for: {name}?")
        print()

    print("Next step: copy this output into ADD.md — Sections 3 and 4.")
    print("Fill in the why_this_choice fields above to complete Section 4.\n")
    print("─" * 64 + "\n")


if __name__ == "__main__":
    run_audit()
