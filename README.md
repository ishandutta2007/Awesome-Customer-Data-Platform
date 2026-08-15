# Awesome-Customer-Data-Platform

![Banner](assets/banner.svg)

<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a> <a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>

## 🚀 Top Customer Data Platforms (CDP) & Open-Source Alternatives

Explore our comprehensive list of the best Customer Data Platforms (CDP). A curated guide to leading **SaaS/cloud-hosted Customer Data Platforms** (like Segment, RudderStack, Snowplow, Jitsu, mParticle, Tealium, ActionIQ, Hightouch, Census, Lytics, Bloomreach) and their **open-source/self-hosted equivalents**. 

**Open-source solutions are emphasized** for data ownership, customization, privacy, and cost efficiency.

---

## ☁️ SaaS / Cloud-Hosted Customer Data Platforms

Popular platforms for collecting, unifying, and activating customer data across sources for marketing, analytics, and personalization.

### 🌟 Leading Options

| Platform | Description | Pricing Model | Free Tier Limits | Company Size |
|---|---|---|---|---|
| **[Segment](https://segment.com)** | Pioneering CDP for event collection and routing to hundreds of tools. | MTU-based | Free up to 1,000 MTUs/mo, 500k records | $3.2B Valuation (Acquired) |
| **[Bloomreach](https://bloomreach.com)** | AI-powered customer journey and personalization platforms. | Custom enterprise | No free tier | $2.2B Valuation |
| **[Tealium](https://tealium.com)** | Enterprise-focused with advanced identity resolution and orchestration. | Event volume-based | No free tier (Custom pricing) | $1.2B Valuation |
| **[Amperity](https://amperity.com)** | Enterprise CDP for identity resolution and activation. | Custom enterprise | No free tier | $1B+ Valuation |
| **[Treasure Data](https://treasuredata.com)** | Enterprise CDP specializing in unified customer views. | Custom enterprise | No free tier | $1B+ Valuation |
| **[mParticle](https://mparticle.com)** | Enterprise-focused with advanced identity resolution and orchestration. | MTU-based | No free tier (Custom pricing) | $800M+ Valuation |
| **[Hightouch](https://hightouch.com)** | Reverse ETL tools for activating warehouse data. | Destination-based | Free for 1 destination, unlimited syncs | $450M Valuation |
| **[ActionIQ](https://actioniq.com)** | AI-powered customer journey and personalization platforms. | Custom enterprise | No free tier | $140M Funding |
| **[Census](https://getcensus.com)** | Reverse ETL tools for activating warehouse data. | Destination-based | Free for 10 connections, basic syncs | $60M Funding |
| **[RudderStack](https://rudderstack.com)** | Warehouse-native CDP with strong open-source roots. | Event volume-based | Free up to 250,000 events/mo | $56M Funding |
| **[Snowplow](https://snowplow.io)** | Behavioral data platform for granular, customizable event pipelines. | Event volume-based | Open Source / Free Community Edition | $50M Funding |
| **[Lytics](https://lytics.com)** | AI-powered customer journey and personalization platforms. | Usage-based | No free tier | $40M Funding |
| **[Jitsu](https://jitsu.com)** | Open-source-friendly real-time CDP for data collection and syncing. | Event volume-based | Free up to 10,000 events/mo on Cloud | $2M Funding |

These platforms help centralize customer data, reduce engineering overhead, and enable omnichannel activation.

---

## 🛠️ Open-Source / Self-Hosted Alternatives

These tools give full control over data pipelines, schemas, and activations while keeping data in your infrastructure.

### 🔥 Featured Projects

- **[Snowplow](https://snowplow.io)** [![GitHub stars](https://img.shields.io/github/stars/snowplow/snowplow?style=social&color=white)](https://github.com/snowplow/snowplow/stargazers) — Open-source behavioral data platform for building scalable, customizable event pipelines and analytics.
- **[RudderStack](https://rudderstack.com)** [![GitHub stars](https://img.shields.io/github/stars/rudderlabs/rudder-server?style=social&color=white)](https://github.com/rudderlabs/rudder-server/stargazers) — Open-source, warehouse-native CDP. Collect events and route to warehouses/tools with Segment-compatible API.
- **[Jitsu](https://jitsu.com)** [![GitHub stars](https://img.shields.io/github/stars/jitsucom/jitsu?style=social&color=white)](https://github.com/jitsucom/jitsu/stargazers) — Open-source CDP focused on real-time data collection and syncing. Lightweight and extensible.
- **[Tracardi](https://github.com/Tracardi/tracardi)** [![GitHub stars](https://img.shields.io/github/stars/Tracardi/tracardi?style=social&color=white)](https://github.com/Tracardi/tracardi/stargazers) — Open-source customer data platform with profiling, segmentation, and journey orchestration.
- **[Apache Unomi](https://unomi.apache.org)** [![GitHub stars](https://img.shields.io/github/stars/apache/unomi?style=social&color=white)](https://github.com/apache/unomi/stargazers) — Apache project for customer data and personalization engine.

### Additional Open-Source Tools
- **OpenTelemetry** + custom pipelines for observability and data collection.
- **Airbyte** or **Meltano** for broad data integration (ELT) supporting CDP-like workflows.
- Warehouse-native tools like **dbt** combined with reverse ETL for activation.

**Tip**: **RudderStack** and **Snowplow** are the strongest open-source CDPs for replacing Segment-like functionality.

---

## ⚖️ Comparison

| Aspect              | SaaS Platforms                        | Open-Source / Self-Hosted                  |
|---------------------|---------------------------------------|--------------------------------------------|
| **Cost**            | Usage/volume-based                    | Free (only infra costs)                    |
| **Customization**   | Config & API limits                   | Full pipeline, schema, and logic control   |
| **Data Ownership**  | Vendor-managed                        | Complete control & privacy                 |
| **Setup Effort**    | Quick integrations                    | Self-hosting & maintenance required        |
| **Use Case**        | Teams seeking managed scale           | Data teams, privacy-first organizations    |

---

## 🏁 Getting Started

1. Map your data sources and destinations (warehouses, tools, activation needs).
2. Start with **RudderStack** for easy Segment migration or **Snowplow** for advanced behavioral modeling.
3. Deploy via Docker/Kubernetes and connect to your data warehouse.
4. Use reverse ETL (e.g., with open tools) for activation.
5. Focus on governance, schema validation, and compliance.

## Contributing

Feel free to submit PRs to expand this list with more projects, tools, or comparisons!

**Last updated**: July 2026  
*CDP landscapes and data privacy rules evolve quickly — always check the latest on official sites and GitHub repos.*

## 📈 Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007/Awesome-Customer-Data-Platform&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Customer-Data-Platform&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Customer-Data-Platform&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Customer-Data-Platform&type=date&legend=bottom-right" />
</picture>
</a>
</div>
# Awesome-Customer-Data-Platform

## Top Customer Data Platform (CDP) Tools Ecosystem
**Curated List of SaaS Products & Open-Source GitHub Projects**
*Focused on Event Collection, Identity Resolution, Audience Building, Data Activation, Warehouse-Native Pipelines & Customer Profiles*
**Last updated: August 2026**

This repository tracks notable **SaaS platforms** and **open-source projects** for **Customer Data Platforms (CDPs)**. These tools collect, unify, and activate customer data from websites, apps, servers, and other sources — enabling identity resolution, audience segmentation, real-time personalization, and routing to analytics, marketing, CRM, and data warehouse destinations.

**Examples** include Segment, mParticle, Tealium, Bloomreach CDP, Treasure Data, ActionIQ, Lytics, BlueConic, Simon Data, RudderStack, Hightouch, Zeotap, Bloomreach Engagement, and Optimove (the category leaders and widely adopted platforms).

**Open-source emphasis**: This category has excellent mature open-source options. The section below prioritizes self-hostable event pipelines, warehouse-native CDPs, and composable activation tools that give teams full control over data and infrastructure without MTU-based pricing lock-in.

Contributions welcome! Open a PR to add/update entries. Keep descriptions factual and link to official sites / GitHub repos.

## Table of Contents
- [SaaS/Hosted Platforms](#saas-hosted-platforms)
- [Open-Source GitHub Projects](#open-source-github-projects)
- [How to Contribute](#how-to-contribute)
- [Disclaimer](#disclaimer)

## SaaS/Hosted Platforms
- **[Segment](https://segment.com/)** (Twilio)  
  Industry-standard customer data platform for collecting events once and routing them to hundreds of destinations, with strong identity resolution and audience tools.
- **[mParticle](https://www.mparticle.com/)**  
  Enterprise CDP particularly strong in mobile, identity resolution, and real-time data orchestration across platforms.
- **[Tealium](https://tealium.com/)**  
  Mature enterprise CDP and tag management platform focused on data governance, audience building, and omnichannel activation.
- **[Bloomreach CDP / Engagement](https://www.bloomreach.com/)**  
  Customer data and engagement platform combining CDP capabilities with personalization and marketing automation.
- **[Treasure Data](https://www.treasuredata.com/)**  
  Enterprise customer data platform emphasizing large-scale data collection, unification, and activation.
- **[ActionIQ](https://www.actioniq.com/)**  
  Enterprise CDP focused on composable architecture, audience management, and activation for large organizations.
- **[Lytics](https://www.lytics.com/)**  
  Behavioral CDP with machine-learning-driven audience scoring and predictive capabilities.
- **[BlueConic](https://www.blueconic.com/)**  
  Customer data platform centered on unified profiles, lifecycle orchestration, and marketing use cases.
- **[Simon Data](https://www.simondata.com/)**  
  CDP and marketing platform focused on data-driven customer journeys and activation.
- **[RudderStack](https://www.rudderstack.com/)** (Cloud)  
  Warehouse-native customer data platform with open-source core, event collection, transformations, and extensive destination support.
- **[Hightouch](https://hightouch.com/)**  
  Leading reverse-ETL / composable CDP platform that activates data from the warehouse to business tools without a separate customer store.
- **[Zeotap](https://zeotap.com/)**  
  Customer data and identity platform with strong privacy and compliance focus.
- **[Optimove](https://www.optimove.com/)**  
  Customer-led marketing platform with CDP-like capabilities for segmentation and multichannel orchestration.
- **[Census](https://www.getcensus.com/)** / other reverse-ETL players  
  Additional warehouse-native activation tools frequently evaluated alongside Hightouch.

## Open-Source GitHub Projects
- **[RudderStack](https://github.com/rudderlabs/rudder-server)**  
  Leading open-source (and cloud) Segment alternative. Collects events from SDKs, applies transformations, and routes to 180+ destinations while treating the data warehouse as the source of truth. Production-ready and the closest feature parity to classic Segment Connections.
- **[Jitsu](https://github.com/jitsucom/jitsu)**  
  Open-source (MIT), lightweight, high-performance event collection and routing pipeline. Excellent Segment-compatible alternative focused on simplicity, speed, and direct warehouse loading (ClickHouse, BigQuery, Snowflake, etc.).
- **[Snowplow](https://github.com/snowplow/snowplow)**  
  Mature open-source behavioral data pipeline with strong schema validation, data quality guarantees, and warehouse-native design. Favored by data engineering teams that want governed, AI-ready event data.
- **[PostHog](https://github.com/PostHog/posthog)**  
  Fully open-source product analytics + CDP-style event collection platform. Captures events, supports destinations, and includes built-in analytics, session replay, feature flags, and experiments — ideal for product-led teams.
- **[TRACARDI](https://github.com/tracardi/tracardi)**  
  Open-source, API-first, composable engine for building custom Customer Data Platforms with event processing, profiling, and workflow capabilities.
- **[Multiwoven](https://github.com/Multiwoven/multiwoven)**  
  Open-source Reverse ETL and CDP-style activation platform positioned as an alternative to Hightouch and Census. Syncs warehouse data to business tools with self-hosting support.
- **Airbyte** (open-source ELT)  
  Widely used open-source data integration platform that can form part of a composable CDP stack by moving data into warehouses for activation.
- **Warehouse-native activation patterns**  
  Community and vendor-neutral approaches combining open event pipelines (RudderStack/Jitsu/Snowplow) with dbt models and reverse-ETL tools for full composable CDPs.

### Additional Strong Open-Source Options
- Schema registries and event validation tools that complement Snowplow or custom pipelines.
- Identity resolution libraries and graph-based profile stores built on open databases.
- Real-time streaming components (Kafka, Redpanda, etc.) used as the backbone of self-hosted CDPs.
- Privacy and consent management open-source tools that integrate with event collection layers.
- Emerging composable CDP accelerators that combine Snowplow + warehouse + activation.

**Frameworks for building custom systems**: The most common modern pattern is a **composable CDP**:  
**RudderStack** or **Jitsu** (or **Snowplow**) for collection → data warehouse (Snowflake/BigQuery/ClickHouse) as the source of truth → **dbt** for modeling → **Multiwoven** or similar reverse-ETL for activation. **PostHog** can serve as an all-in-one alternative when product analytics and event collection are needed together.

## How to Contribute
1. Fork the repo.
2. Add/edit entries in `README.md` (follow existing format).
3. Include: name, link, 1–2 sentence description, and whether it's SaaS or open-source.
4. Submit PR with a short explanation.

Star the repo if you find it useful!

## Disclaimer
- This is a **community-curated** list — not exhaustive and not an endorsement.
- Customer Data Platforms should be evaluated for event volume pricing, identity resolution quality, destination coverage, warehouse-native capabilities, privacy/compliance features (GDPR, CCPA), and total cost of ownership.
- Open-source CDPs give full data ownership and eliminate per-MTU fees but require engineering resources for deployment, scaling, schema management, and destination maintenance.
---
**Made for data engineers, product analytics teams, growth engineers, and anyone who wants control over customer event data without proprietary lock-in or unpredictable MTU pricing.**
Let's make customer data infrastructure more open, warehouse-native, and free from black-box platforms.
