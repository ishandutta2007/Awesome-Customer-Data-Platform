<p align="center">
  <img src="assets/banner.svg" alt="Awesome Customer Data Platform Banner" width="100%" />
</p>

# Awesome Customer Data Platform (CDP) ⚡ 📊 🚀

<p align="center">
  <b>A curated directory of leading SaaS Customer Data Platforms, Warehouse-Native Composable CDPs, and Open-Source Behavioral Event Streaming Pipelines</b>
</p>

<p align="center">
  <a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>
  <a href="https://github.com/ishandutta2007/Awesome-Customer-Data-Platform/stargazers"><img src="https://img.shields.io/github/stars/ishandutta2007/Awesome-Customer-Data-Platform?style=social" alt="GitHub Stars"/></a>
  <a href="https://github.com/ishandutta2007/Awesome-Customer-Data-Platform/network/members"><img src="https://img.shields.io/github/forks/ishandutta2007/Awesome-Customer-Data-Platform?style=social" alt="GitHub Forks"/></a>
  <a href="https://github.com/ishandutta2007/Awesome-Customer-Data-Platform/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square" alt="License: MIT"/></a>
  <a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>
</p>

---

## 📖 Table of Contents

- [🌟 Overview & Core Capabilities](#-overview--core-capabilities)
- [☁️ SaaS / Cloud-Hosted Customer Data Platforms](#️-saas--cloud-hosted-customer-data-platforms)
- [💻 Open-Source / Self-Hosted CDP Projects](#-open-source--self-hosted-cdp-projects)
- [🏗️ Composable CDP Architecture Patterns](#️-composable-cdp-architecture-patterns)
- [⚖️ SaaS vs. Open-Source Comparison](#️-saas-vs-open-source-comparison)
- [🏁 Quickstart Guide](#-quickstart-guide)
- [🤝 How to Contribute](#-how-to-contribute)
- [⚠️ Evaluation & Privacy Disclaimer](#️-evaluation--privacy-disclaimer)
- [  Star History](#--star-history)

---

## 🌟 Overview & Core Capabilities

A **Customer Data Platform (CDP)** is packaged software that builds a persistent, unified customer database (Single Customer View / Customer 360) accessible to other systems. CDPs ingest first-party customer behavioral data across web, mobile apps, CRM, POS, and offline systems, resolve user identities deterministically or probabilistically, perform audience segmentation, and activate targeted audiences into downstream marketing, ad platforms, and analytics destinations in real time.

Modern Customer Data architectures encompass:
- **Packaged Traditional CDPs**: Turnkey all-in-one SaaS platforms managing ingestion, profile storage, identity graphs, and multi-channel orchestration.
- **Warehouse-Native & Composable CDPs**: Modern modular stacks leveraging cloud data warehouses (Snowflake, BigQuery, Databricks, ClickHouse) as the single source of truth, paired with Reverse ETL activation tools and modeling layers.
- **Open-Source Behavioral Data Pipelines**: Self-hosted event collectors and routing pipelines providing complete data privacy, sovereign data control, and zero vendor lock-in.

---

## ☁️ SaaS / Cloud-Hosted Customer Data Platforms

The table below lists leading SaaS and cloud-hosted Customer Data Platforms, **sorted in descending order by company size (valuation / revenue)**.

| Platform | Description & Key Focus | Company Size / Valuation 👑 | Pricing (Starting Tier) 💳 | Free Tier Limits / Trial 🎁 |
|---|---|---|---|---|
| **[Segment](https://segment.com)** | Pioneering industry-standard CDP for event collection, identity resolution, and real-time routing to 450+ marketing & analytics destinations. | **$3.2B Valuation** (Acquired by Twilio) | Starts at **$120/mo** (Team plan, up to 10k MTUs; custom Business tiers) | **Free forever** up to 1,000 MTUs/mo (2 sources, unlimited destinations, 500k sync records); 14-day Team trial |
| **[Bloomreach](https://bloomreach.com)** | AI-powered commerce customer data and engagement platform combining CDP profile unification with real-time web personalization and omni-channel campaigns. | **$2.2B Valuation** ($175M+ Raised) | Starts at **~$2,900/mo** ($35k/yr starting module; full platform scales to $150k+/yr) | **14-to-30-day guided evaluation / developer environment trial** upon demo (No permanent free tier) |
| **[Tealium](https://tealium.com)** | Enterprise-grade customer data hub and tag management platform specializing in granular data governance, identity resolution, and real-time activation. | **$1.2B Valuation** (Series G / Silver Lake) | Starts at **~$1,000/mo** ($12k/yr for Data Cloud Activation; core AudienceStream CDP from $30k/yr) | **30-day proof-of-concept sandbox trial** upon enterprise demo & qualification (No permanent free tier) |
| **[Amperity](https://amperity.com)** | AI-driven enterprise CDP engineered for patented identity resolution (AmpID), predictive customer analytics (AmpIQ), and warehouse activation. | **$1.0B+ Valuation** (Unicorn / Series D) | Starts at **~$8,300/mo** ($100k/yr entry tier based on "Amps" compute credits) | **30-day guided proof-of-concept pilot** with custom dataset upon enterprise qualification (No permanent free tier) |
| **[Treasure Data](https://treasuredata.com)** | Enterprise Customer Data Cloud engineered for petabyte-scale streaming ingestion, unified customer profile management, and AI journey orchestration. | **$1.0B+ Valuation** (SoftBank subsidiary / $234M Funding) | Starts at **~$3,500/mo** ($42k/yr entry package; large enterprise scales to $200k–$500k+/yr) | **14-to-30-day guided POC sandbox** via sales / AWS Marketplace demo (No permanent free tier) |
| **[mParticle](https://mparticle.com)** | Multi-channel enterprise CDP with exceptional strength in mobile SDK data capture, cross-device identity resolution, and real-time audience orchestration. | **$800M+ Valuation** (Series E / Harmony Partners) | Starts at **~$1,000/mo** ($15k/yr entry tier via mParticle Credits; enterprise $60k–$150k+/yr) | **30-day proof-of-concept sandbox trial** upon sales consultation (No permanent free tier) |
| **[Hightouch](https://hightouch.com)** | Leading warehouse-native composable CDP and Reverse ETL platform that activates customer data directly from warehouses into 200+ SaaS tools and ad networks. | **$600M+ Valuation** ($140M+ Funding) | Starts at **$350/mo** (Starter tier for sub-hourly sync frequency and added destinations) | **Free forever** with 2 active syncs/mo (hourly frequency, up to 100M operations/mo, unlimited destinations/users); 14-day trial |
| **[ActionIQ](https://actioniq.com)** | Hybrid composable enterprise CDP enabling business and marketing teams to build self-service audiences directly on top of cloud data warehouses. | **$450M Valuation** ($140M Funding / March Capital) | Starts at **~$8,300/mo** ($100k/yr entry platform tier; custom enterprise contracts up to $400k+/yr) | **30-day customized enterprise pilot / POC** upon architecture assessment (No permanent free tier) |
| **[Optimove](https://optimove.com)** | Relationship marketing CDP combining unified customer profile models with AI predictive analytics and autonomous multi-channel campaign orchestration. | **$400M+ Valuation** ($120M Funding / Summit Partners) | Starts at **~$4,000/mo** ($48k/yr base tier scaling with monthly active customer database size) | **14-day guided proof-of-concept / sandbox demo** upon consultation (No permanent free tier) |
| **[RudderStack](https://rudderstack.com)** (Cloud) | Warehouse-native customer data platform with open-source roots, real-time event routing, data transformations, and built-in Reverse ETL pipelines. | **$300M+ Valuation** ($56M Series B / Insight Partners) | Starts at **$265/mo** (Growth plan for 1M events/mo, 15% annual discount) | **Free forever** up to 250,000 events/mo (16+ SDKs, 200+ destinations, 5 JS transformations, 3h sync); 30-day Growth trial |
| **[Snowplow](https://snowplow.io)** (BDP Cloud) | Behavioral data platform generating rich, structured, validated event data streams engineered for AI, machine learning, and cloud data warehouses. | **$250M+ Valuation** ($50M Funding / NEA) | Starts at **~$800/mo** ($30k/yr for BDP Cloud Growth tiers up to 30M events/mo) | **14-day free trial** on Snowplow BDP Cloud (no credit card); Free forever self-hosted Community Edition |
| **[Zeotap](https://zeotap.com)** | Privacy-first European CDP built with strict GDPR/ePrivacy compliance, identity resolution, consent orchestration, and omnichannel marketing activation. | **$250M+ Valuation** ($90M Funding) | Starts at **~$2,000/mo** ($24k/yr entry tier based on Monthly Active Profiles) | **14-to-30-day POC trial environment** upon sales qualification (No permanent free tier) |
| **[BlueConic](https://blueconic.com)** | Pure-play customer data platform providing first-party profile unification, lifecycle journey orchestration, and predictive customer scoring. | **$150M+ Valuation** (Vista Equity Partners) | Starts at **~$2,500/mo** ($30k/yr base license scaling with total profile count and domains) | **14-to-30-day testing sandbox / demo trial** provided after qualification (No permanent free tier) |
| **[Simon Data](https://simondata.com)** | Snowflake-connected CDP and marketing platform designed to build complex, trigger-based multi-channel customer journeys directly from the warehouse. | **$150M+ Valuation** ($60M Funding / Polaris Partners) | Starts at **~$3,000/mo** ($36k/yr entry tier based on connected contact profiles) | **90-day assisted enterprise pilot program** or 14-day demo environment (No permanent free tier) |
| **[Census](https://getcensus.com)** (Fivetran Activations) | Warehouse-native activation and Reverse ETL platform (part of Fivetran) syncing data warehouse models to CRMs, marketing platforms, and operational tools. | **$60M Funding** ($5.6B Parent Fivetran) | Starts at **$350/mo** (Census Starter) or **$5/conn** base + MAR via Fivetran | **Free forever** for 10 destination connections & basic syncs; 14-day free trial on Fivetran Activations |
| **[Lytics](https://lytics.com)** (Contentstack) | Behavioral CDP featuring machine-learning-driven content affinity scoring, audience segmentation, and profile unification (part of Contentstack). | **$40M Funding** ($1B+ Parent Contentstack) | Starts at **~$500/mo** (Legacy Cloud tier) or custom via Contentstack DXP suite | **14-day free trial** / guided demo via Contentstack (Legacy Developer plan had 10k profile limit) |
| **[Jitsu](https://jitsu.com)** (Cloud) | Open-source-friendly, high-performance real-time CDP for event collection, transformation functions, and direct data warehouse streaming. | **$15M Valuation** ($2M Funding / Y Combinator) | Starts at **$99/mo** (Premium plan, 5 daily active syncs, +$10/mo per extra sync) | **Free forever** up to 200,000 active events/mo (1 daily sync, unlimited captured events, free ClickHouse) |

---

## 💻 Open-Source / Self-Hosted CDP Projects

The table and list below feature top open-source Customer Data Platforms, behavioral event pipelines, Reverse ETL frameworks, and composable data layers, **sorted in descending order by GitHub Stars ⭐**.

| Repository | GitHub Stars Badge | Primary Focus / Category | License |
|---|---|---|---|
| **[PostHog](https://github.com/PostHog/posthog)** | [![GitHub stars](https://img.shields.io/github/stars/PostHog/posthog?style=social&color=white)](https://github.com/PostHog/posthog/stargazers) | Product Analytics + Event Capture & CDP Pipelines | MIT / Open Core |
| **[Airbyte](https://github.com/airbytehq/airbyte)** | [![GitHub stars](https://img.shields.io/github/stars/airbytehq/airbyte?style=social&color=white)](https://github.com/airbytehq/airbyte/stargazers) | ELT Data Ingestion & Warehouse Connectors | ELv2 / MIT Connectors |
| **[dbt Core](https://github.com/dbt-labs/dbt-core)** | [![GitHub stars](https://img.shields.io/github/stars/dbt-labs/dbt-core?style=social&color=white)](https://github.com/dbt-labs/dbt-core/stargazers) | In-Warehouse Customer Profile Modeling & Metrics | Apache-2.0 |
| **[Snowplow](https://github.com/snowplow/snowplow)** | [![GitHub stars](https://img.shields.io/github/stars/snowplow/snowplow?style=social&color=white)](https://github.com/snowplow/snowplow/stargazers) | Enterprise Behavioral Event Collection & Validation | Apache-2.0 / SLULA |
| **[OpenTelemetry Collector](https://github.com/open-telemetry/opentelemetry-collector)** | [![GitHub stars](https://img.shields.io/github/stars/open-telemetry/opentelemetry-collector?style=social&color=white)](https://github.com/open-telemetry/opentelemetry-collector/stargazers) | Universal Telemetry & Event Ingestion Proxy | Apache-2.0 |
| **[RudderStack](https://github.com/rudderlabs/rudder-server)** | [![GitHub stars](https://img.shields.io/github/stars/rudderlabs/rudder-server?style=social&color=white)](https://github.com/rudderlabs/rudder-server/stargazers) | Warehouse-Native CDP & Segment-Compatible Router | SSPL |
| **[Jitsu](https://github.com/jitsucom/jitsu)** | [![GitHub stars](https://img.shields.io/github/stars/jitsucom/jitsu?style=social&color=white)](https://github.com/jitsucom/jitsu/stargazers) | Lightweight Real-Time Event Pipeline & Syncing | MIT |
| **[Meltano](https://github.com/meltano/meltano)** | [![GitHub stars](https://img.shields.io/github/stars/meltano/meltano?style=social&color=white)](https://github.com/meltano/meltano/stargazers) | Declarative DataOps & Composable ELT Engine | MIT |
| **[Tracardi](https://github.com/tracardi/tracardi)** | [![GitHub stars](https://img.shields.io/github/stars/tracardi/tracardi?style=social&color=white)](https://github.com/tracardi/tracardi/stargazers) | API-First Low-Code CDP & Journey Automation | MIT |
| **[Multiwoven](https://github.com/multiwoven/multiwoven)** | [![GitHub stars](https://img.shields.io/github/stars/multiwoven/multiwoven?style=social&color=white)](https://github.com/multiwoven/multiwoven/stargazers) | Composable Reverse ETL & Warehouse Activation | AGPL-3.0 |
| **[Apache Unomi](https://github.com/apache/unomi)** | [![GitHub stars](https://img.shields.io/github/stars/apache/unomi?style=social&color=white)](https://github.com/apache/unomi/stargazers) | OASIS Standard Customer Data Platform Engine | Apache-2.0 |
| **[Uniflow](https://github.com/maroil/uniflow)** | [![GitHub stars](https://img.shields.io/github/stars/maroil/uniflow?style=social&color=white)](https://github.com/maroil/uniflow/stargazers) | AWS-Native Self-Hosted CDP & Identity Resolution | MIT |

---

### 🔥 Featured Open-Source Projects Deep-Dive

- **[PostHog](https://github.com/PostHog/posthog)** [![GitHub stars](https://img.shields.io/github/stars/PostHog/posthog?style=social&color=white)](https://github.com/PostHog/posthog/stargazers)  
  ⚡ **All-in-one product analytics, session recording, and event capture CDP.** Captures web and mobile events automatically, manages user identities, creates dynamic cohort segments, and routes customer events to external data destinations.

- **[Airbyte](https://github.com/airbytehq/airbyte)** [![GitHub stars](https://img.shields.io/github/stars/airbytehq/airbyte?style=social&color=white)](https://github.com/airbytehq/airbyte/stargazers)  
  📥 **Leading open-source ELT data integration engine.** Ingests customer data from 300+ SaaS applications (Stripe, HubSpot, Salesforce, Zendesk) directly into data warehouses to power composable CDP identity graphs.

- **[dbt Core](https://github.com/dbt-labs/dbt-core)** [![GitHub stars](https://img.shields.io/github/stars/dbt-labs/dbt-core?style=social&color=white)](https://github.com/dbt-labs/dbt-core/stargazers)  
  🏛️ **In-warehouse data transformation framework.** Serves as the computational modeling core of modern composable CDPs by turning raw event logs into unified customer profiles, RFM scores, and predictive traits via SQL.

- **[Snowplow](https://github.com/snowplow/snowplow)** [![GitHub stars](https://img.shields.io/github/stars/snowplow/snowplow?style=social&color=white)](https://github.com/snowplow/snowplow/stargazers)  
  ❄️ **Enterprise behavioral data platform.** Ingests, validates, enriches, and models real-time customer event streams with strict schema validation directly into Snowflake, BigQuery, ClickHouse, and Databricks.

- **[OpenTelemetry Collector](https://github.com/open-telemetry/opentelemetry-collector)** [![GitHub stars](https://img.shields.io/github/stars/open-telemetry/opentelemetry-collector?style=social&color=white)](https://github.com/open-telemetry/opentelemetry-collector/stargazers)  
  📡 **High-throughput event proxy & collector.** Receives, batches, scrubs PII, transforms, and fans out event streams to multiple storage layers and analytical endpoints with high performance.

- **[RudderStack](https://github.com/rudderlabs/rudder-server)** [![GitHub stars](https://img.shields.io/github/stars/rudderlabs/rudder-server?style=social&color=white)](https://github.com/rudderlabs/rudder-server/stargazers)  
  🚀 **Leading open-source warehouse-native CDP.** Offers 100% Segment-compatible SDK APIs, handles real-time event streaming, user transformations via JavaScript, and routes to 180+ cloud destinations and warehouses.

- **[Jitsu](https://github.com/jitsucom/jitsu)** [![GitHub stars](https://img.shields.io/github/stars/jitsucom/jitsu?style=social&color=white)](https://github.com/jitsucom/jitsu/stargazers)  
  ⚡ **High-speed, lightweight event collection pipeline.** Written in Go and TypeScript, Jitsu captures browser/mobile events with zero third-party cookie issues and streams them directly into ClickHouse, Postgres, or BigQuery.

- **[Meltano](https://github.com/meltano/meltano)** [![GitHub stars](https://img.shields.io/github/stars/meltano/meltano?style=social&color=white)](https://github.com/meltano/meltano/stargazers)  
  🛠️ **Declarative, code-first DataOps and ELT platform.** Combines Singer taps and targets with dbt transformations in a single version-controlled repository for managing custom customer data stacks.

- **[Tracardi](https://github.com/tracardi/tracardi)** [![GitHub stars](https://img.shields.io/github/stars/tracardi/tracardi?style=social&color=white)](https://github.com/tracardi/tracardi/stargazers)  
  🧩 **API-first open-source customer data platform.** Built for real-time profiling, identity stitching, and automated marketing workflows with an intuitive low-code visual workflow editor.

- **[Multiwoven](https://github.com/multiwoven/multiwoven)** [![GitHub stars](https://img.shields.io/github/stars/multiwoven/multiwoven?style=social&color=white)](https://github.com/multiwoven/multiwoven/stargazers)  
  🔄 **Open-source Reverse ETL activation engine.** Bridges data warehouses directly to business tools (HubSpot, Salesforce, Google Ads, Mailchimp, Slack) with self-hosted container deployments.

- **[Apache Unomi](https://github.com/apache/unomi)** [![GitHub stars](https://img.shields.io/github/stars/apache/unomi?style=social&color=white)](https://github.com/apache/unomi/stargazers)  
  🏛️ **Reference OASIS CDP standard server.** Java-based customer data platform and personalization engine designed to integrate with CMSs, web applications, and marketing automation suites.

- **[Uniflow](https://github.com/maroil/uniflow)** [![GitHub stars](https://img.shields.io/github/stars/maroil/uniflow?style=social&color=white)](https://github.com/maroil/uniflow/stargazers)  
  ☁️ **Self-hosted AWS customer data platform.** Serverless CDP built on AWS Lambda, DynamoDB, and Kinesis providing event tracking, deterministic identity resolution, and user segmentation.

---

## 🏗️ Composable CDP Architecture Patterns

Modern engineering teams increasingly replace monolithic black-box CDPs with a **Composable CDP architecture**:

```
[ Sources: Web, Mobile, CRM, Ads ]
               │
               ▼
[ 1. Ingestion / Collection: RudderStack / Snowplow / Jitsu / Airbyte ]
               │
               ▼
[ 2. Single Source of Truth: Data Warehouse (Snowflake / BigQuery / ClickHouse / Databricks) ]
               │
               ▼
[ 3. Modeling & Identity Resolution: dbt Core (Customer 360 / Traits / Cohorts) ]
               │
               ▼
[ 4. Data Activation / Reverse ETL: Multiwoven / Hightouch / Census ]
               │
               ▼
[ Destinations: CRMs, Ad Audiences, Email/SMS, Support, Analytics ]
```

### Key Advantages of Composable CDPs:
1. **No Data Redundancy**: Avoid paying SaaS vendors to store a duplicate copy of data already residing in your warehouse.
2. **Zero MTU Tax**: Eliminate restrictive Monthly Tracked User (MTU) pricing limits that penalize website growth and high visitor counts.
3. **Full Governance & Privacy**: Sensitive customer data remains encrypted within your own cloud boundary (AWS / GCP / Azure).
4. **Flexible Modeling**: Define custom business logic, churn predictions, and LTV scores in SQL without proprietary CDP schema constraints.

---

## ⚖️ SaaS vs. Open-Source Comparison

| Evaluation Metric | ☁️ SaaS / Hosted CDPs | 💻 Open-Source / Composable CDPs |
|---|---|---|
| **Cost Predictability** | Tiered by MTUs/Profiles; can scale rapidly with traffic spikes | Predictable flat infrastructure compute and storage costs |
| **Implementation Speed** | Turnkey SDKs, out-of-the-box UI, and pre-built integrations | Requires developer configuration, container orchestration & CI/CD |
| **Data Governance** | Data stored in vendor cloud; subject to third-party sub-processors | 100% data sovereignty; compliant with GDPR, HIPAA, and CCPA |
| **Custom Transformations** | Limited to vendor UI functions and rate-limited APIs | Unlimited custom transformation logic, SQL models, and code plugins |
| **Operational Overhead** | Fully managed SLAs, automatic scaling, and vendor support | Self-managed maintenance, database tuning, and pipeline observability |
| **Best Suited For** | Marketing/growth teams requiring immediate UI tools without engineering | Data engineering and product teams seeking maximum customization and data control |

---

## 🏁 Quickstart Guide

1. **Map Your Architecture**: Identify all upstream data sources (Web, iOS/Android apps, backend servers, Stripe, CRMs) and downstream activation targets.
2. **Deploy Event Collection**:
   - For fast Segment drop-in compatibility: Deploy **[RudderStack](https://github.com/rudderlabs/rudder-server)** or **[Jitsu](https://github.com/jitsucom/jitsu)** via Docker/Kubernetes.
   - For granular, schema-validated behavioral pipelines: Deploy **[Snowplow](https://github.com/snowplow/snowplow)**.
3. **Establish Warehouse Source of Truth**: Route all event streams into your cloud data warehouse (Snowflake, BigQuery, ClickHouse, or PostgreSQL).
4. **Build Identity Graphs with dbt**: Create `dbt` data models that merge anonymous cookie IDs, email addresses, and user IDs into unified `dim_customers` tables.
5. **Activate via Reverse ETL**: Use **[Multiwoven](https://github.com/multiwoven/multiwoven)** or **[Hightouch](https://hightouch.com)** to sync customer audiences into Facebook Ads, Google Ads, Klaviyo, Salesforce, and HubSpot.

---

## 🤝 How to Contribute

Contributions from data engineers, analytics engineers, and open-source creators are warmly welcome!

1. 🍴 **Fork the repository** on GitHub.
2. 🌿 **Create a feature branch**: `git checkout -b add-new-cdp-tool`
3. 📝 **Add your entry** in `README.md` following the established table structure:
   - For **SaaS platforms**: Include Platform Name, Link, Description, Company Size/Valuation, Starting Tier Price, and specific Free Tier/Trial Limits. Insert in the correct sorted order by valuation.
   - For **Open-Source tools**: Include Repository Name, GitHub URL, Social Star Badge (`style=social&color=white` linking to stargazers), Category, and License. Insert in the correct sorted order by stars.
4. 🚀 **Submit a Pull Request** with a brief summary of the addition.

⭐ **Star the repo** if you find this customer data infrastructure curated guide valuable!

---

## ⚠️ Evaluation & Privacy Disclaimer

- This repository is a **community-curated index** created for informational and educational purposes — listings do not constitute a commercial endorsement.
- Customer Data Platforms should be evaluated against your organization's specific event volume, identity resolution requirements, compliance constraints (GDPR, CCPA, HIPAA), and total cost of ownership (TCO).
- When self-hosting open-source CDPs, teams are responsible for data security, role-based access control, encryption in transit/rest, and database backup redundancy.

---

##  Star History

[![Star History Chart](https://star-history.dera.page/svg?repos=ishandutta2007/Awesome-Customer-Data-Platform&type=date&legend=top-left)](https://star-history.dera.page/#ishandutta2007/Awesome-Customer-Data-Platform&type=date&legend=top-left)

---

<p align="center">
  <sub>Made with ❤️ for data engineers, product analytics teams, growth engineers, and anyone who wants control over customer event data without proprietary lock-in.</sub>
</p>
