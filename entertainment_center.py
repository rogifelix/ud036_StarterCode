import media
import fresh_tomatoes

# List of movies goes here
lotr_fotr = media.Movie("Lord of The Rings: The Fellowship of The Ring",
                        "The Fellowship of the Ring is the first of three volumes in The Lord of the Rings, an epic set in the fictional world of Middle-earth.",
                        "https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=V75dMMIW2B4")

lotr_tt = media.Movie("Lord of The Rings: The Two Towers",
                      "The Two Towers opens with the disintegration of the Fellowship, as Merry and Pippin are taken captive by Orcs after the death of Boromir in battle.",
                      "https://upload.wikimedia.org/wikipedia/pt/5/59/The_Lord_of_the_Rings_The_Two_Towers.jpg",
                      "https://www.youtube.com/watch?v=LbfMDwc4azU")

lotr_rotk = media.Movie("The Lord of the Rings: The Return of the King",
                        "The Return of the King, the third and final volume in The Lord of the Rings, opens as Gandalf and Pippin ride east to the city of Minas Tirith in Gondor, just after parting with King Th�oden and the Riders of Rohan at the end of The Two Towers.",
                        "https://upload.wikimedia.org/wikipedia/pt/thumb/0/0d/EsdlaIII.jpg/250px-EsdlaIII.jpg",
                        "https://www.youtube.com/watch?v=y2rYRu8UW8M")

hobbit_auj = media.Movie("The Hobbit: An Unexpected Journey",
                         "The adventure follows the journey of title character Bilbo Baggins, who is swept into an epic quest to reclaim the lost Dwarf Kingdom of Erebor from the fearsome dragon Smaug.",
                         "https://upload.wikimedia.org/wikipedia/en/b/b3/The_Hobbit-_An_Unexpected_Journey.jpeg",
                         "https://www.youtube.com/watch?v=JTSoD4BBCJc")

hobbut_dos = media.Movie("The Hobbit: The Desolation of Smaug",
                         "Bilbo and his companions reach the Lonely Mountain, where they encounter the fearsome dragon Smaug.",
                         "https://upload.wikimedia.org/wikipedia/en/4/4f/The_Hobbit_-_The_Desolation_of_Smaug_theatrical_poster.jpg",
                         "https://www.youtube.com/watch?v=fnaojlfdUbs")

hobbit_botfa = media.Movie("The Hobbit: The Battle of the Five Armies",
                           "Men, Dwarves and Elves must decide whether to unite and prevail -- or be destroyed -- and Middle Earth hangs in the balance.",
                           "https://upload.wikimedia.org/wikipedia/en/0/0e/The_Hobbit_-_The_Battle_of_the_Five_Armies.jpg",
                           "https://www.youtube.com/watch?v=iVAgTiBrrDA")

# add movies to an array
movies = [lotr_fotr, lotr_tt, lotr_rotk, hobbit_auj, hobbut_dos, hobbit_botfa]
# send the array
fresh_tomatoes.open_movies_page(movies)
