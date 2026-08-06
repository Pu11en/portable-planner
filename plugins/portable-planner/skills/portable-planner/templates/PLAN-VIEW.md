# {{Plan title}}

**Status:** {{planning | awaiting approval | approved for build}}

**Destination:** {{one-line destination}}

**Success:** {{one-line objective proof}}

**Now:** {{current state and blocker, or ready}}

**Next:** {{one exact action}}

```mermaid
flowchart LR
    P1(["NOW · {{milestone 1}}"])
    P2["2 · {{milestone 2 outcome}}"]
    P3["3 · {{milestone 3 outcome}}"]
    P4["4 · {{milestone 4 outcome}}"]
    D(["DONE · {{short destination}}"])
    P1 --> P2 --> P3 --> P4 --> D
    {{Use five to nine overview milestones. Add a branch only when required for truthful order. Do not add architecture or supporting-system nodes here.}}

    classDef current stroke-width:3px,font-weight:700;
    classDef milestone stroke-width:2px;
    classDef proof stroke-width:3px,font-weight:700;
    classDef blocked stroke-width:3px;

    class P1 current;
    class P2,P3,P4 milestone;
    class D proof;
```

**Text route:** Goal → {{step 1}} → {{step 2}} → {{step 3}} → {{remaining steps}}

## Step details

<details open>
<summary>{{current step ID and title}}</summary>

- Outcome: {{one line}}
- Owner: {{human, agent, automatic system, or shared}}
- Inputs: {{minimum required context or links}}
- Proof: {{objective completion evidence}}
- If blocked or changed: {{recovery or return path}}

</details>

{{Add one compact details block for each remaining route step so selection/click reveals the same five fields in ordinary Markdown.}}

## Plan-wide safety

- {{No more than six short rules that protect the whole route.}}

Details: [plan](PLAN.md) · [current decision]({{relative current ticket link}})
