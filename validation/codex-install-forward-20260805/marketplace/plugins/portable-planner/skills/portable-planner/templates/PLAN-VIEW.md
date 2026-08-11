# {{Plan title}}

**Status:** {{planning | awaiting approval | approved for build}}

**Destination:** {{one-line destination}}

**Success:** {{one-line objective proof}}

**Now:** {{current state and blocker, or ready}}

**Next:** {{one exact action}}

```mermaid
flowchart TB
    subgraph R1[ ]
    direction LR
    G["Goal: {{short destination}}"] --> P1["{{status}} {{step 1}}"]
    P1 --> P2["{{status}} {{step 2}}"]
    P2 --> P3["{{status}} {{step 3}}"]
    end
    {{Add more left-to-right row subgraphs only when needed. Connect each row end to the next row start; never reverse a row.}}
    {{Add only comprehension-changing support or dependency links with -.->.}}
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
