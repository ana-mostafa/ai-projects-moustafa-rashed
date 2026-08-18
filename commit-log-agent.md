# Commit Log Agent

Name: Moustafa Rashed
Apprenticeship route: Level 4 AI and Automation Practitioner - AI Developer
Main workplace project:AI-powered Guest Feedback Analysis and Reporting System
GitHub profile or repository link:https://github.com/ana-mostafa/ai-projects-moustafa-rashed/

## Agent purpose

Help me record technical evidence from Modules 5 to 9. The agent should help me turn practical work into concise Commit Log entries, GitHub-ready notes and professional portfolio evidence.

## Agent rules

- Ask before drafting if any key detail is missing.
- Keep entries concise and evidence-focused.
- Include workplace value, possible use cases and limitations.
- Remind me to remove API keys, personal data, confidential workplace information and anything I do not have permission to share.
- Suggest GitHub commit messages and README updates, but do not claim anything has been committed or published unless I confirm it.
- Do not invent screenshots, links, code or results.

## Questions the agent should ask me

1. What did you build, test, configure or decide?
2. Which module and lesson does this relate to?
3. What evidence can you link or screenshot?
4. What did you learn from the task?
5. How could this skill apply to your workplace or main project?
6. What risks, limitations or follow-up questions should you discuss with your instructor or line manager?

## Output format

### Commit Log entry

- Date:
- Module / lesson:
- What I did:
- Evidence:
- Why it matters:
- Workplace application:
- Risks or limitations:
- Follow-up question:

### GitHub-ready update

- Suggested commit message:
- Suggested README note:
- Files or evidence to check before publishing:

## L1.1 - AI Architecture Constraints Note
# L1.1 - AI Architecture Constraints Note


## Context

My existing workflow diagram is from:

Both Module 1 and Module 3.

Current workflow:

Guest reviews are extracted daily, cleaned, translated if required, analysed for sentiment, negative reviews are summarised into recurring issues, and the weekly report is reviewed by the Head of Guest Services.

AI component:

Gemini Flash API performs translation, sentiment analysis and issue summarisation.

Systems involved:

Booking.com, CSV files, Python, and Gemini API.

Longest input:

Approximately one day's reviews (around 50 reviews).

Token estimate:

Not estimated yet.

Usage scale:

Department pilot.

Model:

Gemini Flash.

Main uncertainty:

How the architecture will scale when more review platforms are added.


---

# 1. Input analysis

The AI system will analyse batches of guest reviews collected daily. For the initial pilot, the expected volume is approximately 50 reviews per day.

Assuming an average review length of approximately 75 words per review:

50 reviews × 75 words = approximately 3,750 words.

Using an estimated conversion of around 0.75 words per token, this represents approximately 5,000 input tokens per AI request.

Compared with the context window of Gemini Flash, this is a relatively small input size. Therefore, context length is not expected to be a limitation during the pilot phase.

However, as the solution expands to additional review platforms and larger volumes of feedback, token usage, latency, cost, and processing limits will become important architectural considerations.


---

# 2. Scale estimate

The initial implementation will be tested as a department-level pilot. The expected usage is based on analysing daily guest reviews and generating weekly reports.

Estimated usage scenarios:

## Pilot scale

Approximately:
- 50 reviews per day
- One department using the system
- Daily analysis and weekly reporting

At this stage, the main considerations are:
- validating AI accuracy
- testing workflow reliability
- ensuring human review remains effective


## Department scale

A larger deployment may include:
- Multiple properties
- Additional review platforms
- Increased daily review volume

At this stage, considerations include:
- higher token usage
- increased API requests
- processing time
- monitoring model performance


## Organisation-wide scale

If expanded across the organisation, the system may require:

- better data pipelines
- stronger monitoring
- improved cost forecasting
- possible changes to model selection or processing approach

At higher volumes, architectural improvements may include:
- reducing unnecessary prompt length
- processing reviews in batches
- using retrieval approaches where appropriate
- selecting smaller models where possible
- controlling output length


The main scalability uncertainty is how token volume and operational costs will change when additional review platforms and properties are introduced.


---

# 3. Model selection decision

The initial solution will use a standard instruct-tuned model (Gemini Flash) because the main requirements are sentiment classification, translation, information extraction, and summarisation rather than complex reasoning.

The system does not require real-time responses because it will process guest reviews asynchronously and generate reports for management review. This allows the system to process batches of reviews without strict latency requirements.

A reasoning model is not required because the AI is supporting structured analysis tasks rather than making complex decisions. Human managers will remain responsible for interpreting insights and making operational decisions.

The expected usage volume supports using a smaller, faster model. Gemini Flash provides sufficient capability while reducing latency and resource requirements compared with larger frontier or reasoning models.

If future requirements become more complex, such as advanced predictive analytics or generating strategic recommendations, the model choice can be reassessed.


---

# 4. Open questions

The following questions require further investigation before moving from pilot to larger deployment:

1. How will token usage and operating costs change when additional review platforms are connected?

2. What level of accuracy will Gemini Flash achieve when analysing different languages, slang, sarcasm, and informal customer expressions?

3. Should reviews continue to be processed through direct prompting, or would a retrieval-based architecture (RAG) become more suitable as the data volume increases?

4. What monitoring approach should be used to detect model drift and declining sentiment analysis performance over time?


---

# Commit Log entry

(To be completed after the activity is reviewed or committed)

- Date:
- Module / lesson:
- What I did:
- Evidence:
- Why it matters:
- Workplace application:
- Risks or limitations:
- Follow-up question:


---

# GitHub-ready update

Suggested commit message:

Add AI architecture constraints note for guest feedback analysis system

Suggested README note:

Added an AI Architecture Constraints Note documenting initial architecture decisions, including input size estimation, scalability considerations, and model selection rationale for the guest feedback analysis project.

Files or evidence to check before publishing:

- Remove any confidential workplace information.
- Remove customer data or real guest reviews.
- Remove API keys or credentials.
- Confirm that shared screenshots and documents do not contain private information.

## L1.2 - Controlled Agent Loop Build

Use the Commit Log Agent rules above. Help me document the controlled agent loop I built in L1.2.

Context:
- Notebook name:
- What my agent loop does:
- The approved tool or knowledge source:
- The fallback route:
- The human review point:
- One change I tested:
- What happened when I tested it:
- Evidence I can safely link or screenshot:
- Anything I must keep private:

Please draft:
1. A concise Commit Log entry for this build.
2. A short Agent Component Map with these headings:
   - LLM core
   - Instructions and context
   - Tools and actions
   - Memory and knowledge
   - Orchestration and state
3. A suggested GitHub commit message or README note.
4. One likely failure mode and one practical control.
5. Two questions I should discuss with my instructor or line manager.

Before drafting, ask me up to three questions if any important detail is missing. Do not invent outputs, screenshots, links, test results, workplace systems or confidential details.

## L1.3 - Agent Control Map Evidence

Use the Commit Log Agent rules above. Help me document the Agent Control Map evidence I created in L1.3.

Context:

- Notebook name:
l1_3_agent_control_map.ipynb

- What my agent loop does:
A controlled AI agent loop that receives a service request, uses Gemini Flash to propose a classification and action, allows Python to control tool usage, creates a review package and requires human review before action.

- The execution trace file:
l1_3_agent_execution_trace.json

- The visual evidence created:
l1_3_agent_control_map.png

- The approved tool or knowledge source:
retrieve_guidance() using the approved_guidance dictionary.

- The fallback route:
Unknown topics, low-confidence decisions or sensitive requests are routed to human review.

- The human review point:
The generated recommendation is reviewed by a manager or staff member before any action is taken.

- One control test I performed:
Tested different service requests including delivery delay, unknown topics, account access and ambiguous requests.

- What happened:
The system retrieved approved guidance for supported requests and used fallback routes when the request was unclear or unsupported.

- Evidence I can safely share:
Clean notebook, execution trace JSON and Agent Control Map PNG.

- Anything I must keep private:
API keys, real customer data and confidential workplace information.

Please draft:

1. A concise Commit Log entry.
2. A GitHub-ready summary.
3. A suggested commit message.
4. One failure mode and one practical control.
5. Two questions to discuss with my instructor or line manager.

Do not invent results, screenshots or links.

## L2.1 - Multimodal Decision Gate Review

Use the Commit Log Agent rules above. Help me review and document my L2.1 multimodal decision gate.

Context:
- Notebook filename or link:
- Sample image filename or link:
- Modality decision JSON filename or link:
- Route recommended for the sample case:
- Other routes I tested:
- Evidence that visual layout matters or does not matter:
- Evidence that OCR-first was considered:
- Evidence that sensitive data handling was considered:
- Evidence I can safely share:
- Evidence I must keep private:

Please draft:
1. A short evidence review: does my decision justify text-only, OCR-first, multimodal or human review?
2. A concise Commit Log entry for this lesson.
3. A GitHub-ready README note.
4. A suggested commit message.
5. Two questions I should discuss with my instructor or line manager before choosing a platform.

Before drafting, ask me up to three questions if any important detail is missing. Do not invent links, screenshots, repository paths, test results, workplace systems, risks or confidential details.

## L2.1 - Multimodal Decision Gate

Built a multimodal decision gate to determine the safest AI processing route before selecting a model.

Created a safe synthetic receipt image and added a preflight inspection step to check image quality and metadata. The decision gate used Python rules to recommend between text-only, OCR-first, multimodal processing or human review.

Evidence created:
- l2_1_multimodal_decision_gate.ipynb
- l2_1_sample_receipt.png
- l2_1_modality_decision.json

Testing completed:
- plain_support_email → text_only
- clean_scanned_form → ocr_first
- poor_quality_photo → human_review_or_rescan
- identity_document → human_review_or_approved_route

Key learning:
Multimodal processing should only be considered when visual information affects the task outcome. The decision gate ensures image quality, OCR suitability and sensitive data handling are considered before choosing an AI route.
## L2.2 - Platform Shortlist Review

Use the Commit Log Agent rules above. Help me review and document my L2.2 platform shortlist.

Context:
- L2.1 modality decision file or link:
- Recommended route from L2.1:
- Shortlist file or link:
- Candidates considered:
- Candidates kept:
- Candidates rejected:
- Candidates marked needs more evidence:
- Sources checked:
- Possible disqualifiers:
- Questions still open:
- Evidence I can safely share:
- Evidence I must keep private:

Please draft:
1. A short evidence review: does my shortlist follow from the L2.1 route?
2. A concise Commit Log entry for this lesson.
3. A GitHub-ready README note.
4. A suggested commit message.
5. Three questions I should answer before building the L2.3 Platform Evaluation Matrix.

Before drafting, ask me up to three questions if any important detail is missing. Do not invent sources, links, policies, prices, test results, workplace systems, approvals or confidential details.

## L2.3 - Platform Evaluation Matrix Review

Use the Commit Log Agent rules above. Help me review and document my L2.3 Platform Evaluation Matrix and recommendation.

Context:
- L2.1 modality decision file or link:
- L2.2 shortlist file or link:
- Matrix file or link:
- Recommendation file or link:
- Candidates evaluated:
- Hard constraints:
- Criteria and weights used:
- Highest-scoring option:
- Recommended option:
- Trade-off accepted:
- Reversal point:
- Sources checked:
- Evidence I can safely share:
- Evidence I must keep private:

Please draft:
1. A short evidence review: does the recommendation follow from the matrix, hard constraints and sensitivity check?
2. A concise Commit Log entry for this lesson.
3. A GitHub-ready README note.
4. A suggested commit message.
5. Three questions I should discuss with my coach, instructor or line manager before implementation.

Before drafting, ask me up to three questions if any important detail is missing. Do not invent scores, sources, links, policies, prices, platform capabilities, workplace systems, approvals or confidential details.

## L3.1 — First OpenAI API Call

**Model:** `gpt-4o-mini`

I set up the Unit 3 Python environment with the `openai` and `python-dotenv` packages, configured the `OPENAI_API_KEY` through the existing `.env` file, and added `.env` to `.gitignore` to keep the credential out of version control. I implemented the OpenAI Chat Completions API call with a system prompt, user message, temperature and maximum output limit, and added code to extract the response and token usage. The live API request was not completed because the API account returned `insufficient_quota / credit_balance_exhausted`; therefore, no successful API output or token usage was captured. I would refine the system prompt for the guest-review project by explicitly defining the task, expected output format and sentiment categories so that responses are more consistent and easier to process programmatically.

**Status:** Code prepared and tested up to the API request; live execution blocked by API account credit.

## L3.2 — First OpenAI API Call

Application to organisation: Tool calling could allow an AI component to retrieve approved internal information through controlled Python functions. Read-only tools could be used for information retrieval, while actions that modify records or have business impact could require additional validation or human approval.

### Module 5 — Unit 3 — Lesson 3

- Estimated monthly reviews: approximately 333
- Estimated monthly AI cost: approximately $0.01
- Token reduction techniques:
  - Output length control using a Positive/Negative-only response and low `max_tokens`.
  - System prompt discipline by keeping the classification instructions concise.
- Architecture decision: to be decided with instructor.

The proposed system will analyse future Booking.com guest reviews as they are received and return a simple Positive/Negative classification. Synchronous processing is currently proposed because the output is small, the estimated workload is approximately 11 reviews per day, and the sentiment result may be useful shortly after a new review arrives. The main trade-offs are API latency, failures and rate limits, which will need to be handled in the production implementation. If review volume increases significantly or immediate results are no longer required, asynchronous queue or batch processing could be considered.