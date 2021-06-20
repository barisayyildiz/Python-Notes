class TeamItearator:
	def __init__(self, obj):
		self._team = obj._myarr
		self._index = 0
	def __next__(self):
		result = None
		if self._index < len(self._team):
			result = self._team[self._index]
			self._index += 1
			return result
		else:
			raise StopIteration("cannot iterate further...")
		self._index += 1


class Team:
	def __init__(self, team = []):
		self._myarr = team
	def __iter__(self):
		return TeamItearator(self)

team = Team(["baris", "ayyildiz", "john", "doe"])
for i in team:
	print(i)

print("-----------")

iterator = iter(team)
while True:
	try:
		print(next(iterator))	
	except StopIteration:
		break

