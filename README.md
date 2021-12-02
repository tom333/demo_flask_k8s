
# Pré requis
- [docker](https://docs.docker.com/engine/install/ubuntu/)
- [k3d](https://k3d.io/v5.1.0/#install-script)
- [kubectl](https://kubernetes.io/fr/docs/tasks/tools/install-kubectl/)
- [skaffold](https://skaffold.dev/docs/install/)
 
## Recommandé
- [nss-myhostname](apt:nss-myhostname)
- [kail](https://github.com/boz/kail)

# Initalisation
`make init`

# Lancement de k3s 
`make start`

# let's dev !
`skaffold dev`

and [Here it is](http://todolist.localhost/)

# Autres
## PgAdmin 4
Console Pg Admin 4 [ici](http://pgadmin.localhost/)

## local registry catalog
[http://k3d-registry.localhost:12345/v2/_catalog](http://k3d-registry.localhost:12345/v2/_catalog)

## Visualisation des logs
`kail -l flask-backend`

## Un peu de ménage 
`docker rmi $(docker images --format '{{.Repository}}:{{.Tag}}' | grep 'todolist')`
