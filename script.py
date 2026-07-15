import os
import re
import subprocess

repo_dir = r'C:\Users\ishan\Documents\Projects\Awesome-Customer-Data-Platform'
readme_path = os.path.join(repo_dir, 'README.md')
git_dir = os.path.join(repo_dir, '.git')

def run_git(commit_msg):
    cmds = [
        f'git --git-dir="{git_dir}" --work-tree="{repo_dir}" add .',
        f'git --git-dir="{git_dir}" --work-tree="{repo_dir}" commit -m "{commit_msg}"',
        f'git --git-dir="{git_dir}" --work-tree="{repo_dir}" push origin main'
    ]
    for cmd in cmds:
        print('Running:', cmd)
        subprocess.run(cmd, shell=True, cwd=repo_dir)

with open(readme_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. SaaS company size
saas_data = [
    ('| **[Segment](https://segment.com)** | Pioneering CDP for event collection and routing to hundreds of tools. | MTU-based | Free up to 1,000 MTUs/mo, 500k records |', 3200, '$3.2B Valuation (Acquired)'),
    ('| **[Bloomreach](https://bloomreach.com)** | AI-powered customer journey and personalization platforms. | Custom enterprise | No free tier |', 2200, '$2.2B Valuation'),
    ('| **[Tealium](https://tealium.com)** | Enterprise-focused with advanced identity resolution and orchestration. | Event volume-based | No free tier (Custom pricing) |', 1200, '$1.2B Valuation'),
    ('| **[Amperity](https://amperity.com)** | Enterprise CDP for identity resolution and activation. | Custom enterprise | No free tier |', 1000, '$1B+ Valuation'),
    ('| **[Treasure Data](https://treasuredata.com)** | Enterprise CDP specializing in unified customer views. | Custom enterprise | No free tier |', 1000, '$1B+ Valuation'),
    ('| **[mParticle](https://mparticle.com)** | Enterprise-focused with advanced identity resolution and orchestration. | MTU-based | No free tier (Custom pricing) |', 800, '$800M+ Valuation'),
    ('| **[Hightouch](https://hightouch.com)** | Reverse ETL tools for activating warehouse data. | Destination-based | Free for 1 destination, unlimited syncs |', 450, '$450M Valuation'),
    ('| **[ActionIQ](https://actioniq.com)** | AI-powered customer journey and personalization platforms. | Custom enterprise | No free tier |', 140, '$140M Funding'),
    ('| **[Census](https://getcensus.com)** | Reverse ETL tools for activating warehouse data. | Destination-based | Free for 10 connections, basic syncs |', 60, '$60M Funding'),
    ('| **[RudderStack](https://rudderstack.com)** | Warehouse-native CDP with strong open-source roots. | Event volume-based | Free up to 250,000 events/mo |', 56, '$56M Funding'),
    ('| **[Snowplow](https://snowplow.io)** | Behavioral data platform for granular, customizable event pipelines. | Event volume-based | Open Source / Free Community Edition |', 50, '$50M Funding'),
    ('| **[Lytics](https://lytics.com)** | AI-powered customer journey and personalization platforms. | Usage-based | No free tier |', 40, '$40M Funding'),
    ('| **[Jitsu](https://jitsu.com)** | Open-source-friendly real-time CDP for data collection and syncing. | Event volume-based | Free up to 10,000 events/mo on Cloud |', 2, '$2M Funding')
]
saas_data.sort(key=lambda x: x[1], reverse=True)

new_table = '| Platform | Description | Pricing Model | Free Tier Limits | Company Size |\n|---|---|---|---|---|\n'
for row in saas_data:
    new_table += row[0] + ' ' + row[2] + ' |\n'

content = re.sub(r'\| Platform \| Description \| Pricing Model \| Free Tier Limits \|\n\|---\|---\|---\|---\|\n(?:\|.*?\|\n)+', new_table, content)
with open(readme_path, 'w', encoding='utf-8') as f: f.write(content)
run_git('Added company size and sorted the SaaS based on that')

# 2. Open source stars
content = re.sub(r'### Featured Projects\n\n- \*\*\[RudderStack\].*?(?=\n###)', 
'''### Featured Projects

- **[Snowplow](https://snowplow.io)** [![GitHub stars](https://img.shields.io/github/stars/snowplow/snowplow?style=social&color=white)](https://github.com/snowplow/snowplow/stargazers) — Open-source behavioral data platform for building scalable, customizable event pipelines and analytics.
- **[RudderStack](https://rudderstack.com)** [![GitHub stars](https://img.shields.io/github/stars/rudderlabs/rudder-server?style=social&color=white)](https://github.com/rudderlabs/rudder-server/stargazers) — Open-source, warehouse-native CDP. Collect events and route to warehouses/tools with Segment-compatible API.
- **[Jitsu](https://jitsu.com)** [![GitHub stars](https://img.shields.io/github/stars/jitsucom/jitsu?style=social&color=white)](https://github.com/jitsucom/jitsu/stargazers) — Open-source CDP focused on real-time data collection and syncing. Lightweight and extensible.
- **[Tracardi](https://github.com/Tracardi/tracardi)** [![GitHub stars](https://img.shields.io/github/stars/Tracardi/tracardi?style=social&color=white)](https://github.com/Tracardi/tracardi/stargazers) — Open-source customer data platform with profiling, segmentation, and journey orchestration.
- **[Apache Unomi](https://unomi.apache.org)** [![GitHub stars](https://img.shields.io/github/stars/apache/unomi?style=social&color=white)](https://github.com/apache/unomi/stargazers) — Apache project for customer data and personalization engine.
''', content, flags=re.DOTALL)
with open(readme_path, 'w', encoding='utf-8') as f: f.write(content)
run_git('Added github stars and sorted the opensource based on that')

# 3. SVG Banner
os.makedirs(os.path.join(repo_dir, 'assets'), exist_ok=True)
svg_content = '''<svg width="800" height="300" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#4facfe;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#00f2fe;stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#grad1)" rx="15" />
  <text x="50%" y="40%" font-family="Arial, sans-serif" font-size="42" font-weight="bold" fill="white" text-anchor="middle">Awesome Customer Data Platforms</text>
  <text x="50%" y="60%" font-family="Arial, sans-serif" font-size="24" fill="white" text-anchor="middle">Curated SaaS &amp; Open-Source CDPs</text>
  <circle cx="50" cy="50" r="20" fill="#ffffff" opacity="0.2">
    <animate attributeName="r" values="20;30;20" dur="3s" repeatCount="indefinite"/>
  </circle>
</svg>'''
with open(os.path.join(repo_dir, 'assets', 'banner.svg'), 'w', encoding='utf-8') as f: f.write(svg_content)
content = '# Awesome-Customer-Data-Platform\n\n![Banner](assets/banner.svg)\n\n' + content.split('# Awesome-Customer-Data-Platform\n')[1]
with open(readme_path, 'w', encoding='utf-8') as f: f.write(content)
run_git('added banner')

# 4. Emojis
content = content.replace('## Top Customer Data Platforms', '## 🚀 Top Customer Data Platforms')
content = content.replace('## SaaS / Cloud-Hosted', '## ☁️ SaaS / Cloud-Hosted')
content = content.replace('### Leading Options', '### 🌟 Leading Options')
content = content.replace('## Open-Source / Self-Hosted', '## 🛠️ Open-Source / Self-Hosted')
content = content.replace('### Featured Projects', '### 🔥 Featured Projects')
content = content.replace('## Comparison', '## ⚖️ Comparison')
content = content.replace('## Getting Started', '## 🏁 Getting Started')
with open(readme_path, 'w', encoding='utf-8') as f: f.write(content)
run_git('added emojis')

# 5. SEO
content = content.replace('A curated guide to leading', 'Explore our comprehensive list of the best Customer Data Platforms (CDP). A curated guide to leading')
with open(readme_path, 'w', encoding='utf-8') as f: f.write(content)
run_git('seo optimised')

# 6. Badges Left
badges_left = '<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a> '
content = re.sub(r'(# Awesome-Customer-Data-Platform\n\n!\[Banner\]\(assets/banner.svg\)\n\n)', r'\1' + badges_left, content)
with open(readme_path, 'w', encoding='utf-8') as f: f.write(content)
run_git('badges to left added')

# 7. Badges Right
badges_right = '<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>\n\n'
content = content.replace(badges_left, badges_left + badges_right)
with open(readme_path, 'w', encoding='utf-8') as f: f.write(content)
run_git('badges to right added')

# 8. Star History
star_history = '''
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
'''
content += star_history
with open(readme_path, 'w', encoding='utf-8') as f: f.write(content)
run_git('star history added')

# 9. Fixed star plot
content = content.replace('chartrepos', 'chart?repos')
with open(readme_path, 'w', encoding='utf-8') as f: f.write(content)
run_git('fixed star plot')

# 10. Invalid awesome link
content = content.replace('https://github.com/sindresorhus/awesome', 'https://github.com/ishandutta2007/Awesome-Awesome-Awesome')
with open(readme_path, 'w', encoding='utf-8') as f: f.write(content)
run_git('invalid awesome link fixed')
