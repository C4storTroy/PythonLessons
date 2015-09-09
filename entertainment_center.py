import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                         "A story of a boy and his toys that come to life",
                         "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                         "https://www.youtube.com/watch?v=2BlMNH1QTeE")

#print (toy_story.storyline)

lord_of_the_rings = media.Movie("Lord Of The Rings",
                         "The Lord of the Rings is a film series consisting of three epic fantasy adventure films directed by Peter Jackson. They are based on the novel The Lord of the Rings by J. R. R. Tolkien. The films are subtitled The Fellowship of the Ring (2001), The Two Towers (2002) and The Return of the King (2003). They were distributed by New Line Cinema.",
                         "https://upload.wikimedia.org/wikipedia/en/8/87/Ringstrilogyposter.jpg",
                         "https://www.youtube.com/watch?v=aStYWD25fAQ")

#print (avatar.storyline)

#avatar.show_trailer()

star_wars = media.Movie("Star Wars - The Force Awaken",
                      "The force rise again",
                      "http://i2.wp.com/bitcast-a-sm.bitgravity.com/slashfilm/wp/wp-content/images/star-wars-7-struzan-poster-full.jpg",
                      "https://www.youtube.com/watch?v=ngElkyQ6Rhs")

#star_wars.show_trailer()

the_warriors = media.Movie("The Warriors",
                      "In it, a New York City gang must return to their home turf after they are framed for the murder of a respected gang leader.",
                      "https://upload.wikimedia.org/wikipedia/en/0/03/TheWarriors_1979_Movie_Poster.jpg",
                      "https://www.youtube.com/watch?v=4GxSwUcm_XE")

school_of_rock = media.Movie("School of Rock",
                      "Using to learn rock at school",
                      "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                      "https://www.youtube.com/watch?v=5afGGGsxvEA")


conan_the_barbarian = media.Movie("Conan the Barbarian",
                      "It is based on stories by Robert E. Howard, a pulp fiction writer of the 1930s, about the adventures of the eponymous character in a fictional pre-historic world of dark magic and savagery.",
                      "https://upload.wikimedia.org/wikipedia/en/8/81/Conan_the_Barbarian_by_Renato_Casaro.jpg",
                      "https://www.youtube.com/watch?v=Y0cxNbz4yKc")

movies = [toy_story, lord_of_the_rings, star_wars,the_warriors,school_of_rock,conan_the_barbarian]

fresh_tomatoes.open_movies_page(movies)
