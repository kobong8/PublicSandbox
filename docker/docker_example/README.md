- Docker 관련 명령어
```bash
sudo apt -y install \
apt-transport-https \
ca-certificates \
curl \
gnupg-agent \
software-properties-common

sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

```bash
echo "deb [arch=$( dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt-cache policy docker-ce
sudo apt -y install docker-ce
```

```bash
sudo usermod -aG docker kevin
sudo systemctl daemon-reload
sudo systemctl enable docker
sudo systemctl restart docker
sudo systemctl status docker
# q를 누를 경우 멈춤
```

```bash
docker run -it --name=sys-container-l centos:7 echo 'Hello World!'
```

```bash
docker cp index.html webserver1:/usr/share/nginx/html/index.html
```