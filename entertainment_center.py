import media

toy_story = media.Movie("Toy Story",
                         "A story of a boy and his toys that come to life",
                         "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                         "https://www.youtube.com/watch?v=2BlMNH1QTeE")

print (toy_story.storyline)

avatar = media.Movie("Avatar",
                      "A marine on an alien planet",
                      "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                      "https://www.youtube.com/watch?v=2v-svozQvc4")

print (avatar.storyline)

#avatar.show_trailer()

star_wars = media.Movie("Star Wars - The Force Awaken",
                      "The force rise again",
                      "http://i2.wp.com/bitcast-a-sm.bitgravity.com/slashfilm/wp/wp-content/images/star-wars-7-struzan-poster-full.jpg",
                      "https://www.youtube.com/watch?v=ngElkyQ6Rhs")

star_wars.show_trailer()
