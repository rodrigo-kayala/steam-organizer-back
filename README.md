# steam-organizer backend

Usando o vagrant:

1. Instale o virtualbox: https://www.virtualbox.org/
2. Instale o vagrant: https://www.vagrantup.com/
3. Execute `vagrant up`
4. Execute `vagrant ssh`
5. No terminal do vagrant execute `cd /vagrant`

Para iniciar o servidor web: `./start-gunicorn.sh`
Para iniciar o worker celery: `./start-celery.sh`

Para suspender a vm vagrant: `vagrant suspend`
