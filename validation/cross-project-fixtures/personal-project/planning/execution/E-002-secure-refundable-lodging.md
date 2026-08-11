# E-002 — Secure refundable lodging

- Outcome: All 13 nights have confirmed qualifying lodging without exceeding the $2,600 all-in lodging cap.
- Depends on: [P-001](../decisions/P-001-trip-blueprint.md), [E-001](E-001-verify-live-route-and-costs.md), and human approval of the E-001 booking sheet

## Context

- [Trip blueprint](../decisions/P-001-trip-blueprint.md)
- The completed E-001 booking sheet and human-approved selections

## In scope

- Recheck price and cancellation terms immediately before checkout.
- Prepare the eight approved lodging checkouts covering all 13 nights: two separate Texarkana stays plus Hot Springs, Memphis, Nashville, Mammoth Cave area, Jackson, and Little Rock.
- Immediately before each checkout, recheck the property on its official booking page and verify the exact adjacent lodging-to-lodging leg or legs with a direct mapping provider. Stop if any normal leg exceeds five hours.
- Have the human complete payment or provide explicit transaction authorization through the active harness.
- Save property, address, dates, occupancy, private-bath confirmation, all-in amount, confirmation number, and cancellation deadline.
- Update the trip ledger with actual lodging charges.

## Out of scope

- Activity tickets, meals, transportation purchases, room upgrades, loyalty offers, or nonrefundable substitutions.
- Storing full payment-card details in project files.

## Constraints

- The human controls every purchase.
- Each reservation must cover four legal occupants and a private bathroom.
- The combined all-in lodging total must remain at or below $2,600; parking must be included or charged to the transport cap.
- Aggregator or secondary evidence cannot authorize checkout. If a primary/direct source is temporarily unavailable, stop rather than convert a provisional claim into a charge.
- Do not start until E-001 proof and its required human review are complete.

## Proof

- Confirmations cover outbound Texarkana 1 night, Hot Springs 2, Memphis 2, Nashville 3, Mammoth Cave area 2, Jackson 1, Little Rock 1, and return Texarkana 1, with no gap or overlap; direct-provider route rechecks remain at most five hours; the recorded all-in sum is at most $2,600; every cancellation deadline is documented.

## If blocked or disproven

- Stop before purchase and return to E-001 if a selected rate, occupancy, bathroom, or cancellation term changed.
- Return to planning if no approved replacement keeps the full trip at or below $6,000 and every drive leg within five hours.

## Human review

- Verify confirmation emails, dates, room occupancy, cancellation terms, and ledger total before this ticket closes.

## Next eligible ticket

- [E-003 — Reserve dated activities](E-003-reserve-dated-activities.md), only after all lodging proof is complete.
