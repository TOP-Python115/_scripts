# Имеется список словарей, в каждом содержится информация о пользователе: имя, e-mail, номер телефона (опицонально)
# Программа должна вывести имена всех пользователей, у которых нет информации о номере телефона


data = [{'name': "Kimberly",'email': "magnis.dis.parturient@icloud.edu",'phone': ""},
	   {'name': "Hilda",'email': "sed.dui.fusce@yahoo.net",'phone': "7-965-821-0202"},
	   {'name': "Audrey",'email': "tempor@protonmail.ca",'phone': "7-917-202-6736"},
	   {'name': "Quinn",'email': "adipiscing.non@yahoo.edu",'phone': "7-998-879-5823"},
	   {'name': "Joelle",'email': "mollis.phasellus.libero@yahoo.couk",'phone': ""},
	   {'name': "Hannah",'email': "fusce.aliquet@icloud.net",'phone': "7-976-713-2361"},
	   {'name': "Sylvia",'email': "bibendum.donec.felis@hotmail.ca",'phone': ""},
	   {'name': "Karly",'email': "turpis.egestas@yahoo.couk",'phone': "7-954-740-1967"},
	   {'name': "Murphy",'email': "et.magnis.dis@hotmail.org",'phone': "7-984-851-4331"},
	   {'name': "Eugenia",'email': "nisi.dictum@outlook.com",'phone': "7-908-306-9976"},
	   {'name': "Brianna",'email': "vestibulum@google.ca",'phone': "7-945-342-5585"},
	   {'name': "Mechelle",'email': "enim.consequat.purus@hotmail.ca",'phone': ""},
	   {'name': "Nicholas",'email': "mauris.elit.dictum@outlook.org",'phone': ""},
	   {'name': "Beau",'email': "vivamus.rhoncus.donec@google.ca",'phone': ""},
	   {'name': "Noelani",'email': "diam.proin.dolor@aol.couk",'phone': "7-971-346-8475"},
	   {'name': "Ginger",'email': "integer.mollis@hotmail.couk",'phone': ""},
	   {'name': "Erica",'email': "nunc.ac@outlook.net",'phone': "7-956-888-2689"},
	   {'name': "Irene",'email': "magnis@outlook.couk",'phone': "7-974-963-6771"},
	   {'name': "Elijah",'email': "malesuada.malesuada@yahoo.edu",'phone': ""},
	   {'name': "Sade",'email': "nec.ante@google.net",'phone': "7-966-407-4498"}]

# res = [u for u in data if not u['phone']]
# print(*res)

[print(u['name'], u['email']) for u in data if not u['phone']]
