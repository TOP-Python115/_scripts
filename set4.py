data = [
	{
		'name': "Brandon",
		'languages': "Russian French Spanish"
	},
	{
		'name': "Kelsey",
		'languages': "Spanish"
	},
	{
		'name': "Amethyst",
		'languages': "Russian"
	},
	{
		'name': "Jonas",
		'languages': "Russian French"
	},
	{
		'name': "Stuart",
		'languages': "Russian French"
	},
	{
		'name': "Lane",
		'languages': "English Russian"
	},
	{
		'name': "Mohammad",
		'languages': "Russian French"
	},
	{
		'name': "Sylvester",
		'languages': "Russian French"
	},
	{
		'name': "Melissa",
		'languages': "French Spanish"
	},
	{
		'name': "Clare",
		'languages': "French Spanish"
	},
	{
		'name': "Mechelle",
		'languages': "Russian"
	},
	{
		'name': "Leroy",
		'languages': "English Russian"
	},
	{
		'name': "Flavia",
		'languages': "Russian French Spanish"
	},
	{
		'name': "Vivian",
		'languages': "French"
	},
	{
		'name': "Shaine",
		'languages': "Russian French"
	},
	{
		'name': "Haviva",
		'languages': "French"
	},
	{
		'name': "Carly",
		'languages': "English Russian French"
	},
	{
		'name': "Cathleen",
		'languages': "French Spanish"
	},
	{
		'name': "Francis",
		'languages': "English Russian French"
	},
	{
		'name': "Jack",
		'languages': "Russian French Spanish"
	},
	{
		'name': "Kirestin",
		'languages': "Russian French"
	},
	{
		'name': "Britanni",
		'languages': "Russian French"
	},
	{
		'name': "Jesse",
		'languages': "Russian French"
	},
	{
		'name': "Susan",
		'languages': "Spanish"
	},
	{
		'name': "Herman",
		'languages': "Spanish"
	},
	{
		'name': "Chantale",
		'languages': "Russian French Spanish"
	},
	{
		'name': "Chandler",
		'languages': "Russian"
	},
	{
		'name': "Joel",
		'languages': "Russian French Spanish"
	},
	{
		'name': "Eric",
		'languages': "English Russian"
	},
	{
		'name': "Stone",
		'languages': "Russian French"
	}
]

for p in data:
    if {'Russian', 'Spanish'}.issubset(set(p['languages'].split())):
        print(p['name'])
