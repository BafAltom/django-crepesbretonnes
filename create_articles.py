from blog.models import Article, Category

cat = Category(name="blog")
cat.save()

art = Article(title="My first blog lol", author="Me lol", content="This is a blog it's so blog lolg")
art.category = cat
art.save()

art = Article(title="Anotherone", author="Me lol", content="Has someone seen my pie it's cherry tasting?")
art.category = cat
art.save()

art = Article(title="Life is sad", author="Me lol", content="For when the rain is hard and the dead leaves on the ground smell like the harsh reality of the lives of forgotten souls of the past, my pie is gone and so am I.")
art.category = cat
art.save()

