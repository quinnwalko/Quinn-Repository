#FIRST AND LAST NAMES OF ACTOR
use sakila;
select first_name, last_name from actor;

#FIRST AND LAST NAMES OF ACTOR SINGLE COLUMN
use sakila;
select concat(first_name, " ", last_name) as Actor_Name
from actor;

#FIND JOE
use sakila;
select actor_id, first_name, last_name
from actor
where first_name = "Joe";

#fIND GEN
use sakila;
select last_name, first_name
from actor
where last_name like "%GEN%";

#FIND LI
use sakila;
select last_name, first_name
from actor 
where last_name like "%LI%"
order by last_name, first_name;

#FIND ABC COUNTRIES
use sakila;
select country_id, country
from country
where country in ("Afghanistan", "Bangladesh", "China");

#CREATE DESCRIPTION
use sakila;
alter table actor
add column middle_name varchar(30);
alter table actor
modify middle_name blob;

#UNDO DESCRIPTION
alter table actor
drop column middle_name;

#COUNT LAST NAMES
use sakila;
select last_name, count(last_name) as "Last Name Count"
from actor
group by last_name
having count(last_name) >=2;

#SWITCH TO HARPO
use sakila;
update actor
set first_name = "Harpo"
where first_name = "Groucho" and last_name = "Williams";

#SWITCH IT BACK
use sakila;
update actor
set first_name = 
case
when first_name = "Harpo"
then "Groucho"
else "Mucho Groucho"
end
where actor_id = 172;

#FIND ADDRESS TABLE
use sakila;
show create table sakila.address;

#SHOW STAFF
use sakila;
select first_name, last_name, address
from staff s
inner join address a
on s.address_id = a.address_id;

#SHOW STAFF REVENUE
use sakila;
select first_name, last_name, sum(amount)
from staff s
inner join payment p
on s.staff_id = p.staff_id
group by p.staff_id
order by last_name asc;

#LIST ACTORS BY FILM
use sakila;
select title, count(actor_id)
from film f
inner join film_actor fa
on f.film_id = fa.film_id
group by title;

#HOW MANY HUNCHBACK IMPOSSIBLE
use sakila;
select title, count(inventory_id)
from film f
inner join inventory i
on f.film_id = i.film_id
where title = "Hunchback Impossible";

#TOTAL PER CUSTOMER
use sakila;
select last_name, first_name, sum(amount)
from payment p
inner join customer c
on p.customer_id = c.customer_id
group by p.customer_id
order by last_name asc;

#QUEEN AND KRIS KRISTOFFERSON
use sakila;
select title 
from film
where language_id in
	(select language_id
    from language
    where name = "English")
and (title like "K%") or (title like "Q%");

#ALONE TRIP
use sakila;
select last_name, first_name
from actor
where actor_id in 
	(select actor_id from film_actor
    where film_id in 
		(select film_id from film
        where title = "Alone Trip"));
        
#CANADA
use sakila;
select country, last_name, first_name, email
from country c
left join customer cu
on c.country_id = cu.customer_id
where country = "Canada";

#FAMILY FILMS
use sakila;
select title, category
from film_list
where category = "Family";

#MOST FREQUENTLY RENTED MOVIES
use sakila;
select i.film_id, f.title, count(r.inventory_id)
from inventory i
inner join rental r
on i.inventory_id = r.inventory_id
inner join film_text f
on i.film_id = f.film_id
group by r.inventory_id
order by count(r.inventory_id) desc;

#BUSINESS PER STORE
use sakila;
select store.store_id, sum(amount)
from store
inner join staff
on store.store_id = staff.store_id
inner join payment p
on p.staff_id = staff.staff_id
group by store.store_id
order by sum(amount);

#STORE ID, CITY, COUNTRY
use sakila;
select s.store_id, city, country
from store s
inner join customer cu
on s.store_id = cu.store_id
inner join staff st
on s.store_id = st.store_id
inner join address a
on cu.address_id = a.address_id
inner join city ci
on a.city_id = ci.city_id
inner join country co
on ci.country_id = co.country_id
where country = "Canada" and country = "Austraila";

#TOP 5 GENRES
use sakila;
select name, sum(p.amount)
from category c
inner join film_category fc
inner join inventory i
on i.film_id = fc.film_id
inner join rental r
on r.inventory_id = i.inventory_id
inner join payment p
group by name
limit 5;

#VIEW TOP FIVE GENRES
use sakila;
create view top_five_genres as
select name, sum(p.amount)
from category c
inner join film_category fc
inner join inventory i
on i.film_id = fc.film_id
inner join rental r
on r.inventory_id = i.inventory_id
inner join payment p
group by name
limit 5;

use sakila;
select * from top_five_genres;

use sakila;
drop view top_five_genres;






		
