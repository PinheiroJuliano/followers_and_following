{
  "descricao": "Este script em Python compara os usuários que você segue com aqueles que te seguem de volta no Instagram.",
  "funcionamento": {
    "1": "Carrega dois arquivos JSON exportados do Instagram: um com a lista de seguidores e outro com a lista de contas que você segue.",
    "2": "Extrai os nomes de usuário (usernames) de cada arquivo.",
    "3": "Exibe o total de pessoas que você segue e o total de seguidores.",
    "4": "Compara os dois conjuntos e imprime os nomes dos usuários que você segue, mas que não te seguem de volta."
  },
  "como_obter_os_arquivos": {
    "passo_1": "Acesse seu perfil do Instagram pelo navegador.",
    "passo_2": "Clique em 'Configurações' > 'Privacidade e segurança' > 'Download de dados'.",
    "passo_3": "Solicite um download dos seus dados informando seu e-mail.",
    "passo_4": "Você receberá um e-mail com um link para baixar um arquivo ZIP contendo todos os seus dados.",
    "passo_5": "Extraia o arquivo ZIP e localize os arquivos JSON dentro da pasta 'followers_and_following'.",
    "passo_6": "Use o arquivo 'followers_1.json' como seguidores.json e 'following.json' como seguindo.json (renomeie se necessário)."
  },
  "requisitos": {
    "python": "Versão 3.6 ou superior",
    "arquivos": ["seguidores.json", "seguindo.json"],
    "estrutura_esperada": {
      "seguidores.json": "Lista de objetos com a chave 'string_list_data'",
      "seguindo.json": "Objeto com a chave 'relationships_following', contendo uma lista com 'string_list_data'"
    }
  }
}
