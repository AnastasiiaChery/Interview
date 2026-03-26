
1️⃣ Compute Models
Model	Who manages	Use case
VM (Compute Engine)	You manage everything (OS, runtime, scaling)	Long-running processes, legacy apps
GKE / Kubernetes	You manage orchestration	Microservices, complex scalable systems
Cloud Run / Functions	Google manages everything	APIs, event-driven tasks

Tip: Higher abstraction → less infra management, more automation.

2️⃣ Serverless / Cloud Run
Request-driven: container starts only on request, stops when idle → pay only for usage.
Good for APIs, web apps, event-driven workloads.
Not suitable for long-running background jobs.
3️⃣ Storage & Databases
Data type	Service	Notes
Files / images / videos	Cloud Storage	Object storage, scalable, cheap
Real-time app / chat	Firestore	NoSQL document DB, real-time sync
Structured tables / transactions	Cloud SQL	MySQL / PostgreSQL
Big data / time-series / analytics	Bigtable	High throughput, scalable

Rule: Objects → Cloud Storage, Documents → Firestore, Tables → Cloud SQL, Analytics → Bigtable

4️⃣ Networking & Autoscaling
VPC → connects resources inside cloud
Load Balancer → distributes traffic across instances, improves availability
Autoscaling → automatically adjusts resources based on load

Tip: Load Balancer = traffic routing, Autoscaling = resource scaling.

5️⃣ Event-driven Architecture

Flow example (Image App):

User
 ↓
Cloud Run (API)
 ↓
Cloud Storage (store files)
 ↓
Pub/Sub (queue events)
 ↓
Cloud Run / Functions (process files)
 ↓
Cloud Storage (processed files)

Key points:

Pub/Sub → reliable event queue (no lost events)
Eventarc → routes events to services
Cloud Run / Functions → handle events asynchronously
6️⃣ DevOps & Deployment
Deployment models: Blue/Green, Canary
Blue/Green → parallel new version, seamless switch
Autoscaling: VM → manual / managed, GKE → container scaling, Cloud Run → automatic
CI/CD: Cloud Build + Artifact Registry + tests
Principle: DevOps = run code + scale + store data + connect everything

💡 Quick Exam Tips:

Long-running job → VM
API, pay-per-request → Cloud Run
Microservices → GKE
File storage → Cloud Storage
Real-time app → Firestore
Analytics → Bigtable
Structured DB → Cloud SQL
Multiple VM → Load Balancer
Single service scaling → Autoscaling
Reliable event-driven → Cloud Storage → Pub/Sub → Cloud Run


