from TomeRater import *

Tome_Rater = TomeRater()

#Create some books:
print("Creating books:")
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)

print("\nCreating users:")
#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")


#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

print("\nAdding books:")

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)

#Uncomment these to test your functions:
print("\nThis is our catalog:")
Tome_Rater.print_catalog()
print("\nOur users are:")
Tome_Rater.print_users()

print("\nMost positive user:")
print(Tome_Rater.most_positive_user())
print("\nHighest rated book:")
print(Tome_Rater.highest_rated_book())
print("\nMost read book:")
print(Tome_Rater.most_read_book())
print("\n4 most read books:")
print(Tome_Rater.get_n_most_read_books(4))
print("\n4 most prolific users:")
print(Tome_Rater.get_n_most_prolific_readers(4))
print("\nPrint Tome_Rater:\n")
print(Tome_Rater)

print("\nWe are going to create a new empty Tome_Rater and see if the comparison it's fine (should return False):")
Tome_Rater_2 = TomeRater()
print(Tome_Rater == Tome_Rater_2)

