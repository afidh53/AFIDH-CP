student={"Anu":340,"Teena":458,"John":300}
asc_by_name=dict(sorted(student.items()))
print("sorted by name(ascending):")
print(asc_by_name)
desc_by_name=dict(sorted(student.items(),reverse=True))
print("\nSorted by name(descending):")
print(desc_by_name)
