
check: # vérification que les pré requis sont bien installés
	@docker --version
	@k3d --version
	@echo "skaffold `skaffold version`"
	@echo "kubectl `kubectl version --short=true`"

init: check # création du cluster k3s et de sa registry
	k3d registry create registry.localhost --port 12345
	k3d cluster delete flask-demo && k3d cluster create flask-demo --registry-use k3d-registry.localhost:12345 -p "80:80@loadbalancer" -p "443:443@loadbalancer"

start: # démarrage du cluster
	k3d cluster start flask-demo

stop: # arret du cluser
	k3d cluster stop flask-demo

delete: # suppression du cluster
	k3d registry delete registry.localhost
	k3d cluster delete flask-demo
