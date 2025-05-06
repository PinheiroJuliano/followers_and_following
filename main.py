import json

def extrair_usernames(arquivo, chave_lista=None):
    with open(arquivo, 'r', encoding='utf-8') as f:
        dados = json.load(f)

    if chave_lista:
        dados = dados[chave_lista]

    usernames = []
    for item in dados:
        if 'string_list_data' in item and item['string_list_data']:
            usernames.append(item['string_list_data'][0]['value'])
    return usernames

def main():
    seguindo = set(extrair_usernames('following.json', chave_lista='relationships_following'))
    seguidores = set(extrair_usernames('followers_1.json'))  # sem chave externa

    print(f"Total seguindo: {len(seguindo)}")
    print(f"Total seguidores: {len(seguidores)}\n")

    nao_seguem_de_volta = seguindo - seguidores

    print("Usuários que você segue, mas que não te seguem de volta:")
    for nome in sorted(nao_seguem_de_volta):
        print(nome)

if __name__ == '__main__':
    main()
