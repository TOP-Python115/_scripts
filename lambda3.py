from pprint import pprint

books = [
	{
		'title': "odio. Phasellus",
		'publish_date': "1982-03-16",
		'pages': "227"
	},
	{
		'title': "sit amet",
		'publish_date': "2019-03-31",
		'pages': "482"
	},
	{
		'title': "pede. Suspendisse",
		'publish_date': "1961-03-11",
		'pages': "484"
	},
	{
		'title': "a felis",
		'publish_date': "1979-02-22",
		'pages': "198"
	},
	{
		'title': "Donec",
		'publish_date': "1999-07-19",
		'pages': "260"
	},
	{
		'title': "montes,",
		'publish_date': "1976-12-31",
		'pages': "465"
	},
	{
		'title': "sem molestie sodales.",
		'publish_date': "1976-07-02",
		'pages': "205"
	},
	{
		'title': "dignissim tempor arcu.",
		'publish_date': "2002-10-13",
		'pages': "452"
	},
	{
		'title': "eget ipsum. Suspendisse",
		'publish_date': "1999-05-28",
		'pages': "375"
	},
	{
		'title': "a, enim.",
		'publish_date': "1957-05-05",
		'pages': "439"
	},
	{
		'title': "nulla magna,",
		'publish_date': "1978-01-18",
		'pages': "190"
	},
	{
		'title': "vehicula et, rutrum",
		'publish_date': "1983-07-15",
		'pages': "200"
	},
	{
		'title': "ipsum dolor sit",
		'publish_date': "1967-02-12",
		'pages': "430"
	},
	{
		'title': "Nullam",
		'publish_date': "1971-01-12",
		'pages': "482"
	},
	{
		'title': "molestie arcu.",
		'publish_date': "1989-10-30",
		'pages': "423"
	},
	{
		'title': "orci sem",
		'publish_date': "1965-03-09",
		'pages': "371"
	},
	{
		'title': "metus. Aliquam erat",
		'publish_date': "1996-09-03",
		'pages': "402"
	},
	{
		'title': "mauris a nunc.",
		'publish_date': "2005-06-03",
		'pages': "462"
	},
	{
		'title': "nec, cursus a,",
		'publish_date': "1959-06-19",
		'pages': "373"
	},
	{
		'title': "Phasellus at",
		'publish_date': "1994-12-30",
		'pages': "164"
	}
]

for book in books:
	book['pages'] = int(book['pages'])

# не рекомендуется использовать – создаётся полная копия -> неэффективная работа с памятью
# books2 = [{k: v if k != 'pages' else int(v) for k, v in book.items()} for book in books]

books_XXcen = filter(lambda b: 1900 <= int(b['publish_date'][:4]) < 2000, books)

books_title_sort = sorted(books, key=lambda b: b['title'].lower())
