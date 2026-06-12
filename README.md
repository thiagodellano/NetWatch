# 🖥️ NetWatch

### Disciplina: Redes de Computadores e Internet

### Alunos: Thiago Dellano Machado de Oliveira | 24101272

Sistema de monitoramento de infraestrutura e segurança desenvolvido em Python com Flask.

O NetWatch foi criado com o objetivo de centralizar informações sobre serviços de rede, permitindo a visualização de métricas, alertas e indicadores de segurança em um dashboard web simples e intuitivo.

---

## 📋 Objetivo

O projeto tem como finalidade demonstrar conceitos de monitoramento de infraestrutura, análise de métricas e detecção de possíveis ameaças em ambientes computacionais.

Através de uma interface web, o usuário pode acompanhar o estado dos principais serviços de rede e receber alertas quando situações anormais forem identificadas.

---

## 🚀 Funcionalidades

### Monitoramento de Serviços

- Web Server
- Database
- DNS
- SMTP

### Métricas

- Latência
- Requests por segundo (Requests/s)
- Uso de CPU
- Uso de Memória
- Tempo de resposta DNS
- Falhas SMTP

### Dashboard

- Interface web desenvolvida com Bootstrap
- Exibição de métricas em tempo real simuladas
- Resumo geral do ambiente
- Indicadores visuais de status

### Alertas

- Latência acima do recomendado
- Serviço SMTP Offline
- Eventos de segurança

### Segurança

- Detecção de possível ataque DDoS
- Detecção de possível ataque de força bruta (Brute Force)
- Monitoramento de vulnerabilidades

### Visualização

- Gráfico de latência utilizando Chart.js

---

## 🏗️ Arquitetura do Sistema

```text
Usuário
   │
   ▼
Dashboard Web
(Flask + Bootstrap)
   │
   ▼
Módulo de Monitoramento
   │
   ├── Web Server
   ├── Database
   ├── DNS
   └── SMTP
   │
   ▼
Módulo de Segurança
   │
   ├── DDoS
   ├── Brute Force
   └── Vulnerabilidades
```

---

## 📁 Estrutura do Projeto

```text
NetWatch/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── dashboard.html
│
├── static/
│
├── docs/
│
└── .venv/
```

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- Flask
- Bootstrap 5
- Chart.js
- HTML5
- Git
- GitHub
- WSL (Windows Subsystem for Linux)

---

## ⚙️ Instalação

Clone o repositório:

```bash
git clone https://github.com/thiagodellano/NetWatch.git
```

Entre na pasta do projeto:

```bash
cd NetWatch
```

Crie o ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual:

Linux / WSL:

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## ▶️ Executando o Projeto

Execute:

```bash
python app.py
```

Abra o navegador:

```text
http://127.0.0.1:5000
```

---

## 📊 Funcionalidades de Segurança

O sistema possui mecanismos simples de detecção de ameaças:

### DDoS

Quando o número de requisições por segundo ultrapassa o limite definido, o sistema gera um alerta indicando possível ataque DDoS.

### Brute Force

Quando o número de tentativas de login excede o limite configurado, o sistema gera um alerta indicando possível ataque de força bruta.

---

## 👨‍💻 Equipe

Projeto desenvolvido para a disciplina de Redes de Computadores.

**Aluno:** Thiago Dellano

---

## 📄 Licença

Projeto desenvolvido exclusivamente para fins acadêmicos e educacionais.