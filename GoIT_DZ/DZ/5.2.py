articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    matching_articles = []

    for article in articles_dict:
        title = article['title']
        author = article['author']

        if not letter_case:
            author = author.lower()
            title = title.lower()
            key = key.lower()

        if key in author or key in title:
            matching_articles.append({
                'title': article['title'],
                'author': article['author'],
                'year': article['year']
            })

    return matching_articles


result = find_articles(key="name")
print(result)
