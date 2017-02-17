import MovieClass
import fresh_tomatoes
Wonder_Woman = MovieClass.Movie("Wonder Woman",
                               "Before she was Wonder Woman, she was Diana, princess of the Amazons, trained to be an unconquerable warrior. Raised on a sheltered island paradise, when an American pilot crashes on their shores and tells of a massive conflict raging in the outside world, Diana leaves her home, convinced she can stop the threat. Fighting alongside man in a war to end all wars, Diana will discover her full powers...and her true destiny.",
                               "http://s3.birthmoviesdeath.com/images/made/Wonder-Woman-Poster_1200_1778_81_s.jpg",
                               "https://www.youtube.com/watch?v=T1j7qWUQjog")
Pirates_Five = MovieClass.Movie("Pirates Of The Caribbean 5",
                               "Thrust into an all-new adventure, a down-on-his-luck Capt. Jack Sparrow feels the winds of ill-fortune blowing even more strongly when deadly ghost sailors led by his old nemesis, the terrifying Capt. Salazar, escape from the Devil's Triangle. Jack's only hope of survival lies in seeking out the legendary Trident of Poseidon",
                               "http://t2.gstatic.com/images?q=tbn:ANd9GcRepmoIdnj8wBiwrLF-866UZtQsaN3y3WIjTCsAUzP9oI6XXzVV",
                               "https://www.youtube.com/watch?v=NSWV0hzLFzc")
Transformers_Five = MovieClass.Movie("Transformers 5",
                                    "Humans are at war with the Transformers, and Optimus Prime is gone. The key to saving the future lies buried in the secrets of the past and the hidden history of Transformers on Earth. Now, it's up to the unlikely alliance of Cade Yeager (Mark Wahlberg), Bumblebee, an English lord and an Oxford professor to save the world.",
                                    "http://orig08.deviantart.net/f934/f/2014/206/1/2/transformers_5__rise_of_unicron__2016__poster_by_krallbaki-d7s716l.jpg",
                                    "https://www.youtube.com/watch?v=MIR6iJ9VNlI")
Beauty_Beast = MovieClass.Movie("Beauty And The Beast",
                               "The fantastic journey of Belle, a bright, beautiful and independent young woman who is taken prisoner by a beast in his castle. Despite her fears, she befriends the castle's enchanted staff and learns to look beyond the Beast's hideous exterior and realize the kind heart and soul of the true Prince within.",
                               "http://cdn3-www.comingsoon.net/assets/uploads/gallery/beauty-and-the-beast-2017/15039604_1408397595845793_8833883194110677407_o.jpg",
                               "https://www.youtube.com/watch?v=_0c3iOb5KCU")

Logan = MovieClass.Movie("Logan",
                         "In the near future, a weary Logan cares for an ailing Professor X in a hide out on the Mexican border. But Logan's attempts to hide from the world and his legacy are up-ended when a young mutant arrives, being pursued by dark forces.",
                         "http://cdn2-www.comingsoon.net/assets/uploads/gallery/untitled-wolverine-sequel/cuaiczwueaaid_w-jpg-large.jpg",
                         "https://www.youtube.com/watch?v=RH3OxVFvTeg")
Cars_3 = MovieClass.Movie("Cars 3",
                          "Blindsided by a new generation of blazing-fast racers, the legendary Lightning McQueen pushes himself beyond his limits. To get back in the game, he will need the help of an eager young female race technician, Cruz Ramirez. Proving that #95 isn’t through yet, he will test the heart of a champion on Piston Cup Racing’s biggest stage against his new rival, Jackson Storm.",
                          "http://t1.gstatic.com/images?q=tbn:ANd9GcSa2d_wpxpjmS9LSp19Bh6d6QMrWaSNsn20l1N5bccHFwiwAHxN",
                          "https://www.youtube.com/watch?v=ob4rImr5r9o")


movies = [Wonder_Woman,Pirates_Five,Transformers_Five,Beauty_Beast,Logan,Cars_3]
fresh_tomatoes.open_movies_page(movies)
