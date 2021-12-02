


init:
	k3d registry create registry.localhost --port 12345
	k3d cluster delete flask-demo && k3d cluster create flask-demo --registry-use k3d-registry.localhost:12345 -p "80:80@loadbalancer" -p "443:443@loadbalancer"

start:
	k3d cluster start flask-demo

stop:
	k3d cluster stop flask-demo

reset:
	k3d registry delete registry.localhost
	k3d cluster delete flask-demo