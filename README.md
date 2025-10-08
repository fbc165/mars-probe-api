# Mars Probe API

API para lançamento, listagem e movimentação de sondas em um planalto marciano. Esse projeto faz parte do desafio técnico da RD Station
Foi utilizado FastAPI para a criação da API.

---
## Versões
| Componente | Versão |
|------------|--------|
| API        | 0.0.1  |
| Python     | 3.13.8 |

---
## Execução

Fluxo recomendado:
1. Subir servidor do banco de dados
2. Criar e validar banco
3. Rodar testes
4. Subir aplicação
5. Consumir endpoints

---
## Pré-requisitos
| Requisito | Versão mínima | Observação |
|-----------|---------------|------------|
| Docker    | 20.x          | Necessário |
| Docker Compose | 1.29+    | Necessário |
| curl (opcional) | -       | Testar endpoints |

- Caso não tenha o docker ou o docker compose instalado, siga as instruções disponíveis [aqui](https://docs.docker.com/engine/)
---
## Estrutura Simplificada
```
mars_probe_api/
	app.py
	probes/
		models.py
		views.py
		services.py
		payloads.py
		responses.py
```

---
## Setup

### 1. Subir o MySQL
```
docker-compose up mysql
```
- verifique se a porta 3306 já não está sendo utilizada por outro contêiner ou aplicação. Em caso afirmativo, libera a porta

### 2. Criar banco de dados (primeira vez)
```
docker exec -i mysql-probe mysql -u root -p'iqui1234' -e "CREATE DATABASE IF NOT EXISTS mars_probe;"
```

### 3. Verificar criação do banco de dados
```
docker exec -i mysql-probe mysql -u root -p'iqui1234' -e "SHOW DATABASES;"
```
Confirme se `mars_probe` está na lista.

### 4. Rodar testes

```
docker exec -i mars-probe-api pytest -vv
```

### 5. Subir a aplicação
```
docker-compose up --build app
```
Disponível em: `http://localhost:9900`

---
## Endpoints
Base URL: `http://localhost:9900`

| Método | Rota | Descrição |
|--------|------|-----------|
| POST | /probes | Lança uma nova sonda |
| GET  | /probes | Lista as sondas |
| PATCH | /probes/{probe_id} | Move uma sonda |

### Lançar sonda
```
curl -X POST http://localhost:9900/probes \
	-H 'Content-Type: application/json' \
	-d '{"x":5, "y":5, "direction":"NORTH"}'
```

### Listar sondas
```
curl http://localhost:9900/probes
```

### Mover sonda
Comandos aceitos:
| Letra | Ação |
|-------|------|
| L | Gira 90° à esquerda |
| R | Gira 90° à direita |
| M | Move 1 unidade para frente |

```
curl -X PATCH http://localhost:9900/probes/<ID-DA-SONDA> \
	-H 'Content-Type: application/json' \
	-d '{"commands":"RM"}'
```

Resposta típica:
```json
{
	"id": "<ID-DA-SONDA>",
	"x": 6,
	"y": 5,
	"direction": "EAST"
}
```

---
## Qualidade
| Ferramenta | Função |
|------------|--------|
| pytest | Testes |
| mypy | Tipagem estática |
| black | Formatação |

- Obs.: credenciais e variáveis de ambientes estão hardcoded para facilitar ao rodar localmente