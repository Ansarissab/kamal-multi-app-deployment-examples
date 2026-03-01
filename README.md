# Multi-App Deployment with Kamal 2 and Docker on a single Virtual Machine

Deploy multiple independent applications (FastAPI, Rails, WordPress) to a single Ubuntu VM using Kamal 2. This setup eliminates high cloud costs by utilizing Docker and Kamal Proxy to route traffic based on domain names.

## 🚀 Architecture

- **Server:** 1 Ubuntu VM (VMware, DigitalOcean, Hetzner, AWS, Hostinger etc.)
- **Orchestration:** Kamal 2
- **Proxy:** Kamal Proxy (handles routing for `app1.local`, `app2.local`, etc.)
- **Containers:** Each app runs in its own Docker container with its own private Database accessory.

## 🛠 Prerequisites

1. Docker Desktop installed on your Mac/PC.
2. Kamal 2 installed: `gem install kamal` needed ruby installation as well, you can install ruby via `mise` package manager
3. A Remote Server: A VM with Docker installed (accessible via SSH).
4. Local Host Mapping: Add your VM IP to your `/etc/hosts` for testing:

```
172.16.189.131  fastapi.local
172.16.189.131  rails-app.local
172.16.189.131  wordpress.local
```

OR

```
172.16.189.131 fastapi.local rails-app.local wordpress.local
```

## 📁 Project Structure

```
.
├── fastapi-app/        # Project 1 (Python)
├── rails-app/          # Project 2 (Ruby on Rails)
└── wordpress-site/     # Project 3 (PHP/WordPress)
```

## 1. Shared Networking (The Secret Sauce)

To allow different apps to live on one server without port conflicts, we use the default `kamal` Docker network. Accessories will also run from within the kamal network.

## 2. Avoiding Database Port Conflicts

Since we are running multiple PostgreSQL or MySQL instances on one IP, we must map the Host Port uniquely while keeping the Internal Port at the default (5432 or 3306).

**App 1 (FastAPI) `deploy.yml`:**

```yaml
accessories:
  db:
    image: postgres:17
    port: "5432:5432" # Host 5432
```

**App 2 (Rails) `deploy.yml`:**

```yaml
accessories:
  db:
    image: postgres:17
    port: "5433:5432" # Host 5433
```

## 3. Deployment Steps

For each project folder, follow these steps:

### Step A: Configure Secrets

Create `.kamal/secrets` and add your Registry password and Database passwords.

```
KAMAL_REGISTRY_PASSWORD=your_token
POSTGRES_PASSWORD=secure_password
RAILS_MASTER_KEY=...
```

### Step B: Setup & Deploy

Run these commands from inside the specific project directory:

```bash
# 1. Initialize the server and proxy (only needed once)
kamal setup

# 2. Deploy the application
kamal deploy
```

## 4. Adding a WordPress Site

```
Coming Soon
```

## 🔍 Useful Commands

- Check all running apps: `ssh user@ip "docker ps"`
- View Proxy Logs: `kamal proxy logs`
- Clean up old images (Save Disk Space): `kamal prune all`
- Check Proxy Routing Table: `ssh user@ip "docker exec kamal-proxy kamal-proxy list"`

## 💡 Pro-Tips for Small Servers

1. **Prune Frequently:** Small VMs fill up disk space quickly with Docker images. Run `kamal prune all` after every few deploys.
2. **Swap File:** If your VM has only 1GB–2GB of RAM, enable a Swap file to prevent "Out of Memory" crashes during Rails/FastAPI builds.
3. **One Proxy to Rule Them All:** Kamal Proxy will automatically detect when you add a new app and start routing traffic to it based on the `host` defined in `deploy.yml`.

Built with ❤️ by [Ansarissab](https://github.com/Ansarissab)
