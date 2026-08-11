# P-001 Evidence — Family road-trip blueprint

Accessed: 2026-08-05

Only facts that change the route, paired two-day indoor coverage, budget allowance, or booking order are retained. No travel aggregator or other secondary source is used to settle the blueprint. Route estimates come from a direct routing service; operating details come from the park, museum, or ticket provider that controls them.

## Route feasibility — direct-provider baseline

OpenStreetMap Nominatim supplied direct geocoding results for [Dallas](https://nominatim.openstreetmap.org/search?q=Dallas%2C+Texas&format=jsonv2&limit=1), [Texarkana](https://nominatim.openstreetmap.org/search?q=Texarkana%2C+Texas&format=jsonv2&limit=1), [Hot Springs](https://nominatim.openstreetmap.org/search?q=Hot+Springs%2C+Arkansas&format=jsonv2&limit=1), [Memphis](https://nominatim.openstreetmap.org/search?q=Memphis%2C+Tennessee&format=jsonv2&limit=1), [Nashville](https://nominatim.openstreetmap.org/search?q=Nashville%2C+Tennessee&format=jsonv2&limit=1), [Mammoth Cave visitor center](https://nominatim.openstreetmap.org/search?q=Mammoth+Cave+Visitor+Center&format=jsonv2&limit=1), [Jackson](https://nominatim.openstreetmap.org/search?q=Jackson%2C+Tennessee&format=jsonv2&limit=1), and [Little Rock](https://nominatim.openstreetmap.org/search?q=Little+Rock%2C+Arkansas&format=jsonv2&limit=1). The linked [OSRM Route Service](https://project-osrm.org/docs/v5.24.0/api/#route-service) calls route those points directly. These are purchase-free planning baselines without future traffic, not exact hotel-to-hotel promises.

| Planned leg | Direct OSRM result | Decision effect |
|---|---:|---|
| [Dallas → Texarkana](https://router.project-osrm.org/route/v1/driving/-96.7968559,32.7762719;-94.0765653,33.4466208?overview=false&steps=false) | about 3h05 | Under the five-hour cap. |
| [Texarkana → Hot Springs](https://router.project-osrm.org/route/v1/driving/-94.0765653,33.4466208;-93.0552437,34.5038393?overview=false&steps=false) | about 2h02 | Under the cap; NPS also gives an [official Texarkana-to-Fordyce baseline](https://www.nps.gov/hosp/planyourvisit/directions.htm) of about two hours. |
| [Hot Springs → Memphis](https://router.project-osrm.org/route/v1/driving/-93.0552437,34.5038393;-90.0517786,35.1460260?overview=false&steps=false) | about 3h24 | Under the cap. |
| [Memphis → Nashville](https://router.project-osrm.org/route/v1/driving/-90.0517786,35.1460260;-86.7742984,36.1622767?overview=false&steps=false) | about 3h56 | Under the cap. |
| [Nashville → Mammoth Cave visitor center](https://router.project-osrm.org/route/v1/driving/-86.7742984,36.1622767;-86.1012576,37.1868964?overview=false&steps=false) | about 1h50 | Under the cap. |
| [Mammoth Cave visitor center → Jackson](https://router.project-osrm.org/route/v1/driving/-86.1012576,37.1868964;-88.8177418,35.6144446?overview=false&steps=false) | about 4h08 | Under the cap. |
| [Jackson → Little Rock](https://router.project-osrm.org/route/v1/driving/-88.8177418,35.6144446;-92.2896267,34.7465071?overview=false&steps=false) | about 4h04 | Under the cap. |
| [Little Rock → Texarkana](https://router.project-osrm.org/route/v1/driving/-92.2896267,34.7465071;-94.0765653,33.4466208?overview=false&steps=false) | about 2h35 | Under the cap. |
| [Texarkana → Dallas](https://router.project-osrm.org/route/v1/driving/-94.0765653,33.4466208;-96.7968559,32.7762719?overview=false&steps=false) | about 3h06 | Under the cap. |

The direct audit rejected three tempting longer segments: [Dallas → Hot Springs](https://router.project-osrm.org/route/v1/driving/-96.7968559,32.7762719;-93.0552437,34.5038393?overview=false&steps=false) is about 5h01, [Mammoth Cave → Memphis](https://router.project-osrm.org/route/v1/driving/-86.1012576,37.1868964;-90.0517786,35.1460260?overview=false&steps=false) about 5h38, and [Little Rock → Dallas](https://router.project-osrm.org/route/v1/driving/-92.2896267,34.7465071;-96.7968559,32.7762719?overview=false&steps=false) about 5h32. The corrected route therefore uses Texarkana in both directions and Jackson on the return. It stays at 13 nights by assigning Texarkana 1+1 nights, Hot Springs 2, Memphis 2, Nashville 3, Mammoth Cave 2, Jackson 1, and Little Rock 1.

All route durations remain estimates. Before any lodging charge, E-001 must verify all nine exact lodging-to-lodging routes with a direct mapping provider and expected departure windows; E-002 must recheck the adjacent direct-provider routes immediately before each lodging checkout. Any normal leg above five hours returns the route to planning.

## Indoor coverage and booking behavior — official providers

These official pages support a planning baseline for the seven paired windows. They do not promise October inventory or unchanged hours; E-001 must recheck the date-specific official calendar before purchases, and E-003 must recheck the direct ticket provider immediately before activity checkout.

- [Hot Springs National Park — Fordyce Bathhouse](https://www.nps.gov/hosp/learn/historyculture/fordyce-bathhouse.htm): the NPS lists the visitor center and museum daily, 9 a.m.–5 p.m., with October 11–12 outside its named holiday closures. This covers days 1–2 and 3–4 from Hot Springs on days 2–3.
- [MoSH official contact page](https://moshmemphis.com/contact-us/): Pink Palace Museum is listed Tuesday–Sunday, 10:30 a.m.–5 p.m. This supports Tuesday, October 13 as a Memphis fallback.
- [National Civil Rights Museum official visit page](https://civilrightsmuseum.org/visit/): the museum is listed open Wednesday, October 14; it uses timed online tickets and publishes $25 adult/$22 child admission, or $94 for this party before any changed fees. Its family guide warns that some material may trouble children, so the adults must review suitability in E-001.
- [Adventure Science Center official visit page](https://www.adventuresci.org/visit/) and [pricing](https://www.adventuresci.org/visit/pricing/): it is listed open Friday and Saturday, October 16–17; general admission is $22 per adult and $18 per youth, or $80 for this party before add-ons.
- [Mammoth Cave NPS tour guidance](https://www.nps.gov/maca/planyourvisit/cave-tours.htm) and [official tour descriptions](https://www.nps.gov/maca/planyourvisit/explore-all-tours.htm): reservations are strongly recommended, schedules can appear only one to three months ahead, and exact October 18–19 inventory is not yet established here. Mammoth Passage and Frozen Niagara are published as all-ages options with materially fewer stairs than strenuous tours, but the adults must confirm the exact offered tour and its demands before purchase. This uncertainty makes cave availability a required E-001 gate before lodging is booked.
- [Casey Jones Home & Railroad Museum official page](https://www.caseyjones.com/museum/): the museum is listed open Tuesday, October 20. This supports the days 11–12 window from Jackson on day 11.
- [Museum of Discovery official visit page](https://museumofdiscovery.org/plan-your-visit/): the museum is listed open Wednesday, October 21 and publishes $15 adult/$13 child admission, or $56 for this party. [Clinton Library official visitor information](https://www.clintonlibrary.gov/about-us/admission-tours-and-directions) provides a second direct-provider Little Rock option, listed open Wednesday with $12 adult/$7 youth admission, or $38.
- [Texarkana Museums System official site](https://texarkanamuseum.org/): the Museum of Regional History is listed open Thursday, October 22. This supports the days 13–14 window on day 13.

## Decision effect and source-quality disposition

- The original aggregator-supported Dallas → Hot Springs and Little Rock → Dallas legs are removed, not merely relabeled. Direct routing produced over-cap baselines, so Texarkana becomes an outbound and return overnight.
- Every selected city-center leg now has a direct-router baseline below five hours, while exact addresses, traffic assumptions, closures, and departure windows remain mandatory pre-purchase checks.
- Official operating pages establish plausible indoor coverage for all seven paired windows. Future-dated hours, ticket inventory, prices, child suitability, and cave schedules remain execution gates at the direct provider.
- Published admission examples are ledger inputs, not permission to spend. E-001 must show the complete activity set at or below $650 and the whole trip at or below $6,000 before any purchase.
- No secondary fallback remains in the corrected evidence. If execution later cannot obtain a primary/direct answer to a narrow fact, it must mark the secondary claim provisional, corroborate it independently, and require a direct-provider recheck before commitment; it may not use an uncorroborated secondary claim to pass a ticket.

Additional research is unlikely to change the planning route. A failed direct-provider route, lodging, cave, indoor-cadence, or total-budget check returns the work to planning.
