# P-001 — Set the complete family road-trip blueprint

- Status: complete
- Depends on: none

## Decision

Set the dates, route, day-level activity rhythm, cost guardrails, booking order, and safety boundaries for a two-adult/two-child road trip from and back to Dallas. These choices determine whether the trip is enjoyable, bookable, and provably inside the $6,000 ceiling and five-hour driving limit.

## Viable options

- A. October 10–23, 2026 and an Arkansas–Tennessee–Kentucky loop — recommended because it matches the requested autumn outdoor/indoor character; tradeoffs are possible school absence and four one-night transit stays.
- B. March 13–26, 2027 with the same desired character — preserves the region, but requires fresh seasonal, calendar, and route research before it can replace A.
- C. June 5–18, 2027 with a Texas/Gulf emphasis — changes the trip character and requires a new evidence audit rather than borrowing A's route assumptions.

## Recommendation

A — Travel October 10–23, 2026 on a Dallas → Texarkana → Hot Springs → Memphis → Nashville → Mammoth Cave → Jackson → Little Rock → Texarkana → Dallas loop. Direct-router baselines put all nine selected city-center legs under five hours. Texarkana is required in both directions because the same direct provider places Dallas → Hot Springs and Little Rock → Dallas above the cap; Jackson remains required because Mammoth Cave → Memphis is also above it.

## Confirmed decision

The simulated preference turns selected A twice, as recorded in [the test transcript](../TEST-TRANSCRIPT.md):

- Dates: Saturday, October 10 through Friday, October 23, 2026 — 14 days and 13 nights.
- Travelers: two adults and children ages 8 and 12.
- Route character: autumn forest, approachable outdoor stops, city museums, and one family-suitable Mammoth Cave tour, subject to the direct-provider gates below.
- Lodging: family hotel room or cabin, private bathroom, legal occupancy for four, parking included or explicitly budgeted; refundable rates preferred until the final recheck.
- Driving: each planned normal leg must verify at five hours or less of steering time, excluding meal/rest breaks; plan a break at least every 2.5 hours. No optional detour may break the cap.
- Purchases: no charge is authorized by this plan. A human must approve the live booking sheet and complete or explicitly authorize every purchase.

### Day-by-day route

| Day | Date | Overnight / drive | Outdoor plan | Indoor plan or weather fallback |
|---|---|---|---|---|
| 1 | Sat Oct 10 | Texarkana; Dallas → Texarkana, direct baseline 3h05 | Short arrival walk selected in E-004 | No required paid stop; Fordyce on day 2 covers the paired window |
| 2 | Sun Oct 11 | Hot Springs; Texarkana → Hot Springs, direct baseline 2h02 | Grand Promenade or an E-001-verified easy park walk | Fordyce Bathhouse Visitor Center and Museum |
| 3 | Mon Oct 12 | Hot Springs | Easy park trail selected in E-004 | Fordyce exhibits/revisit or another official-provider option verified in E-001 |
| 4 | Tue Oct 13 | Memphis; Hot Springs → Memphis, direct baseline 3h24 | Riverfront or park walk if conditions allow | MoSH Pink Palace Museum |
| 5 | Wed Oct 14 | Memphis | Shelby Farms or another E-001-verified easy outing | National Civil Rights Museum after adult suitability review |
| 6 | Thu Oct 15 | Nashville; Memphis → Nashville, direct baseline 3h56 | Centennial Park or another E-001-verified easy outing | Day 5 museum covers the paired window; E-001 may name a same-city backup |
| 7 | Fri Oct 16 | Nashville | Radnor Lake or another E-001-verified easy outing | Adventure Science Center |
| 8 | Sat Oct 17 | Nashville | Stones River grounds or another E-001-verified easy outing | Adventure Science Center or another official-provider Nashville option |
| 9 | Sun Oct 18 | Mammoth Cave area; Nashville → visitor center, direct baseline 1h50 | Short surface trail if conditions allow | Visitor center; cave tour may occur if this is the verified reservation date |
| 10 | Mon Oct 19 | Mammoth Cave area | Easy surface trail if conditions allow | Reserved Mammoth Passage, Frozen Niagara, or a comparable verified family-suitable cave tour |
| 11 | Tue Oct 20 | Jackson, TN; Mammoth Cave → Jackson, direct baseline 4h08 | Short arrival walk | Casey Jones Home & Railroad Museum or another official-provider Jackson option |
| 12 | Wed Oct 21 | Little Rock; Jackson → Little Rock, direct baseline 4h04 | Arkansas River Trail segment if conditions allow | Museum of Discovery; Clinton Library is the official-provider alternate |
| 13 | Thu Oct 22 | Texarkana; Little Rock → Texarkana, direct baseline 2h35 | Short arrival walk | Museum of Regional History or another Texarkana Museums System option verified in E-001 |
| 14 | Fri Oct 23 | Home; Texarkana → Dallas, direct baseline 3h06 | Planned rest/stretch stop | No new paid activity; day 13 museum covers the paired window |

Indoor-fallback cadence is explicit for the seven paired two-day windows: days 1–2 Fordyce; 3–4 Fordyce/MoSH; 5–6 National Civil Rights Museum; 7–8 Adventure Science Center; 9–10 visitor center/cave tour; 11–12 Casey Jones/Museum of Discovery; 13–14 Museum of Regional History. All future-dated operations must pass the official-provider checks in E-001 before any booking.

### Fixed budget envelope

| Category | Hard cap | Control |
|---|---:|---|
| Lodging, 13 nights | $2,600 | Maximum $200/night average, all taxes and mandatory parking/fees included |
| Food, 14 days | $1,900 | Maximum $135/day family average; favor included breakfast, groceries/picnics, and one restaurant meal per day |
| Vehicle fuel, tolls, parking | $450 | Personal vehicle assumed; no rental-car cost; verify exact mileage and current fuel estimate in E-001 |
| Activities | $650 | Includes taxes/fees; protect the cave tour first and swap optional paid museums for free fallbacks if needed |
| Contingency | $400 | Untouched buffer for price drift or genuine trip disruption, not routine upgrades |
| **Total ceiling** | **$6,000** | No category overage unless another category is reduced first and the total remains at or below $6,000 |

## Evidence

- [Decision-changing research](../evidence/P-001-evidence.md)

## Effects

- Aggregator route estimates are removed. Direct-router baselines require two Texarkana nights and exclude direct Dallas → Hot Springs, Mammoth Cave → Memphis, and Little Rock → Dallas legs.
- Live inventory, exact lodging-to-lodging routes, departure windows, official attraction calendars, taxes, and fees are checked without purchase in E-001.
- Before each lodging checkout, E-002 rechecks the property and its adjacent legs with direct providers. Before each activity checkout, E-003 rechecks the official operator or ticket provider.
- Lodging is secured only after E-001 confirms a suitable October 18 or 19 cave-tour candidate; the cave tour is the first activity priority.
- The final itinerary must retain an official-provider indoor option in each paired two-day window and stay inside the fixed budget envelope.
- Any inability to meet private-bath lodging, direct-provider drive checks, cave/indoor cadence, or the $6,000 ceiling triggers the return-to-planning rules in the execution tickets.

## Complete when

Dates, travelers, route, all 14 days, all nine drive legs, paired indoor cadence, lodging standard, budget caps, purchase authority, execution dependencies, direct-provider rechecks, and return-to-planning conditions are explicit; decision-changing evidence meets the canonical source rule; and `PLAN.md`, `PLAN-VIEW.md`, and `NEXT.md` all point to human visual approval rather than execution.
