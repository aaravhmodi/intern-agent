# Aarav Modi — application context

Use this file, the configured resume, and the public sources linked below to prepare accurate, tailored application materials. This context includes work verified from the local project repositories, including work that is not on the resume. These facts are candidate-confirmed unless identified as coming from a project repository or public portfolio source. Tailor wording to each role, but never invent personal facts, qualifications, dates, technologies, metrics, employers, or project outcomes. If required information is not in this context, the resume, the public sources, or `data/answer-bank.json`, leave it unanswered and do not submit.

## Candidate and search preferences

- Legal/full name: Aarav Modi. Preferred name: Aarav. Pronouns: he/him only when a form requires them.
- Systems Design Engineering, University of Waterloo; candidate-confirmed expected graduation: April 2029. (The currently published resume says May 2029; use the candidate's direct confirmation of April 2029.)
- Candidate-confirmed current year of study: third year.
- Enrolled in a co-op program.
- Seeking only a four-month term from January through April 2027. Do not apply to postings requiring a different term length.
- If a form requires a precise start date, use January 11, 2027 as an inference from Waterloo's published Winter 2027 co-op start date; actual employer-specific dates may differ.
- Location-only fields: Toronto, Ontario, Canada. If a form explicitly requires a street address, use the candidate-provided Waterloo address stored in the local answer bank; do not put the street address into city/location-only fields.
- Willing to relocate anywhere.
- No active offers; no referral. Background-check consent: yes. Interview recording/data processing consent: yes.
- Current employer and role: Enerzen, Founding Software Engineer.
- Salary expectation: CAD $30/hour or higher when required.
- Work authorization: candidate confirms Canadian citizenship and authorization to work in Canada without sponsorship. For the United States, candidate confirms currently legally authorized to work and that future employer sponsorship will be required. Do not infer authorization for other countries.
- Candidate asks that jobs requiring a transcript be skipped for automatic application. GPA, test scores, transcript, and optional demographic questions remain unanswered; do not apply when a transcript is required.
- Contact from public resume/site: aarav.modi@uwaterloo.ca; 437-553-9632.
- Portfolio: https://aaravmodi.ca/
- Experience: https://aaravmodi.ca/experience
- Projects: https://aaravmodi.ca/projects
- Resume: https://aaravmodi.ca/ModiAaravResume.pdf
- GitHub: https://github.com/aaravhmodi
- LinkedIn: https://www.linkedin.com/in/aaravhmodi
- Articles: https://aaravmodi.ca/articles

## Experience

### Enerzen — Founding Software Engineer (Aug 2026–present)

Early-stage startup; four-person founding team. Resume says Aarav owns software architecture and implementation. The resume describes an Ontario land-data and energy-optimization pipeline, OpenUSD/Omniverse scenes, EnergyPlus simulations, and a Mississauga pilot. Aarav confirms Enerzen also has pilot projects in Pickering and Dryden; do not imply a completed deployment or measured outcome for either. The more recent local `enerzen-mvp` repository shows additional hands-on work: a Python/FastAPI optimization engine with a Next.js/React frontend that recommends prefabricated wall, floor, and roof assemblies across construction cost, build time, embodied carbon, and operational energy; a passive-solar site planner that places buildings and driveways within lot setbacks; and a project wizard with optional AI-assisted specification entry. Aarav also built a Pickering parcel and zoning workflow that gathers municipal and regional GIS layers, zoning by-laws, amendments, and supporting documents, records completeness gaps, and presents source-linked lot standards and preliminary reviews. The October 14, 2026 Pickering pipeline snapshot contains 395 downloaded GIS layers with 530,931 feature records counted across layers (some layers cover the same entities), including a parcel-fabric layer with 34,334 features, plus 177 PDFs and 23 web pages. The repo estimates roughly 1.5 GB per scrape. The manifest reports unresolved document/completeness gaps, so never describe the snapshot as fully complete. The API uses a bounded queue for CPU-heavy tasks and runs with the web app in Docker on the home server. These are features of an early-stage product; do not describe optimization outputs as measured building performance, regulatory approval, or broad customer adoption. Match the specific Enerzen work to the role instead of repeating the whole list. Sources: local `../enerzen-mvp/README.md` and the home-server Pickering `manifest.json` snapshot retrieved October 14, 2026.

### Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume)

An early-stage robotics company. Built a production performance dashboard used by 35+ staff and executive leadership. Portfolio details include a FastAPI service with 48 endpoints across 12 modules; PostgreSQL/RDS read and write pools; Redshift warehouse queries; Redis TTL caching; and AWS ECS. Built data pipelines and machine-learning workflows for agricultural robotics, including crop simulations, geospatial field plans, and robot telemetry. The public experience page reports 40% simulated corn-yield improvement over an agronomist baseline at flat nitrogen across 800+ seasons, and a 60% reduction in analysis time from SHAP-based feature analysis. Integrated trained policies into prescription pipelines, with field plans used across 40 fields. Built ETL that loaded 200,000+ warehouse rows daily; S3 staging and Redshift COPY cut load times 80%. Migrated telemetry from polling to WebSockets and Zenoh pub/sub, reducing production message latency 50%. Use only details relevant to the role and keep the simulation result clearly identified as simulated.

### CIBC — Software Engineering Intern (Aug–Dec 2025 per resume)

Built a React/Django dashboard covering 25+ projects, batching Jira API access to reduce calls 67% and page loads from 8 seconds to under 1 second. Engineered Dagster ETL pipelines over 100GB+ of data, saving 2+ days monthly. Built Python/GraphQL GitHub activity analytics for 40+ offshore engineers. Implemented Jenkins/Docker CI pipelines and PostgreSQL read replicas. Integrated scikit-learn anomaly detection through FastAPI.

### CIBC — IT Project Coordinator Intern (Winter 2025)

Coordinated planning and reporting for a large Azure migration. Portfolio reports supporting a Cloud@Scale migration of 400+ applications; automated reporting with Excel VBA/Power Query, cutting manual reporting 30%; managed $3.5M initiatives across six delivery teams; built Power BI reporting that reduced status turnaround from three days to same day. The resume describes selection for CIBC Spark as 1 of 30 company-wide from 800+ interns.

## Projects and public work

Use the project's public page or repository to verify details before adding claims. Select the closest projects instead of listing everything.

- **Lockerlink (founder):** social platform for Ontario Volleyball Association athletes and coaches. 100+ users across 15+ clubs; backend models for 1,000+ profile attributes and 300+ athlete-coach connections. Next.js, React, TypeScript, Firebase/Firestore, PWA, and computer-vision work using OpenCV, SAM3, and pose estimation. https://aaravmodi.ca/projects
- **GitGrade:** analyzes GitHub engineering signals rather than commit volume. Public project page reports 2,234 labeled commits, 47 features, a random-forest classifier, Next.js dashboard, FastAPI, and GitHub App integrations. The repository describes hybrid scoring that combines deterministic impact rules with the trained classifier, with Supabase report storage and Redis caching. Useful for ML systems, developer tools, and API integration roles. Sources: local `../gitgrade/README.md`; https://github.com/aaravhmodi/gitgrade.
- **Senior Check-In:** public portfolio describes a multilingual voice/text check-in prototype for older adults. FastAPI, Deepgram, OpenAI, DuckDB, Docker, and a deterministic safety layer: red-flag rules set the minimum action level, extraction can add symptoms but not remove those found by the six-language lexicon, and tests check equivalent complaints across languages. Frame as a prototype, never as a clinically validated or deployed medical device. Source: https://aaravmodi.ca/projects.
- **CRai (HackMIT 2025):** infant-cry audio ML prototype. Public page reports 92% accuracy on labeled datasets and a FastAPI inference API on Modal. Describe as a prototype/research project, not a clinical diagnostic product.
- **NASA Design Challenge:** grand-prize-winning team among 4,000+ teams; space agriculture/health concept, Python ecosystem simulations, and 3D orbital colony model.
- **A New Dawn:** Python/FastAPI terminal RPG with Supabase persistence, Docker, AWS EC2, and generative narration.
- **Wrapped Spotify:** React Native/Expo app for listening-session insights using Spotify API; OAuth callback handled server-side.
- **OSINT Canada:** open-source intelligence pipelines and counterfeit currency analysis dashboard. Currency model used synthetic data.
- More public work is linked from https://aaravmodi.ca/projects and GitHub, including BiasBuster, UrbanQuiet, NameSlot, EchoSphere, and AI Paper-to-Code. Check the actual repository before describing specifics.
- **StudyAgent:** Aarav's local-first course tutor and study planner. The repository documents read-only collection from Waterloo LEARN and Outline through a signed-in Chromium session, Pydantic validation of browser output, SQLite storage and course-file indexing, answers grounded in file/page citations, diagrams and cited question screenshots, practice tracking with spaced review, and a deterministic daily plan based on deadlines and past answers. FastAPI dashboard, Docker Compose home-server deployment, bounded task queue, and n8n reminders/sync workflows. Do not claim that it changes LMS data, serves other students, or has educational outcome metrics. Source: local `../agent/README.md`; https://github.com/aaravhmodi/study-agent.
- **Winter 2027 Internship Agent:** Aarav's local-first Python internship-search system. It gathers startup and job leads, checks source evidence, scores fit, stores preferences and answer-bank facts, drafts role-specific responses and cover letters, and tracks applications in a FastAPI dashboard with ntfy reporting. Its architecture separates AI/browser output from deterministic decisions and validates structured output with Pydantic. Outlook access is read-only. Describe the implemented workflow precisely; never imply broad automatic submission success or other users. Source: this repository and https://github.com/aaravhmodi/intern-agent.
- **Homelab:** Aarav built and runs a Tailscale-only Ubuntu home server on a MacBook. It hosts StudyAgent, the Internship Tracker, Enerzen, n8n, and supporting PostgreSQL/Redis services with Docker Compose. Homepage shows live service and container status; Uptime Kuma, Grafana, and Prometheus provide monitoring. The dashboard uses a read-only Docker proxy, and repository updates deploy from GitHub with rollback on failure. A filtered laptop-backup script copies personal project files to the server. Use as evidence of self-hosting, deployment, observability, and practical operations; do not claim uptime or scale. Source: local `../home-dashboard/README.md`.

## Writing and answering rules

- For narrative questions and cover letters, use the resume, this file, the posting, and relevant public website/GitHub details. Treat repository-verified projects as first-class evidence even if they are absent from the resume. Pick one or two specific projects that best match the role: Enerzen for early-stage product, optimization, geospatial, and full-stack work; StudyAgent or Internship Agent for agents, retrieval, browser integration, and structured-output validation; Homelab for infrastructure and operations; GitGrade for developer tools and ML; Senior Check-In for safety-conscious AI. You may synthesize concise first-person answers from verified facts and make the framing sound natural; do not fabricate supporting facts or outcomes.
- For personal questions, use only the explicit values above or the local answer bank. Never infer or fabricate contact details, legal status, compensation, demographic information, consent, or availability.
- Leave unanswered optional questions blank. Never guess an answer just to complete a form.
- Skip automatic application if a transcript is required. Skip Workday applications. Never bypass CAPTCHA, access controls, or required unanswered fields.
- Do not mention visa, J-1, sponsorship, or work authorization in prospective-lead emails or outreach drafts.
- Sign off as “Aarav” when a sign-off is needed.
