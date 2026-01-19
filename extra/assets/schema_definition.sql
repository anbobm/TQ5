CREATE TABLE category (
	id integer primary key,
	parent_category integer,
	name varchar(255) not null,
	foreign key (parent_category) references category (id) 
);

CREATE TABLE payment_method (
	id integer primary key,
	name varchar(255) not null
);

CREATE TABLE expense (
	id integer primary key,
	amount float not null,
	date date not null,
	category_id integer not null,
	payment_method_id integer not null,
	notes text,
	recurring varchar(50) default null,
	foreign key (category_id) references category (id),
	foreign key (payment_method_id) references payment_method (id)
);
