# Controlled Agent Loop - L1.2 / L1.3 Evidence

## Overview

This project demonstrates a controlled AI agent loop built using Python and the Gemini API.

The system shows how an AI model can suggest a decision while Python controls tool access, validation rules and human review points.

The purpose is to demonstrate responsible AI architecture rather than a fully automated production system.

---

## Agent Flow

The controlled agent loop follows this process:

1. A service request enters the system.
2. Gemini analyses the request and proposes an action.
3. Python checks whether the proposed action is allowed.
4. Python retrieves information only from an approved knowledge source.
5. Gemini creates an internal draft recommendation.
6. The output is passed to a human reviewer before any action is taken.

---

## Agent Components

### LLM Core

Gemini Flash is used to analyse the service request, classify the topic and generate an internal recommendation draft.

### Instructions and Context

The model receives:
- service request details
- allowed actions
- approved guidance topics
- system rules

### Tools and Actions

The agent uses a controlled `retrieve_guidance` Python function.

The model cannot directly execute actions. Python decides whether the tool can run based on:
- allowed topics
- confidence threshold
- fallback rules

### Memory and Knowledge

The system uses a small approved knowledge source stored as a Python dictionary.

In a production system this could be replaced with:
- internal knowledge bases
- CRM data
- document repositories
- vector databases

### Orchestration and State

Python manages the agent loop by storing:
- user request
- model decision
- tool usage
- tool result
- review status
- generated draft

---

## Control Measures

The system includes:

- Confidence threshold before tool execution
- Approved tool access only
- Fallback route for unknown requests
- Human review before final decisions

---

## Execution Trace Evidence

The system exports an execution trace:

`l1_3_agent_execution_trace.json`

This records:

- input request
- model decision
- confidence level
- tool used
- fallback status
- human review requirement

---

## Control Testing

The agent was tested with:

| Test | Expected behaviour |
|---|---|
| Delivery delay request | Retrieve approved guidance |
| Unknown topic | Fallback to human review |
| Account access request | Keep human review required |
| Ambiguous request | Use fallback route |

---

## Limitations

This is a learning prototype and not a production system.

Current limitations:

- Small knowledge source
- Limited validation rules
- No real database integration
- Requires human review
- Does not process real customer data

---

## Future Improvements

Possible improvements:

- Connect to approved review platforms
- Add real sentiment analysis models
- Use embeddings and retrieval (RAG) for larger knowledge sources
- Add monitoring and logging
- Improve classification accuracy with ML models

## L1.3 - Agent Control Map Evidence

### Controlled Agent Loop

I built a controlled AI agent loop using Gemini Flash and Python.

The system receives a service request, asks the LLM to propose an action, then uses Python control logic to decide whether the action is allowed.

The model does not directly execute actions. Python controls tool usage, fallback routes and human review requirements.

### Architecture Components

- **LLM Core**
  - Gemini Flash analyses the request and proposes:
    - action
    - topic
    - confidence score

- **Python Control Gate**
  - Validates:
    - allowed topics
    - confidence threshold
    - approved tool usage
    - human review requirement

- **Approved Knowledge Source**
  - Python retrieves information only from the approved guidance dictionary using `retrieve_guidance()`.

- **Fallback Route**
  - Unknown topics, low-confidence decisions and sensitive requests are routed to human review.

- **Human Review**
  - The system creates a review package rather than automatically sending a response.

### Evidence Files

- `l1_3_agent_control_map.png`
  - Visual representation of the AI control architecture.

- `l1_3_agent_execution_trace.json`
  - Execution evidence showing:
    - model decision
    - confidence score
    - tool usage
    - fallback status
    - human review requirement

- `l1_3_agent_control_map.ipynb`
  - Notebook containing the controlled agent loop implementation.

### Safety Considerations

Before publishing evidence:

- No API keys are included.
- No personal data or customer information is included.
- Workplace examples are replaced with safe practice examples.
- The model output is reviewed by a human before any action is taken.
### L2.1 - Multimodal Decision Gate

I built a Jupyter notebook that inspects a safe image input and routes the task to text-only, OCR-first, multimodal candidate or human review. The decision is exported as JSON so my model choice is evidence-based and can feed into the platform evaluation in Unit 2.
