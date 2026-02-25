## Overview of Cloud Computing

Cloud computing is a model of using IT resources defined by the U.S. National Institute of Standards and Technology (NIST). It is based on five essential characteristics:

1. **On-Demand Self-Service**  
   Users can provision computing resources such as processing power, storage, and networking automatically through a web interface, without human intervention from the provider.

2. **Broad Network Access**  
   Resources are accessible over the internet from anywhere with a connection.

3. **Resource Pooling**  
   The provider pools computing resources to serve multiple customers. Resources are dynamically allocated, and users do not need to know the physical location of the infrastructure.

4. **Rapid Elasticity**  
   Resources can be scaled up or down quickly depending on demand.

5. **Measured Service**  
   Customers pay only for the resources they use. If usage stops, billing stops.

### Evolution Toward the Cloud

Cloud computing evolved in three major waves:

- **Colocation** – Companies rented physical space in data centers instead of owning real estate.
- **Virtualized Data Centers** – Infrastructure components (servers, CPUs, storage, load balancers) became virtualized, but enterprises still managed and configured their own environments.
- **Container-Based Cloud Architecture** – Fully automated and elastic systems where services automatically provision and configure infrastructure.

Today, companies increasingly rely on cloud platforms to build scalable, data-driven software. As technology becomes central to business strategy, organizations are evolving into data-driven companies.


## Cloud Service Models: IaaS, PaaS, Serverless, and SaaS

The shift to virtualized data centers introduced two main cloud service models: **Infrastructure as a Service (IaaS)** and **Platform as a Service (PaaS)**.

### Infrastructure as a Service (IaaS)
IaaS provides raw compute, storage, and networking resources, organized virtually like a traditional physical data center.

- Customers manage the infrastructure configuration.
- Resources are allocated in advance.
- Payment is based on the resources provisioned.

Example: Compute Engine (Google Cloud).

---

### Platform as a Service (PaaS)
PaaS provides a platform where code is connected to managed libraries and services that handle infrastructure needs.

- Developers focus more on application logic.
- Infrastructure management is handled by the provider.
- Payment is based on actual resource usage.

Example: App Engine (Google Cloud).

---

### Managed Infrastructure and Managed Services
As cloud computing evolved, the focus shifted toward managed services.

Benefits:
- Less time and money spent on infrastructure maintenance.
- Greater focus on business goals.
- Faster and more reliable product delivery.

---

### Serverless Computing
Serverless is the next stage of cloud evolution.

- Developers focus only on writing code.
- No infrastructure management required.
- Fully managed execution environment.
- Pay-as-you-go pricing model.

Examples:
- Cloud Run — deploy containerized microservices in a fully managed environment.
- Cloud Run functions — run event-driven code as a managed service.

---

### Software as a Service (SaaS)
SaaS delivers the entire application stack as a cloud-based service.

- Applications run in the cloud.
- No local installation required.
- Accessed directly over the internet by end users.

Examples:
- Gmail
- Google Docs
- Google Drive

These applications are part of Google Workspace and are consumed directly as services.


## Google Cloud Global Infrastructure

Google Cloud runs on Google’s own global network — one of the largest and most advanced networks in the world. Google has invested billions of dollars over many years to build infrastructure designed for:

- High throughput  
- Low latency  
- Global reliability  

The network includes more than 100 content caching nodes worldwide. These nodes store frequently accessed content closer to users, allowing applications to respond from the nearest location and reduce response time.

---

## Global Geographic Coverage

Google Cloud infrastructure spans seven major geographic areas:

- North America  
- South America  
- Europe  
- Africa  
- Middle East  
- Asia  
- Australia  

This global presence ensures services can be delivered reliably to users anywhere in the world.

---

## Regions and Zones

Google Cloud infrastructure is organized into **regions** and **zones**.

### Regions
- Independent geographic areas.
- Each region contains multiple zones.
- Example: London (`europe-west2`) is a region with three zones.

### Zones
- A deployment area for Google Cloud resources.
- When launching a virtual machine (e.g., using Compute Engine), you specify a zone.
- Zones provide resource redundancy within a region.

---

## Why Location Matters

Choosing where to deploy resources affects:

- **Availability** – system uptime.
- **Durability** – data protection.
- **Latency** – time it takes for data to travel from source to destination.

Deploying resources in multiple regions helps:
- Reduce latency for global users.
- Protect against regional failures (e.g., natural disasters).

---

## Multi-Region Services

Some services support **multi-region** configurations.

Example:
- Spanner multi-region setups replicate data:
  - Across multiple zones  
  - Across multiple regions  

This allows:
- Low-latency reads from different geographic areas.
- Higher resilience and fault tolerance.

The number of regions and zones continues to grow as Google expands its global infrastructure.

## Sustainability and Google Cloud Infrastructure

Although cloud computing operates in a virtual environment, it relies on physical infrastructure. Data centers worldwide consume approximately **2% of global electricity**, making energy efficiency critically important.

Google works continuously to make its data centers as efficient and environmentally responsible as possible. Running workloads on Google Cloud can also help customers meet their own sustainability goals.

---

## Environmental Certifications

Google’s data centers were the first to achieve **ISO 14001 certification**, an international standard for environmental management systems.  

ISO 14001 provides a framework for:
- Improving resource efficiency  
- Reducing waste  
- Enhancing overall environmental performance  

---

## Example: Hamina Data Center (Finland)

One example of Google’s innovation is its data center in **Hamina, Finland**.

Key features:
- One of the most advanced and efficient facilities in Google’s fleet  
- Uses seawater from the Bay of Finland for cooling  
- First cooling system of its kind  
- Significantly reduces energy consumption  

---

## Google’s Climate Commitments

- Became the first major company to achieve **carbon neutrality**  
- Achieved **100% renewable energy usage**  
- Goal: operate completely **carbon-free by 2030**

Google’s sustainability strategy demonstrates that large-scale cloud infrastructure can grow while reducing environmental impact.


## Google Cloud Security Architecture

Google’s infrastructure is built with **security by design** at every layer. Since many Google services each serve over one billion users, protecting data is a top priority.

Google Cloud security can be understood as a set of layered protections:

---

## 1. Hardware Infrastructure Layer

### Hardware Design and Provenance
- Custom-designed server boards and networking equipment.
- Custom security chips deployed on servers and peripherals.

### Secure Boot Stack
- Cryptographic signatures verify:
  - BIOS
  - Bootloader
  - Kernel
  - Base OS image  
- Ensures servers boot only trusted software.

### Physical (Premises) Security
- Google designs and builds its own data centers.
- Multiple physical security layers.
- Very limited employee access.
- Additional Google-controlled protections in third-party data centers.

---

## 2. Service Deployment Layer

### Encryption of Inter-Service Communication
- Services communicate using Remote Procedure Calls (RPC).
- All inter–data center RPC traffic is encrypted by default.
- Hardware cryptographic accelerators extend encryption within data centers.

---

## 3. User Identity Layer

- Central Google identity service (Google login).
- Risk-based authentication challenges.
- Support for multi-factor authentication.
- Use of Universal 2nd Factor (U2F) security keys.

---

## 4. Storage Services Layer

### Encryption at Rest
- Data is encrypted at the storage service layer.
- Centrally managed encryption keys.
- Hardware encryption on HDDs and SSDs.

---

## 5. Internet Communication Layer

### Google Front End (GFE)
- Terminates all TLS connections.
- Uses public-private key pairs and X.509 certificates from trusted Certificate Authorities.
- Supports best practices such as Perfect Forward Secrecy.

### Denial of Service (DoS) Protection
- Global infrastructure scale helps absorb attacks.
- Multi-layered DoS protections.
- Services behind GFE are shielded from large-scale attacks.

---

## 6. Operational Security Layer

### Intrusion Detection
- Automated rules and machine intelligence.
- Red Team exercises to test defenses.

### Reducing Insider Risk
- Strict access controls.
- Active monitoring of administrative actions.

### Mandatory U2F for Employees
- Required security keys to prevent phishing attacks.

### Secure Software Development
- Central source control.
- Mandatory two-party code review.
- Secure coding libraries to prevent common vulnerabilities.
- Vulnerability Rewards Program for external security researchers.

---

## Summary

Google Cloud security is based on a **defense-in-depth model**, combining:

- Physical security  
- Hardware and software integrity  
- Encryption in transit and at rest  
- Identity protection  
- DDoS defense  
- Operational monitoring and secure development practices  

This layered approach ensures strong protection of customer data and services.


## Avoiding Vendor Lock-In in Google Cloud

Some organizations hesitate to move to the cloud because they fear **vendor lock-in** — becoming dependent on a single provider.

Google addresses this concern by promoting **openness, portability, and interoperability**, allowing customers to run their applications beyond Google Cloud if needed.

---

## Open Source Commitment

Google publishes key technologies under open source licenses to build broad ecosystems.

Example:

- **TensorFlow** — an open source machine learning library originally developed at Google.  
  It supports a large global ecosystem and can run on multiple platforms, not just Google Cloud.

This open approach ensures customers are not restricted to one environment.

---

## Interoperability Across Clouds

Google supports flexibility at multiple layers of the technology stack:

### Kubernetes and Google Kubernetes Engine (GKE)
- Enable deployment of containerized microservices.
- Workloads can run across different cloud providers.
- Support hybrid and multi-cloud architectures.

### Google Cloud Observability
- Allows monitoring of workloads across multiple cloud environments.
- Provides visibility beyond just Google Cloud infrastructure.

---

## Key Takeaway

Google Cloud reduces vendor lock-in by:

- Supporting open source technologies  
- Enabling multi-cloud and hybrid deployments  
- Providing cross-platform monitoring tools  

This gives customers flexibility and long-term strategic freedom.


## Google Cloud Pricing and Cost Management

Google Cloud offers flexible and transparent pricing designed to help customers control costs and optimize usage.

---

## Per-Second Billing

Google was the first major cloud provider to introduce **per-second billing** for its Infrastructure as a Service (IaaS) offering, **Compute Engine**.

Per-second billing is also available for:

- Google Kubernetes Engine (GKE)  
- Dataproc  
- App Engine flexible environment VMs  

This ensures customers only pay for the exact time resources are used.

---

## Sustained-Use Discounts

Compute Engine provides **automatic sustained-use discounts**:

- Applied automatically when a VM runs more than 25% of the billing month.
- Discounts increase incrementally based on usage time.
- No upfront commitment required.

---

## Custom Machine Types

Compute Engine allows creation of **custom VM types**:

- Tailor vCPU and memory to application needs.
- Avoid overprovisioning.
- Optimize pricing for specific workloads.

---

## Pricing Calculator

Google Cloud provides an online pricing calculator to estimate projected costs based on selected services and configurations.

---

## Budgets and Alerts

To prevent unexpected charges:

### Budgets
- Can be set at the billing account or project level.
- Can be:
  - A fixed amount  
  - A percentage of previous spending  

### Alerts
- Trigger notifications when spending approaches the budget.
- Common thresholds: 50%, 90%, and 100%.
- Custom alert percentages are also supported.

Example:  
If the budget is $20,000 and an alert is set at 90%, a notification is sent at $18,000.

---

## Reports

The **Reports** tool in the Google Cloud Console:

- Provides visual cost analysis.
- Allows monitoring by project or service.
- Helps track and optimize spending.

---

## Quotas

Quotas prevent accidental or malicious overuse of resources.

There are two types:

### 1. Rate Quotas
- Limit the number of API requests within a time window.
- Reset after a specified period.
- Example: GKE allows 3,000 API calls per project every 100 seconds.

### 2. Allocation Quotas
- Limit the total number of resources in a project.
- Example: Default limit of 15 Virtual Private Cloud (VPC) networks per project.

Projects start with standard quotas, but some limits can be increased by requesting approval from Google Cloud Support.

---

## Key Takeaway

Google Cloud pricing emphasizes:

- Pay-for-what-you-use billing  
- Automatic discounts  
- Flexible configuration  
- Built-in cost control tools  
- Resource protection through quotas  

These mechanisms help organizations manage spending efficiently while scaling their workloads.


## Google Cloud Resource Hierarchy

Google Cloud uses a hierarchical structure to organize and manage resources.  
From bottom to top, the hierarchy consists of:

1. **Resources**
2. **Projects**
3. **Folders**
4. **Organization Node**

Understanding this structure is essential because **policies and permissions are applied and inherited through this hierarchy**.

---

## 1. Resources (Lowest Level)

Resources include:
- Virtual machines  
- Cloud Storage buckets  
- BigQuery tables  
- Any other Google Cloud service component  

Each resource belongs to **exactly one project**.

Some services allow policies to be applied directly to individual resources.

---

## 2. Projects

Projects are the core unit of Google Cloud usage.

They are used for:
- Enabling APIs  
- Managing billing  
- Adding/removing collaborators  
- Managing services  

### Key Characteristics:
- Each project is separate and independently billed.
- Each resource belongs to one project only.
- Projects can have different owners and users.

### Project Identifiers:

Each project has three identifiers:

1. **Project ID**
   - Globally unique
   - Assigned by Google
   - Immutable (cannot be changed)

2. **Project Name**
   - User-defined
   - Not required to be unique
   - Can be changed

3. **Project Number**
   - Automatically generated
   - Mainly used internally by Google Cloud

---

## Resource Manager

Google Cloud **Resource Manager** is an API that allows you to:

- List projects
- Create projects
- Update projects
- Delete projects
- Recover deleted projects

It is accessible via:
- RPC API
- REST API

---

## 3. Folders

Folders organize projects within an organization.

They allow:
- Policy assignment at a grouped level
- Delegation of administrative rights
- Logical grouping (e.g., by department)

Folders can contain:
- Projects
- Other folders
- Or both

### Policy Inheritance

Policies applied to a folder are automatically inherited by:
- All projects inside the folder
- Any subfolders and their projects

This reduces duplication and prevents configuration errors.

---

## 4. Organization Node (Top Level)

The **Organization Node** is the root of the hierarchy.

It contains:
- Folders
- Projects
- All associated resources

Folders and projects are considered “children” of the organization node.

### Special Roles at Organization Level:

- **Organization Policy Administrator**  
  Controls who can modify policies.

- **Project Creator**  
  Controls who can create projects (and therefore spend money).

---

## Creating an Organization Node

- If your company uses **Google Workspace**, projects automatically belong to your organization node.
- Otherwise, you can use **Cloud Identity** to create one.

---

## Key Concept: Policy Inheritance

Policies can be applied at:
- Organization level
- Folder level
- Project level
- (Sometimes) Resource level

Policies flow **downward** through the hierarchy.

Example:
If a policy is set on a folder, all projects inside that folder automatically inherit it.

---

## Summary

The Google Cloud hierarchy provides:

- Clear ownership structure  
- Scalable policy management  
- Simplified administration  
- Controlled billing and access  

This structured model enables secure and organized cloud resource management.


## Identity and Access Management (IAM) in Google Cloud

When an organization has many folders, projects, and resources, access must be carefully controlled.  
Google Cloud uses **Identity and Access Management (IAM)** to define:

- **Who** can access resources  
- **What** they can do  
- **Which** resources they can access  

---

## IAM Policy Components

An IAM policy has three main elements:

### 1. Principal (“Who”)

A principal can be:
- A Google account  
- A Google group  
- A Service account  
- A Cloud Identity domain  

Each principal is identified by a unique ID (usually an email address).

---

### 2. Role (“Can do what”)

A role is a **collection of permissions**.

When a role is granted to a principal, all permissions inside that role are granted.

Example:  
Managing virtual machines requires permissions to:
- Create  
- Delete  
- Start  
- Stop  
- Modify VMs  

These permissions are grouped into a role for easier management.

---

### 3. Resource (“On which resource”)

Roles are assigned at a specific level of the resource hierarchy:
- Organization  
- Folder  
- Project  
- (Sometimes) Individual resource  

Permissions are **inherited downward** through the hierarchy.

---

## Allow and Deny Policies

- **Allow policies** grant permissions.
- **Deny policies** explicitly block permissions.
- IAM always checks **deny policies first**.
- Deny policies are also inherited down the hierarchy.

---

## Types of IAM Roles

There are three types of IAM roles:

---

### 1. Basic Roles

Broad and project-wide.

Include:
- **Owner**
- **Editor**
- **Viewer**
- **Billing Administrator**

#### Capabilities:
- **Viewer** – Can view resources, cannot modify.
- **Editor** – Can view and modify resources.
- **Owner** – Can modify resources + manage roles and billing.
- **Billing Administrator** – Manages billing but cannot modify resources.

⚠ Basic roles are often too broad for sensitive projects.

---

### 2. Predefined Roles

More granular and service-specific.

- Created and maintained by Google Cloud.
- Designed for specific services.
- Can be applied at project, folder, or organization level.

Example (Compute Engine):
- `instanceAdmin` role allows management of VM instances.

Predefined roles support better security practices than basic roles.

---

### 3. Custom Roles

Allow organizations to define **exact sets of permissions**.

Useful for implementing the **principle of least privilege** —  
giving users only the permissions they absolutely need.

Example:
- A custom `instanceOperator` role that allows starting and stopping VMs but not modifying them.

Important limitations:
- Custom roles must be maintained by your organization.
- Can only be applied at:
  - Project level  
  - Organization level  
- Cannot be applied at the folder level.

---

## Key Concept: Least Privilege

Many organizations follow the **least-privilege model**, meaning:

- Each user receives the minimum permissions required to perform their job.
- Reduces security risks.
- Improves compliance and governance.

---

## Summary

IAM enables secure access management in Google Cloud by:

- Defining principals (who)
- Assigning roles (what actions)
- Applying them at specific hierarchy levels (where)
- Supporting policy inheritance
- Enabling deny policies for stronger control

This structured approach ensures scalable and secure access control across the cloud environment.


## Service Accounts in Google Cloud

When a virtual machine (VM) needs to access other Google Cloud services automatically, it shouldn’t rely on human authentication.  
Instead, it uses a **service account**.

---

## What Is a Service Account?

A **service account** is a special identity used by applications or virtual machines to:

- Authenticate to other Google Cloud services
- Access resources securely
- Operate without human intervention

It allows a VM to act securely on its own.

---

## Example Use Case

Imagine:

- A Compute Engine VM runs an application.
- The application needs to store data in Cloud Storage.
- You want **only that VM** to access the storage bucket.

Solution:

- Create a service account.
- Grant it the necessary permissions (e.g., access to Cloud Storage).
- Attach the service account to the VM.

Now the VM can securely authenticate and access the storage resource.

---

## How Service Accounts Authenticate

- Identified by an email address.
- Do **not** use passwords.
- Use **cryptographic keys** for secure authentication.

---

## Permissions and Roles

Service accounts receive permissions through IAM roles.

Example:
If a service account is granted the **Compute Engine Instance Admin** role:

- Any application running on a VM with that service account  
  can create, modify, or delete virtual machines.

---

## Managing Service Accounts

Service accounts must be managed like other resources.

Important concept:
A service account is both:

- An **identity**
- A **resource**

Because of this, you can apply IAM policies directly to a service account.

Example:
- Alice can have the **Editor** role on a service account (can manage it).
- Bob can have the **Viewer** role (can only view it).

This follows the same IAM structure used across Google Cloud.

---

## Key Takeaway

Service accounts enable:

- Secure machine-to-machine authentication  
- Automated access to cloud services  
- Fine-grained permission control  
- Role-based management through IAM  

They are essential for secure, automated cloud operations.



## Cloud Identity in Google Cloud

When new Google Cloud users begin working with the platform, they often:

- Log in using personal Gmail accounts  
- Use Google Groups to collaborate  

While this is simple at first, it can create problems later because identities are **not centrally managed**.

For example:
- If someone leaves the organization, it may be difficult to immediately remove their access to cloud resources.

---

## What Is Cloud Identity?

Cloud Identity is a tool that allows organizations to:

- Centrally manage users and groups  
- Define identity and access policies  
- Control authentication across Google Cloud  

Management is done through the **Google Admin Console**.

---

## Key Benefits

### Centralized User Management
- Admins manage users and groups from one place.
- Accounts can be disabled immediately if someone leaves.

### Integration with Existing Systems
- Supports existing identity systems such as:
  - Active Directory
  - LDAP  
- Users can log in with familiar credentials.

### Improved Security
- Faster removal of access
- Better control over permissions
- Reduced risk of unauthorized access

---

## Editions

Cloud Identity is available in:

- **Free edition** – Basic identity and access management  
- **Premium edition** – Includes mobile device management capabilities  

---

## Google Workspace Customers

If your organization uses **Google Workspace**, Cloud Identity features are already available within the Google Admin Console.

---

## Key Takeaway

Cloud Identity provides:

- Centralized identity management  
- Secure access control  
- Integration with enterprise identity systems  
- Easier offboarding and user lifecycle management  

It is an important step toward enterprise-grade governance in Google Cloud.



## Four Ways to Access Google Cloud

There are four main ways to access and interact with Google Cloud:

1. Google Cloud Console  
2. Google Cloud SDK and Cloud Shell  
3. APIs  
4. Google Cloud App  

---

## 1. Google Cloud Console (Web GUI)

The Google Cloud Console is a web-based graphical user interface (GUI).

It allows you to:
- Deploy and scale resources
- Monitor resource health
- Manage services
- Set budgets and monitor costs
- Search for resources
- Connect to Compute Engine instances via SSH in the browser

It is ideal for visual management and quick administration tasks.

---

## 2. Google Cloud SDK and Cloud Shell

### Google Cloud SDK

A set of command-line tools for managing Google Cloud resources.

Includes:
- `gcloud` (main CLI tool)
- `bq` (BigQuery command-line tool)

All SDK tools are located in the `bin` directory after installation.

---

### Cloud Shell

A browser-based command-line environment.

Features:
- Debian-based virtual machine
- 5 GB persistent home directory
- Pre-installed and always up-to-date `gcloud` CLI
- Fully authenticated environment

Cloud Shell eliminates the need for local installation.

---

## 3. APIs (Application Programming Interfaces)

Google Cloud services expose APIs that allow programmatic control.

You can:
- Automate tasks
- Build custom applications
- Integrate services into your own systems

### Google APIs Explorer
- Available in the Cloud Console
- Lets you test APIs interactively
- Shows available APIs and versions

### Client Libraries

Google provides Cloud Client Libraries and API Client Libraries in multiple languages:

- Java  
- Python  
- PHP  
- C#  
- Go  
- Node.js  
- Ruby  
- C++  

These libraries simplify API integration and reduce development effort.

---

## 4. Google Cloud App (Mobile App)

The Google Cloud mobile app allows you to:

- Start/stop Compute Engine instances
- Connect via SSH
- View logs
- Start/stop Cloud SQL instances
- Manage App Engine deployments
- View billing information
- Receive budget alerts
- Monitor metrics (CPU, network usage, errors, etc.)
- Manage alerts and incidents

It provides quick, on-the-go cloud management.

---

## Summary

Google Cloud can be accessed through:

- A graphical web interface (Console)
- Command-line tools (SDK & Cloud Shell)
- Programmatic APIs
- A mobile management app

This flexibility allows users to choose the interface that best fits their workflow and technical needs.






