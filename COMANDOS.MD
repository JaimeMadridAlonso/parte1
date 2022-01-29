Crear proyecto
Crear mv: Ubuntu 18.04 LTS / e2-medium / Allow http y https / Allow default access
Crear regla de fw: 
                    destinos http-server
                    intervalos 0.0.0.0/0
                    tcp:9080

nano parte1.py

nano run.sh
chmod u+x run.sh

./run.sh