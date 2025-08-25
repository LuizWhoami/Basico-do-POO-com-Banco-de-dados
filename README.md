# 📊 Sistema de Controle de Funcionários  

Este projeto é um sistema simples em **Python + SQLite** para gerenciar funcionários.  
Ele permite **armazenar** e **visualizar** dados de funcionários de forma prática usando o terminal.  

---

## ✨ Funcionalidades  

✅ Criação automática do banco de dados `Funcionario.db`  
✅ Cadastro de funcionários (nome, cargo e salário)  
✅ Visualização de todos os funcionários cadastrados  
✅ Interface de menu interativo no terminal  

---

## 🛠️ Tecnologias Utilizadas  

- [Python 3](https://www.python.org/)  
- [SQLite3](https://www.sqlite.org/index.html) (já incluso no Python, não precisa instalar nada)  

---

## 📂 Estrutura do Projeto  

```
📦 projeto-funcionarios
 ┣ 📜 main.py        # Código principal
 ┣ 📜 README.md      # Documentação
 ┗ 📜 Funcionario.db # Banco de dados (criado automaticamente)
```

---

## ▶️ Como Executar  

1. Clone este repositório ou copie o código para `main.py`  
2. Execute no terminal:  

```bash
python main.py
```

3. Será exibido o menu:  

```
==================================================
Sistema de Controle de Funcionarios
        [1] Armazenar
        [2] Visualizar
==================================================
```

4. Escolha:  
   - **[1] Armazenar** → cadastra um novo funcionário  
   - **[2] Visualizar** → lista todos os funcionários  

---

## 💾 Estrutura do Banco de Dados  

Tabela criada: `funcionarios`  

| Campo   | Tipo     | Descrição                        |
|---------|----------|----------------------------------|
| id      | INTEGER  | Chave primária (auto incremento) |
| nome    | TEXT     | Nome do funcionário              |
| cargo   | TEXT     | Cargo do funcionário             |
| salario | REAL     | Salário do funcionário           |

---

## 📌 Exemplo de Uso  

**Cadastro de funcionário:**  

```
Nome: João Silva
Cargo: Desenvolvedor
Salario: 4500
```

**Visualização no banco:**  

```
========================================
Banco de dados
========================================
(1, 'João Silva', 'Desenvolvedor', 4500.0)
```

---

## 🚀 Melhorias Futuras  

- Função para editar e excluir funcionários  
- Validação de dados (ex: impedir salário inválido)  
- Interface gráfica com **Tkinter**, **Flask** ou **Streamlit**  
