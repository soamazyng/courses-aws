# Udemy - AWS Lambda and the Serverless Framework - Hands On Learning!

Link da empresa do Teacher: [https://courses.datacumulus.com](https://courses.datacumulus.com/)

Pacote de instalação para trabalhar com serverless: [https://github.com/serverless/serverless](https://github.com/serverless/serverless)

**Instalação global:**

```jsx
yarn global add serverless
```

Configurar a conta serverless que terá acesso ao pacote

```jsx
serverless config credentials --provider aws --key XXX --secret YYY --profile serverless-admin
```

Pode utilizar no terminal uma forma curta de escrever serverless que é `sls`

Criando um projeto

```jsx
sls create --template aws-python --path hello-world-python
```

Após criar o projeto deve alterar as configurações dentro do arquivo serverless.yml

Colocando a região e o profile criado anteriormente.

Fazendo deploy da aplicação na AWS

```jsx
sls deploy -v
```

Invocando a função no terminal

```jsx
sls invoke -f hello -l
```

Realizando update da função

```jsx
sls deploy -v
```

Realizando o deploy apenas da função

```jsx
sls deploy function -f hello
```

Realizar este tipo de deploy depois que já fez o deploy da stack inteira e também se só a função for atualizada, caso tenha alterações de dependências ou outras coisas devemos enviar a stack inteiro com o `sls deploy -v`.

Recuperar os logs

```jsx
sls logs -f hello -t
```

Deletando a função

```jsx
sls remove
```

## Converter json2yaml

www.json2yaml.com

## Timeout e memória

É possível configurar a quantidade de memória e o timeout default da função dentro do arquivo serverless.yml.

Também é possível determinar a memória e o timeout de cada uma das funções.

## Python

Boto3 é uma biblioteca utilizada para conectar-se ao aws console utilizando python.

## IAM Policy

Dentro do arquivo serverless é possível determinar quais as roles policy que serão utilizadas na function.

## Environment Variables

É possível definir environment variables para cada uma das funções ou de forma global.

## VPC

Para habilitar o VPC precisa configurar dentro do serverless file.

## API Gateway

Para encontar a url da api basta acessar o item no menu chamado estágios.

## Roles Cloud Watch

Os CronJobs que são instalados na AWS ficam dentro do CloudWatch >> Regras (Rules)
