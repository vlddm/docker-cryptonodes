# docker-cryptonodes
Setup:

```
docker swarm init
docker network create -d overlay --attachable --opt encrypted backend
docker stack deploy -c docker-cryptonodes-swarm.yml cryptonodes
```

script `build_push_nodes.sh` can be used to rebuild and push node images under your docker hub account
