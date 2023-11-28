from collections import deque

# Função principal (exemplo de uso)
if __name__ == "__main__":
    lista_de_contatos = deque()

    # Adicionando contatos à lista
    lista_de_contatos.append({"nome": "Maria", "contato": 1234567890, "email": "maria@example.com"})
    lista_de_contatos.append({"nome": "Joao", "contato": 9876543210, "email": "joao@example.com"})
    lista_de_contatos.append({"nome": "Ana", "contato": 11112222333, "email": "ana@example.com"})

    # Mostrando os contatos da lista
    print("Lista de Contatos:")
    for contato in lista_de_contatos:
        print(f"Nome: {contato['nome']}, Contato: {contato['contato']}, Email: {contato['email']}")

    # Removendo um contato da lista
    lista_de_contatos = [contato for contato in lista_de_contatos if contato['nome'] != "Maria"]

    # Mostrando os contatos após a remoção
    print("\nLista de Contatos apos a remocao:")
    for contato in lista_de_contatos:
        print(f"Nome: {contato['nome']}, Contato: {contato['contato']}, Email: {contato['email']}")
