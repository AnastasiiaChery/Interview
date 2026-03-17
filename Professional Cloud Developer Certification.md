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



## Google Compute Engine and Virtual Networking

In Google Cloud, virtual networking is built around the concept of a **Virtual Private Cloud (VPC)**.

Many users begin by either:
- Creating their own VPC network, or  
- Using the default VPC created within their first project.

---

## What Is a VPC?

A **Virtual Private Cloud (VPC)** is a secure, private cloud environment hosted inside a public cloud provider like Google Cloud.

It allows customers to:

- Run applications
- Store data
- Host websites
- Manage infrastructure

While benefiting from:
- Public cloud scalability
- Private cloud isolation

VPCs combine the flexibility of public cloud with the security of private infrastructure.

---

## What VPC Networks Do

VPC networks:

- Connect Google Cloud resources to each other
- Connect resources to the internet
- Segment networks
- Apply firewall rules
- Define static routes for traffic forwarding

---

## Key Feature: Global VPC Networks

Unlike many cloud providers, **Google Cloud VPC networks are global**.

This means:

- One VPC can span multiple regions worldwide.
- Subnets can be created in any region.
- Subnets span all zones within a region.

---

## Subnets

A **subnet** is a segmented portion of a VPC network.

Key characteristics:

- Created within a specific region
- Span all zones in that region
- Can contain resources in different zones
- IP address range can be expanded without affecting existing VMs

---

## Example Architecture

Imagine a VPC network called `vpc1` with:

- One subnet in `asia-east1`
- One subnet in `us-east1`
- Three Compute Engine VMs attached

If the VMs are on the same subnet:
- They can be in different zones
- They behave like neighbors
- They communicate within a unified network layout

---

## Benefits

This global architecture enables:

- Simple network design
- Cross-zone communication
- Cross-region scalability
- Resilience against zone-level disruptions

Google Cloud’s global VPC model makes it easier to build distributed yet logically unified network architectures.



## Google Compute Engine (IaaS)

**Compute Engine** is Google Cloud’s Infrastructure as a Service (IaaS) offering.  
It allows users to create and run virtual machines (VMs) on Google’s global infrastructure.

---

## Key Features

- No upfront investment
- Thousands of virtual CPUs available
- High performance and consistent reliability
- Full operating system functionality per VM

Each VM can be configured like a physical server by choosing:

- CPU power (vCPUs)
- Memory
- Storage type and size
- Operating system

---

## Creating Virtual Machines

VM instances can be created using:

- Google Cloud Console (web interface)
- Google Cloud CLI (`gcloud`)
- Compute Engine API

Supported operating systems include:

- Linux images
- Windows Server images
- Custom images
- Other OS builds

VMs can be reconfigured flexibly after deployment.

---

## Cloud Marketplace

Cloud Marketplace offers ready-to-deploy solutions from:

- Google
- Third-party vendors

Benefits:
- No manual configuration required
- Preconfigured software stacks
- Many images are free (standard infrastructure charges apply)
- Commercial software may include additional licensing fees
- Pricing estimates are shown before deployment

---

## Pricing and Billing

### Per-Second Billing
- Billed per second
- 1-minute minimum
- Sustained-use discounts applied automatically

### Sustained-Use Discounts
- Automatically applied when a VM runs more than 25% of a month
- Increase with longer usage

### Committed-Use Discounts
- Up to 57% discount
- 1-year or 3-year commitment
- Ideal for stable, predictable workloads

---

## Preemptible and Spot VMs

Designed for fault-tolerant workloads such as:

- Batch processing
- Large-scale data analysis
- Jobs that can be stopped and restarted

### Benefits:
- Up to 90% cost savings

### Preemptible VMs:
- Can run up to 24 hours
- May be terminated at any time

### Spot VMs:
- No maximum runtime
- Same pricing as Preemptible (currently)
- More flexible features

Both can be terminated if resources are needed elsewhere.

---

## Storage Performance

- High throughput between VMs and persistent disks
- No special machine type required
- No extra cost for baseline high performance

---

## Machine Types

Compute Engine offers:

- Predefined machine types
- Custom machine types

Custom machine types allow:
- Selection of exact vCPU count
- Selection of exact memory size
- Cost optimization
- Avoiding overprovisioning

---

## Summary

Compute Engine provides:

- Flexible VM configuration
- Multiple pricing options
- Automatic discounts
- Deep cost optimization tools
- High-performance infrastructure
- Support for fault-tolerant workloads

It is a powerful and scalable IaaS solution for running virtual machines in Google Cloud.




## Autoscaling and Load Balancing in Compute Engine

Compute Engine allows you to choose machine properties such as:

- Number of virtual CPUs (vCPUs)
- Amount of memory
- Predefined or custom machine types

To efficiently handle changing workloads, Google Cloud provides **Autoscaling**.

---

## Autoscaling

Autoscaling automatically:

- Adds virtual machines when demand increases
- Removes virtual machines when demand decreases

Scaling decisions are based on load metrics such as:

- CPU utilization
- Traffic levels
- Custom monitoring metrics

This ensures:
- High availability
- Performance stability
- Cost optimization

---

## Load Balancing

To support autoscaling, incoming traffic must be distributed efficiently.

Google Cloud VPC supports multiple types of **load balancing**, which:

- Distribute traffic across multiple VMs
- Improve reliability
- Prevent overload on individual instances
- Increase fault tolerance

Load balancing works together with autoscaling to maintain performance.

---

## Scaling Up vs. Scaling Out

There are two ways to increase capacity:

### Scaling Up
- Increase VM size (more CPUs and memory)
- Useful for:
  - In-memory databases
  - CPU-intensive analytics

### Scaling Out (Most Common)
- Add more VM instances
- Improves redundancy
- Provides better fault tolerance
- Preferred by most Google Cloud customers

---

## Machine Families and Limits

The maximum number of CPUs per VM depends on:

- The selected machine family
- Available quotas (zone-dependent)

Quotas limit how many resources can be used within a region or zone.

---

## Summary

Compute Engine supports:

- Flexible machine type selection
- Autoscaling based on demand
- Integrated load balancing
- Horizontal (scale-out) and vertical (scale-up) scaling
- Large VM configurations for specialized workloads

These features help applications remain scalable, reliable, and cost-efficient.




## Virtual Private Cloud (VPC) Compatibility Features

### Built-in Routing
- VPCs automatically include routing tables.
- No need to provision or manage routers.
- Routes traffic:
  - Between instances in the same network
  - Across subnetworks
  - Across zones
- Does not require external IP addresses.

---

### Global Distributed Firewall
- Built-in firewall included with VPC.
- No firewall appliance needed.
- Controls:
  - Ingress (incoming traffic)
  - Egress (outgoing traffic)

#### Network Tags
- Firewall rules can target instances using network tags.
- Example:
  - Tag web servers as "WEB"
  - Allow ports 80 (HTTP) and 443 (HTTPS)
  - Rule applies to all VMs with the "WEB" tag regardless of IP address.

---

### VPC Peering
- VPCs belong to individual projects.
- VPC Peering connects two VPC networks.
- Enables private traffic exchange.
- No public internet required.

---

### Shared VPC
- Allows one project (host project) to share its VPC.
- Other projects (service projects) use the shared network.
- IAM controls access and permissions.

---

## Summary
- Built-in routing
- Global firewall
- Network tag-based rules
- Cross-project connectivity
- Centralized IAM control


## Cloud Load Balancing

### Purpose
- Distributes user traffic across multiple VM instances.
- Ensures application availability during autoscaling.
- Reduces risk of performance issues.

---

### Key Characteristics
- Fully distributed, software-defined managed service.
- No need to manage or scale load balancer VMs.
- Supports:
  - HTTP / HTTPS
  - TCP / SSL
  - UDP
- Cross-region load balancing.
- Automatic multi-region failover.
- No pre-warming required.
- Reacts quickly to traffic and backend health changes.

---

## Types of Load Balancers

### 1️⃣ Application Load Balancers (Layer 7)
- Operate at the Application Layer.
- Handle HTTP and HTTPS traffic.
- Ideal for web applications.
- Support:
  - Content-based routing
  - SSL/TLS termination
- Function as reverse proxies.
- Can be:
  - External (internet-facing)
  - Internal

---

### 2️⃣ Network Load Balancers (Layer 4)
- Operate at the Transport Layer.
- Handle TCP, UDP, and other IP protocols.

#### a) Proxy Network Load Balancer
- Acts as a reverse proxy.
- Terminates client connections.
- Establishes new connections to backends.
- Supports hybrid backends (cloud and on-premises).
- Advanced traffic management.

#### b) Passthrough Network Load Balancer
- Does NOT terminate connections.
- Forwards traffic directly to backend.
- Preserves original source IP address.
- Suitable for:
  - Direct server return
  - Applications needing broader protocol support

---

## Summary
Cloud Load Balancing:
- Automatically distributes traffic
- Supports multiple protocols
- Works globally
- Requires no manual scaling
- Provides Layer 7 and Layer 4 solutions



## DNS and Content Delivery in Google Cloud

### Public DNS (8.8.8.8)
- 8.8.8.8 is Google’s public DNS service.
- Translates domain names into IP addresses.
- Free and available worldwide.
- Built on Google’s global DNS infrastructure.

---

## Cloud DNS

- Managed DNS service in Google Cloud.
- Runs on Google’s infrastructure.
- Provides:
  - Low latency
  - High availability
  - Global redundancy
- Cost-effective way to publish applications.
- DNS records are served from multiple global locations.

### Management Options
You can manage DNS zones and records using:
- Google Cloud Console
- Command-line interface (CLI)
- API

Supports millions of DNS zones and records.

---

## Cloud CDN (Content Delivery Network)

### What is Edge Caching?
- Stores content closer to users.
- Reduces latency.
- Improves performance.

### Cloud CDN Benefits
- Faster content delivery.
- Reduced load on origin servers.
- Potential cost savings.
- Uses Google’s global edge network.

### Setup
- Enabled with a single checkbox after configuring an Application Load Balancer.

---

## CDN Interconnect
- Supports third-party CDN providers.
- If you already use another CDN, it may be part of Google Cloud’s CDN Interconnect partner program.
- Allows continued use of existing CDN solutions.

---

## Summary
Google Cloud provides:
- Public DNS (8.8.8.8)
- Managed Cloud DNS
- Global edge caching
- Cloud CDN for faster content delivery
- Integration with third-party CDNs



## Connecting Google Cloud VPC to Other Networks

Many organizations need to connect their Google VPC to:
- On-premises networks
- Other cloud providers

Google Cloud provides several connectivity options.

---

## 1️⃣ Cloud VPN

- Creates encrypted tunnels over the public internet.
- Connects on-premises network to Google VPC.
- Can use **Cloud Router** for dynamic routing (BGP).
- Automatically updates routes when new subnets are added.

Best when:
- Private-to-private connectivity is required
- Internet bandwidth meets business needs

---

## 2️⃣ Direct Peering

- Connect at a Google Point of Presence (PoP).
- Exchange traffic directly with Google.
- Requires colocating routing equipment.

Best when:
- No private IP connectivity needed
- Higher performance than standard internet is required
- You can install/manage equipment

⚠️ Not covered by a Google SLA.

---

## 3️⃣ Carrier Peering

- Connect through a supported service provider.
- No need to colocate equipment.
- Access Google services via public IPs.

Best when:
- You prefer working with a partner
- Installing equipment is not an option

---

## 4️⃣ Dedicated Interconnect

- Private physical connection to Google.
- High bandwidth and reliability.
- SLA up to 99.99% (if topology requirements met).
- Can be backed up with VPN.

Best when:
- Private, high-performance connectivity required
- You can colocate equipment in a Google PoP

---

## 5️⃣ Partner Interconnect

- Private connectivity via a service provider.
- Good alternative if you cannot access a Dedicated Interconnect location.
- Supports lower bandwidth needs.
- SLA up to 99.99% (if requirements met).

Note:
Google is not responsible for third-party provider issues.

---

## 6️⃣ Cross-Cloud Interconnect

- Dedicated physical connection between Google Cloud and another cloud provider.
- Supports multicloud strategy.
- Enables private VPC peering across clouds.
- Available in:
  - 10 Gbps
  - 100 Gbps

Benefits:
- Reduced complexity
- Site-to-site data transfer
- Encryption support

---

## How to Choose?

Ask three questions:

1. Do you need private-to-private connectivity?
2. Does your current internet bandwidth meet requirements?
3. Can you install/manage routing equipment at a Google PoP?

---

## Quick Decision Guide

- Private + Internet OK → **Cloud VPN**
- No private needed + Internet OK → **Public IP access**
- No private needed + Internet not enough → **Peering**
- Private + High performance + Can install equipment → **Dedicated Interconnect**
- Private + No equipment installation → **Partner Interconnect**
- Multicloud dedicated connectivity → **Cross-Cloud Interconnect**

---

## Summary

Google Cloud provides:
- VPN-based connectivity
- Public peering options
- Private interconnect solutions
- Multicloud connectivity support

Choice depends on performance, security, bandwidth, and operational requirements.



## Google Cloud Storage and Database Solutions

Every application needs a way to store data such as:
- Media files
- Application data
- Sensor data
- Transaction records

Different workloads require different storage solutions.

Google Cloud provides storage options for:
- Structured data
- Unstructured data
- Transactional data
- Relational data

---

## Core Google Cloud Storage Products

### 1️⃣ Cloud Storage
- Object storage service.
- Ideal for:
  - Images
  - Videos
  - Backups
  - Static website content
  - Large unstructured data

---

### 2️⃣ Cloud SQL
- Managed relational database service.
- Supports:
  - MySQL
  - PostgreSQL
  - SQL Server
- Good for traditional applications requiring relational databases.

---

### 3️⃣ Cloud Spanner
- Globally distributed relational database.
- Combines:
  - SQL capabilities
  - Horizontal scalability
  - Strong consistency
- Ideal for large-scale mission-critical applications.

---

### 4️⃣ Firestore
- NoSQL document database.
- Designed for:
  - Mobile apps
  - Web applications
- Supports real-time synchronization and offline mode.

---

### 5️⃣ Bigtable
- Fully managed NoSQL wide-column database.
- Designed for:
  - Massive analytical workloads
  - Large datasets
  - High-throughput applications

Examples:
- IoT data
- Financial data analysis
- Time-series data

---

## Summary

Google Cloud offers five core storage services:

| Service | Type | Best For |
|------|------|------|
| Cloud Storage | Object storage | Unstructured data, media |
| Cloud SQL | Relational DB | Traditional applications |
| Spanner | Distributed relational DB | Global scalable systems |
| Firestore | NoSQL document DB | Web & mobile apps |
| Bigtable | NoSQL wide-column DB | Big data & analytics |

Applications may use one or several of these services depending on their data requirements.



## Google Cloud Storage

### What is Cloud Storage?
Cloud Storage is Google Cloud’s **object storage service** that provides:
- High durability
- High availability
- Unlimited scalability

It is commonly used to store **large binary objects (BLOBs)** such as:
- Videos
- Images
- Audio files
- Backups
- Archived data

---

## What is Object Storage?

Object storage stores data as **objects**, not as:
- File systems (files and folders)
- Disk blocks

Each object contains:

1. **The data itself** (binary content)
2. **Metadata**  
   Examples:
   - Date created
   - Author
   - Resource type
   - Permissions
3. **Unique identifier**

Objects are accessed using **URL-based identifiers**, which makes them ideal for **web applications**.

---

## Key Features

### Unlimited Storage
- Store any amount of data
- Retrieve data whenever needed

### Fully Managed
- Google manages scaling and infrastructure

### High Availability and Durability

---

## Common Use Cases

- Website content hosting
- Backup and disaster recovery
- Media storage (images, videos)
- Data processing pipelines
- Large data distribution to users

---

## Buckets

Objects are stored inside **buckets**.

Bucket requirements:
- Must have a **globally unique name**
- Must be assigned a **location**

Bucket location options:
- Specific region
- Multi-region (e.g., EU)

Choosing a location close to users helps **reduce latency**.

---

## Object Immutability

Objects in Cloud Storage are **immutable**.

This means:
- Objects cannot be edited directly
- A **new version is created** when changes occur

---

## Object Versioning

Versioning can be enabled in a bucket.

### If versioning is OFF
- New versions **overwrite old ones**

### If versioning is ON
Cloud Storage keeps previous versions.

You can:
- View older versions
- Restore previous versions
- Permanently delete versions

---

## Access Control

Security is managed using:

### 1️⃣ IAM (recommended)
Roles are inherited:


## Google Cloud Storage

### What is Cloud Storage?
Cloud Storage is Google Cloud’s **object storage service** that provides:
- High durability
- High availability
- Unlimited scalability

It is commonly used to store **large binary objects (BLOBs)** such as:
- Videos
- Images
- Audio files
- Backups
- Archived data

---

## What is Object Storage?

Object storage stores data as **objects**, not as:
- File systems (files and folders)
- Disk blocks

Each object contains:

1. **The data itself** (binary content)
2. **Metadata**  
   Examples:
   - Date created
   - Author
   - Resource type
   - Permissions
3. **Unique identifier**

Objects are accessed using **URL-based identifiers**, which makes them ideal for **web applications**.

---

## Key Features

### Unlimited Storage
- Store any amount of data
- Retrieve data whenever needed

### Fully Managed
- Google manages scaling and infrastructure

### High Availability and Durability

---

## Common Use Cases

- Website content hosting
- Backup and disaster recovery
- Media storage (images, videos)
- Data processing pipelines
- Large data distribution to users

---

## Buckets

Objects are stored inside **buckets**.

Bucket requirements:
- Must have a **globally unique name**
- Must be assigned a **location**

Bucket location options:
- Specific region
- Multi-region (e.g., EU)

Choosing a location close to users helps **reduce latency**.

---

## Object Immutability

Objects in Cloud Storage are **immutable**.

This means:
- Objects cannot be edited directly
- A **new version is created** when changes occur

---

## Object Versioning

Versioning can be enabled in a bucket.

### If versioning is OFF
- New versions **overwrite old ones**

### If versioning is ON
Cloud Storage keeps previous versions.

You can:
- View older versions
- Restore previous versions
- Permanently delete versions

---

## Access Control

Security is managed using:

### 1️⃣ IAM (recommended)
Roles are inherited:



## Cloud Storage Storage Classes

Cloud Storage provides **four main storage classes**, designed for different access frequencies and cost needs.

---

## 1️⃣ Standard Storage
Best for **frequently accessed ("hot") data**.

Characteristics:
- Low latency
- High performance
- Ideal for frequently used data

Examples:
- Websites
- Streaming media
- Active application data

---

## 2️⃣ Nearline Storage
Designed for **infrequently accessed data**.

Access frequency:
- About **once per month or less**

Examples:
- Data backups
- Long-tail multimedia content
- Archival storage

---

## 3️⃣ Coldline Storage
Low-cost storage for **rarely accessed data**.

Access frequency:
- **Once every 90 days or less**

Examples:
- Disaster recovery backups
- Long-term data storage

---

## 4️⃣ Archive Storage
**Lowest-cost storage option**.

Access frequency:
- **Less than once per year**

Characteristics:
- Higher retrieval costs
- Minimum storage duration: **365 days**

Examples:
- Long-term archives
- Compliance storage
- Historical backups

---

## Comparison

| Storage Class | Access Frequency | Cost | Example Use |
|------|------|------|------|
| Standard | Frequent | Highest | Websites, apps |
| Nearline | Monthly | Lower | Backups |
| Coldline | Every 90 days | Lower | DR storage |
| Archive | Yearly | Lowest | Long-term archive |

---

## Common Features Across All Classes

All Cloud Storage classes provide:

- Unlimited storage
- No minimum object size
- Global accessibility
- Low latency
- High durability
- Unified APIs and tools
- Security features
- Geo-redundancy (multi-region / dual-region)

Geo-redundancy means data is stored in **multiple geographic locations** for disaster protection.

---

## Autoclass

Cloud Storage includes **Autoclass**, which automatically moves objects between storage classes.

Behavior:
- Moves inactive data to **colder storage classes**
- Moves frequently accessed data to **Standard storage**

Benefits:
- Reduces storage costs
- Automatic optimization

---

## Security

Cloud Storage security features include:

- **Server-side encryption by default**
- Encryption occurs before writing data to disk
- **HTTPS/TLS encryption** for data in transit

---

## Data Transfer Methods

### 1️⃣ Command Line
Using **gcloud storage** from the Cloud SDK.

### 2️⃣ Cloud Console
Drag-and-drop upload via the web interface.

### 3️⃣ Storage Transfer Service
Used for **large online transfers**.

Can transfer data from:
- Other cloud providers
- Different Cloud Storage regions
- HTTP(S) endpoints

---

## Transfer Appliance

Used for **very large datasets** (terabytes or petabytes).

Process:
1. Lease the appliance from Google
2. Load data locally
3. Ship it to Google
4. Data uploaded to Cloud Storage

Capacity:
- Up to **1 PB per appliance**

---

## Integration With Other Google Cloud Services

Cloud Storage integrates with many services including:

- BigQuery (import/export tables)
- Cloud SQL
- Firestore backups
- App Engine logs
- Compute Engine images and startup scripts

---

## Summary

Cloud Storage provides:
- Multiple storage classes for cost optimization
- Automated storage tiering with Autoclass
- Secure encrypted storage
- Several data transfer options
- Tight integration with other Google Cloud services


## Google Cloud SQL

### What is Cloud SQL?

Cloud SQL is a **fully managed relational database service** in Google Cloud.

It supports:
- **MySQL**
- **PostgreSQL**
- **SQL Server**

Cloud SQL allows developers to focus on building applications while Google manages the database infrastructure.

---

## Fully Managed Service

Google handles many administrative tasks such as:

- Software installation
- Database patching
- System updates
- Backups
- Replication configuration
- Maintenance

This reduces operational overhead for developers and IT teams.

---

## Scalability

Cloud SQL can scale up to:

- **128 CPU cores**
- **864 GB RAM**
- **64 TB storage**

This makes it suitable for many production workloads.

---

## Replication Support

Cloud SQL supports several replication scenarios:

- Replication from a **Cloud SQL primary instance**
- Replication from an **external primary database**
- Replication from **external MySQL instances**

Replication helps improve:
- Availability
- Disaster recovery
- Performance

---

## Managed Backups

Cloud SQL includes automated backups.

Features:
- Secure storage of backups
- Easy restore if needed
- Instance price includes **7 backups**

---

## Security Features

Cloud SQL provides built-in security mechanisms.

### Encryption
Customer data is encrypted:

- On Google's internal networks
- In database tables
- In temporary files
- In backups

### Network Firewall
Each database instance includes a firewall that:

- Controls network access
- Limits which systems can connect to the database

---

## Integration With Google Cloud Services

Cloud SQL can easily integrate with other Google Cloud services.

Examples:

### App Engine
Use standard database drivers:
- **Connector/J** for Java
- **MySQLdb** for Python

### Compute Engine
Virtual machines can be authorized to access Cloud SQL instances.

Best practice:
- Place Cloud SQL in the **same zone** as the VM to reduce latency.

---

## External Tool Support

Cloud SQL works with many common database tools.

Examples:
- SQL Workbench
- Toad
- Other applications using standard MySQL drivers

---

## Summary

Cloud SQL provides:

- Fully managed relational databases
- Automatic backups and updates
- Built-in security and encryption
- High scalability
- Easy integration with Google Cloud services

It is ideal for **traditional applications that require relational databases**.



## Google Cloud Spanner

### What is Cloud Spanner?

Cloud Spanner is a **fully managed relational database service** that combines:

- **Horizontal scalability**
- **Strong consistency**
- **SQL relational capabilities**

It is designed for **large-scale, mission-critical applications**.

Spanner is the same technology used internally by Google to power many of its major services.

---

## Key Characteristics

### Horizontally Scalable
Unlike traditional relational databases that scale vertically, Spanner can **scale horizontally across multiple servers and regions**.

Benefits:
- Handles very large datasets
- Supports massive workloads

---

### Strong Consistency
Cloud Spanner provides **strong global consistency**.

This means:
- All users see the same data at the same time
- Transactions are reliable across regions

---

### SQL Support
Spanner supports **SQL queries**, allowing developers to:

- Use relational database structures
- Perform **joins**
- Use **secondary indexes**

This makes it easier to migrate applications from traditional relational databases.

---

## High Availability

Spanner is designed with **built-in high availability**.

Features include:
- Automatic replication
- Global distribution
- Fault tolerance

This ensures applications remain available even if infrastructure fails.

---

## High Performance

Spanner supports extremely high workloads, including:

- **Tens of thousands of reads per second**
- **Tens of thousands of writes per second**

This makes it ideal for systems requiring high input/output operations.

---

## Typical Use Cases

Cloud Spanner is best suited for:

- Global financial systems
- Large-scale e-commerce platforms
- Global inventory management
- Online gaming platforms
- Enterprise SaaS applications

---

## Summary

Cloud Spanner provides:

- Fully managed relational database
- Global horizontal scalability
- Strong transactional consistency
- SQL support with joins and indexes
- High availability and performance

It is ideal for **large-scale, globally distributed applications that require relational databases and strong consistency**.


## Google Cloud Firestore

**Firestore** is a flexible, horizontally scalable **NoSQL document database** designed for **mobile, web, and server applications**.

### Data Model
Firestore stores data in **documents**, which are organized into **collections**.

Structure:
- Collections contain **documents**
- Documents contain **key–value pairs**
- Documents can include:
  - Nested objects
  - Subcollections

Example document:


User
{
firstname: "John",
lastname: "Doe"
}


### Queries
Firestore provides powerful **NoSQL queries** that can:

- Retrieve a specific document
- Retrieve multiple documents from a collection
- Filter results using multiple conditions
- Combine filtering and sorting

All queries are **indexed by default**, so performance depends on the **size of the result set**, not the total dataset.

### Real-Time Synchronization
Firestore supports **real-time data updates**.

- Changes to data are automatically pushed to connected clients.
- Applications receive updates immediately when data changes.

### Offline Support
Firestore caches data used by an application, allowing it to:

- Read
- Write
- Listen for updates
- Run queries

even when the device is **offline**.

When the device reconnects, **local changes are automatically synchronized** with Firestore.

### Infrastructure and Reliability
Firestore runs on Google Cloud infrastructure and provides:

- Automatic **multi-region replication**
- **Strong consistency**
- **Atomic batch operations**
- **ACID transactions**


## Google Cloud Bigtable

**Bigtable** is Google Cloud’s NoSQL big data database service.  
It powers many core Google services such as Search, Analytics, Maps, and Gmail.

### Key Characteristics
- NoSQL database
- Designed for massive workloads
- Low latency
- High throughput
- Handles very large datasets

### When to Use Bigtable
Bigtable is typically chosen when:

- Data size is **greater than 1 TB**
- Data changes **rapidly**
- The workload uses **NoSQL data**
- **Strong relational transactions are not required**
- Data is **time-series or naturally ordered**
- Applications require **big data processing**
- **Machine learning** workloads are used

### Example Use Cases
- Internet of Things (IoT)
- User analytics
- Financial data analysis
- Real-time analytics
- Machine learning workloads

### Integrations
Bigtable can interact with other services through:

- APIs
- Managed VMs
- HBase REST Server
- Java servers using the HBase client

### Streaming Data
Data can be streamed into Bigtable using:

- Dataflow Streaming
- Spark Streaming
- Storm

### Batch Processing
Bigtable also supports batch processing using:

- Hadoop MapReduce
- Dataflow
- Spark

### Data Usage
Data stored in Bigtable is commonly used by:

- Applications
- Dashboards
- Data services

Processed or aggregated data can be written back to Bigtable or sent to downstream databases.


## Google Cloud Storage Services Comparison

Now that we’ve explored the core Google Cloud storage options, it’s helpful to compare them to understand which service is best suited for different applications or workflows.

**Cloud Storage** is ideal when you need to store **immutable binary objects (BLOBs)** larger than **10 MB**, such as images, videos, or backups.  
It provides **petabytes of capacity** and supports objects up to **5 TB per object**.

**Cloud SQL** and **Spanner** are good choices when your application requires **full SQL support for online transaction processing (OLTP)**.

- **Cloud SQL**
  - Supports up to **64 TB** depending on the machine type
  - Best suited for **existing applications and web frameworks**
  - Common use cases include storing **user credentials, transactions, and customer orders**

- **Spanner**
  - Supports **petabyte-scale storage**
  - Provides **horizontal scalability**
  - Ideal when Cloud SQL is not sufficient because the system must scale beyond read replicas

**Firestore** is suitable when applications require **massive scaling, real-time query results, and offline support**.

- Provides **terabytes of capacity**
- Maximum size **1 MB per entity**
- Best used for **mobile and web application data**
- Supports **data synchronization and real-time updates**

**Bigtable** is designed for storing **large volumes of structured or semi-structured data**.

- Does **not support SQL queries**
- Does **not support multi-row transactions**
- Provides **petabyte-scale storage**
- Maximum size **10 MB per cell** and **100 MB per row**

Bigtable is commonly used for **analytical workloads** with heavy read and write operations such as:

- **AdTech**
- **financial data processing**
- **IoT datasets**

Depending on the architecture of your system, you may use **one or multiple storage services** together.

You might notice that **BigQuery** is not included in this comparison. That’s because BigQuery sits between **data storage and data processing**. It is typically used when the main goal is **large-scale data analysis and interactive querying**, rather than acting purely as a storage service.



## Containers in Google Cloud

### What are Containers?

Containers are a lightweight way to package and run applications along with their dependencies.

They provide:
- **Isolation** (like virtual machines)
- **Fast startup time**
- **Portability across environments**

---

## IaaS vs Containers

### Infrastructure as a Service (IaaS)
- Uses **virtual machines (VMs)**
- Each VM includes:
  - Full **operating system**
  - CPU, RAM, storage, networking
- Pros:
  - High flexibility
- Cons:
  - Large size (GBs)
  - Slow startup (minutes)
  - Expensive to scale

---

### Containers

Containers improve on IaaS by:

- Virtualizing the **operating system (not hardware)**
- Sharing the host OS kernel
- Running as lightweight processes

A container includes:
- Application code
- Dependencies (runtime, libraries, etc.)

---

## Key Advantages of Containers

### Lightweight
- No full OS required
- Much smaller than VMs

### Fast Startup
- Start in **seconds (or less)**
- No OS boot required

### Efficient Scaling
- Can run **many containers on a single host**
- Scale quickly based on demand

### Portability
- Run the same container:
  - On a laptop
  - In development
  - In staging
  - In production
  - In the cloud

No need to rebuild or reconfigure.

---

## How Containers Work

- Require:
  - A **host OS kernel**
  - A **container runtime**
- Containers use **system calls** to interact with the OS
- OS and hardware are treated as a **black box**

---

## Containers vs Virtual Machines

| Feature | Virtual Machines | Containers |
|--------|----------------|-----------|
| OS | Full OS per VM | Shared OS kernel |
| Size | Large (GBs) | Small |
| Startup time | Minutes | Seconds |
| Scaling | Slower | Fast |
| Resource usage | Higher | Lower |

---

## Scaling with Containers

Example:
- A web server can be scaled by launching many containers
- Hundreds of containers can run on a single host

---

## Microservices Architecture

Containers are often used for **microservices**:

- Each container runs a **single function**
- Services communicate over the network
- Each component can:
  - Scale independently
  - Be deployed separately

---

## Dynamic Scaling

- Hosts can scale up or down
- Containers can:
  - Start or stop automatically
  - Respond to demand changes
  - Recover from failures

---

## Summary

Containers provide:

- Lightweight application packaging
- Fast startup and scaling
- High portability
- Efficient resource usage
- Support for microservices architecture

They combine the **flexibility of IaaS** with the **scalability of PaaS**.


markdown id="gcp_kubernetes01"
## Kubernetes & Google Kubernetes Engine (GKE)

### What is Kubernetes?

Kubernetes is an **open-source platform** for managing containerized applications.

It allows you to:
- Orchestrate containers across multiple machines
- Scale applications easily
- Perform rollouts and rollbacks
- Manage microservices architectures

At a high level, Kubernetes is a set of **APIs** used to deploy containers on a cluster.

---

## Kubernetes Architecture

### Cluster
A **cluster** is a group of machines (nodes) that run your applications.

### Control Plane
- Manages the cluster
- Makes decisions about scheduling, scaling, and state

### Nodes
- Worker machines where containers run
- Represent computing instances

---

## Core Kubernetes Concepts

### Pod
- Smallest deployable unit in Kubernetes
- Represents a running process
- Usually contains **one container**
- Can contain multiple containers if tightly coupled

Pod features:
- Unique IP address
- Shared networking and storage
- Configuration for how containers run

---

### Deployment
- Manages a group of identical Pods (replicas)
- Ensures Pods stay running
- Handles scaling and updates

Example:
- If a node fails → Deployment recreates Pods automatically

---

### Service
- Provides a **stable endpoint (IP address)** for Pods
- Acts as a load balancer

Why needed:
- Pod IPs change over time
- Service keeps access consistent

Example:
- Frontend connects to backend via Service
- Doesn’t need to know changing Pod IPs

---

## Key kubectl Commands

### Run a container

kubectl run <name>


### View Pods


kubectl get pods


### View Deployments


kubectl get deployments


### Scale application


kubectl scale <deployment>


### Apply configuration


kubectl apply -f <config.yaml>


---

## Scaling in Kubernetes

### Manual Scaling

* Use `kubectl scale`
* Example: increase replicas from 3 → 5

### Autoscaling

* Based on metrics like CPU usage
* Automatically adjusts number of Pods

---

## Declarative vs Imperative

### Imperative (commands)

* Direct commands like:

  * `run`
  * `scale`
  * `expose`
* Good for testing and learning

### Declarative (recommended)

* Use configuration files (YAML)
* Define desired state
* Kubernetes ensures it matches

Example:

* Update replicas in config file
* Run `kubectl apply`

---

## Load Balancing in GKE

* Kubernetes creates a **Service**
* GKE automatically provisions a **network load balancer**
* External users access via public IP
* Traffic is routed to available Pods

---

## Updating Applications

### Rolling Updates

* Gradually replace old Pods with new ones
* Avoid downtime and risk

Process:

1. Update container version
2. Apply new configuration
3. Kubernetes:

   * Creates new Pods
   * Waits until ready
   * Removes old Pods

---

## Summary

Kubernetes provides:

* Container orchestration
* Automatic scaling
* Self-healing (restarts failed Pods)
* Load balancing
* Declarative configuration management

GKE simplifies Kubernetes by:

* Managing cluster setup
* Handling infrastructure
* Integrating with Google Cloud services


`markdown id="gcp_gke01"
## Google Kubernetes Engine (GKE)

### What is GKE?

Google Kubernetes Engine (GKE) is a **managed Kubernetes service** provided by Google Cloud.

- Runs Kubernetes clusters on **Compute Engine instances**
- Simplifies deploying and managing containerized applications
- Handles infrastructure so you can focus on your apps

---

## GKE vs Kubernetes

### Kubernetes (self-managed)
- You manage:
  - Control plane
  - Nodes
  - Scaling
  - Upgrades

### GKE (managed)
- Google manages:
  - **Control plane infrastructure**
  - API endpoint
  - Cluster lifecycle

Result: **Much simpler to use**

---

## GKE Architecture

- Cluster = group of Compute Engine VMs (nodes)
- Kubernetes API endpoint exposed via IP
- Google manages control plane behind the scenes

---

## GKE Modes

### Autopilot Mode (Recommended)

- Fully managed infrastructure
- Google handles:
  - Node configuration
  - Autoscaling
  - Auto-upgrades
  - Security defaults
  - Networking setup

Benefits:
- Optimized for production
- Strong security posture
- High operational efficiency
- Minimal management required

---

### Standard Mode

- You manage:
  - Node configuration
  - Scaling settings
  - Cluster optimization

Use when:
- You need **fine-grained control**

---

## Key GKE Features

### Cluster Management
- Create and customize clusters
- Choose:
  - Machine types
  - Number of nodes
  - Network settings

---

### Node Pools
- Subsets of nodes within a cluster
- Allow flexible workload placement

---

### Auto Scaling
- Automatically adjusts:
  - Number of nodes
  - Resource allocation

---

### Auto Upgrades
- Keeps cluster software up to date

---

### Auto Repair
- Detects and fixes unhealthy nodes

---

### Load Balancing
- Integrated with Google Cloud load balancers
- Distributes traffic across Pods

---

### Monitoring & Logging
- Integrated with Google Cloud Observability
- Provides insights into:
  - Performance
  - Health
  - Logs

---

## Working with GKE

### Create a Cluster
bash id="gke001"
gcloud container clusters create <cluster-name>
`

---

### Manage Applications

Use Kubernetes tools:

* Deploy workloads
* Scale applications
* Monitor cluster health
* Configure policies

---

## Summary

GKE provides:

* Managed Kubernetes environment
* Simplified cluster operations
* Automatic scaling, upgrades, and repairs
* Strong security and production readiness

Use **Autopilot mode** by default unless you need advanced control with Standard mode.


markdown id="gcp_cloudrun01"
## Google Cloud Run

### What is Cloud Run?

Cloud Run is a **serverless compute platform** that runs **stateless containers**.

- Executes containers via:
  - HTTP(S) web requests
  - Pub/Sub events
- Fully managed → no infrastructure management required

---

## Key Characteristics

### Serverless
- No need to manage:
  - Servers
  - Clusters
  - Scaling
- Focus only on application development

---

### Built on Knative
- Based on **Knative** (runs on Kubernetes)
- Can run:
  - Fully managed on Google Cloud
  - On GKE
  - Anywhere Knative is supported

---

### Automatic Scaling
- Scales **from zero to many instances instantly**
- Scales down to zero when idle

---

### Pay-per-Use Pricing
- Charged only when:
  - Container is handling requests
- Billing granularity:
  - **100 milliseconds**
- No cost when idle
- Additional cost per **number of requests**

---

## Cloud Run Workflow

### 1. Write Code
- Use any language
- Must start a web server that listens for requests

---

### 2. Build Container
- Package app into a **container image**

---

### 3. Deploy
- Push image to **Artifact Registry**
- Cloud Run deploys automatically

---

### Result
- Get a **unique HTTPS endpoint**
- Cloud Run:
  - Handles requests
  - Scales containers dynamically

---

## Deployment Options

### Container-based Deployment
- You build and upload container image manually
- More control and flexibility

---

### Source-based Deployment
- Upload source code directly
- Cloud Run:
  - Builds container automatically
  - Uses **Buildpacks**

Benefits:
- Simpler workflow
- Secure and consistent builds

---

## Built-in Features

### HTTPS by Default
- Automatic TLS encryption
- No configuration required

---

### Language Support
Supports any language that can run on:
- Linux (64-bit)

Popular languages:
- Java
- Python
- Node.js
- PHP
- Go
- C++

Also supports:
- Cobol
- Haskell
- Perl

---

## Pricing Model

- Pay only when:
  - Container starts
  - Container processes requests
  - Container shuts down

Factors affecting cost:
- CPU (vCPU)
- Memory
- Number of requests

---

## Summary

Cloud Run provides:
- Serverless container execution
- Automatic scaling (including to zero)
- Simple deployment workflows
- Built-in HTTPS
- Flexible language support
- Cost-efficient usage-based pricing

Best for:
- Web applications
- APIs
- Event-driven services




## Cloud Run Functions

### What are Cloud Run Functions?

Cloud Run Functions is a **serverless, event-driven compute service** for running **small, single-purpose functions**.

- Executes code in response to **events**
- No need to manage:
  - Servers
  - Infrastructure
  - Runtime environments

---

## Event-Driven Applications

Example:
- User uploads an image
- Triggers a function to:
  - Convert image format
  - Generate thumbnails
  - Store processed files

Instead of running this logic continuously, it runs **only when needed**

---

## Key Characteristics

### Event-Based Execution
- Automatically triggered by events such as:
  - Cloud Storage uploads
  - Pub/Sub messages

---

### Lightweight & Single-Purpose
- Designed for **one specific task**
- Ideal for modular application workflows

---

### Asynchronous & Synchronous

- **Asynchronous**:
  - Triggered by events (e.g., file upload)
- **Synchronous**:
  - Triggered via HTTP request

---

## Benefits

### Serverless
- No infrastructure management
- Focus only on code

---

### Cost Efficient
- Billed per execution
- Charged to nearest **100 milliseconds**
- No cost when idle

---

### Integration
- Connects and extends Google Cloud services
- Useful for building workflows from small components

---

## Supported Languages

- Node.js  
- Python  
- Go  
- Java  
- .NET Core  
- Ruby  
- PHP  

---

## Use Cases

- File processing (images, videos)
- Event-driven automation
- Data transformation
- Backend logic for apps
- Cloud service integrations

---

## Summary

Cloud Run Functions provides:
- Event-driven execution model
- Lightweight function-based architecture
- Automatic scaling
- Pay-per-use pricing

Best for:
- Background tasks
- Event processing
- Microservice-style logic units

