# API de Contatos - Backend em Flask

## Descrição

API simples para gerenciamento de contatos utilizando Flask e SQLite. Permite realizar operações CRUD (Criar, Ler, Atualizar, Excluir) em uma agenda de contatos.

## Rotas e Endpoints

### 1. Criar Contato (POST)
- **Rota:** `/api/v1/contato`
- **Método:** POST
- **Descrição:** Cria um novo contato.
- **Exemplo de Request:**
  ```json
  {
      "nome": "João Silva",
      "email": "joao.silva@email.com",
      "telefone": "123456789"
  }
  ```
- **Exemplo de Response:**
  ```json
  {
      "msg": "Contato salvo com sucesso."
  }
  ```

### 2. Obter Todos os Contatos (GET)
- **Rota:** `/api/v1/contato`
- **Método:** GET
- **Descrição:** Retorna todos os contatos cadastrados.
- **Exemplo de Response:**
  ```json
  [
      {
          "id": 1,
          "nome": "João Silva",
          "email": "joao.silva@email.com",
          "telefone": "123456789"
      },
      {
          "id": 2,
          "nome": "Maria Souza",
          "email": "maria.souza@email.com",
          "telefone": "987654321"
      }
  ]
  ```

### 3. Atualizar Contato (PUT)
- **Rota:** `/api/v1/contato`
- **Método:** PUT
- **Descrição:** Atualiza um contato existente.
- **Exemplo de Request:**
  ```json
  {
      "id": 1,
      "nome": "João Silva",
      "email": "joao.silva@novomail.com",
      "telefone": "111223344"
  }
  ```
- **Exemplo de Response:**
  ```json
  {
      "msg": "Contato atualizado com sucesso."
  }
  ```

### 4. Remover Contato (DELETE)
- **Rota:** `/api/v1/contato/<id>`
- **Método:** DELETE
- **Descrição:** Remove um contato pelo ID.
- **Exemplo de Response:**
  ```json
  {
      "msg": "Contato removido com sucesso."
  }
  ```

## Dependências

Para executar o projeto, você precisa das seguintes dependências:

- Flask
- sqlite3 (já integrado com o Python)

### Como Instalar as Dependências

1. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   ```

2. Ative o ambiente virtual:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

3. Instale as dependências:
   ```bash
   pip install flask
   ```

## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/bisnet0/api-flask-contatos.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd api-flask-contatos
   ```

3. Execute o aplicativo Flask:
   ```bash
   python app.py
   ```

A API estará disponível no endereço: [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Testando a API

Use ferramentas como Postman ou Insomnia, ou comandos cURL para testar os endpoints.

### Exemplo de cURL para criar um contato:
```bash
curl -X POST http://127.0.0.1:5000/api/v1/contato -H "Content-Type: application/json" -d '{"nome": "João Silva", "email": "joao.silva@email.com", "telefone": "123456789"}'
```

### Exemplo de cURL para obter todos os contatos:
```bash
curl http://127.0.0.1:5000/api/v1/contato
```

## Licença

Este projeto está licenciado sob a licença MIT.
