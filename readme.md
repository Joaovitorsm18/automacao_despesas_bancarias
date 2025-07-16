# 🧾 Automação de Download de Relatórios de Despesas Bancárias - Superlógica

Este projeto é uma **automação simples para produtividade do dia a dia**, voltada para o download automático de relatórios de despesas bancárias em PDF para diversos condomínios, utilizando a API da Superlógica.

## 🚀 Funcionalidades

- Consulta de relatórios financeiros por condomínio.
- Geração de links de download para os PDFs.
- Download e salvamento automático dos arquivos no Google Drive (`G:/Meu Drive/...`).
- Organização de arquivos por condomínio e período (ex: `2025-06`).

---

## 📁 Estrutura dos Diretórios

Os arquivos são salvos no seguinte caminho:

```

G:/Meu Drive/CONDOMÍNIOS/{NOME DO CONDOMÍNIO}/FINANCEIRO/CONTAS/{YYYY-MM DESPESAS BANCÁRIAS SIGLA}.pdf

```

Exemplo:

```

G:/Meu Drive/CONDOMÍNIOS/ÁGAPE (AP)/FINANCEIRO/CONTAS/2025-06 DESPESAS BANCÁRIAS AP.pdf

````

---

## ⚙️ Pré-requisitos

- Python 3.8+
- Conta na [Superlógica](https://developers.superlogica.com.br/) com acesso à API
- Unidade do Google Drive sincronizada como pasta local (`G:/Meu Drive`)
- Tokens da API (`APP_TOKEN`, `ACCESS_TOKEN`)

---

## 📦 Instalação

1. **Clone o repositório**

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
````

2. **Crie o arquivo `.env` com suas credenciais da API**

```env
APP_TOKEN=seu_app_token
ACCESS_TOKEN=seu_access_token
```

3. **Instale as dependências**

```bash
pip install -r requirements.txt
```

> Se você ainda não tiver o `python-dotenv` instalado:

```bash
pip install python-dotenv
```

---

## ▶️ Como usar

Execute o script principal:

```bash
python main.py
```

O script irá:

* Iterar sobre todos os condomínios definidos em `condominios.py`
* Buscar o relatório mais recente via API
* Baixar e salvar o PDF automaticamente

---

## 🗂 Arquivos principais

* `main.py`: Script principal da automação.
* `condominios.py`: Lista de condomínios com nome, ID e sigla.
* `.env`: Arquivo com tokens de autenticação (não deve ser versionado).
* `requirements.txt`: Lista de dependências.
* `README.md`: Este arquivo.

---


---

## 🧑‍💻 Autor

Automação desenvolvida por [João Vítor](https://github.com/Joaovitorsm18)

```

---


```
