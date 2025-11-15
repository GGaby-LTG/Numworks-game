class Technology:
	technology_list: list["Technology"] = []
	def __init__(self, name: str, requirements: "Technology | None", research_length: int, required_milestone: int):
		self.name = name
		self.requirements = requirements
		self.research_length = research_length
		self.required_milestone = required_milestone
		self.finished = False

		Technology.technology_list.append(self)

	def __repr__(self):
		return  f"Technology(name={self.name!r}, requirements={self.requirements and self.requirements.name!r})"

	# TODO: add is_unlockable()

# Test:
if __name__() == "__main__":
	spear = Technology("Spear", None, 1, 0)
	print("TECH LIST:",Technology.technology_list)
	print("EXAMPLE TECH:",spear)