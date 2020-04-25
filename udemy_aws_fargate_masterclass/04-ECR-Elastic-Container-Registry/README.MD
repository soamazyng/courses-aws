# Anotações

Cria a imagem

```
  docker build -t 712790115760.dkr.ecr.us-east-2.amazonaws.com/aws-ecr-nginx:1.0.0 .
```

Roda a imagem apontando a porta da minha imagem para a porta 80, com isso basta digitar no navegador http://localhost que vai tudo funcionar.

```
docker run --name aws-ecr-nginx -p 80:80 --rm -d 712790115760.dkr.ecr.us-east-2.amazonaws.com/aws-ecr-nginx:1.0.0
```
