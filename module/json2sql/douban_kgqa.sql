create table book_genre
(
  book_genre_id   int         not null
    primary key,
  book_genre_name varchar(20) not null
);

create table book_info
(
  book_info_id               int          not null
    primary key,
  book_info_name             text         null,
  book_info_image_url        varchar(200) null,
  book_info_press            varchar(200) null,
  book_info_publish_year     varchar(200) null,
  book_info_page_num         varchar(200) null,
  book_info_price            varchar(200) null,
  book_info_content_abstract mediumtext   null,
  book_info_catalog          mediumtext   null,
  book_info_rating           varchar(10)  null,
  book_info_review_count     varchar(200) null
);

create table book_person
(
  book_person_id           int          not null
    primary key,
  book_person_name         text         null,
  book_person_image_url    varchar(200) null,
  book_person_gender       varchar(100) null,
  book_person_birthday     varchar(200) null,
  book_person_birthplace   text         null,
  book_person_other_name   text         null,
  book_person_introduction mediumtext   null
);

create table author_to_book
(
  book_info_id   int not null,
  book_author_id int not null,
  primary key (book_info_id, book_author_id),
  constraint author_to_book_book
  foreign key (book_info_id) references book_info (book_info_id),
  constraint author_to_book_person
  foreign key (book_author_id) references book_person (book_person_id)
);

create index author_to_book_person
  on author_to_book (book_author_id);

create index author_to_boox_idx
  on author_to_book (book_info_id);

create table book_to_genre
(
  book_info_id  int not null,
  book_genre_id int not null,
  primary key (book_info_id, book_genre_id),
  constraint book_to_genre_book
  foreign key (book_info_id) references book_info (book_info_id),
  constraint book_to_genre_genre
  foreign key (book_genre_id) references book_genre (book_genre_id)
);

create index book_to_genre_idx
  on book_to_genre (book_genre_id);

create table movie_genre
(
  movie_genre_id   int         not null
    primary key,
  movie_genre_name varchar(20) not null
);

create table movie_info
(
  movie_info_id           int          not null
    primary key,
  movie_info_name         text         null,
  movie_info_image_url    varchar(200) null,
  movie_info_country      varchar(200) null,
  movie_info_language     varchar(200) null,
  movie_info_pubdate      varchar(200) null,
  movie_info_duration     varchar(200) null,
  movie_info_other_name   text         null,
  movie_info_summary      mediumtext   null,
  movie_info_rating       varchar(10)  null,
  movie_info_review_count varchar(200) null
);

create table movie_person
(
  movie_person_id            int          not null
    primary key,
  movie_person_name          text         null,
  movie_person_image_url     varchar(200) null,
  movie_person_gender        varchar(100) null,
  movie_person_constellation varchar(200) null,
  movie_person_birthday      varchar(200) null,
  movie_person_birthplace    text         null,
  movie_person_profession    varchar(200) null,
  movie_person_other_name    text         null,
  movie_person_introduction  mediumtext   null
);

create table actor_to_movie
(
  movie_info_id  int not null,
  movie_actor_id int not null,
  primary key (movie_info_id, movie_actor_id),
  constraint actor_to_movie_movie
  foreign key (movie_info_id) references movie_info (movie_info_id),
  constraint actor_to_movie_person
  foreign key (movie_actor_id) references movie_person (movie_person_id)
);

create index actor_to_movie_person
  on actor_to_movie (movie_actor_id);

create table director_to_movie
(
  movie_info_id     int not null,
  movie_director_id int not null,
  primary key (movie_info_id, movie_director_id),
  constraint director_to_movie_movie
  foreign key (movie_info_id) references movie_info (movie_info_id),
  constraint director_to_movie_person
  foreign key (movie_director_id) references movie_person (movie_person_id)
);

create index director_to_movie_person
  on director_to_movie (movie_director_id);

create table movie_to_genre
(
  movie_info_id  int not null,
  movie_genre_id int not null,
  primary key (movie_info_id, movie_genre_id),
  constraint movie_to_genre_movie
  foreign key (movie_info_id) references movie_info (movie_info_id),
  constraint movie_to_genre_genre
  foreign key (movie_genre_id) references movie_genre (movie_genre_id)
);

create index movie_to_genre_idx
  on movie_to_genre (movie_genre_id);

create table translator_to_book
(
  book_info_id       int not null,
  book_translator_id int not null,
  primary key (book_info_id, book_translator_id),
  constraint translator_to_book_book
  foreign key (book_info_id) references book_info (book_info_id),
  constraint translator_to_book_person
  foreign key (book_translator_id) references book_person (book_person_id)
);

create index translator_to_book_idx
  on translator_to_book (book_info_id);

create index translator_to_book_person
  on translator_to_book (book_translator_id);

create table writer_to_movie
(
  movie_info_id   int not null,
  movie_writer_id int not null,
  primary key (movie_info_id, movie_writer_id),
  constraint writer_to_movie_movie
  foreign key (movie_info_id) references movie_info (movie_info_id),
  constraint writer_to_movie_person
  foreign key (movie_writer_id) references movie_person (movie_person_id)
);

create index writer_to_movie_person
  on writer_to_movie (movie_writer_id);


