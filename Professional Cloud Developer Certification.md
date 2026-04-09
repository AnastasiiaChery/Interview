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




## Generative AI, LLMs & Prompt Engineering

### What is Generative AI?

Generative AI (Gen AI) is a subset of artificial intelligence that can **create content**, such as:
- Text
- Images
- Code
- Other data

It works by:
- Learning patterns from training data
- Generating new content with similar characteristics

Use cases:
- Software development
- Healthcare
- Finance
- Customer service
- Entertainment

---

## What is a Large Language Model (LLM)?

A Large Language Model (LLM) is a **type of generative AI focused on language tasks**.

### Key Characteristics

- **Large dataset** (can be petabytes)
- **Billions or trillions of parameters**
- General-purpose problem solving
- Pre-trained + fine-tuned

---

## How LLMs Work

### Training Process

1. **Pre-training**
   - Model learns patterns from massive datasets (text, code, images)

2. **Fine-tuning**
   - Model is optimized for specific tasks

---

### Inference (When You Ask a Question)

- Model predicts the **most probable next words**
- Works like an advanced autocomplete

---

## Hallucinations

### What are they?

Incorrect or nonsensical outputs generated by an LLM.

### Causes:
- Insufficient or poor-quality training data
- Lack of context in prompt
- Missing constraints
- No access to real-time or proprietary data

### Key limitation:
- Model only knows what it was trained on
- Assumes prompt is correct
- Cannot ask clarifying questions

---

## What is a Prompt?

A **prompt** is the input (instruction/question) given to an LLM.

---

## Prompt Engineering

Prompt engineering is the practice of **designing prompts to get better outputs**.

👉 Better prompts = better results

---

## Types of Prompts

### 1. Zero-shot
- No examples provided

Example:

What is the capital of France?


---

### 2. One-shot
- One example provided

Example:

Italy → Rome
France → ?


---

### 3. Few-shot
- Multiple examples provided

Example:

Italy → Rome
Japan → Tokyo
France → ?


---

### 4. Role Prompting
- Assigns a role/persona

Example:

Act as a cloud architect. Explain VPC design.


---

## Prompt Structure

### 1. Preamble
- Context + instructions
- Sets expectations

### 2. Input
- The actual task/question

Example:

[Preamble] You are a cloud architect...
[Input] Design a VPC network...


---

## Example (Improved Prompt)

Basic:

How can I create a network with IPv4 and IPv6?


Improved:

Act as a Google Cloud architect.
How can I use gcloud to create a dual-stack (IPv4 + IPv6) VPC network?


---

## Prompt Engineering Best Practices

### 1. Be Clear and Specific
- Avoid vague prompts
- Provide detailed instructions

---

### 2. Define Boundaries
- Tell the model what to do
- Add constraints when needed

---

### 3. Use Roles (Personas)
- Example:
  - "Act as a cloud architect"
- Improves relevance and accuracy

---

### 4. Keep It Concise
- Use short, clear sentences
- Break complex tasks into steps

---

### 5. Provide Context
- Add examples when needed (few-shot)
- Improves output quality

---

### 6. Add Fallbacks
- Define what model should say if unsure
- Example:
  - "If unsure, say: I don’t have enough information"

---

## Real Example (Sasha Scenario)

Prompt:

You're a cloud architect.
Design a Google Cloud VPC that:

Is centrally managed
Connects multiple regions
Minimizes firewall rule duplication

Result:
→ Suggestion: **Hub-and-spoke architecture**

---

## Summary

- **Generative AI** creates content
- **LLMs** specialize in language tasks
- **Prompts** control model output
- **Prompt engineering** improves accuracy

Key idea:
👉 The quality of output depends heavily on how you ask



# Developing Applications with Google Cloud: Foundations

## Benefits of Running Applications in the Cloud
- **Scalability** – easily handle varying loads  
- **High availability** – applications stay up even during failures  
- **Global access** – users can access apps from anywhere  
- **Reduced operational costs** – less infrastructure management

---

## Cloud Application Development
- Involves **multiple processes and tools**  
- Google Cloud provides services and products to:
  - Streamline development  
  - Run applications **efficiently and securely**

---

## Course Overview
- Learn **fundamentals of application development on Google Cloud**  
- Understand **best practices** for cloud applications  
- Learn to **select compute and data options** for different use cases  
- Explore Google services for:
  - **Continuous integration and delivery (CI/CD)**  
  - **Application deployment**  
  - **Application monitoring**  

- Security features:
  - **Authentication**  
  - **Authorization**  
  - **General security best practices**  
  - **Integration with AI services**

---

## Target Audience
- Application developers  
- Architects  
- Cloud engineers  

> Goal: Build applications using Google Cloud platforms and services.

---

## Learning Approach
- Series of **video lectures, quizzes, and hands-on labs**  
- Focus areas:
  1. Application development best practices in the cloud  
  2. Choosing the right **data storage options** for use cases  
  3. Using **authentication and authorization** to secure applications  
  4. Understanding **compute options** for running applications



# Developing Applications with Google Cloud: Foundations

## Benefits of Running Applications in the Cloud
- **Scalability** – easily handle varying loads  
- **High availability** – applications stay up even during failures  
- **Global access** – users can access apps from anywhere  
- **Reduced operational costs** – less infrastructure management

---

## Cloud Application Development
- Involves **multiple processes and tools**  
- Google Cloud provides services and products to:
  - Streamline development  
  - Run applications **efficiently and securely**

---

## Course Overview
- Learn **fundamentals of application development on Google Cloud**  
- Understand **best practices** for cloud applications  
- Learn to **select compute and data options** for different use cases  
- Explore Google services for:
  - **Continuous integration and delivery (CI/CD)**  
  - **Application deployment**  
  - **Application monitoring**  

- Security features:
  - **Authentication**  
  - **Authorization**  
  - **General security best practices**  
  - **Integration with AI services**

---

## Target Audience
- Application developers  
- Architects  
- Cloud engineers  

> Goal: Build applications using Google Cloud platforms and services.

---

## Learning Approach
- Series of **video lectures, quizzes, and hands-on labs**  
- Focus areas:
  1. Application development best practices in the cloud  
  2. Choosing the right **data storage options** for use cases  
  3. Using **authentication and authorization** to secure applications  
  4. Understanding **compute options** for running applications


# Module 1 — Best Practices for Cloud Application Development

## Cloud Application Principles
- Applications must handle **global reach** → responsive and accessible worldwide  
- **Scalability & High Availability** → handle high traffic reliably; use cloud platform capabilities to scale elastically  
- **Security** → implement best practices; may require **regional data isolation** for compliance  

---

## Managing Code and Environment
1. **Use a code repository** (e.g., Git)  
   - Track source code changes  
   - Enable **CI/CD pipelines**  
2. **Do not store external dependencies in code repository**  
   - Declare dependencies explicitly with versions  
   - Use a **dependency manager** (e.g., `package.json` + `npm install` for Node.js)  
3. **Separate configuration from code**  
   - Use **environment variables** instead of constants in code  
   - Allows modification between development, test, and production environments  

---

## Application Architecture
- Prefer **microservices over monolithic applications**  
  - Monoliths can become bloated → hard to update, test, deploy  
  - Microservices allow:
    - Modular code bases  
    - Independent updates, testing, deployment  
    - Independent scaling per service  

- Evaluate **costs vs. benefits** before refactoring monoliths  

---

## Backend Operations & Event-Driven Design
- Minimize operations in **user thread** → perform backend tasks asynchronously  
- **Event-driven processing** example:
  1. User uploads image → store in **Cloud Storage**  
  2. Trigger **Cloud Run function** to process image  
  3. Upload processed image to separate **Cloud Storage location**  

- **Loose coupling**:
  - Reduces risk of failure and improves scalability  
  - Use **Eventarc** or **Pub/Sub** for queues and asynchronous processing  
  - Example: Order and inventory services operate independently  

---

## API Design Best Practices
- **Loose binding** with HTTP API payloads:  
  - Services only consume required fields  
  - Allows backward-compatible evolution of APIs  

---

## Stateless Application Components
- Do **not store or share state internally** → scalability bottleneck  
- Components should focus on **compute tasks only** → enables worker pattern  
- **Startup and shutdown**:
  - Components start quickly → efficient scaling  
  - Shutdown gracefully → handle termination signals  
- **Cloud Run example**:
  - Scales based on traffic  
  - Processes requests **without storing state**  
  - Data persisted in separate database (e.g., **Firestore**)  

---

## Resiliency and Error Handling
- Applications must handle **transient and long-lasting errors**  
- **Transient errors** → implement **retry with exponential backoff**  
  - Avoid overloading backend or network  
  - Cloud client libraries often handle retries automatically  
- **Persistent errors** → implement **circuit breaker** and fail gracefully  
- **User-facing errors** → degrade functionality gracefully instead of showing error messages  
  - Example: Recommendation engine down → hide recommendations rather than display errors



## Performance Optimization: Caching & CDN

### Caching
- Improves **performance** and reduces **latency**
- Use for:
  - Frequently accessed data  
  - Computationally expensive results  

**Flow:**
1. Check cache first  
2. If data exists → return cached data  
3. If not → fetch from backend, compute result  
4. Update cache  

- **Memorystore** → managed in-memory cache (Redis / Memcached)

---

### Content Delivery Network (CDN)
- **Cloud CDN** → uses Google’s global edge network  
- Serves content closer to users → faster response times  

**Supports:**
- Cloud Storage (static content)  
- Cloud Run services/functions  
- Compute Engine instances  

---

## API Management

- Use **API gateways** to expose backend services  
- **Apigee** → API management platform  

**Features:**
- Security  
- Rate limiting  
- Quotas  
- Analytics  
- Acts as a **proxy (facade)** for backend APIs  

💡 Useful for integrating **legacy systems** with modern applications  

---

## Authentication & Identity

- Delegate authentication to external providers:
  - Google, Facebook, GitHub  

- **Identity Platform**:
  - User sign-up / sign-in  
  - Supports:
    - Email/password  
    - SAML  
    - OpenID Connect  
    - Multi-factor authentication  

- **Firebase Authentication**:
  - SDKs + UI components  
  - Easy integration into apps  

💡 Benefit: no need to build and maintain your own auth system  

---

## Logging & Observability

- Treat logs as **event streams**, not files  
- Write logs to **standard output (stdout)**  
- Infrastructure handles:
  - Collection  
  - Storage  
  - Analysis  

**Benefits:**
- Logs-based metrics  
- Distributed tracing across services  

- Works especially well with **serverless (Cloud Run)**  

- **Google Cloud Observability**:
  - Logging  
  - Monitoring  
  - Error Reporting  
  - Multi-cloud support  

---

## DevOps & CI/CD

### Why CI/CD?
- Increase **release velocity**  
- Improve **reliability**  
- Reduce risk with **incremental changes**  

---

### CI/CD Concepts

**CI (Continuous Integration):**
- Developers merge code into shared repo  
- Trigger build + automated tests  

**CD (Continuous Delivery):**
- Validated code is ready for deployment  

**Continuous Deployment:**
- Automatically deploy to production if tests pass  

💡 Faster releases, but requires strong testing  

---

### Google Cloud CI/CD Tools

- **Cloud Build**:
  - Detects code changes  
  - Builds application  
  - Runs tests  

- **Artifact Registry**:
  - Stores build artifacts (containers, packages)  

- **Cloud Deploy**:
  - Automates deployments to environments  

---

### Deployment Strategies
- **Blue/Green** → parallel environments, safe switch  
- **Canary** → gradual rollout to small % of users  

---

## Migration Pattern: Strangler Pattern

- Gradually replace legacy system with new services  
- Use a **facade** to route requests:
  - Old system  
  - New services  

**Process:**
1. Replace small components first  
2. Incrementally migrate features  
3. Eventually remove legacy system  

💡 Reduces risk and allows gradual transition  

---

## Key Takeaways
- Use **caching + CDN** for performance  
- Use **API gateways** for secure access to services  
- Delegate **authentication** (don’t build from scratch)  
- Treat logs as **event streams**  
- Use **CI/CD pipelines** for automation  
- Prefer **incremental deployment and migration strategies**



# Cloud APIs and Google Cloud SDK

## Cloud APIs

- Cloud APIs provide **programmatic access** to Google Cloud services  
- Any Google Cloud resource/service can be used by calling its API  

**Capabilities available via APIs:**
- Compute  
- Networking  
- Storage  
- Machine Learning  

---

### How Cloud APIs Work
- APIs are called using:
  - **HTTP requests** with JSON payloads  
  - **gRPC requests** (binary, more efficient)  

- **gRPC**:
  - Open-source framework  
  - Uses efficient binary communication  
  - Can run anywhere  

---

### Authentication
- API calls require **application credentials**  
- Credentials are validated to ensure:
  - The application has access to the Google Cloud project  
  - Permissions are properly enforced  

---

## Google Cloud SDK

- The **Google Cloud SDK** is used to interact with Google Cloud services  

### Components of SDK:
1. **Command-line tools (gcloud CLI)**  
2. **Language-specific Cloud Client Libraries**  

---

### Relationship Between Components
- SDK tools and libraries → use **Cloud APIs** internally  
- Cloud APIs → communicate with Google Cloud services  

---

## Key Idea


Applications / SDK
↓
Cloud APIs
↓
Google Cloud Services


👉 SDK = developer-friendly tools  
👉 Cloud APIs = underlying interface to services  



# Google Cloud APIs & CLI Overview

## Cloud APIs

- Cloud APIs provide **programmatic access** to Google Cloud services  
- They allow applications to interact with:
  - Compute  
  - Networking  
  - Storage  
  - Machine Learning  

### How Cloud APIs Work
- Called via:
  - HTTP requests with JSON payloads  
  - gRPC (efficient binary protocol)  

- gRPC:
  - Open-source framework  
  - More efficient than JSON over HTTP  
  - Suitable for high-performance communication  

### Authentication
- API requests require **application credentials**  
- Credentials are validated to ensure:
  - Access to the correct Google Cloud project  
  - Proper permissions and security enforcement  

---

## Google Cloud SDK

- The **Google Cloud SDK** provides tools to interact with Google Cloud services  

### Components:
1. **Command-line tools (gcloud CLI)**  
2. **Cloud Client Libraries (language-specific SDKs)**  

- These tools internally use **Cloud APIs**  

---

## gcloud CLI

- The **gcloud CLI** is a command-line tool used to:
  - Manage Google Cloud resources  
  - Run commands manually or in scripts  
  - Automate tasks  

### Key Features:
- Uses Cloud APIs behind the scenes  
- Automatically handles authentication  
- Combines multiple API calls into a single command  
- Can perform most tasks available via Cloud APIs  

### Common Use Cases:
- Managing Compute Engine VMs  
- Deploying applications  
- Configuring cloud services  

---

## Other CLI Tools

| Tool | Purpose |
|------|--------|
| **gcloud** | General Google Cloud resource management |
| **gsutil / gcloud storage** | Manage Cloud Storage buckets and objects |
| **bq** | Query and manage BigQuery datasets |

---

## Cloud Storage CLI

### gsutil (legacy)
- Used for managing buckets and objects  
- Handles access control lists (ACLs)  

### gcloud storage (preferred)
- Modern replacement for gsutil  
- Better performance and consistency with gcloud  

**Examples:**
- Create and manage buckets  
- Upload, copy, move, delete objects  
- Control access permissions  

---

## BigQuery CLI (bq)

- Command-line tool for interacting with BigQuery  

### Capabilities:
- Manage datasets and tables  
- Run SQL queries  
- Analyze large datasets  

---

## CLI Management Commands


gcloud compute instances list
Lists VM instances
gcloud components list
Shows installed CLI components
gcloud components install kubectl
Installs additional components (e.g., Kubernetes CLI)
gcloud components update
Updates the CLI to the latest version
Key Summary
Cloud APIs → direct programmatic access to Google Cloud
Cloud SDK → tools built on top of APIs
gcloud CLI → primary command-line interface for managing resources
gsutil / gcloud storage → Cloud Storage management
bq → BigQuery queries and data management

👉 CLI tools simplify working with Cloud APIs by handling authentication, abstraction, and automation.



# Cloud Client Libraries & Google Cloud SDK

## Cloud Client Libraries

Cloud Client Libraries are the recommended way to access Google Cloud services from applications. They are easier to use than making direct API calls because they provide a higher-level abstraction and handle many low-level details automatically.

These libraries manage communication with Google Cloud services, including authentication, request formatting, and response handling. They also include built-in retry logic for transient network failures, improving reliability without additional implementation effort. Many Cloud Client Libraries internally use gRPC APIs, which can provide better performance due to more efficient binary communication compared to HTTP/JSON.

Cloud Client Libraries follow the natural conventions and idioms of each supported programming language, making them more intuitive for developers.

Supported languages include:
- Python  
- Node.js  
- Java  
- Go  
- PHP  
- Ruby  
- C++  
- .NET (including C#)  

If your application is written in one of these languages, you should use the corresponding Cloud Client Library.

Each Cloud Client Library provides a client object that interacts with a specific API. Applications typically run under an identity such as a service account. The library automatically uses default credentials associated with that identity, so authentication does not need to be handled manually.

Typical workflow:
1. Import the client library  
2. Instantiate the client using default credentials  
3. Call methods on the client to perform operations (e.g., create a Cloud Storage bucket)  

---

## Google Cloud SDK

The Google Cloud SDK is a set of tools used to interact with Google Cloud services. It can be installed on Linux, macOS, and Windows.

After installation, it is initialized using:

gcloud init

This command configures:

Authentication
Default project
User preferences

Once initialized, you can immediately start using the SDK.

gcloud CLI

The SDK includes the gcloud CLI, which provides an interactive command-line interface with features such as:

Auto-completion
Command suggestions

It allows you to:

Manage Google Cloud resources manually
Run commands in scripts
Automate workflows
Deploy applications
Perform administrative tasks

gcloud CLI commands can be used interactively or integrated into CI/CD pipelines.

Summary
Cloud Client Libraries are the preferred way to integrate Google Cloud services into applications.
They simplify development by handling:
Authentication
Communication
Retries
They provide language-native APIs for better developer experience.
Google Cloud SDK + gcloud CLI are used for:
Environment setup (gcloud init)
Resource management
Automation and scripting




# Cloud Shell, Cloud Code, Emulators & Cloud Workstations

## Cloud Shell

Cloud Shell is a free, browser-based command-line environment provided by Google Cloud Console.

### Key Features:
- Provides temporary virtual machine instances
- Runs a Debian-based Linux environment
- Includes 5 GB of persistent disk storage per user
- Pre-installed with Google Cloud SDK and authenticated access to your projects

### Lifecycle:
- Provisioned per user and per session
- Persists while the session is active
- Terminates after ~1 hour of inactivity
- Persistent disk is retained across sessions

### Built-in Tools:
- Cloud SDK (gcloud CLI, gsutil, bq, etc.)
- Built-in code editor based on Theia
  - Allows browsing, editing, and managing files directly in the VM

---

## Cloud Code

Cloud Code is a set of IDE plugins that simplify developing, deploying, and debugging applications for Google Cloud.

### Supported IDEs:
- Cloud Shell Editor  
- Visual Studio Code  
- JetBrains IDEs (e.g., IntelliJ, PyCharm)  

### Key Capabilities:
- Streamlines cloud development workflows inside the IDE
- Integrates with:
  - Cloud APIs  
  - Cloud Client Libraries  
  - Deployment tools  
- Provides UI-based workflows instead of manual CLI usage

### Secret Manager Integration:
- Securely store and manage:
  - Passwords  
  - API keys  
  - Certificates  
- Accessible directly from the IDE

### Cloud API Support:
- Browse available APIs
- View language-specific documentation
- Copy code samples for APIs

---

## Cloud Code for Kubernetes

Cloud Code includes tools for Kubernetes development:

### Features:
- Develop, run, and debug Kubernetes applications locally or on Google Kubernetes Engine (GKE)
- Kubernetes Explorer:
  - Visualize and manage Kubernetes resources in the IDE
  - Interact with resources (e.g., view logs, open terminal in Pods)
- YAML assistance:
  - Autocomplete
  - Inline documentation
  - Schema-aware editing for Kubernetes configuration files

---

## Cloud Code for Cloud Run

Cloud Code also supports Cloud Run development:

- Develop Cloud Run services directly in the IDE
- Run and debug locally using Cloud Run Emulator
- Deploy services directly from the IDE
- Manage services using Cloud Run Explorer

---

## Local Emulators

Google Cloud provides local emulators for development without connecting to real cloud services.

### Supported Services:
- Bigtable  
- Datastore  
- Firestore  
- Pub/Sub  
- Spanner  

### Key Features:
- No need to modify application code when switching between emulator and real service  
- Use environment variables to point Cloud Client Libraries to the emulator  
- Avoid consuming real cloud resources during development  

### CLI Usage:
gcloud beta emulators
Cloud Workstations

Cloud Workstations provide fully managed, secure cloud-based development environments.

Key Features:
Preconfigured, reproducible development environments
Accessible via:
Browser
SSH
Local IDE
Supports any tools that run in containers
Centralized management for IT administrators
Infrastructure:
Runs on ephemeral Compute Engine VMs
Uses persistent disks within the customer VPC
Environments can be started/stopped on demand or when idle
Benefits:
Consistent development environments across teams
No need for manual setup on developer machines
Improved security and control
Scalable and manageable for organizations
Summary
Cloud Shell provides a ready-to-use browser-based development environment with preinstalled tools.
Cloud Code integrates cloud development into IDEs and simplifies workflows for APIs, Kubernetes, and Cloud Run.
Local emulators allow safe, offline development without using real cloud resources.
Cloud Workstations offer fully managed, consistent, and secure development environments for teams.



# Module Summary: Tools for Working with Google Cloud

- **Google Cloud APIs** provide programmatic interfaces to Google Cloud services.  
  They allow applications to interact directly with cloud resources using HTTP/JSON or gRPC.

- **Google Cloud SDK** provides a simpler interface for interacting with Google Cloud from the command line or scripts.  
  It includes tools like:
  - gcloud (general resource management)  
  - bq (BigQuery)  
  - gsutil / gcloud storage (Cloud Storage)

- **Cloud Client Libraries** are the recommended way to interact with Google Cloud services from your application code.  
  They:
  - Are language-specific (Python, Java, Node.js, etc.)  
  - Handle authentication automatically  
  - Include retry logic  
  - Follow language-native conventions  

- **Cloud Shell** provides a free, browser-based virtual machine with preinstalled tools (including the Cloud SDK) that you can use to manage Google Cloud resources.

- **Cloud Code** helps you develop applications in your preferred IDE by integrating Google Cloud tools, APIs, and workflows directly into the development environment.


# Overview of Data Storage Options in Google Cloud

Applications often need to handle different types of data, such as:

- Media files (e.g., images, videos)
- High volumes of user-generated content (e.g., messages)
- Transactional data (e.g., orders, payments)
- Frequently accessed data that benefits from caching
- Analytical data used for business intelligence and insights

Google Cloud provides a range of managed storage services, each designed for specific use cases.

In this module, the following services are introduced:

- **Cloud Storage** — object storage for unstructured data such as images and files  
- **Firestore** — NoSQL document database for flexible, scalable applications  
- **Bigtable** — wide-column NoSQL database for high-throughput, low-latency workloads  
- **Cloud SQL** — managed relational database (MySQL, PostgreSQL, SQL Server)  
- **Spanner** — globally distributed relational database with strong consistency  
- **BigQuery** — serverless data warehouse for analytics and large-scale querying  

Each storage option has ideal use cases as well as scenarios where it may not be suitable. Understanding these differences helps you choose the right storage solution based on your application's requirements, including scalability, structure of data, consistency, and query needs.



# Managed Storage Services in Google Cloud

Google Cloud provides a wide range of managed storage services. There is no one-size-fits-all solution — the choice depends on the type of data, workload, scalability needs, and consistency requirements.

---

## Cloud Storage

Cloud Storage is a unified object storage service used for storing and serving unstructured data.

### Key Characteristics:
- Stores data as **objects** accessed via HTTP
- Each object is identified by a unique name (key)
- Data is treated as **unstructured bytes**
- Supports ranged GET requests (retrieve parts of an object)
- Objects can be up to **5 TB**

### Use Cases:
- Static website hosting  
- Image, video, and file storage  
- Backups and archives  
- Serving large static content globally  

### Properties:
- High availability  
- High durability  
- Scalability  
- Strong consistency  

---

## Firestore

Firestore is a fully managed, serverless NoSQL document database.

### Key Features:
- Document-based data model organized into collections
- Supports hierarchical and nested data structures
- Strong consistency
- Real-time updates
- Offline support
- Scales automatically with demand
- Provides mobile and web client libraries

### Use Cases:
- Mobile and web applications  
- Applications requiring flexible schemas  
- Apps with real-time synchronization  
- User-centric applications  

---

## Bigtable

Bigtable is a high-performance NoSQL wide-column database.

### Key Characteristics:
- Sparse table with rows and columns at massive scale  
- Handles billions of rows and thousands of columns  
- Stores terabytes to petabytes of data  
- Optimized for fast key-value lookups  

### Performance:
- Sub-10ms latency  
- High read/write throughput  
- Seamless scaling without downtime  

### Use Cases:
- Time-series data  
- User behavior analytics  
- Large-scale operational and analytical workloads  
- MapReduce-style processing  
- High-throughput, low-latency applications  

### Additional Info:
- Supports HBase API (open standard compatibility)

---

## Cloud SQL

Cloud SQL is a fully managed relational database service.

### Supported Engines:
- MySQL  
- PostgreSQL  
- SQL Server  

### Key Features:
- Managed replication, backups, and failover  
- Read replicas for scaling reads  
- Automatic failover for high availability  

### Cloud SQL Auth Proxy:
- Provides secure connectivity to Cloud SQL instances  
- Uses a local proxy and secure tunnel  
- Eliminates the need to manage:
  - IP allowlists  
  - SSL certificates  

### Use Cases:
- Web applications  
- Structured data applications  
- Online Transaction Processing (OLTP) workloads  
- Applications requiring minimal migration effort from traditional RDBMS  

---

## AlloyDB

AlloyDB is a fully managed, high-performance PostgreSQL-compatible database.

### Key Features:
- Fully compatible with PostgreSQL  
- Separates compute and storage for better scalability  
- High availability with automatic scaling  
- Managed replication, backups, and failover  

### Performance:
- Faster transactional performance than standard PostgreSQL  
- Columnar engine enables:
  - Very fast analytical queries  
  - Efficient hybrid transactional and analytical processing (HTAP)  

### AlloyDB Auth Proxy:
- Similar to Cloud SQL Auth Proxy  
- Provides secure access without managing IPs or SSL certificates  

### Use Cases:
- High-performance PostgreSQL workloads  
- Applications requiring both transactional and analytical processing  
- Systems needing strong performance and scalability  

---

## Spanner

Spanner is a fully managed relational database designed for global scale.

### Key Features:
- Strong consistency  
- Horizontal scalability  
- Automatic synchronous replication  
- Multi-region support  
- High availability with SLA of 99.999%  

### Use Cases:
- Mission-critical OLTP applications  
- Global applications requiring consistent relational data  
- Systems needing both strong consistency and high availability  

---

## Summary

Google Cloud offers multiple storage solutions, each optimized for specific use cases:

- **Cloud Storage** → unstructured object storage (files, media, backups)  
- **Firestore** → NoSQL document database for flexible, real-time apps  
- **Bigtable** → high-throughput NoSQL for large-scale, low-latency workloads  
- **Cloud SQL** → managed relational databases (MySQL, PostgreSQL, SQL Server)  
- **AlloyDB** → high-performance PostgreSQL-compatible database with advanced analytics  
- **Spanner** → globally distributed relational database with strong consistency  

Choosing the right storage solution depends on:
- Data structure (structured vs unstructured)  
- Consistency requirements  
- Latency and throughput needs  
- Scalability and global distribution requirements


# BigQuery, Memorystore & Storage Selection Overview

## BigQuery

BigQuery is a fully managed, serverless enterprise data warehouse designed for analytics.

### Key Features:
- Serverless (no infrastructure management)
- Built-in capabilities:
  - Machine learning
  - Geospatial analysis
  - Business intelligence integration
- Extremely fast query performance:
  - Scans terabytes in seconds
  - Scans petabytes in minutes

### Use Cases:
- Online Analytical Processing (OLAP)
- Big data exploration and analysis
- Reporting and dashboards with BI tools
- Large-scale data processing

---

## Memorystore

Memorystore is a fully managed in-memory data store service.

### Supported Engines:
- Redis  
- Memcached  

### Key Features:
- Fully managed (no need to manage infrastructure)
- Protocol-compatible with Redis and Memcached
- High availability and scalability
- Automatic:
  - Provisioning  
  - Replication  
  - Failover  
  - Patching  

### Use Cases:
- Scalable web applications  
- Gaming applications  
- Stream processing  
- Real-time data access  
- Caching frequently accessed data  

### Security & Networking:
- Uses VPC networks and internal IPs (not exposed to the public internet)
- Integrates with Identity and Access Management (IAM)
- Can be monitored and alerted via Cloud Monitoring  

---

## Choosing the Right Storage Option

When selecting a storage solution in Google Cloud, consider:

- **Data type**:
  - Structured
  - Semi-structured
  - Unstructured  

- **Latency requirements**:
  - Low latency (e.g., Bigtable, Memorystore)  
  - Analytical workloads (e.g., BigQuery)  

- **Data size**:
  - Small to large datasets  
  - Terabytes to petabytes scale  

- **Workload type**:
  - OLTP (transactions) → Cloud SQL, Spanner  
  - OLAP (analytics) → BigQuery  

- **Access patterns**:
  - Frequent reads/writes  
  - Key-value access  
  - Real-time vs batch processing  

---

## Key Principles

- No single database fits all use cases  
- You can use **multiple databases** within one application  
- Each storage system should be chosen based on its strengths  
- Data can be split across services depending on requirements  
- Storage limits apply per database, not per application  

---

## Summary

- **BigQuery** → serverless data warehouse for analytics (OLAP)  
- **Memorystore** → in-memory caching with Redis/Memcached for low-latency access  
- Storage selection depends on:
  - Data structure  
  - Latency  
  - Scale  
  - Use case (OLTP vs OLAP)  
- Applications often combine multiple storage solutions for different needs



# Summary: Google Cloud Data Storage Services

Google Cloud provides a wide range of managed services to store, query, and manage different types of application data. Each service is optimized for specific use cases.

---

## Storage & Database Options

### Cloud Storage
- Managed service for **unstructured data**
- Ideal for:
  - Static website hosting  
  - Images, videos, and large files  
- Designed for high durability, availability, and scalability  

---

### Firestore
- Fully managed, serverless **NoSQL document database**
- Automatically scales with demand  
- Features:
  - Real-time synchronization  
  - Offline support  
  - Transactions  

- Ideal for:
  - Mobile and web applications  
  - User-centric apps with flexible data models  

---

### Bigtable
- High-performance **NoSQL wide-column database**
- Designed for:
  - Very large datasets  
  - High read/write throughput  
  - Low-latency access  

- Ideal for:
  - Analytical workloads  
  - Operational workloads at scale  

---

### Cloud SQL
- Fully managed **relational database service**
- Supports:
  - MySQL  
  - PostgreSQL  
  - SQL Server  

- Ideal for:
  - Traditional applications  
  - Migrating existing systems to the cloud with minimal changes  

---

### AlloyDB
- Fully managed, high-performance **PostgreSQL-compatible database**
- Optimized for:
  - Transactional + analytical workloads (HTAP)  
- Provides better performance than standard PostgreSQL  

---

### Spanner
- Fully managed **globally distributed relational database**
- Features:
  - Strong consistency  
  - Horizontal scalability  
  - High availability  

- Ideal for:
  - Mission-critical systems  
  - Global applications with low-latency requirements  

---

### BigQuery
- Serverless **data warehouse**
- Designed for:
  - OLAP workloads  
  - Large-scale analytics  

- Can process:
  - Terabytes in seconds  
  - Petabytes in minutes  

---

### Memorystore
- Fully managed **in-memory data store (cache)**
- Supports:
  - Redis  
  - Memcached  

- Ideal for:
  - Caching frequently accessed data  
  - Real-time applications  
  - Low-latency data access  

---

## Key Takeaway

Google Cloud provides specialized storage solutions for different needs:

- Unstructured data → Cloud Storage  
- NoSQL apps → Firestore / Bigtable  
- Relational data → Cloud SQL / AlloyDB / Spanner  
- Analytics → BigQuery  
- Caching → Memorystore  

👉 The right choice depends on:
- Data type  
- Scale  
- Performance requirements  
- Application architecture


# Module Overview: Authentication and Authorization in Google Cloud

Implementing authentication and authorization from scratch can be complex and risky. Google Cloud provides built-in services to help secure applications, manage identities, and control access.

---

## Key Concepts Covered

### Identity and Access Management (IAM)

- IAM is used to control:
  - **Who** can access resources (authentication)
  - **What** actions they can perform (authorization)

- IAM allows you to:
  - Define roles and permissions
  - Assign access to users, groups, or service accounts
  - Control access to Google Cloud resources and APIs

---

### Identity Platform (Authentication)

- A managed service for user authentication
- Supports enterprise-grade identity management

### Features:
- User sign-up and sign-in
- Integration with external identity providers
- Token-based authentication
- Secure handling of user credentials

---

### Service Accounts

- Special type of account used by applications and services
- Used for **machine-to-machine authentication**

### Use Cases:
- Applications accessing Google Cloud APIs
- Backend services communicating securely
- Automated workloads and services

---

### Identity-Aware Proxy (IAP)

- Controls access to applications running on Google Cloud
- Provides authentication and authorization at the application layer

### Benefits:
- No need to modify application code for access control
- Centralized access management
- Protects applications behind Google Cloud infrastructure

---

### Firebase Authentication SDK

- Simplifies implementing authentication in applications
- Supports federated identity management

### Features:
- Integrates with Identity Platform
- Validates users against stored credentials
- Supports external identity providers
- Provides ready-to-use authentication flows

---

### Secret Manager

- Securely stores sensitive data such as:
  - API keys  
  - Passwords  
  - Certificates  
  - Credentials  

### Benefits:
- Centralized and secure storage of secrets  
- Avoids hardcoding sensitive data in application code  
- Controlled access via IAM policies  

---

## Summary

- IAM manages **authorization** (access control to resources)
- Identity Platform handles **user authentication**
- Service accounts are used for **application-level authentication**
- Identity-Aware Proxy protects applications at the access layer
- Firebase SDK simplifies authentication integration in apps
- Secret Manager securely stores sensitive credentials

👉 Together, these services provide a comprehensive and secure approach to authentication and authorization in Google Cloud applications.


# IAM Authorization in Google Cloud

## Overview

Identity and Access Management (IAM) is used to control **who can access which resources and what actions they can perform**.

IAM follows three core concepts:
- **Principal (who)**  
- **Role (what permissions)**  
- **Resource (which service/resource)**  

---

## Principle of Least Privilege

- Grant only the **minimum permissions required** for a task  
- Avoid overly broad access  
- Helps reduce security risks  

---

## IAM Principals (Who can access)

Principals are identities that can be granted access:

### 1. Google Account
- Represents an individual user (developer, admin, etc.)
- Used for personal access to Google Cloud

### 2. Service Account
- Represents an application or workload (not a human user)
- Used by:
  - Applications running on Google Cloud
  - Automated services
- A single project can have multiple service accounts for different components

### 3. Google Group
- A collection of Google Accounts and service accounts
- Has a unique email address
- Used to manage permissions for multiple users at once
- Cannot authenticate directly (no login credentials)

### 4. Google Workspace Account
- Represents all users within an organization domain (e.g., example.com)
- Used for centralized access management
- Cannot be used directly for authentication

### 5. Cloud Identity Domain
- Similar to Google Workspace accounts
- Represents an organization’s users
- Does not include Google Workspace applications
- Also used for centralized access control

---

## IAM Resources

IAM controls access to resources such as:
- Projects  
- Compute Engine instances  
- Cloud Storage buckets  
- Artifact Registry repositories  

---

## Permissions and Roles

### Permissions
- Define specific allowed actions on a resource  
- Represented in the format:
  - `service.resource.action`  
  - Example: `pubsub.subscriptions.consume`

- Permissions cannot be assigned directly to users

---

### Roles
- A **collection of permissions**
- Assigned to principals (users, groups, service accounts)

When a role is granted:
- The principal receives **all permissions** included in that role

---

## Example

- A Google Group (e.g., "staff") is assigned the **InstanceAdmin** role on a project  
- All members of the group inherit the permissions of that role  

---

## Types of IAM Roles

### 1. Basic Roles
- Broad and highly permissive
- Examples:
  - Viewer (read-only access)
- Not recommended for production due to wide access scope

---

### 2. Predefined Roles
- Fine-grained roles created and maintained by Google
- Designed for specific services and tasks  
- Example:
  - `run.invoker` → allows invoking Cloud Run services  

---

### 3. Custom Roles
- User-defined roles
- Allow full control over included permissions
- Useful when predefined roles are too broad
- Help enforce the principle of least privilege

---

## Key Takeaways

- IAM manages access using **principals, roles, and permissions**
- Permissions define actions, roles group permissions
- Roles are assigned to principals, not individual permissions
- Use:
  - Basic roles → simple cases (avoid in production)
  - Predefined roles → most common use
  - Custom roles → fine-grained control
- The **principle of least privilege** should always guide access design



# Authentication in Google Cloud

## Overview
- In Google Cloud, **authentication** and **authorization** are distinct concepts:
  - **Authentication**: proves *who you are*
  - **Authorization (IAM)**: determines *what you are allowed to do*
- Authentication requires presenting credentials to verify identity.

---

## Authentication in Applications
Application developers may need authentication in several scenarios:
- Allow applications to access Google Cloud services
- Call services hosted on Google Cloud (e.g., Cloud Run)
- Restrict app access to only authenticated users
- Authenticate end users interacting with an application

- Interactions with Google Cloud services are typically done via **API calls**

---

## Methods of Authorizing API Calls

### 1. API Keys
- A simple string that identifies an application
- Associates requests with a Google Cloud project (for billing and quotas)

**Characteristics:**
- Not tied to a user identity
- Provide long-lasting access if compromised
- Best suited for:
  - Low-security
  - Read-only APIs
- Many Google APIs do not accept API keys

**Security Note:**
- If an API key is exposed, it can lead to full access to the API

---

### 2. User Accounts (OAuth)
- Represents an individual person
- Identified by an email address

**How it works:**
- User logs in with:
  - Email
  - Password (or other credentials)
- This generates an **OAuth token**

**OAuth Token:**
- Grants limited access based on user permissions
- Expires after a period of time
- More secure than API keys

---

### 3. Service Accounts
- Represents a workload or application (not a person)
- Identified by a unique email address

**Key Characteristics:**
- Used by applications to authenticate without user involvement
- Access is controlled via **IAM roles**
- No passwords are used
- Authentication is based on **RSA key pairs**

---

## Service Accounts in Detail

### Purpose
- Act as the identity for applications or compute workloads
- Enable applications to securely call Google APIs

### Authentication Mechanism
- Uses an **RSA private-public key pair**
- Private key can be downloaded as a JSON file

**Important Notes:**
- No password exists → cannot log in via browser
- Private key is equivalent to a user password in terms of security sensitivity

---

## Service Account Keys and Tokens
- The private key is used to generate an **access token**
- The access token:
  - Allows API access on behalf of the service account
  - Inherits permissions from IAM roles assigned to the service account

---

## Security Risks of Service Account Keys

### 1. Credential Leakage
- Example: committing a private key to a public repository
- Attackers can use the key to access cloud resources

### 2. Privilege Escalation
- If an attacker gains access to a service account key:
  - They can use the permissions of that service account
  - Potentially gain access to additional resources (e.g., databases)

- Even after rotating the key, previously granted access may persist

### 3. Identity Masking
- Attackers can hide their identity by acting as the service account
- Actions appear to originate from the service account, not the attacker

---

## Best Practices
- Avoid using downloaded service account keys whenever possible
- Prefer alternative authentication methods for service accounts
- Carefully manage and protect any credentials that are used

---

## Summary
- Authentication verifies identity; IAM handles authorization
- API access in Google Cloud can be authorized via:
  - API keys (simple, less secure)
  - User accounts with OAuth tokens (user-based, time-limited)
  - Service accounts (application identity, role-based access)
- Service accounts use RSA key pairs instead of passwords
- Service account keys are sensitive and pose security risks if exposed
- Best practice: minimize reliance on downloadable service account keys and use more secure authentication methods



# Authentication Methods for Google Cloud APIs

## Overview
- There are multiple ways to authenticate applications to Google Cloud APIs.
- The choice depends on:
  - Where the application is running
  - Whether federation is possible
  - Security requirements

---

## Key Decision: Where is the Application Running?

### 1. Application Running on Google Cloud

#### a) Local Development Environment
- Use:
  - `gcloud auth application-default login`
- Purpose:
  - Allows the application to use **user credentials**
- Behavior:
  - Generates a JSON file with user credentials
  - Stored in a location recognized by **Application Default Credentials (ADC)**

---

#### b) Production (Not GKE)
- Recommended approach:
  - **Attach a service account** to the compute resource

Examples:
- Compute Engine VM
- Cloud Run service
- Cloud Functions

**Best practice:**
- Use a **user-managed service account**
- Assign only the necessary IAM roles (principle of least privilege)

---

#### c) Applications Running on GKE
- Use **Workload Identity**

**What it does:**
- Allows Kubernetes service accounts to impersonate IAM service accounts
- Automatically exchanges Kubernetes tokens for Google Cloud access tokens

**Benefits:**
- Fine-grained identity per workload
- No need for service account keys
- More secure and manageable

---

## 2. Application Not Running on Google Cloud

### a) Workload Identity Federation (Preferred)
- Used for:
  - Multi-cloud environments
  - On-premises systems

**Requirements:**
- External identity provider that supports OpenID Connect (OIDC)
- Ability to generate an ID token

**How it works:**
- External ID token → exchanged for Google Cloud access token
- Allows impersonation of a service account
- No service account keys required

**Advantages:**
- Avoids storing long-lived credentials
- Uses short-lived tokens

---

### b) Service Account Keys (Last Resort)
- Used only if federation is not possible

**Risks:**
- Credential leakage
- Privilege escalation
- Identity masking

**Best practices:**
- Avoid embedding keys in code or binaries
- Never commit keys to source repositories
- Prefer generating your own key pairs:
  - Upload public key to Google
  - Securely manage private key externally
- Apply **least privilege** to service accounts

---

## Application Default Credentials (ADC)

### Purpose
- ADC automatically finds and uses credentials without code changes
- Works across:
  - Local development
  - Google Cloud environments
  - External environments (if configured)

---

### Credential Lookup Order

1. **Environment Variable**
   - `GOOGLE_APPLICATION_CREDENTIALS`
   - Points to a service account JSON file

2. **User Credentials (gcloud CLI)**
   - Credentials created via:
     - `gcloud auth application-default login`

3. **Attached Service Account**
   - Resource-level service account (e.g., Cloud Run, GKE, Compute Engine)

4. **Default Service Account**
   - Platform-provided service account if no custom one is attached

5. **Error**
   - If no credentials are found, authentication fails

---

## gcloud Authentication Commands

### gcloud auth login
- Used for authenticating CLI usage
- Applies to `gcloud` commands only

### gcloud auth application-default login
- Used for application authentication
- Provides credentials for code via ADC
- Stores credentials in a well-known location

---

## Workload Identity (GKE)

- Enables Kubernetes workloads to act as IAM service accounts
- Steps:
  1. Enable Workload Identity on the cluster
  2. Allow Kubernetes service account to impersonate IAM service account
- ADC handles token exchange automatically

---

## Workload Identity Federation

- Allows external workloads to access Google Cloud APIs securely
- Uses:
  - External identity provider
  - OIDC ID tokens
- Flow:
  - External ID token → exchanged for Google Cloud access token
  - Token impersonates a service account

---

## Best Practices

- Prefer:
  - Attached service accounts (on Google Cloud)
  - Workload Identity (for GKE)
  - Workload Identity Federation (for external workloads)

- Avoid:
  - Service account keys whenever possible

- If keys must be used:
  - Do not embed them in code or binaries
  - Do not store them in public repositories
  - Generate and manage keys securely
  - Apply least privilege to service accounts

---

## Summary
- Authentication method depends on deployment environment
- ADC simplifies credential management across environments
- Recommended approaches:
  - Local: `gcloud auth application-default login`
  - Google Cloud: attached service accounts
  - GKE: Workload Identity
  - External: Workload Identity Federation
- Service account keys should be avoided and used only as a last resort



# Additional Authentication & Authorization Methods

## Overview
- Some applications need to **access resources on behalf of a user**
- Google Cloud provides multiple solutions for:
  - User-based access
  - Application access control
  - Mobile/web authentication

---

## OAuth 2.0 (User-Based Access)

### Purpose
- Allows applications to access Google Cloud resources **on behalf of a user**

### Use Cases
- Accessing user-owned resources (e.g., BigQuery datasets)
- Creating resources (projects, services) for users

### How It Works
1. Application requests access to user resources
2. User is prompted to **grant consent**
3. Application requests credentials from an **authorization server**
4. Application uses credentials (tokens) to access resources

**Key Point:**
- Access is limited by user permissions and granted consent

---

## Identity-Aware Proxy (IAP)

### Purpose
- Controls access to applications running on Google Cloud

### Key Features
- Verifies user identity
- Determines access based on IAM configuration
- Works with applications accessed via HTTPS

### Benefits
- No need to write custom authentication code
- Provides a **centralized authorization layer**
- Enables **application-level access control**

### Advantages Over Traditional Methods
- Replaces:
  - VPN-based access
  - Network-level firewalls
  - Custom authorization logic

---

## Firebase Authentication

### Overview
- Part of Firebase platform for mobile/web app development
- Provides ready-to-use authentication features

### Supported Authentication Methods
- Email & password
- Phone number
- Federated identity providers:
  - Google
  - Apple
  - GitHub

### Features
- Pre-built UI components for:
  - Sign-up
  - Sign-in
  - Account recovery
- SDKs for easy integration

### After Authentication
- Access user profile
- Use authentication tokens in:
  - OAuth 2.0 flows
  - OpenID Connect (OIDC)
  - Backend services

---

## Identity Platform

### Overview
- Similar to Firebase Authentication but designed for **enterprise use**

### Key Features
- Supports:
  - OpenID Connect (OIDC)
  - SAML authentication
- Advanced capabilities:
  - Multi-factor authentication (MFA)
  - Integration with Identity-Aware Proxy (IAP)

### Comparison with Firebase Auth

| Feature                     | Firebase Auth | Identity Platform |
|---------------------------|--------------|------------------|
| Basic authentication       | ✅           | ✅               |
| SDKs & UI components       | ✅           | ✅               |
| Federated identity         | ✅           | ✅               |
| OpenID Connect (OIDC)      | ⚠️ Limited   | ✅ Full support  |
| SAML support               | ❌           | ✅               |
| Multi-factor authentication| ❌           | ✅               |
| Enterprise features        | ❌           | ✅               |

---

## Summary
- **OAuth 2.0**: Access resources on behalf of users with consent
- **IAP**: Centralized access control for applications (no custom code needed)
- **Firebase Auth**: Easy-to-use authentication for mobile/web apps
- **Identity Platform**: Enterprise-grade authentication with advanced features


# Secret Manager in Google Cloud

## Overview
- Applications often require sensitive credentials such as:
  - API keys
  - Passwords
  - Certificates
- These credentials must be stored securely

**Problem with traditional storage:**
- Storing secrets in flat files:
  - Easy access
  - Difficult to secure properly
  - Leads to scattered secrets across systems (cloud & on-prem)

**Solution:**
- **Secret Manager** provides a centralized, secure way to store and manage secrets

---

## Key Concepts

- Secrets can be stored as:
  - Text strings
  - Binary data
- Access is controlled via **IAM permissions**
- Only authorized users and applications can access secrets

**Benefits:**
- Centralized storage
- Simplified access control
- Improved security management

---

## Features of Secret Manager

### 1. Global & Regional Storage
- Secret names are **global**
- Secret data can be stored:
  - Automatically (any region)
  - In user-specified regions

---

### 2. Versioning
- Secrets support multiple versions
- Each version:
  - Contains different data
  - Is immutable (cannot be modified)
  - Can be deleted if needed

- No limit on number of versions

---

### 3. Access Control (IAM)
- Secrets are created at the **project level**
- By default:
  - Only project owners have access
- Other users must be explicitly granted permissions

**Follows principle of least privilege**

---

### 4. Auditing
- Integrated with **Cloud Audit Logs**
- Tracks:
  - Reads
  - Writes
  - Updates

**Purpose:**
- Monitor access
- Ensure only authorized usage

---

### 5. Encryption

#### Default Encryption
- Managed automatically by Google
- Uses secure internal key management systems

#### Customer-Managed Encryption (Cloud KMS)
- Optional integration with **Cloud KMS**
- Allows:
  - Custom encryption keys
  - Additional control over security

---

## How Secret Manager Works

### 1. Creating a Secret
- Methods:
  - Google Cloud Console
  - `gcloud` CLI
  - API / code

**Example concept:**
- Create a secret with:
  - Name (e.g., `my-secret`)
  - Data (provided via input or file)
  - Replication policy:
    - `automatic` (default, multi-region)
    - `user-managed` (specific regions)

---

### 2. Accessing a Secret

- Secrets are accessed using a **resource name**, which includes:
  - Project ID
  - Secret name
  - Version

**Versioning:**
- Versions are numbered: `1, 2, 3, ...`
- Can also use:
  - `latest` → retrieves most recent version

---

### 3. Using Client Libraries
- Example: Python SDK

**Steps:**
1. Import Secret Manager library
2. Create a client
3. Specify secret resource name
4. Retrieve and decode secret payload

---

## Best Practices

- Avoid storing secrets in:
  - Flat files
  - Source code
  - Repositories

- Use:
  - Centralized secret storage (Secret Manager)
  - IAM for strict access control
  - Versioning for safe updates

- Apply:
  - Least privilege principle
  - Audit logging for monitoring access

---

## Summary
- Secret Manager securely stores sensitive data in Google Cloud
- Provides:
  - Centralized management
  - Fine-grained access control (IAM)
  - Versioning
  - Auditing
  - Encryption (default + Cloud KMS integration)
- Replaces insecure methods like flat file storage
- Enables secure and scalable handling of application secrets



  # Summary: IAM, Authentication Methods, and Related Services

## Overview
- This section reviews key concepts related to:
  - Authorization (IAM)
  - Authentication methods for applications
  - Secure access to applications and resources
  - Secret management

---

## Identity and Access Management (IAM)

- IAM is used to manage access control in Google Cloud
- Defines:
  - **Who** has access
  - **What** they can access
  - **Which resources** are affected

**Key idea:**
- IAM is the foundation of authorization in Google Cloud

---

## Service Accounts

- Applications access Google Cloud APIs using **service accounts**
- The application assumes the identity of a service account

**Key points:**
- Service accounts represent workloads (not users)
- Can be used to:
  - Authenticate applications
  - Control access via IAM roles
- Multiple service accounts can be created to:
  - Separate access between components
  - Follow the principle of least privilege

---

## Service Account Keys

- Service account keys are used for authentication via private keys
- They allow generation of access tokens

**Risks:**
- Credential leakage
- Privilege escalation
- Identity masking

**Important takeaway:**
- Keys must be handled carefully and are best avoided when possible

---

## Choosing Authentication Methods

- The appropriate authentication method depends on:
  - Where the application is running
  - Whether federation is possible
  - Security requirements

(A decision flow was used to guide selection of methods such as:
service accounts, Workload Identity, federation, or keys)

---

## Identity-Aware Proxy (IAP)

- Controls access to applications hosted on Google Cloud

**How it works:**
- Verifies user identity
- Checks authorization based on configuration
- Grants or denies access accordingly

**Key benefits:**
- Centralized access control layer
- No need for custom authentication code
- Works with HTTPS-based applications
- No VPN required for end users

**User experience:**
- Users access applications via a public URL
- IAP handles authentication and authorization

---

## Firebase Authentication vs Identity Platform

- Both provide user authentication for applications

### Firebase Authentication
- Designed for mobile and web apps
- Supports:
  - Email/password
  - Phone authentication
  - Federated identity providers (Google, Apple, GitHub)
- Provides:
  - SDKs
  - Pre-built UI components
  - Easy integration

### Identity Platform
- Enterprise-focused alternative to Firebase Auth
- Adds advanced features:
  - OpenID Connect (OIDC) support
  - SAML authentication
  - Multi-factor authentication (MFA)
  - Integration with IAP

---

## Secret Manager

- Used to securely store sensitive information such as:
  - API keys
  - Passwords
  - Certificates

**Key features:**
- Centralized secret storage
- Access controlled via IAM
- Supports versioning
- Integrates with Cloud KMS for encryption
- Provides audit logging for monitoring access

---

## Summary
- IAM controls authorization in Google Cloud
- Service accounts are used for application authentication and access control
- Service account keys introduce security risks and should be avoided when possible
- IAP provides centralized, secure access control for applications without requiring VPNs
- Firebase Authentication and Identity Platform manage user authentication
- Secret Manager securely stores and manages sensitive application data



# Adding Intelligence to Your Application

## Overview
- This module introduces how to add **intelligence (AI/ML)** to applications using Google Cloud
- Focus areas:
  - Machine learning concepts
  - Pre-trained APIs
  - Generative AI

---

## Machine Learning (ML)

- Machine learning is about teaching machines to **recognize patterns**, similar to humans

**Concept:**
- Humans can easily classify objects (e.g., apple vs orange)
- For computers, this task is complex and requires training data and models

---

## Pre-trained Machine Learning Models

- Google provides **pre-trained ML models** as APIs
- These models are already trained and ready to use

**Benefits:**
- No need to build models from scratch
- Can be integrated with just a few lines of code
- Accessible via Google Cloud APIs

---

## Types of Pre-trained AI APIs

Google Cloud offers APIs in several AI domains:

- **Vision AI** – image recognition and analysis  
- **Speech AI** – speech-to-text and text-to-speech  
- **Video Intelligence** – video analysis and understanding  
- **Natural Language Processing (NLP)** – text analysis and understanding  

---

## Generative AI

### Definition
- Generative AI is a type of AI that **creates new content** based on learned patterns from existing data

### Capabilities
- Generates text, images, code, and other content
- Extends traditional AI by producing outputs rather than just analyzing data

### Benefits
- Enhances application capabilities
- Improves developer productivity
- Enables more intelligent and interactive user experiences

---

## Summary
- Machine learning enables pattern recognition similar to human cognition
- Google Cloud provides pre-trained AI APIs for easy integration into applications
- Developers can add AI features (vision, speech, NLP, video) with minimal code
- Generative AI goes further by creating new content, making applications more powerful and efficient


# Pre-trained Machine Learning Models & Google Cloud APIs

## Overview
- Google Cloud provides **pre-trained machine learning (ML) models** that can be easily integrated into applications
- These models are accessible via **simple REST APIs**
- No deep ML expertise is required to use them

---

## Pre-trained ML APIs

### 1. Vision API
- Performs **image analysis and detection**

**Capabilities:**
- Object labeling (categorization of items in images)
- Optical Character Recognition (OCR)
- Detection of:
  - Faces
  - Landmarks
  - Logos
  - Explicit content

**Examples:**
- Detects emotional expressions in faces
- Identifies landmarks and distinguishes between similar structures

---

### 2. Speech APIs

#### Speech-to-Text API
- Converts audio into text

**Features:**
- Supports ~110 languages and variants
- Use cases:
  - Voice dictation
  - Voice commands (command-and-control)
  - Audio transcription

#### Text-to-Speech API
- Converts text into spoken audio

---

### 3. Cloud Translation API
- Translates text between languages

**Key points:**
- Supports arbitrary text input
- Highly responsive (suitable for real-time applications)
- Enables dynamic translation in:
  - Websites
  - Applications

---

### 4. Cloud Natural Language API
- Analyzes and extracts insights from text

**Capabilities:**
- Entity extraction (people, places, topics)
- Sentiment analysis
- Intent detection

**Use cases:**
- Analyzing customer feedback
- Understanding social media sentiment
- Processing customer conversations

---

### 5. Video Intelligence API
- Analyzes video content

**Capabilities:**
- Identifies and labels entities in videos
- Detects entities at:
  - Frame level
  - Shot level
  - Entire video level
- Annotates videos stored in Cloud Storage

**Use cases:**
- Searching video content
- Identifying key moments in videos
- Extracting meaningful metadata

---

## AutoML and Custom Models (Vertex AI)

### AutoML (Vertex AI)
- Allows users with limited ML expertise to:
  - Train high-quality models
  - Without writing code

**Supported data types:**
- Images
- Text
- Tabular data
- Video

---

### Custom ML Models
- Developers can build their own models using frameworks such as:
  - TensorFlow
  - PyTorch
  - Vertex AI tools

**Use case:**
- When pre-trained models are not sufficient for specific business needs

---

## Using ML APIs

- ML functionality can be accessed via **REST APIs**
- Typical workflow:
  1. Send a JSON request
  2. API processes the input (e.g., image, audio)
  3. Receive a JSON response with analyzed results

---

## Example: Vision API

- Input: Image stored in Cloud Storage
- Output: JSON response with detected attributes

**Example capabilities:**
- Label detection
- OCR (text extraction from images)
- Face analysis (emotions, attributes like headwear)
- Landmark and object recognition

---

## Example: Speech-to-Text API

- Converts spoken audio into text
- Supports multiple use cases:
  - Voice transcription
  - Voice-enabled applications
  - Audio file processing

---

## Example: Google Use Case (Occupancy Detection)

- Google uses ML to optimize meeting room usage

**How it works:**
- Motion detection via cameras
- Pub/Sub notifications sent periodically:
  - Motion detected
  - Meeting start/end events

**Logic:**
- If motion is detected within a specific time window after meeting start:
  - Room is considered occupied
- Otherwise:
  - Room is marked as empty and available

---

## Summary
- Google Cloud provides multiple pre-trained ML APIs for common AI tasks:
  - Vision, Speech, Translation, Natural Language, Video Intelligence
- These APIs are:
  - Easy to integrate via REST
  - Require no ML expertise
- AutoML (Vertex AI) allows training custom models without coding
- Developers can also build custom ML models using frameworks like TensorFlow and PyTorch



# Generative AI

## Overview
- **Generative AI** is a type of artificial intelligence that creates new content based on existing data
- It learns patterns from large datasets and uses them to generate outputs in response to user input (prompts)

---

## How Generative AI Works

### Training
- The process of learning from large amounts of existing data (text, images, audio)
- Produces a **statistical model** based on patterns in the data

### Foundation Models
- The result of training on large datasets is called a **foundation model**
- These models can:
  - Be used directly for general tasks
  - Be fine-tuned for specific use cases

### Prompts and Outputs
- Users provide an input called a **prompt**
- The model predicts a response based on learned patterns
- New content is generated from this predicted response

---

## Large Language Models (LLMs)

### Definition
- A type of foundation model trained primarily on text data

### Characteristics of "Large"
- Large datasets (often petabyte-scale)
- Large number of parameters (billions or trillions)

### Parameters
- Represent the learned knowledge of the model
- Influence the model’s ability to generate accurate and relevant outputs

### Key Properties
- **General-purpose**:
  - Can solve common language-related tasks
- **Pre-trained + Fine-tuned**:
  - Pre-trained on large general datasets
  - Fine-tuned on smaller, domain-specific datasets for specialized tasks

---

## Comparison with Traditional Approaches

### Traditional Programming
- Developer defines explicit rules
- Machine follows predefined logic

**Limitation:**
- Hard to account for all possible scenarios

---

### Machine Learning (Non-generative)
- Model learns patterns from labeled data
- Typically designed for a specific task
- Example: classifying images as cats or non-cats

---

### Generative AI
- Learns from large, multimodal datasets
- Develops broader understanding across domains
- Capable of generating new content and solving more general problems

---

## Use Cases of Generative AI

### 1. Content Generation
- Generate:
  - Stories
  - Poems
  - Images (based on instructions)

---

### 2. Knowledge Summarization
- Summarize:
  - Documents
  - Audio
  - Video
- Generate:
  - Questions and answers from content

---

### 3. Search and Discovery
- Help find:
  - Documents
  - Products based on features
- Improves information retrieval and recommendations

---

### 4. Workflow Automation
- Automate business processes such as:
  - Extracting and labeling contracts
  - Classifying customer feedback
  - Creating support tickets

---

## Generative AI for Developers

Generative AI can assist in software development through coding assistants.

### Key Capabilities

#### Code Generation
- Generate code from natural language descriptions

#### Code Completion
- Suggest and complete lines or entire functions based on context

#### Code Explanation
- Explain how code works and its purpose

#### Code Fixing
- Identify bugs and suggest corrections

#### Documentation
- Generate:
  - Comments
  - Release notes
  - Documentation summaries

#### Code Translation
- Convert code between programming languages while following conventions

---

## Tools and Platforms

- **Vertex AI Codey APIs**
  - Powered by the Codey foundation model
  - Supports:
    - Code generation
    - Code chat
    - Code completion

- **Gemini**
  - Provides advanced AI assistance for developers
  - Helps improve productivity and efficiency in coding tasks

---

## Summary
- Generative AI creates new content based on learned patterns from large datasets
- Foundation models (especially LLMs) are trained on massive data and can be fine-tuned for specific tasks
- Compared to traditional programming and ML, generative AI is more general-purpose and flexible
- It supports a wide range of use cases including content creation, summarization, search, automation, and coding assistance
- Tools like Vertex AI Codey and Gemini help developers integrate generative AI into applications


  # CI/CD Pipeline (Continuous Integration & Continuous Delivery)

## Overview
- A **CI/CD pipeline** provides a stable and repeatable process for:
  - Building applications
  - Testing applications
  - Deploying applications

---

## Continuous Integration (CI)

### Process
- Developers commit code changes to a **feature branch** in a code repository
- A build service (e.g., **Cloud Build**) is automatically triggered

### Key Steps
- Code is built according to predefined rules
- Application artifacts (containers, executables) are generated
- Artifacts are stored in a repository such as **Artifact Registry**

---

## Continuous Delivery (CD)

### Trigger
- Occurs when changes are pushed to the **main branch**

### Process
1. Build system creates application images
2. Deployment system (e.g., **Cloud Deploy**) deploys images to:
   - **Cloud Run** or
   - **GKE**
3. Deployment happens in a **staging environment**
4. Automated tests are executed:
   - Integration tests
   - Performance tests

### Release Candidate
- If tests pass:
  - Build is marked as a **release candidate**

### Approval & Deployment
- Manual approval can trigger deployment to production
- Deployment strategies include:
  - Canary release
  - Blue-green deployment

### Monitoring
- Application performance is monitored using **Cloud Monitoring**

### Rollout / Rollback
- If stable:
  - Traffic is fully switched to the new version
- If issues are found:
  - Rollback to the previous stable version

---

## Continuous Deployment

- Similar to continuous delivery, but:
  - **No manual approval step**
  - Release candidates are automatically deployed to production

---

## CI/CD Pipeline Summary
- Ensures:
  - Efficiency
  - Consistency
  - Automation of build and deployment processes

---

## Security in CI/CD

Security must be integrated throughout the pipeline.

### Software Delivery Shield
- Fully managed solution for securing the entire software supply chain
- Protects all stages of CI/CD

---

## Key Security Services

### Assured Open Source Software
- Provides verified open-source Java and Python packages
- Packages are:
  - Built using secure pipelines
  - Regularly scanned and analyzed for vulnerabilities
  - Maintained and patched by Google

---

### Cloud Build
- Builds source code and imports verified dependencies
- Runs builds on Google Cloud infrastructure
- Maintains **verifiable metadata** for traceability

---

### Artifact Registry
- Stores and manages build artifacts securely
- Works with **Artifact Analysis** for vulnerability scanning

---

### Artifact Analysis
- Scans:
  - Container images
  - Maven and Go packages
- Detects vulnerabilities in:
  - Base images
  - Open-source dependencies
- Continuously monitors artifacts for new vulnerabilities

---

### Cloud Deploy
- Automates delivery across environments in a defined sequence
- Supports:
  - Cloud Run
  - GKE
  - One-click approvals
  - Rollbacks
- Provides security insights for deployments

---

### Binary Authorization
- Enforces a chain of trust in the supply chain
- Uses **attestations**:
  - Digital proofs that an image was built through a trusted process
- Ensures:
  - Only verified images are deployed
  - Policies are enforced
- Alerts on policy violations

---

### GKE Security
- Evaluates clusters and workloads
- Provides recommendations for:
  - Cluster configuration
  - Workload security
  - Vulnerability mitigation

---

### Cloud Run Security
- Provides a security panel with:
  - Build insights
  - Vulnerability information for running services

---

## Summary
- CI/CD pipelines automate build, test, and deployment workflows
- Continuous integration focuses on building and validating code changes
- Continuous delivery/deployment focuses on releasing those changes to environments
- Google Cloud provides integrated services for:
  - Automation (Cloud Build, Cloud Deploy)
  - Storage (Artifact Registry)
  - Security (Binary Authorization, Artifact Analysis, Software Delivery Shield)
- Security is embedded across the entire software supply chain to ensure trusted and reliable deployments


# Containerized Applications on Google Cloud

## Overview
- **Containers** are a preferred way to package and deploy applications
- Provide a lightweight alternative to traditional **virtual machines (VMs)**
- Widely used in modern cloud-native development

---

## Containers vs Virtual Machines

### Virtual Machines (VMs)
- Each VM includes:
  - Full operating system (OS)
  - Application and dependencies
- Characteristics:
  - Slower to boot
  - Resource-heavy

---

### Containers
- Use OS-level virtualization instead of hardware virtualization
- Share the host OS kernel
- Include only:
  - Application code
  - Required libraries and dependencies

**Advantages:**
- Faster startup (seconds vs minutes)
- Lower resource usage
- Lightweight and efficient

---

## How Containers Work

- Based on **process isolation** in operating systems
- Use features such as:
  - Memory isolation
  - Namespaces
  - Resource limits

### Container Runtime
- Lightweight software responsible for:
  - Running containers
  - Managing container lifecycle
  - Interacting with the OS kernel
  - Defining container image format

---

## Container Images

- A **container image** is a complete package containing:
  - Application binary
  - Dependencies
  - Required libraries

**Key benefit:**
- Same image runs consistently across:
  - Development
  - Testing
  - Production

---

## Benefits of Containers

### 1. Separation of Responsibilities
- Developers:
  - Focus on application code and dependencies
- Operations teams:
  - Manage deployment and infrastructure

---

### 2. Portability
- Containers can run anywhere:
  - Local machines
  - On-premises environments
  - Any cloud provider

**Benefit:**
- Same application behaves consistently across environments

---

### 3. Application Isolation
- Each container runs in its own isolated environment
- Allows:
  - Multiple applications on same hardware
  - Different dependency versions without conflict

---

### 4. Fast Startup
- Containers start in seconds
- VMs can take minutes to boot

---

## Deployment Targets

- Containers can be deployed to:
  - **Cloud Run**
  - **Google Kubernetes Engine (GKE)**

---

## Building Containers with Cloud Build

### Overview
- **Cloud Build** is a fully managed service for:
  - Building container images
  - Creating build pipelines
  - Pushing images to **Artifact Registry**

---

### Key Features

- No need to manage build infrastructure
- Automatically triggered builds on code commits
- Integration with source repositories

---

## Build Triggers

- Define when builds should run

**Trigger types:**
- Code commits to specific branches
- Code commits with specific tags

---

## Build Configuration

- Defined using:
  - YAML or JSON files

### Build Steps
- Each step:
  - Is a Docker container
  - Executes a specific task (command/script)

**Example tasks:**
- Compile code
- Run tests
- Build container image

---

### Important Fields

- **steps**:
  - Define sequence of build operations
- **name**:
  - Specifies container image used for the step
- **images**:
  - Defines the output container image

---

## Build Execution

- Source code is mounted in:
  - `/workspace` directory
- Artifacts generated by steps:
  - Stored in `/workspace`
  - Passed to subsequent steps

---

## Artifact Registry Integration

- Cloud Build automatically:
  - Pushes container images to **Artifact Registry**

**Capabilities:**
- View build history
- Manage container images
- Track versions

---

## Notifications

- Cloud Build can send build status updates via **Pub/Sub**
- Enables:
  - Automation based on build results
  - Integration with other services

---

## Summary
- Containers provide a lightweight, portable, and efficient alternative to VMs
- Enable consistent application behavior across environments
- Cloud Build automates container creation and deployment workflows
- Artifact Registry stores and manages container images
- Together, these tools support modern, scalable application development on Google Cloud



# Compute Options for Your Application (Google Cloud)

## Overview
- Google Cloud provides multiple **compute options** to run applications
- Choice depends on:
  - Required level of infrastructure control
  - Operational complexity you are willing to manage

**Key trade-off:**
- More control → More operational burden  
- Less control → More automation and simplicity

---

## Flexibility Across Platforms
- Applications using **cloud client libraries** can:
  - Move between platforms with minimal changes
- Enables flexibility in choosing or switching compute options

---

## Main Compute Options

### 1. Compute Engine (Virtual Machines)

#### Overview
- Provides **Virtual Machines (VMs)** similar to traditional servers
- Runs on Google Cloud infrastructure

#### Characteristics
- High flexibility
- Full control over:
  - Operating system
  - Software configuration
  - Environment setup

#### Use Cases
- Lift-and-shift workloads
- Legacy applications
- Custom environments requiring full control

---

### 2. Google Kubernetes Engine (GKE)

#### Overview
- Managed service for running **containerized applications**
- Uses Kubernetes to orchestrate containers

#### How it Works
- Creates a **cluster of virtual machines**
- Runs containers across the cluster

#### Features
- Automated:
  - Scaling
  - Security management
- Reduces operational overhead compared to managing Kubernetes manually

#### Use Cases
- Complex containerized applications
- Microservices architectures
- Applications requiring orchestration and scalability

---

### 3. Cloud Run

#### Overview
- Fully managed **serverless platform** for containerized applications

#### Characteristics
- No infrastructure management required
- Automatically scales:
  - Up and down
  - Even to zero when not in use

#### Benefits
- Pay only when code is running
- Fast and automatic scaling
- Simplified deployment

#### Additional Capability
- Can build and manage containers from source code

#### Use Cases
- Stateless applications
- APIs and web services
- Event-driven workloads

---

## Choosing the Right Compute Option

| Platform        | Control Level | Operational Effort | Best For |
|----------------|--------------|-------------------|----------|
| Compute Engine | High         | High              | Full control, legacy apps |
| GKE            | Medium       | Medium            | Container orchestration, microservices |
| Cloud Run      | Low          | Low               | Serverless, simple deployments |

---

## Summary
- Google Cloud offers flexible compute options:
  - **Compute Engine** → maximum control
  - **GKE** → container orchestration with managed infrastructure
  - **Cloud Run** → fully managed serverless containers
- The right choice depends on:
  - Control vs simplicity
  - Application architecture
  - Operational requirements
 

# Google Kubernetes Engine (GKE)

## Overview
- **Kubernetes** is an open-source platform for:
  - Deploying
  - Scaling
  - Operating containerized applications
- Originally developed at Google, now maintained by the Cloud Native Computing Foundation (CNCF)

- **Google Kubernetes Engine (GKE)** is a **managed Kubernetes service** on Google Cloud
- Simplifies deploying and managing containerized applications at scale

---

## Kubernetes Basics

### Cluster Architecture
- A **Kubernetes cluster** consists of:
  - **Control Plane**
  - **Worker Nodes**

#### Control Plane
- Manages:
  - Nodes
  - Pods
  - Cluster state

#### Nodes
- Machines (VMs or physical) that run applications

#### Pods
- Smallest deployable unit
- Group of one or more containers sharing:
  - Networking
  - Storage

---

## What Kubernetes Provides

- Scaling of applications
- Network abstraction
- Failover handling
- Rolling updates
- Storage orchestration
- Secret and configuration management

---

## GKE: Managed Kubernetes

### Benefits
- Eliminates much of the operational complexity
- Google manages:
  - Control plane
  - Monitoring
  - Availability and reliability
  - Pod scaling
  - Node patching and upgrades

---

## GKE Modes

### 1. Standard Mode
- User manages:
  - Nodes and node pools
  - Provisioning and lifecycle
  - Networking and security configuration

**Best for:**
- Maximum flexibility and control

---

### 2. Autopilot Mode
- Fully managed cluster infrastructure
- Google manages:
  - Control plane
  - Nodes
  - Node pools

**Benefits:**
- Reduced operational overhead
- Improved resource utilization
- Built-in security best practices
- Blocks unsafe configurations

**Best for:**
- Simplicity and minimal infrastructure management

---

## Key Features of GKE

### 1. AutoUpgrade
- Automatically updates clusters to latest stable Kubernetes version

---

### 2. AutoRepair
- Detects unhealthy nodes
- Drains workloads safely
- Recreates nodes automatically

---

### 3. Scalability
- Supports:
  - Pod scaling (workloads)
  - Cluster scaling (nodes)

- **Autoscaling:**
  - Adds/removes resources based on demand

---

### 4. Monitoring & Logging
- Integrated with:
  - Cloud Monitoring
  - Cloud Logging

---

### 5. Integration with Google Cloud

- **Cloud Build** → build and deploy containers  
- **Artifact Registry** → store container images  
- **IAM** → access control  
- **VPC** → networking  
- **Cloud Console** → cluster management  

---

## Deployment & Management

### Tools
- `kubectl` (command-line tool)
- Google Cloud Console

---

### Best Practice: YAML Manifests
- Define application configuration declaratively

**Used to define:**
- Containers
- Networking
- Security policies
- Other Kubernetes resources

---

### Workload Types

#### Deployments (Stateless)
- Ensures a specified number of pod replicas are running

#### StatefulSets (Stateful)
- Used when persistent storage is required

---

## Infrastructure Automation

- Automatically provisions:
  - Persistent disks for storage
  - Network load balancers
  - HTTP/HTTPS load balancing via Ingress

---

## Observability

- Integrated with Google Cloud Observability tools
- Enables:
  - Monitoring
  - Troubleshooting
  - Performance analysis

---

## AI/ML Support

- Supports:
  - GPUs
  - TPUs

### Standard Mode
- Manually configure node pools with GPUs/TPUs

### Autopilot Mode
- Automatically provisions required resources

---

## Hybrid & Multi-Cloud Support

- Run workloads:
  - On-premises
  - In multiple clouds

---

## CI/CD Integration

- Works with:
  - Cloud Build
  - Artifact Registry
  - Cloud Deploy

**Workflow:**
1. Build container image
2. Store in registry
3. Deploy to GKE
4. Promote across environments

---

## Summary
- GKE is a managed Kubernetes service for running containerized applications
- Simplifies cluster management while retaining Kubernetes flexibility
- Offers two modes:
  - Standard (more control)
  - Autopilot (fully managed)
- Provides built-in:
  - Scaling
  - Monitoring
  - Security
  - Integration with Google Cloud services
- Ideal for scalable, production-ready, containerized applications




# Cloud Run

## Overview
- **Cloud Run** is a **fully managed serverless compute platform**
- Runs:
  - Request-driven workloads (HTTP/gRPC)
  - Event-driven workloads
- No need to manage servers or infrastructure

---

## Key Characteristics

### Serverless Execution
- Fully abstracts infrastructure:
  - Provisioning
  - Configuration
  - Management

---

### Automatic Scaling
- Scales automatically:
  - Up → when traffic increases
  - Down to **zero** → when idle
- Near-instant scaling

---

### Pay-per-Use Pricing
- Pay only for:
  - CPU
  - Memory
  - Networking
- Billed per **100 ms**
- No cost when not in use

---

### GPU Support
- Supports **1 GPU per instance**
- Fully managed (no setup required)
- Scales to zero when idle

**Use cases:**
- AI inference (LLMs)
- Video transcoding
- 3D rendering

---

## Containers & Flexibility

- Deploy **any stateless container**
- Supports:
  - Any language
  - Any framework

### Requirements
- Container must:
  - Listen on `0.0.0.0`
  - Use HTTP/gRPC
- TLS handled by Cloud Run

---

## Deployment Options

### 1. Container-Based Deployment
- Deploy container images from:
  - Artifact Registry
  - Docker Hub

---

### 2. Source-Based Deployment
- Deploy using:
  gcloud run deploy


**Process:**
1. Cloud Build builds container
2. Buildpacks create image
3. Image stored in Artifact Registry

**Supported languages:**
- Python
- Node.js
- Go
- Java
- Ruby
- PHP
- .NET

---

### 3. Functions (Event-Driven)
- Single-purpose functions
- Triggered by:
- Pub/Sub
- Eventarc
- HTTP

- Automatically packaged as containers

---

### 4. Continuous Deployment
- Integrates with GitHub
- Auto build & deploy on commits

- Can also use:
- Cloud Build
- Cloud Deploy

---

## Developer Workflow

### 3 Steps
1. Write app (handles HTTP requests)
2. Build container image
3. Deploy to Cloud Run

**Result:**
- App gets HTTPS URL
- Auto scaling and request handling

---

## Build Approaches

### Container-Based
- Full control over:
- Build process
- Dependencies

### Source-Based
- Simpler
- Cloud Run:
- Builds container automatically
- Uses secure base images

---

## Cloud Run Jobs

### Overview
- For **non-HTTP workloads**
- Used for:
- Batch jobs
- One-time tasks
- Scheduled jobs

---

### Features
- No web server required
- Triggered by:
- Workflows
- Cloud Scheduler

---

### Task Execution
- Jobs contain:
- One or multiple tasks

**Tasks:**
- Run in parallel
- Have task index
- Can retry on failure
- Run container to completion

---

## Use Cases

### Web & APIs
- Web apps
- REST APIs

---

### Event Processing
- Pub/Sub
- Eventarc triggers

---

### Data Processing
- Batch processing
- Pipelines

---

### Microservices
- Lightweight services
- Webhooks

---

### ETL
- Extract, Transform, Load
- Message processing

---

## Summary
- Fully managed serverless platform
- Runs containerized apps
- Key benefits:
- No infrastructure management
- Auto scaling (including zero)
- Pay-per-use
- Supports:
- Containers
- Source code
- Functions
- Jobs
- Ideal for modern, scalable applications
