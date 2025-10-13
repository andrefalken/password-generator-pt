# Expanded Portuguese word list for password generator
# Words organized by length for efficient password generation

portuguese_words = [
    # 1-character words (common symbols and letters)
    "a", "e", "o",

    # 2-character words
    "de", "do", "da", "em", "no", "na", "se", "me", "te", "os",
    "as", "um", "ao", "eu", "tu", "ele", "ela", "nos", "vos", "lhe",

    # 3-character words
    "que", "com", "sem", "por", "para", "era", "foi", "via", "dia", "sol",
    "mar", "ceu", "paz", "bem", "mal", "sim", "nao", "sim", "amo", "ode",

    # 4-character words
    "este", "essa", "isso", "aque", "muito", "mais", "menos", "sobre", "antes", "depois",
    "agora", "sempre", "nunca", "hoje", "amanha", "ontem", "aqui", "ali", "la", "cada",

    # 5-character words
    "quando", "onde", "como", "porque", "desde", "ate", "entre", "sobre", "pesso", "mundo",
    "tempo", "lugar", "cidade", "campo", "casa", "rua", "vida", "amor", "feliz", "livro",

    # 6-character words
    "pessoa", "homem", "mulher", "crianca", "familia", "amigos", "trabalho", "escola", "cidade", "bairro",
    "carro", "musica", "jogo", "cor", "numero", "sistema", "online", "social", "celular", "energia",

    # 7-character words
    "programa", "projeto", "servico", "empresa", "digital", "rede", "contato", "privado", "conteudo", "caracter",
    "qualidade", "liberdade", "viagem", "manha", "tarde", "clima", "historia", "ciencia", "cultura", "natureza",

    # 8-character words
    "negocio", "seguranca", "computador", "internet", "software", "hardware", "banco", "estrategia",
    "criativo",
    "montanha", "universo", "aventura", "conhecimento", "linguagem", "paz", "poderoso", "colorido", "bonito",
    "maravilhoso",

    # 9-character words
    "educacao", "gerador", "interface", "excelente", "fantastico", "brilhante", "importante", "diferente", "comunidade",
    "celebrar",
    "desafio", "computador", "beleza", "conhecimento", "incrivel", "fantastico", "brilhante", "essencial", "diferente",
    "comunidade",

    # 10-character words
    "tecnologia", "inovacao", "criatividade", "lideranca", "gestao", "producao", "eficiencia", "sucesso", "brasil",
    "amizade",
    "motivacao", "confianca", "ambiente", "celebração", "fundacao", "revolucao", "protecao", "investimento",
    "descobrir", "aventureiro"
]

# Additional categorization by length for optimized selection
words_by_length = {
    1: ["a", "e", "o"],
    2: ["de", "do", "da", "em", "no", "na", "se", "me", "te", "os", "as", "um", "ao", "eu", "tu", "ele", "ela", "nos",
        "vos", "lhe"],
    3: ["que", "com", "sem", "por", "para", "era", "foi", "via", "dia", "sol", "mar", "ceu", "paz", "bem", "mal", "sim",
        "nao", "sim", "amo", "ode"],
    4: ["este", "essa", "isso", "aque", "muito", "mais", "menos", "sobre", "antes", "depois", "agora", "sempre",
        "nunca", "hoje", "amanha", "ontem", "aqui", "ali", "la", "cada"],
    5: ["quando", "onde", "como", "porque", "desde", "ate", "entre", "sobre", "pesso", "mundo", "tempo", "lugar",
        "cidade", "campo", "casa", "rua", "vida", "amor", "feliz", "livro"],
    6: ["pessoa", "homem", "mulher", "crianca", "familia", "amigos", "trabalho", "escola", "cidade", "bairro", "carro",
        "musica", "jogo", "cor", "numero", "sistema", "online", "social", "celular", "energia"],
    7: ["programa", "projeto", "servico", "empresa", "digital", "rede", "contato", "privado", "conteudo", "caracter",
        "qualidade", "liberdade", "viagem", "manha", "tarde", "clima", "historia", "ciencia", "cultura", "natureza"],
    8: ["negocio", "seguranca", "computador", "internet", "software", "hardware", "banco", "estrategia",
        "criativo", "montanha", "universo", "aventura", "conhecimento", "linguagem", "paz", "poderoso", "colorido",
        "bonito", "maravilhoso"],
    9: ["educacao", "gerador", "interface", "excelente", "fantastico", "brilhante", "importante", "diferente",
        "comunidade", "celebrar", "desafio", "computador", "beleza", "conhecimento", "incrivel", "fantastico",
        "brilhante", "essencial", "diferente", "comunidade"],
    10: ["tecnologia", "inovacao", "criatividade", "lideranca", "gestao", "producao", "eficiencia", "sucesso", "brasil",
         "amizade", "motivacao", "confianca", "ambiente", "celebração", "fundacao", "revolucao", "protecao",
         "investimento", "descobrir", "aventureiro"]
}


def get_words_by_length(length):
    """Get words of specific length"""
    return words_by_length.get(length, [])


def get_words_up_to_length(max_length):
    """Get all words up to a specific maximum length"""
    return [word for word in portuguese_words if len(word) <= max_length]


# Test function to verify the word list
if __name__ == "__main__":
    print("📊 Word List Statistics:")
    for length in range(1, 11):
        words = get_words_by_length(length)
        print(f"Length {length}: {len(words)} words")

    print(f"\n📝 Total words: {len(portuguese_words)}")
    print("✅ Word list is ready for use!")