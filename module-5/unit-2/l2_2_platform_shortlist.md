## Route brief from L2.1
- L2.1 modality decision file: module-5/unit-2/l2_1_modality_decision.json
- Recommended route: multimodal_candidate
- Why this route was recommended: Visual layout and handwritten content may affect the task.
- Evidence that visual layout matters or does not matter: The sample receipt includes a visual layout and a handwritten note.
- Evidence that OCR-first was considered: L2.1 tested whether text could be extracted first; the sample case was set to false because visual information may be needed.
- Sensitive-data, quality or approval constraints: The sample contains practice data only. Image quality passed the preflight check. Sensitive data was set to false.
## Platform requirements
- The platform route must support: Image and text input, with multimodal processing where visual information affects the result.
- The platform route must avoid: Processing routes that lose important visual or handwritten information.
- Data handling requirements: Practice data only for this exercise; any real workplace data would require an approved handling route.
- Integration requirements: A practical API or managed service that can be integrated into an AI application.
- Cost or usage constraints: Cost and usage limits must be checked before selecting a platform.
- Human review requirements: Human review must remain available when quality, sensitivity or model confidence makes automated processing unsafe.
## Source log
| Source                                                  | What I checked                                                                       | Date checked | What it proves                                                                                                                                                                                                   | Link or private reference              |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------ | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| Official OpenAI API documentation                       | Image input and image analysis support                                               | 2026-08-09   | Confirms that OpenAI API models can accept image input and analyse images, supporting the multimodal route from L2.1.                                                                                            | OpenAI API Developer documentation     |
| Official OpenAI API data controls                       | Whether API inputs/outputs are used for model training and what data may be retained | 2026-08-09   | OpenAI states that API inputs and outputs are not used to train models by default; some API data may still be retained for abuse monitoring or application state.                                                | OpenAI API Data Controls               |
| Official OpenAI model/pricing documentation             | Pricing and usage limits                                                             | 2026-08-09   | Shows that API usage is charged according to model/token usage and that usage limits depend on the account and model.                                                                                            | OpenAI API pricing/model documentation |
| Official OpenAI Developer documentation                 | API integration and image input method                                               | 2026-08-09   | Confirms that an application can connect to OpenAI through an API and send image inputs programmatically.                                                                                                        | OpenAI Developer documentation         |
| Official OpenAI API data controls                       | Regional processing and data-retention options                                       | 2026-08-09   | Shows that OpenAI provides data-residency and retention controls, but the exact configuration needs to be checked against organisational requirements.                                                           | OpenAI API Data Controls               |
| Official Google Gemini API file-input documentation     | Image and file input support                                                         | 2026-08-09   | Confirms that Gemini API supports image and other file inputs, including programmatic use from Python.                                                                                                           | Gemini API File Input Methods          |
| Official Google Gemini API data-retention documentation | Training restrictions and retention                                                  | 2026-08-09   | For paid Gemini API services, Google states that prompts, files and responses are not used to improve products, while some limited logging/retention can still occur depending on the service and features used. | Gemini API Zero Data Retention         |
| Official Google Gemini API logging documentation        | Logging and sharing of API data                                                      | 2026-08-09   | Explains how API prompts/responses may be logged for abuse monitoring and how separately shared datasets can be used for improvement.                                                                            | Gemini API Data Logging and Sharing    |
| Official Google Gemini API pricing documentation        | Input/output pricing and usage tiers                                                 | 2026-08-09   | Shows current Gemini API pricing and different usage/billing tiers, providing evidence for the later cost evaluation.                                                                                            | Gemini API Pricing                     |
| Official Google Gemini API billing documentation        | Billing tiers and limits                                                             | 2026-08-09   | Shows how Gemini API billing tiers work and that higher-volume production use requires higher usage tiers.                                                                                                       | Gemini API Billing                     |
| Official Google Gemini API agent documentation          | Human oversight and output verification                                              | 2026-08-09   | Google recommends verifying generated outputs before deployment, supporting the need for human oversight in our controlled workflow.                                                                             | Gemini API Agents Overview             |

## Candidate shortlist
| Candidate | Platform route | Why it fits the L2.1 route | Main concern | Evidence still needed | Decision |
|---|---|---|---|---|---|
| OpenAI API | Third-party model API | Supports image input, so it can process the receipt directly as a multimodal candidate. | Need to check data handling, cost and limits for our actual use case. | Current pricing, data handling and image/file limits. | needs more evidence |
| Google Gemini API | Third-party model API | Supports image input and multimodal processing, so it can process the receipt directly. | Need to check data handling, cost and limits for our actual use case. | Current pricing, data handling and image/file limits. | needs more evidence |
| OCR/document-processing service + text model | OCR or document-processing service plus text model | Could extract the receipt text before sending it to a text model. | OCR may lose visual layout or handwritten information that matters to the task. | Test extraction quality and whether the handwritten note and layout are preserved. | reject |


## Disqualifier pass
| Candidate | Possible disqualifier | Evidence found | Status | What I will do next |
|---|---|---|---|---|
| OpenAI API | Organisation may not permit external processing of receipt images. | No internal approval information checked yet. | unknown | Check organisation's approved-technology and data-handling policy. |
| Google Gemini API | Organisation may not permit external processing of receipt images. | No internal approval information checked yet. | unknown | Check organisation's approved-technology and data-handling policy. |
| OCR/document-processing service + text model | The OCR-first route may lose visual information needed for the task. | L2.1 identified visual layout and handwritten content as potentially important. | fail | Reject for this use case; retain multimodal routes for further evaluation. |

