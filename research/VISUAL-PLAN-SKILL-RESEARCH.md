# Visual Plan Skill Research

**Researched:** 2026-08-05  
**Question:** Is there an existing agent skill that can turn a Wayfinder-style project plan into a beginner-friendly visual with very short labels and optional deeper detail?

## Finding

No existing skill I found completes the whole desired workflow:

> Wayfinder/GitHub issues -> simple visual overview -> open a step for its full explanation

The strongest approach is to adapt an established diagram skill rather than invent the renderer. The missing piece is a small course-specific layer that reads the Wayfinder map and its child GitHub issues, limits the overview to short outcome labels, and links each visual step back to its detailed issue.

## Best options

| Option | Evidence of adoption | Output | Beginner/non-software fit | Wayfinder or GitHub issue support | Verdict |
|---|---:|---|---|---|---|
| [Cole Medin's Excalidraw Diagram Skill](https://github.com/coleam00/excalidraw-diagram-skill) | [6.8K skills.sh installs and 4.2K GitHub stars](https://www.skills.sh/coleam00/excalidraw-diagram-skill/excalidraw-diagram) at research time | Editable `.excalidraw` plus rendered PNG | Strong. It supports timelines, flows, conceptual diagrams, grouped phases, and multi-zoom visuals. Its mandatory render-view-fix loop is unusually good quality control. | None built in. It accepts supplied content, not issue-tracker data. | **Best visual foundation.** Most aligned with a friendly high-level map that can also contain deeper sections. |
| [GitHub Awesome Copilot Excalidraw Generator](https://github.com/github/awesome-copilot/tree/main/skills/excalidraw-diagram-generator) | [27K installs and 37.1K repository stars](https://www.skills.sh/github/awesome-copilot/excalidraw-diagram-generator) | Editable `.excalidraw` JSON | Good. Supports flowcharts, mind maps, swimlane business flows, relationships, and architecture; recommends no more than 20 elements. | None built in. Requires a clear description of the steps and relationships. | **Safest mainstream option.** Strong publisher and adoption, but less opinionated about visual simplicity and validation. |
| [Softaworks Mermaid Diagrams](https://github.com/softaworks/agent-toolkit/tree/main/skills/mermaid-diagrams) | [About 4.6K skills.sh installs](https://www.skills.sh/softaworks/agent-toolkit) | Mermaid text inside Markdown | Very readable when kept to a small flowchart or Gantt chart. Easy to update, diff, and store beside the plan. The skill is written primarily for software, though basic flows work for any project. | No direct ingestion. GitHub renders Mermaid in Markdown, so the result can live close to GitHub issues. | **Best lightweight operational option.** Less friendly and expressive than Excalidraw, but much easier to generate reliably and maintain. |

## Why Cole Medin's Excalidraw skill ranks first

Its design rules directly match the course need:

- A summary flow can show the entire journey at a glance.
- Grouped sections can show phases without turning every item into an equal-looking card.
- A timeline represents a sequence; branching and convergence represent dependencies.
- Visual hierarchy, whitespace, and scale identify what matters most.
- The agent must render the file, inspect it, and fix clipping, overlap, bad arrows, and unreadable text before stopping.

The main drawback is that `.excalidraw` JSON is verbose. The visual should be a generated view of the canonical GitHub issues, not another place where planning decisions must be maintained manually.

## Recommended adaptation

Create a small **Visual Plan** skill around the Excalidraw foundation:

1. Use `gh` to read the Wayfinder map issue and its child issues.
2. Extract only outcome, dependency, status, and phase.
3. Show **5-9 short labels** in the overview; use verbs such as “Choose audience” or “Test demand.”
4. Group work into a few plain-language phases that work for any project.
5. Keep detailed reasoning in GitHub issues and provide a companion Markdown index of visual label -> issue link. Excalidraw links could be added later, but should not be the only navigation mechanism.
6. If the overview becomes crowded, produce one overview plus one diagram per phase.
7. Regenerate the visual from GitHub rather than editing two competing sources of truth.

This makes GitHub the durable brain, Wayfinder the decision process, and the visual a beginner-friendly view.

## What not to choose for the core lesson

- **Draw.io:** powerful and professional, but its extra setup, XML, shape libraries, and precision are unnecessary for a student's high-level plan.
- **A generic image-generation skill:** attractive output is not reliably editable or synchronized with the plan.
- **A highly detailed architecture diagram:** software-specific and too dense for the promised quick comprehension.
- **A custom viewer format:** creates another tool students must learn and another dependency the course must support.

## Quality gate for a prototype

Before choosing the final skill, run the same completed Wayfinder map through Excalidraw and Mermaid. A beginner should be able to answer these in under 30 seconds:

1. What is the destination?
2. What phase are we in?
3. What can happen next?
4. What is blocked?
5. Where do I open the deeper explanation?

Choose Excalidraw unless Mermaid performs equally well with materially less friction.

## Primary sources

- [Cole Medin Excalidraw skill source](https://github.com/coleam00/excalidraw-diagram-skill/blob/main/SKILL.md)
- [Cole Medin skill listing](https://www.skills.sh/coleam00/excalidraw-diagram-skill/excalidraw-diagram)
- [GitHub Awesome Copilot skill catalog](https://github.com/github/awesome-copilot/blob/main/docs/README.skills.md)
- [GitHub Awesome Copilot Excalidraw source](https://github.com/github/awesome-copilot/blob/main/skills/excalidraw-diagram-generator/SKILL.md)
- [Softaworks Mermaid source](https://github.com/softaworks/agent-toolkit/blob/main/skills/mermaid-diagrams/SKILL.md)
- [Softaworks skills.sh listing](https://www.skills.sh/softaworks/agent-toolkit)
- [Wayfinder documentation](https://github.com/mattpocock/skills/blob/main/docs/engineering/wayfinder.md)
- [Wayfinder source](https://github.com/mattpocock/skills/blob/main/skills/engineering/wayfinder/SKILL.md)
- [skills.sh installation and telemetry documentation](https://www.skills.sh/docs/cli)

## Confidence and caveats

- Install and star counts are snapshots and will change.
- skills.sh says its install ranking is based on anonymous CLI telemetry; install count is evidence of usage, not proof of quality.
- None of the shortlisted skills claims native Wayfinder parsing or GitHub-issue ingestion.
- No skill was installed or executed during this research.
