# States of a Pirate:
- The state of a pirate is stored in his own signal
- A and D pirates also have an additional attribute x, where x (= 1, 2, or 3) is the island being attacked or defended.
- The different states of a pirate are as follows:

## Scout (S):
- This is the default of a newly created pirate.
- S will always attempt to move outward from the deploy point.
- If S reaches an island that is either neutral or belongs to the opponent, he becomes A.
- If S finds that a particular island that belongs to the home team is currently being captured by the opponent, he becomes D.
- If S finds the call to attack on the team signal, there is a chance that he becomes of type A.

## Passive Scout (P):
- The difference between S and P is that when there is a call to attack on the team signal, no P gets converted to A.
- P always moves away from the deploy point.
- If P reaches an island that is either neutral or belongs to the opponent, he becomes A.
- If P finds that a particular island that belongs to the home team is currently being captured, he becomes D.
- Once P finds that the home team is not attempting to capture anything, he becomes S. 

## Attacker (A):
- S upon reaching an island that is either neutral or belongs to the opponent, becomes A.
- An S reads the call to attack in the team signal and can become A.
- On any move, A moves towards the island x.
- A has an attribute x, where x is the island number which he is attacking.
- A has the method to call in reinforcements. 
- This means that the call to attack now also includes island x.
- This signal will be read by all S and there is a chance for it to become an A.
- Once A has captured the island, he becomes S.

## Defender (D):
- S upon reading Dx in the team signal, becomes D.
- On any move, D moves towards the island x.
- D has an attribute x, where x is the island number which he is defending.
- Once the opponent stops trying to capture the island, D becomes S.

------------------------------------------------------------------------------------------------------------------------

### What does a "Call to attack" mean?:
- If the team signal reads "Ax", each S has a 50-50 chance of becoming an A (for island x) or a P.
- If the team signal reads "Axy", each S has a 45-45-10 chance of becoming an A (for island x), an A (for island y), or a P.
- If the team signal reads "Axyz", each S has a 33-33-33 chance of becoming an A for islands x, y and z.
