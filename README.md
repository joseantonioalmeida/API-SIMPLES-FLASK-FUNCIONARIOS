# Cadastro de Funcionários – API Flask

## Descrição
Esta é uma API simples em **Flask** para gerenciar funcionários armazenados em um banco de dados MySQL. Ela oferece dois endpoints principais:

- **GET `/funcionarios/`** – Retorna a lista de todos os funcionários.
- **POST `/funcionarios/`** – Cria um novo registro de funcionário.

## Sumário
1. [Pré‑requisitos](#-pré-requisitos)
2. [Instalação](#-instalação)
3. [Configuração](#-configuração)
4. [Executando a aplicação](#-executando-a-aplicação)
5. [Endpoints da API](#-endpoints-da-api)
6. [Estrutura da tabela](#-estrutura-da-tabela)
7. [Melhorias sugeridas](#-melhorias-sugeridas)

---

## Pré‑requisitos
- Python 3.8 ou superior
- MySQL rodando (local ou remoto)
- `pip` para gerenciamento de pacotes

## Instalação
```bash
# (Opcional) Crie um ambiente virtual
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate   # macOS/Linux

# Instale as dependências
pip install flask pymysql
```

## Configuração
A conexão com o banco está definida na função `connect_db` em **app.py**:
```python
def connect_db(
        db_host='localhost', 
        db_user='root', 
        db_password='12345678', 
        db_name='banco_funcionarios'
    ):
    db = pymysql.connect(host=db_host, user=db_user, passwd=db_password, database=db_name)
    return db
```
Altere os valores padrão para refletir seu ambiente ou modifique a função para ler variáveis de ambiente.

## Executando a aplicação
```bash
python app.py
```
A API será iniciada em modo debug na URL **http://127.0.0.1:5000/**. 
> **Atenção:** Não mantenha `debug=True` em produção.

## Endpoints da API
### 1. Listar todos os funcionários
- **Método:** `GET`
- **URL:** `/funcionarios/`
- **Resposta (200):**
```json
{
  "mensagem": "Lista de Funcionarios",
  "total": 2,
  "dados": [
    {"id": 2, "nome": "Maria", "telefone": "9999-8888"},
    {"id": 1, "nome": "João", "telefone": "1111-2222"}
  ]
}
```
A lista é ordenada por `id` em ordem decrescente.

### 2. Criar um novo funcionário
- **Método:** `POST`
- **URL:** `/funcionarios/`
- **Corpo (JSON):**
```json
{
  "nome": "Pedro",
  "telefone": "3333-4444"
}
```
- **Resposta (201):**
```json
{
  "mensagem": "Funcionario cadastrado com sucesso.",
  "carro": {"id": 3, "nome": "Pedro", "telefone": "3333-4444"}
}
```
O campo `id` é gerado automaticamente pelo MySQL.

## Estrutura da tabela MySQL
```sql
CREATE TABLE funcionario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    telefone VARCHAR(50) NOT NULL
);
```

## Melhorias sugeridas
- **Segurança:** Não deixar credenciais no código; usar variáveis de ambiente ou um arquivo de configuração seguro.
- **Tratamento de erros:** Envolver operações de banco em `try/except` e devolver mensagens de erro adequadas (400, 500, etc.).
- **Validação de entrada:** Verificar se `nome` e `telefone` foram enviados e obedecem ao formato esperado.
- **CORS:** Caso a API seja consumida por front‑ends de outros domínios, habilitar CORS (`flask-cors`).
- **Deploy:** Utilizar um servidor de produção como Gunicorn ou Waitress e desativar o modo debug.

---

Feito com ❤️ por **[José Antonio]**.