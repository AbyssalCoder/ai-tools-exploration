## Docker Networking

### Network drivers
- **bridge** (default) — isolated network on host
- **host** — shares host's network stack
- **none** — no networking
- **overlay** — multi-host (Swarm)

```bash
docker network create mynet
docker run --network mynet --name app1 nginx
docker run --network mynet --name app2 alpine ping app1
```

Containers on the same user-defined bridge can resolve each other by name.

## Docker Basics

Docker packages applications into containers — lightweight, portable units.

### Key commands
```bash
docker run hello-world              # Run a test container
docker ps                            # List running containers
docker ps -a                         # List all containers
docker images                        # List local images
docker stop <container_id>           # Stop a container
docker rm <container_id>             # Remove a container
docker rmi <image_id>                # Remove an image
```

**Container ≠ VM** — containers share the host kernel.
