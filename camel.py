import camelcase

c = camelcase.CamelCase()

text = "hello world from python"
camel_text= c.hump(text)
print(camel_text)

