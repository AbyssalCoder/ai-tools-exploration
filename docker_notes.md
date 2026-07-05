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
