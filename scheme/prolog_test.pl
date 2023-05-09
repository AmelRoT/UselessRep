


parent(john,paul).
parent(paul,tom).
parent(tom,mery).

ancestor(X,Y) :- parent(X,Y).
ancestor(X,Y) :- parent(X,Z), ancestor(Z,Y).


/*
parent(tom, tom1). 
parent(tom1, tom) :- parent(tom,tom1).*/
blue_box.

match(X,[X|_]). 
match(X,[_|T]) :- match(X,T).

/*List1 = [a|[b,c]].  this is just to add an element to the list    */


f(p1,p1).

/*this_is_john. */



parent1(john,bill). 
parent1(john, austin). 
parent1(bill, medin).
parent1(bill, adin). 
parent1(adin,eldin). 
parent1(adin, jasna).


ancestor1(X1,Y1) :- parent1(X1,Y1). 
ancestor1(X1,Y1) :- parent1(X1,Z1), ancestor1(Z1,Y1).

/* thse are called realtions and are useful */
eats(fred,_).

f111(a,_). 

human(soc).
die1(X) :- human(X).

red1(wine). 
bluish1(wine).
red(red). 
bluish(bluish).


funwhatever(X) :- red(X), bluish(X). 
funwhatever(Y) :- red1(Y), bluish1(Y). 



route(rome). 
route(X) :- move(X,_,Z), route(Z). 


move(home,taxi,halifax).
move(halifax,train,gatwick).
move(gatwick,plane,rome).

/*
A1 = [robet(hess), hunny, bunny, _, what,ther].

A2 = [abc, dcasd, asdas]. 
*/

insideList(X,[X|Y]). 
insideList(X,[_|Y]) :- insideList(X,Y). 


/*
List1 = [lisp,c,pascal,basic].
List2 = [prolog|List1].
*/

/* [1,12,3,14,5,8]  -> [12 14 8]*/

connect([],Y,Y). 
connect([X|T],Y,[X|Res]) :- connect(T,Y,Res).

/* start when both of them start from empty list */
greaterThanSix([],[]). 
greaterThanSix([X|T],[X|Res]) :- X>6, greaterThanSix(T,Res). 
greaterThanSix([X|T],Res) :-  greaterThanSix(T,Res). 


/* [a,b,c] a -> [b,c]*/

same(X,X).
deleteElementsFromList([],_,[]).   
deleteElementsFromList([X|T], Y,Res) :- same(X,Y), deleteElementsFromList(T,Y,Res).
deleteElementsFromList([X|T], Y,[X|Res] ) :- \+(X=Y), deleteElementsFromList(T,Y,Res).

/* not is not used here but that crazy symbol  */ 

/*
addElementList([],List,List). 
addElementList([Head|T],List,[Head|ListResult]) :- addElementList(T,List,ListResult). 

*/




parenT(tom, tom1).
parenT(tom, tom2).

parenTT(X,Y) :- parenT(tom,Y),!. 

/* this ! eliminates the backtracking because it stops it there. */



par(fred,mike). 
par(mike,joe). 
par(mike,mary). 
brother(mike,fred). 

brother(X,Y) :- brother(Y,X).


ances(X,Y) :- par(X,Y). 
siblings(X,Y) :- par(Z,X),par(Z,Y). 
uncle(X,Y) :- brother(X,Z), par(Z,Y). 


/*
maxOfList([],[]).
maxOfList([X,X1|T],X) :- X>X1 , maxOfList(T,Res).  
maxOfList([X,X1|T],X1) :- X<=X1 , maxOfList(T,Res).  
maxOfList([X|T],Res) :- maxOfList(T,Res).  

*/

maxOfList1([],V,V).
maxOfList1([X|T],V,Res) :- X>=V,maxOfList1(T,X,Res).  
maxOfList1([X|T],V,Res) :- maxOfList1(T,V,Res).  


finalElement([],_). 
finalElement([X|T],X) :- T=[], finalElement(T,Res).
finalElement([X|T],Res) :- finalElement(T,Res).