% Facts
male(jay).
male(sunil).
male(amit).
male(jr).
male(anish).
male(chad).
male(deep).
male(mogg).

female(jaya).
female(sunita).
female(amita).
female(deepa).
female(lara).
female(robbi).
female(anisha).
female(emma).

parent(jay, sunil).
parent(jay, amit).
parent(jaya, sunil).
parent(jaya, amit).
parent(sunil, jr).
parent(sunil, deepa).
parent(sunita, jr).
parent(sunita, deepa).
parent(deepa, mogg).
parent(deepa, emma).
parent(deep, mogg).
parent(deep, emma).
parent(amit, anish).
parent(amit, anisha).
parent(amita, anish).
parent(amita, anisha).
parent(anish, chad).
parent(anisha, chad).
parent(anish, robbi).
parent(anisha, robbi).

% Rules
father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).

grandfather(X, Z) :- parent(X, Y), parent(Y, Z), male(X).
grandmother(X, Z) :- parent(X, Y), parent(Y, Z), female(X).
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).

sister(X, Y) :- parent(Z, X), parent(Z, Y), female(X), X \= Y.
brother(X, Y) :- parent(Z, X), parent(Z, Y), male(X), X \= Y.
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

uncle(X, Y) :- brother(X, Z), parent(Z, Y).
uncle(X, Y) :- spouse(X, Z), sister(Z, P), parent(P, Y).
aunt(X, Y) :- sister(X, Z), parent(Z, Y).
aunt(X, Y) :- spouse(X, Z), brother(Z, P), parent(P, Y).

husband(X, Y) :- male(X), spouse(X, Y).
wife(X, Y) :- female(X), spouse(X, Y).

spouse(X, Y) :- parent(X, Z), parent(Y, Z), X \= Y.

greatgrandparent(X, Y) :- parent(X, Z), parent(Z, P), parent(P, Y).

grandson(X, Y) :- parent(Y, Z), parent(Z, X), male(X).
granddaughter(X, Y) :- parent(Y, Z), parent(Z, X), female(X).
grandchildren(X, Y) :- parent(Y, Z), parent(Z, X).

brotherinlaw(X, Y) :- brother(X, Z), spouse(Z, Y).
sisterinlaw(X, Y) :- sister(X, Z), spouse(Z, Y).

nephew(X, Y) :- (uncle(Y, X) ; aunt(Y, X)), male(X).
niece(X, Y) :- (uncle(Y, X) ; aunt(Y, X)), female(X).

cousin(X, Y) :- parent(Z, X), parent(P, Y), sibling(Z, P).
