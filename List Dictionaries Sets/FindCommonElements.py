developer1 = {"python", "java", "javascript"}
developer2 = {"java", "python", "php"}

common = developer1.intersection(developer2)

print(common)

# unique skills
employee1 = {"java", "selenium", "api rest assured"}
employee2 = {"java", "playwright", "gen ai"}
all_skills = employee1.union(employee2)
print(all_skills)


