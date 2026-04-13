from studentDAO import studentDAO

# create
latestid = studentDAO.create(("mark", 45))
print("Inserted ID:", latestid)

# find by id
result = studentDAO.findByID(latestid)
print("Found by ID:", result)

# update
studentDAO.update(("Fred", 21, latestid))
result = studentDAO.findByID(latestid)
print("After update:", result)

# get all
allStudents = studentDAO.getAll()
for student in allStudents:
    print(student)

# delete
studentDAO.delete(latestid)
print("Deleted ID:", latestid)