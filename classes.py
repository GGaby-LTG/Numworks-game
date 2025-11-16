class Technology:
	technology_list: list["Technology"] = []
	def __init__(self, name: str, requirement: "Technology | None", research_length: int, required_milestone: int, called_function: "function | None" = None):
		self.name = name
		self.requirement = requirement
		self.research_length = research_length
		self.required_milestone = required_milestone
		self.called_function = called_function
		self.finished = False

		Technology.technology_list.append(self)

	def __repr__(self):
		return  f"Technology(name={self.name!r}, requirement={self.requirement and self.requirement.name!r},research_length={self.research_length!r},required_milestone={self.required_milestone!r})"

	def is_unlockable(self):
		if self.requirement == None:
			return True
		elif self.requirement.finished:
			return True
		return False

# Test:
if __name__() == "__main__":
	spear = Technology("Spear", None, 1, 0)
	print("TECH LIST:",Technology.technology_list)
	print("EXAMPLE TECH:",spear)
	print("IS UNLOCKABLE:",spear.is_unlockable())







