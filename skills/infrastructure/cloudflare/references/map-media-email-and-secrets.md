# Secrets, privacy, media, realtime, and email

Need-to-product rows for this area. Products can appear in several rows and a solution can combine products. Read the linked reference or docs before implementing; load named skills when installed. Local links open bundled references: start with the README, then follow configuration, API, pattern, or gotcha links as needed. If a named skill is unavailable, use the product docs through the [Cloudflare directory](https://developers.cloudflare.com/directory/index.md).

| What you need to do | Product or tool to consider | When to choose it | Skill or reference |
| --- | --- | --- | --- |
| Store a Worker's API keys and credentials | Workers secrets | Bind secrets to a Worker without committing values to source | `wrangler` skill; [secrets docs](https://developers.cloudflare.com/workers/configuration/secrets/index.md) |
| Share managed secrets across services | Secrets Store | Manage reusable account-level secrets | [Secrets Store](secrets-store/README.md) |
| Control where data is processed and stored | Data Localization Suite | Evaluate regional processing and storage controls against the actual requirements | [Data Localization docs](https://developers.cloudflare.com/data-localization/index.md) |
| Prove a claim without identifying or tracking the user | Privacy Pass | Use privacy-preserving tokens in a supported integration | [Privacy Pass docs](https://developers.cloudflare.com/privacy-pass/index.md) |
| Store, resize, transform, and deliver images | Cloudflare Images | Use managed image processing and delivery | [Images](images/README.md) |
| Encode, store, and deliver live or on-demand video | Stream | Use managed video infrastructure | [Stream](stream/README.md) |
| Build an audio/video calling application with SDKs | RealtimeKit | Use application-level SDKs for calls and meetings | [RealtimeKit](realtimekit/README.md) |
| Build custom real-time media infrastructure | Realtime SFU | Control the application while using a selective forwarding unit for media | [Realtime SFU](realtime-sfu/README.md) |
| Relay WebRTC connections through restrictive networks | TURN Service | Clients need a connectivity relay | [TURN](turn/README.md) |
| Deliver live media over QUIC | MoQ | Use the Media over QUIC protocol; check current compatibility and availability | [MoQ docs](https://developers.cloudflare.com/moq/index.md) |
| Send transactional email | Email Service | Send application-generated messages | `cloudflare-email-service` skill; [Email Service docs](https://developers.cloudflare.com/email-service/index.md) |
| Forward incoming email | Email Routing | Route addresses on a domain to destination mailboxes | [Email Routing](email-routing/README.md) |
| Process incoming email in code | Email Workers | Apply custom logic to inbound messages | [Email Workers](email-workers/README.md) |
| Manage third-party tags and scripts | Zaraz | Load and manage third-party tools through Cloudflare | [Zaraz](zaraz/README.md) |
