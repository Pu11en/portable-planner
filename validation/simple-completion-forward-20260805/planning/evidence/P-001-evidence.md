# P-001 Evidence — YouTube Access and Provenance

Accessed: 2026-08-05

## Sources and decision-changing findings

### YouTube Terms of Service

- Source: [YouTube Terms of Service](https://www.youtube.com/t/terms)
- Finding: YouTube allows browsing and searching some content without a Google account, but restricts automated access such as robots or scrapers except in stated circumstances. It also restricts downloading or using content outside functionality YouTube provides.
- Decision changed: The skill must use only a harness-provided compliant public browsing/search route, stay read-only and human-scale, avoid scraping/circumvention/downloads, and stop with a clear limitation when no permitted route is available.

### YouTube comment viewing and shareable links

- Source: [View, organize, or delete comments — YouTube Help](https://support.google.com/youtube/answer/6000976?hl=en)
- Finding: The web interface supports `Newest first` and `Top comments`. Clicking a comment timestamp creates a highlighted-comment URL for that comment thread.
- Decision changed: Review can prefer recent comments while using top comments as a secondary source, and the report can provide a direct comment link when the interface exposes the timestamp action.

### YouTube Data API requirements

- Sources: [YouTube Data API overview](https://developers.google.com/youtube/v3/getting-started), [API reference](https://developers.google.com/youtube/v3/docs), and [Search: list](https://developers.google.com/youtube/v3/docs/search/list)
- Finding: The official API can list search results and comment threads, but setup requires a Google account, a Google Cloud project, API enablement, and credentials; requests also consume quota.
- Decision changed: The API is not a core dependency for the confirmed no-account/no-paid-service experience. It is not offered as a hidden fallback.

### Channel identity

- Source: [Work with channel IDs — YouTube Data API](https://developers.google.com/youtube/v3/guides/working_with_channel_ids)
- Finding: Channel display names are not unique, while channel IDs identify canonical channels; YouTube also supports shareable handle URLs.
- Decision changed: The skill resolves names to canonical channel identities and asks for a handle or URL only when ambiguity cannot be resolved safely. Every selected video is rechecked against the locked identity.

## Research conclusion

The viable core is a bounded, user-initiated, read-only skill that works from public pages through compliant harness capabilities, preserves exact provenance, and fails closed when access is unavailable. A key-requiring API, bulk scraper, downloader, or account-dependent route would contradict the confirmed product boundary.
