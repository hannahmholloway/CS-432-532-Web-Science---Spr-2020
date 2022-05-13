from math import sqrt

def sim_pearson(prefs,p1,p2):
  # Get the list of mutually rated items
  si={}
  for item in prefs[p1]: 
    if item in prefs[p2]: si[item]=1

  # if they are no ratings in common, return 0
  if len(si)==0: return 0

  # Sum calculations
  n=len(si)
  
  # Sums of all the preferences
  sum1=sum([prefs[p1][it] for it in si])
  sum2=sum([prefs[p2][it] for it in si])
  
  # Sums of the squares
  sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
  sum2Sq=sum([pow(prefs[p2][it],2) for it in si]) 
  
  # Sum of the products
  pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])
  
  # Calculate r (Pearson score)
  num=pSum-(sum1*sum2/n)
  den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
  if den==0: return 0

  r=num/den

  return r

def topMatches(prefs,person,t=5,b=-5,similarity=sim_pearson):
  scores=[(similarity(prefs,person,other),other) 
                  for other in prefs if other!=person]
  scores.sort()
  scores.reverse()
  return scores[0:t], scores[b:]


def transformPrefs(prefs):
  result={}
  for person in prefs:
    for item in prefs[person]:
      result.setdefault(item,{})
      
      # Flip item and person
      result[item][person]=prefs[person][item]
  return result

movies={}
for line in open('./ml-100k/u.item'):
  (id,title)=line.split('|')[0:2]
  movies[id]=title

# Load data
prefs={}
for line in open('./ml-100k/u.data'):
  (user,movieid,rating,ts)=line.split('\t')
  prefs.setdefault(user,{})
  prefs[user][movies[movieid]]=float(rating)

favorite = 'Aristocats, The (1970)'
leastfavorite = 'Cable Guy, The (1996)'
remap = transformPrefs(prefs)
(favTop, favBot) = topMatches(remap,favorite,similarity=sim_pearson)
(leastTop, leastBot) = topMatches(remap, leastfavorite,similarity=sim_pearson)

print 'The top 5 movies similar to "Aristocats, The (1970)" are:'
print str(favTop[0]) + '\n' + str(favTop[1]) + '\n' + str(favTop[2]) + '\n' + str(favTop[3]) + '\n' + str(favTop[4]) + '\n'
print 'The bottom 5 movies similar to "Aristocats, The (1970)" are:'
print str(favBot[0]) + '\n' + str(favBot[1]) + '\n' + str(favBot[2]) + '\n' + str(favBot[3]) + '\n' + str(favBot[4]) + '\n'
print 'The top 5 movies similar to "Cable Guy, The (1996)" are:'
print str(leastTop[0]) + '\n' + str(leastTop[1]) + '\n' + str(leastTop[2]) + '\n' + str(leastTop[3]) + '\n' + str(leastTop[4]) + '\n'
print 'The bottom 5 movies similar to "Cable Guy, The (1996)" are:'
print str(leastBot[0]) + '\n' + str(leastBot[1]) + '\n' + str(leastBot[2]) + '\n' + str(leastBot[3]) + '\n' + str(leastBot[4]) + '\n'
