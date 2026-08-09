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
| Source | What I checked | Date checked | What it proves | Link or private reference |
|---|---|---|---|---|
|  |  |  |  |  |
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

