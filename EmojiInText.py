import demoji

text =  """sometimes I'm 😔, and sometimes I'm 🤔. But most of the times I'm 😣 and 🥱"""
demoji.download_codes()
result =  demoji.findall(text)
print(result)