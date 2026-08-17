# I-01 fidelity contract

These six sanitized fixtures freeze the objective contract for the accepted
Journey plus focus lens candidate. They preserve decision-changing structure,
not private transcripts, patient data, sibling-project files, screenshots, or
renderer-specific markup.

Each `fixtures/f-*.json` file contains:

- one distinct failure claim;
- a sanitized canonical source state;
- a valid semantic candidate view;
- one deliberately malformed view;
- the exact assertion that malformed view must trigger; and
- the expected first-read or safety behavior.

Run:

```bash
python validation/i01-plan-comprehension/validate_fixtures.py
```

The check requires exactly F-01 through F-06, rejects duplicate claims, proves
every valid view passes, and proves every malformed view fails for its declared
reason. It does not judge aesthetics or replace Drew's fresh-session acceptance.

## Claim map

| ID | Objective claim |
|---|---|
| F-01 | Canonical meaning survives compression |
| F-02 | Material state changes advance the visible current step |
| F-03 | Blocked work and recovery stay visible |
| F-04 | Rendering never creates human authority or build approval |
| F-05 | The first read stays bounded without hiding essential orientation |
| F-06 | Rich and compact-text routes preserve the same semantics |

One fixture exists per distinct claim. Repetition is added only after observed
variance or a protected high-risk failure, never to satisfy an arbitrary run
count.
