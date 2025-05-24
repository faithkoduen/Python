#level 1

it_companies={'Google','Apple','Microsoft','Amazon','Facebook'}

#length of the set
print(len(it_companies))

#add 'twitter'
it_companies.add('Twitter')
print(it_companies)

#insert multiple IT companies
it_companies.update(['Safaricom','Intagram','Oracle'])
print(it_companies)

#remove one company
it_companies.remove('Apple')
print(it_companies)


#level 2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

#join A and B
print(A.union(B))

#Find A intersection B
print(A.intersection(B))

#Is A subset of B
print(A.issubset(B))

#Are A and B disjoint sets
print(A.isdisjoint(B))

#Join A with B and B with A
print(A|B)
print(B|A)

#symetric difference
print(A.symmetric_difference(B))

#delete sets
del A
del B

#level 3
# compare the length of the list and the set
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages_set=set(ages)
print(len(ages))
print(len(ages_set))

#unique words in the lists

sentence='I am a teacher and I love to inspire and teach people'
words=sentence.split()
unique_words=set(words)
print(len(unique_words))